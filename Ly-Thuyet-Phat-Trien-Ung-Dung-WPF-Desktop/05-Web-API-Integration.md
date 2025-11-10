# WEB API INTEGRATION TRONG C#

## 📚 Mục Lục

1. [Giới Thiệu RESTful API](#1-giới-thiệu-restful-api)
2. [HttpClient trong C#](#2-httpclient-trong-c)
3. [CRUD Operations](#3-crud-operations)
4. [JSON Serialization](#4-json-serialization)
5. [Async/Await Programming](#5-asyncawait-programming)
6. [Error Handling](#6-error-handling)
7. [Authentication](#7-authentication)
8. [Best Practices](#8-best-practices)
9. [Dự Án Thực Tế](#9-dự-án-thực-tế)

---

## 1. Giới Thiệu RESTful API

### 1.1. REST Là Gì?

**REST (Representational State Transfer)** là architectural style cho web services sử dụng HTTP methods.

### 1.2. HTTP Methods

```
GET    - Lấy dữ liệu (Read)
POST   - Tạo mới (Create)
PUT    - Cập nhật toàn bộ (Update)
PATCH  - Cập nhật một phần (Partial Update)
DELETE - Xóa (Delete)
```

### 1.3. HTTP Status Codes

```csharp
// Success
200 OK                  // Request thành công
201 Created             // Tạo mới thành công
204 No Content          // Thành công, không có content

// Client Errors
400 Bad Request         // Request không hợp lệ
401 Unauthorized        // Chưa authenticate
403 Forbidden           // Không có quyền
404 Not Found           // Không tìm thấy resource

// Server Errors
500 Internal Server Error    // Lỗi server
503 Service Unavailable      // Service tạm ngừng
```

---

## 2. HttpClient trong C#

### 2.1. Tạo HttpClient

```csharp
// ❌ BAD - Tạo mới mỗi lần (socket exhaustion)
using (var client = new HttpClient())
{
    // Use client...
}

// ✅ GOOD - Singleton hoặc IHttpClientFactory
public class ApiService
{
    private static readonly HttpClient client = new HttpClient
    {
        BaseAddress = new Uri("https://api.example.com/"),
        Timeout = TimeSpan.FromSeconds(30)
    };

    // Or better: Use IHttpClientFactory in .NET Core
}
```

### 2.2. IHttpClientFactory (.NET Core/5+)

```csharp
// Startup.cs hoặc Program.cs
services.AddHttpClient("MyApi", client =>
{
    client.BaseAddress = new Uri("https://api.example.com/");
    client.DefaultRequestHeaders.Add("Accept", "application/json");
    client.Timeout = TimeSpan.FromSeconds(30);
});

// Service class
public class ApiService
{
    private readonly HttpClient httpClient;

    public ApiService(IHttpClientFactory httpClientFactory)
    {
        httpClient = httpClientFactory.CreateClient("MyApi");
    }

    // Use httpClient...
}
```

### 2.3. Request Headers

```csharp
var client = new HttpClient();

// Add headers
client.DefaultRequestHeaders.Add("User-Agent", "MyApp/1.0");
client.DefaultRequestHeaders.Add("Accept", "application/json");
client.DefaultRequestHeaders.Authorization =
    new AuthenticationHeaderValue("Bearer", "your-token-here");

// Custom headers
client.DefaultRequestHeaders.Add("X-Custom-Header", "value");
```

---

## 3. CRUD Operations

### 3.1. GET Request

```csharp
public class ApiService
{
    private readonly HttpClient client;

    public ApiService(HttpClient client)
    {
        this.client = client;
    }

    // GET all
    public async Task<List<Product>> GetProductsAsync()
    {
        try
        {
            var response = await client.GetAsync("api/products");
            response.EnsureSuccessStatusCode();

            var json = await response.Content.ReadAsStringAsync();
            var products = JsonSerializer.Deserialize<List<Product>>(json);

            return products;
        }
        catch (HttpRequestException ex)
        {
            // Handle error
            throw new Exception($"Error getting products: {ex.Message}");
        }
    }

    // GET by ID
    public async Task<Product> GetProductByIdAsync(int id)
    {
        var response = await client.GetAsync($"api/products/{id}");
        response.EnsureSuccessStatusCode();

        var json = await response.Content.ReadAsStringAsync();
        return JsonSerializer.Deserialize<Product>(json);
    }

    // GET with query parameters
    public async Task<List<Product>> SearchProductsAsync(string keyword, int page = 1, int pageSize = 10)
    {
        var url = $"api/products/search?keyword={Uri.EscapeDataString(keyword)}&page={page}&pageSize={pageSize}";
        var response = await client.GetAsync(url);
        response.EnsureSuccessStatusCode();

        var json = await response.Content.ReadAsStringAsync();
        return JsonSerializer.Deserialize<List<Product>>(json);
    }
}
```

### 3.2. POST Request

```csharp
// POST - Create
public async Task<Product> CreateProductAsync(Product product)
{
    var json = JsonSerializer.Serialize(product);
    var content = new StringContent(json, Encoding.UTF8, "application/json");

    var response = await client.PostAsync("api/products", content);
    response.EnsureSuccessStatusCode();

    var responseJson = await response.Content.ReadAsStringAsync();
    return JsonSerializer.Deserialize<Product>(responseJson);
}

// POST - With form data
public async Task<bool> UploadFileAsync(string filePath)
{
    using var form = new MultipartFormDataContent();
    using var fileStream = File.OpenRead(filePath);
    using var streamContent = new StreamContent(fileStream);

    form.Add(streamContent, "file", Path.GetFileName(filePath));
    form.Add(new StringContent("additional data"), "description");

    var response = await client.PostAsync("api/upload", form);
    return response.IsSuccessStatusCode;
}
```

### 3.3. PUT Request

```csharp
// PUT - Update
public async Task<Product> UpdateProductAsync(int id, Product product)
{
    var json = JsonSerializer.Serialize(product);
    var content = new StringContent(json, Encoding.UTF8, "application/json");

    var response = await client.PutAsync($"api/products/{id}", content);
    response.EnsureSuccessStatusCode();

    var responseJson = await response.Content.ReadAsStringAsync();
    return JsonSerializer.Deserialize<Product>(responseJson);
}
```

### 3.4. PATCH Request

```csharp
// PATCH - Partial update
public async Task<Product> PartialUpdateProductAsync(int id, object updates)
{
    var json = JsonSerializer.Serialize(updates);
    var content = new StringContent(json, Encoding.UTF8, "application/json");

    var request = new HttpRequestMessage(new HttpMethod("PATCH"), $"api/products/{id}")
    {
        Content = content
    };

    var response = await client.SendAsync(request);
    response.EnsureSuccessStatusCode();

    var responseJson = await response.Content.ReadAsStringAsync();
    return JsonSerializer.Deserialize<Product>(responseJson);
}
```

### 3.5. DELETE Request

```csharp
// DELETE
public async Task<bool> DeleteProductAsync(int id)
{
    var response = await client.DeleteAsync($"api/products/{id}");
    return response.IsSuccessStatusCode;
}
```

---

## 4. JSON Serialization

### 4.1. System.Text.Json (Recommended)

```csharp
using System.Text.Json;
using System.Text.Json.Serialization;

public class Product
{
    [JsonPropertyName("id")]
    public int Id { get; set; }

    [JsonPropertyName("product_name")]
    public string Name { get; set; }

    [JsonPropertyName("price")]
    public decimal Price { get; set; }

    [JsonIgnore]
    public string InternalField { get; set; }
}

// Serialize
var product = new Product { Id = 1, Name = "Laptop", Price = 1000 };
var json = JsonSerializer.Serialize(product);
// {"id":1,"product_name":"Laptop","price":1000}

// Serialize with options
var options = new JsonSerializerOptions
{
    WriteIndented = true,
    PropertyNamingPolicy = JsonNamingPolicy.CamelCase,
    DefaultIgnoreCondition = JsonIgnoreCondition.WhenWritingNull
};
var jsonFormatted = JsonSerializer.Serialize(product, options);

// Deserialize
var productFromJson = JsonSerializer.Deserialize<Product>(json);

// Deserialize to anonymous type
var data = JsonSerializer.Deserialize<dynamic>(json);
```

### 4.2. Newtonsoft.Json (Json.NET)

```csharp
using Newtonsoft.Json;

public class Product
{
    [JsonProperty("id")]
    public int Id { get; set; }

    [JsonProperty("product_name")]
    public string Name { get; set; }

    [JsonIgnore]
    public string InternalField { get; set; }
}

// Serialize
var json = JsonConvert.SerializeObject(product);
var jsonFormatted = JsonConvert.SerializeObject(product, Formatting.Indented);

// Deserialize
var product = JsonConvert.DeserializeObject<Product>(json);

// Deserialize to dynamic
dynamic data = JsonConvert.DeserializeObject(json);
Console.WriteLine(data.product_name);
```

---

## 5. Async/Await Programming

### 5.1. Async Best Practices

```csharp
// ✅ GOOD - Async all the way
public async Task<List<Product>> GetProductsAsync()
{
    var response = await client.GetAsync("api/products");
    var json = await response.Content.ReadAsStringAsync();
    return JsonSerializer.Deserialize<List<Product>>(json);
}

// ❌ BAD - Blocking async code
public List<Product> GetProducts()
{
    return GetProductsAsync().Result; // Deadlock risk!
}

// ✅ GOOD - ConfigureAwait(false) in library code
public async Task<Product> GetProductAsync(int id)
{
    var response = await client.GetAsync($"api/products/{id}")
        .ConfigureAwait(false);

    var json = await response.Content.ReadAsStringAsync()
        .ConfigureAwait(false);

    return JsonSerializer.Deserialize<Product>(json);
}
```

### 5.2. Parallel Requests

```csharp
// Execute multiple requests in parallel
public async Task<(List<Product> products, List<Category> categories)> LoadDataAsync()
{
    var productsTask = GetProductsAsync();
    var categoriesTask = GetCategoriesAsync();

    await Task.WhenAll(productsTask, categoriesTask);

    return (productsTask.Result, categoriesTask.Result);
}

// Or using ValueTuple
public async Task<(List<Product>, List<Category>)> LoadDataAsync()
{
    var tasks = new[]
    {
        GetProductsAsync(),
        GetCategoriesAsync()
    };

    var results = await Task.WhenAll(tasks);

    return (results[0], results[1]);
}
```

### 5.3. Cancellation Token

```csharp
public async Task<List<Product>> GetProductsAsync(CancellationToken cancellationToken = default)
{
    var response = await client.GetAsync("api/products", cancellationToken);
    response.EnsureSuccessStatusCode();

    var json = await response.Content.ReadAsStringAsync(cancellationToken);
    return JsonSerializer.Deserialize<List<Product>>(json);
}

// Usage
var cts = new CancellationTokenSource(TimeSpan.FromSeconds(10));
try
{
    var products = await GetProductsAsync(cts.Token);
}
catch (OperationCanceledException)
{
    Console.WriteLine("Request was cancelled");
}
```

---

## 6. Error Handling

### 6.1. Try-Catch Pattern

```csharp
public async Task<Product> GetProductAsync(int id)
{
    try
    {
        var response = await client.GetAsync($"api/products/{id}");
        response.EnsureSuccessStatusCode();

        var json = await response.Content.ReadAsStringAsync();
        return JsonSerializer.Deserialize<Product>(json);
    }
    catch (HttpRequestException ex)
    {
        // Network error
        throw new Exception($"Network error: {ex.Message}", ex);
    }
    catch (TaskCanceledException ex)
    {
        // Timeout
        throw new Exception("Request timeout", ex);
    }
    catch (JsonException ex)
    {
        // JSON parsing error
        throw new Exception("Invalid JSON response", ex);
    }
}
```

### 6.2. Custom Error Response

```csharp
public class ApiResponse<T>
{
    public bool Success { get; set; }
    public T Data { get; set; }
    public string Message { get; set; }
    public List<string> Errors { get; set; }
}

public async Task<ApiResponse<Product>> GetProductSafeAsync(int id)
{
    try
    {
        var response = await client.GetAsync($"api/products/{id}");

        if (response.IsSuccessStatusCode)
        {
            var json = await response.Content.ReadAsStringAsync();
            var product = JsonSerializer.Deserialize<Product>(json);

            return new ApiResponse<Product>
            {
                Success = true,
                Data = product
            };
        }
        else if (response.StatusCode == System.Net.HttpStatusCode.NotFound)
        {
            return new ApiResponse<Product>
            {
                Success = false,
                Message = "Product not found"
            };
        }
        else
        {
            return new ApiResponse<Product>
            {
                Success = false,
                Message = $"Error: {response.StatusCode}"
            };
        }
    }
    catch (Exception ex)
    {
        return new ApiResponse<Product>
        {
            Success = false,
            Message = ex.Message,
            Errors = new List<string> { ex.StackTrace }
        };
    }
}
```

### 6.3. Retry Logic with Polly

```csharp
// Install: Polly NuGet package
using Polly;
using Polly.Retry;

public class ApiService
{
    private readonly HttpClient client;
    private readonly AsyncRetryPolicy<HttpResponseMessage> retryPolicy;

    public ApiService(HttpClient client)
    {
        this.client = client;

        // Retry 3 times with exponential backoff
        retryPolicy = Policy
            .HandleResult<HttpResponseMessage>(r => !r.IsSuccessStatusCode)
            .Or<HttpRequestException>()
            .WaitAndRetryAsync(
                retryCount: 3,
                sleepDurationProvider: attempt => TimeSpan.FromSeconds(Math.Pow(2, attempt)),
                onRetry: (outcome, timespan, retryCount, context) =>
                {
                    Console.WriteLine($"Retry {retryCount} after {timespan.TotalSeconds}s");
                }
            );
    }

    public async Task<List<Product>> GetProductsWithRetryAsync()
    {
        var response = await retryPolicy.ExecuteAsync(async () =>
            await client.GetAsync("api/products")
        );

        response.EnsureSuccessStatusCode();
        var json = await response.Content.ReadAsStringAsync();
        return JsonSerializer.Deserialize<List<Product>>(json);
    }
}
```

---

## 7. Authentication

### 7.1. Bearer Token (JWT)

```csharp
public class AuthService
{
    private readonly HttpClient client;
    private string accessToken;

    public async Task<bool> LoginAsync(string username, string password)
    {
        var loginData = new { username, password };
        var json = JsonSerializer.Serialize(loginData);
        var content = new StringContent(json, Encoding.UTF8, "application/json");

        var response = await client.PostAsync("api/auth/login", content);

        if (response.IsSuccessStatusCode)
        {
            var responseJson = await response.Content.ReadAsStringAsync();
            var result = JsonSerializer.Deserialize<LoginResponse>(responseJson);

            accessToken = result.AccessToken;

            // Set Authorization header
            client.DefaultRequestHeaders.Authorization =
                new AuthenticationHeaderValue("Bearer", accessToken);

            return true;
        }

        return false;
    }
}

public class LoginResponse
{
    [JsonPropertyName("access_token")]
    public string AccessToken { get; set; }

    [JsonPropertyName("expires_in")]
    public int ExpiresIn { get; set; }

    [JsonPropertyName("token_type")]
    public string TokenType { get; set; }
}
```

### 7.2. API Key

```csharp
public class ApiService
{
    private readonly HttpClient client;

    public ApiService(string apiKey)
    {
        client = new HttpClient();
        client.DefaultRequestHeaders.Add("X-API-Key", apiKey);
        // Or
        client.DefaultRequestHeaders.Add("Authorization", $"ApiKey {apiKey}");
    }
}
```

### 7.3. Basic Authentication

```csharp
public class ApiService
{
    private readonly HttpClient client;

    public ApiService(string username, string password)
    {
        client = new HttpClient();

        var credentials = Convert.ToBase64String(
            Encoding.ASCII.GetBytes($"{username}:{password}")
        );

        client.DefaultRequestHeaders.Authorization =
            new AuthenticationHeaderValue("Basic", credentials);
    }
}
```

---

## 8. Best Practices

### 8.1. Do's ✅

```csharp
// ✅ Use IHttpClientFactory
services.AddHttpClient<IApiService, ApiService>();

// ✅ Use async/await
public async Task<Product> GetProductAsync(int id)

// ✅ Handle errors properly
try { } catch (HttpRequestException ex) { }

// ✅ Use cancellation tokens
public async Task<List<Product>> GetAsync(CancellationToken ct)

// ✅ Set timeouts
client.Timeout = TimeSpan.FromSeconds(30);

// ✅ Dispose HttpClient properly (or use singleton)
private static readonly HttpClient client = new HttpClient();
```

### 8.2. Don'ts ❌

```csharp
// ❌ Don't create HttpClient in using statement
using (var client = new HttpClient()) { } // Socket exhaustion!

// ❌ Don't block async code
var result = GetProductsAsync().Result; // Deadlock!

// ❌ Don't ignore exceptions
try { } catch { } // Silent failure!

// ❌ Don't hardcode URLs
var url = "http://example.com/api"; // Use configuration!

// ❌ Don't forget to set headers
// Missing: Content-Type, Accept, Authorization
```

---

## 9. Dự Án Thực Tế

### 9.1. Complete API Service

```csharp
// Services/IProductApiService.cs
public interface IProductApiService
{
    Task<List<Product>> GetAllAsync();
    Task<Product> GetByIdAsync(int id);
    Task<Product> CreateAsync(Product product);
    Task<Product> UpdateAsync(int id, Product product);
    Task<bool> DeleteAsync(int id);
}

// Services/ProductApiService.cs
public class ProductApiService : IProductApiService
{
    private readonly HttpClient httpClient;
    private readonly ILogger<ProductApiService> logger;

    public ProductApiService(HttpClient httpClient, ILogger<ProductApiService> logger)
    {
        this.httpClient = httpClient;
        this.logger = logger;
    }

    public async Task<List<Product>> GetAllAsync()
    {
        try
        {
            logger.LogInformation("Getting all products");

            var response = await httpClient.GetAsync("api/products");
            response.EnsureSuccessStatusCode();

            var json = await response.Content.ReadAsStringAsync();
            var products = JsonSerializer.Deserialize<List<Product>>(json);

            logger.LogInformation($"Retrieved {products.Count} products");
            return products;
        }
        catch (Exception ex)
        {
            logger.LogError(ex, "Error getting products");
            throw;
        }
    }

    public async Task<Product> GetByIdAsync(int id)
    {
        logger.LogInformation($"Getting product {id}");

        var response = await httpClient.GetAsync($"api/products/{id}");

        if (response.StatusCode == System.Net.HttpStatusCode.NotFound)
        {
            logger.LogWarning($"Product {id} not found");
            return null;
        }

        response.EnsureSuccessStatusCode();

        var json = await response.Content.ReadAsStringAsync();
        return JsonSerializer.Deserialize<Product>(json);
    }

    public async Task<Product> CreateAsync(Product product)
    {
        logger.LogInformation($"Creating product: {product.Name}");

        var json = JsonSerializer.Serialize(product);
        var content = new StringContent(json, Encoding.UTF8, "application/json");

        var response = await httpClient.PostAsync("api/products", content);
        response.EnsureSuccessStatusCode();

        var responseJson = await response.Content.ReadAsStringAsync();
        var createdProduct = JsonSerializer.Deserialize<Product>(responseJson);

        logger.LogInformation($"Created product with ID: {createdProduct.Id}");
        return createdProduct;
    }

    public async Task<Product> UpdateAsync(int id, Product product)
    {
        logger.LogInformation($"Updating product {id}");

        var json = JsonSerializer.Serialize(product);
        var content = new StringContent(json, Encoding.UTF8, "application/json");

        var response = await httpClient.PutAsync($"api/products/{id}", content);
        response.EnsureSuccessStatusCode();

        var responseJson = await response.Content.ReadAsStringAsync();
        return JsonSerializer.Deserialize<Product>(responseJson);
    }

    public async Task<bool> DeleteAsync(int id)
    {
        logger.LogInformation($"Deleting product {id}");

        var response = await httpClient.DeleteAsync($"api/products/{id}");
        return response.IsSuccessStatusCode;
    }
}
```

### 9.2. ViewModel Integration

```csharp
using CommunityToolkit.Mvvm.ComponentModel;
using CommunityToolkit.Mvvm.Input;

public partial class ProductViewModel : ObservableObject
{
    private readonly IProductApiService apiService;

    [ObservableProperty]
    private ObservableCollection<Product> products;

    [ObservableProperty]
    private Product selectedProduct;

    [ObservableProperty]
    private bool isLoading;

    [ObservableProperty]
    private string errorMessage;

    public ProductViewModel(IProductApiService apiService)
    {
        this.apiService = apiService;
        Products = new ObservableCollection<Product>();
    }

    [RelayCommand]
    private async Task LoadProductsAsync()
    {
        IsLoading = true;
        ErrorMessage = null;

        try
        {
            var products = await apiService.GetAllAsync();
            Products = new ObservableCollection<Product>(products);
        }
        catch (Exception ex)
        {
            ErrorMessage = $"Error loading products: {ex.Message}";
        }
        finally
        {
            IsLoading = false;
        }
    }

    [RelayCommand]
    private async Task CreateProductAsync(Product product)
    {
        IsLoading = true;
        try
        {
            var created = await apiService.CreateAsync(product);
            Products.Add(created);
        }
        catch (Exception ex)
        {
            ErrorMessage = $"Error creating product: {ex.Message}";
        }
        finally
        {
            IsLoading = false;
        }
    }

    [RelayCommand(CanExecute = nameof(CanDeleteProduct))]
    private async Task DeleteProductAsync()
    {
        if (SelectedProduct == null) return;

        IsLoading = true;
        try
        {
            var success = await apiService.DeleteAsync(SelectedProduct.Id);
            if (success)
            {
                Products.Remove(SelectedProduct);
                SelectedProduct = null;
            }
        }
        catch (Exception ex)
        {
            ErrorMessage = $"Error deleting product: {ex.Message}";
        }
        finally
        {
            IsLoading = false;
        }
    }

    private bool CanDeleteProduct() => SelectedProduct != null;
}
```

---

## 📝 Tóm Tắt

### Key Points:

1. **HttpClient** - Sử dụng singleton hoặc IHttpClientFactory
2. **REST methods** - GET, POST, PUT, PATCH, DELETE
3. **JSON** - System.Text.Json hoặc Newtonsoft.Json
4. **Async/Await** - Always use async for I/O operations
5. **Error Handling** - Try-catch và check status codes
6. **Authentication** - Bearer token, API key, Basic Auth
7. **Retry Logic** - Sử dụng Polly cho resilience

### Best Practices:

- ✅ Use IHttpClientFactory
- ✅ Async/await properly
- ✅ Handle errors gracefully
- ✅ Set timeouts
- ✅ Use cancellation tokens
- ✅ Log requests and errors
- ✅ Implement retry logic

---

**Next:** [06-Autodesk-Addin-Development.md](06-Autodesk-Addin-Development.md)
