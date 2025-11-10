# MVVM PATTERN TRONG WPF

## 📚 Mục Lục

1. [Giới Thiệu MVVM](#1-giới-thiệu-mvvm)
2. [Model-View-ViewModel](#2-model-view-viewmodel)
3. [Data Binding trong MVVM](#3-data-binding-trong-mvvm)
4. [INotifyPropertyChanged](#4-inotifypropertychanged)
5. [ICommand Interface](#5-icommand-interface)
6. [RelayCommand Implementation](#6-relaycommand-implementation)
7. [Dependency Injection](#7-dependency-injection)
8. [MVVM Frameworks](#8-mvvm-frameworks)
9. [Best Practices](#9-best-practices)
10. [Dự Án Thực Tế](#10-dự-án-thực-tế)

---

## 1. Giới Thiệu MVVM

### 1.1. MVVM Là Gì?

**MVVM (Model-View-ViewModel)** là architectural pattern giúp tách biệt UI (View) khỏi business logic (Model) thông qua lớp trung gian (ViewModel).

```
┌─────────────────────────────────────────────┐
│                   View                      │
│  (XAML - User Interface)                    │
└────────────┬────────────────────────────────┘
             │ Data Binding
             │ Commands
┌────────────▼────────────────────────────────┐
│                 ViewModel                   │
│  (Presentation Logic, Commands, Properties) │
└────────────┬────────────────────────────────┘
             │ Business Logic
             │ Data Access
┌────────────▼────────────────────────────────┐
│                   Model                     │
│  (Business Objects, Data, Validation)       │
└─────────────────────────────────────────────┘
```

### 1.2. Tại Sao Sử Dụng MVVM?

✅ **Separation of Concerns**: UI tách biệt khỏi logic
✅ **Testability**: Dễ dàng unit test ViewModel
✅ **Maintainability**: Code dễ maintain và mở rộng
✅ **Reusability**: ViewModel có thể reuse cho nhiều Views
✅ **Designer-Developer Workflow**: Designer làm XAML, Developer làm ViewModel

### 1.3. MVVM vs Code-Behind

#### ❌ Code-Behind Approach (Bad):

```xml
<!-- MainWindow.xaml -->
<TextBox x:Name="txtName" />
<TextBlock x:Name="lblDisplay" />
<Button Content="Show" Click="Button_Click" />
```

```csharp
// MainWindow.xaml.cs
private void Button_Click(object sender, RoutedEventArgs e)
{
    lblDisplay.Text = $"Hello, {txtName.Text}";
    // Logic mixed with UI - Hard to test!
}
```

#### ✅ MVVM Approach (Good):

```xml
<!-- MainWindow.xaml -->
<TextBox Text="{Binding Name, UpdateSourceTrigger=PropertyChanged}" />
<TextBlock Text="{Binding DisplayText}" />
<Button Content="Show" Command="{Binding ShowCommand}" />
```

```csharp
// MainViewModel.cs - Testable!
public class MainViewModel : INotifyPropertyChanged
{
    private string name;
    private string displayText;

    public string Name
    {
        get => name;
        set { name = value; OnPropertyChanged(); }
    }

    public string DisplayText
    {
        get => displayText;
        set { displayText = value; OnPropertyChanged(); }
    }

    public ICommand ShowCommand { get; }

    public MainViewModel()
    {
        ShowCommand = new RelayCommand(ExecuteShow);
    }

    private void ExecuteShow()
    {
        DisplayText = $"Hello, {Name}";
    }

    // INotifyPropertyChanged implementation...
}
```

---

## 2. Model-View-ViewModel

### 2.1. Model

**Model** chứa business objects, data, và validation logic.

```csharp
// Models/Student.cs
public class Student
{
    public int Id { get; set; }
    public string Name { get; set; }
    public string Email { get; set; }
    public int Age { get; set; }
    public double GPA { get; set; }

    // Validation
    public bool IsValid()
    {
        return !string.IsNullOrWhiteSpace(Name) &&
               !string.IsNullOrWhiteSpace(Email) &&
               Age > 0 && Age < 100 &&
               GPA >= 0 && GPA <= 4.0;
    }

    // Business logic
    public string GetClassification()
    {
        if (GPA >= 3.6) return "Xuất sắc";
        if (GPA >= 3.2) return "Giỏi";
        if (GPA >= 2.5) return "Khá";
        if (GPA >= 2.0) return "Trung bình";
        return "Yếu";
    }
}

// Models/Product.cs
public class Product
{
    public int Id { get; set; }
    public string Name { get; set; }
    public decimal Price { get; set; }
    public int Stock { get; set; }
    public string Category { get; set; }

    public decimal GetTotalValue() => Price * Stock;

    public bool IsInStock() => Stock > 0;
}
```

### 2.2. View

**View** chỉ chứa XAML, không có logic (hoặc rất ít).

```xml
<!-- Views/StudentView.xaml -->
<UserControl x:Class="MyApp.Views.StudentView"
             xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="clr-namespace:MyApp.ViewModels">

    <UserControl.DataContext>
        <vm:StudentViewModel />
    </UserControl.DataContext>

    <Grid Margin="20">
        <Grid.RowDefinitions>
            <RowDefinition Height="Auto" />
            <RowDefinition Height="Auto" />
            <RowDefinition Height="Auto" />
            <RowDefinition Height="Auto" />
            <RowDefinition Height="Auto" />
            <RowDefinition Height="*" />
            <RowDefinition Height="Auto" />
        </Grid.RowDefinitions>

        <Grid.ColumnDefinitions>
            <ColumnDefinition Width="Auto" />
            <ColumnDefinition Width="*" />
        </Grid.ColumnDefinitions>

        <!-- Name -->
        <TextBlock Grid.Row="0" Grid.Column="0" Text="Name:" Margin="5" />
        <TextBox Grid.Row="0" Grid.Column="1"
                 Text="{Binding SelectedStudent.Name, UpdateSourceTrigger=PropertyChanged}"
                 Margin="5" />

        <!-- Email -->
        <TextBlock Grid.Row="1" Grid.Column="0" Text="Email:" Margin="5" />
        <TextBox Grid.Row="1" Grid.Column="1"
                 Text="{Binding SelectedStudent.Email, UpdateSourceTrigger=PropertyChanged}"
                 Margin="5" />

        <!-- Age -->
        <TextBlock Grid.Row="2" Grid.Column="0" Text="Age:" Margin="5" />
        <TextBox Grid.Row="2" Grid.Column="1"
                 Text="{Binding SelectedStudent.Age, UpdateSourceTrigger=PropertyChanged}"
                 Margin="5" />

        <!-- GPA -->
        <TextBlock Grid.Row="3" Grid.Column="0" Text="GPA:" Margin="5" />
        <TextBox Grid.Row="3" Grid.Column="1"
                 Text="{Binding SelectedStudent.GPA, UpdateSourceTrigger=PropertyChanged}"
                 Margin="5" />

        <!-- Classification -->
        <TextBlock Grid.Row="4" Grid.Column="0" Text="Classification:" Margin="5" />
        <TextBlock Grid.Row="4" Grid.Column="1"
                   Text="{Binding SelectedStudent.Classification}"
                   FontWeight="Bold"
                   Margin="5" />

        <!-- Student List -->
        <DataGrid Grid.Row="5" Grid.Column="0" Grid.ColumnSpan="2"
                  ItemsSource="{Binding Students}"
                  SelectedItem="{Binding SelectedStudent}"
                  AutoGenerateColumns="False"
                  Margin="5">
            <DataGrid.Columns>
                <DataGridTextColumn Header="ID" Binding="{Binding Id}" Width="50" />
                <DataGridTextColumn Header="Name" Binding="{Binding Name}" Width="*" />
                <DataGridTextColumn Header="Email" Binding="{Binding Email}" Width="*" />
                <DataGridTextColumn Header="Age" Binding="{Binding Age}" Width="50" />
                <DataGridTextColumn Header="GPA" Binding="{Binding GPA}" Width="60" />
            </DataGrid.Columns>
        </DataGrid>

        <!-- Buttons -->
        <StackPanel Grid.Row="6" Grid.Column="0" Grid.ColumnSpan="2"
                    Orientation="Horizontal"
                    HorizontalAlignment="Right"
                    Margin="5">
            <Button Content="Add" Command="{Binding AddCommand}" Width="80" Margin="5" />
            <Button Content="Update" Command="{Binding UpdateCommand}" Width="80" Margin="5" />
            <Button Content="Delete" Command="{Binding DeleteCommand}" Width="80" Margin="5" />
            <Button Content="Clear" Command="{Binding ClearCommand}" Width="80" Margin="5" />
        </StackPanel>
    </Grid>
</UserControl>
```

```csharp
// Views/StudentView.xaml.cs - Code-behind gần như rỗng!
public partial class StudentView : UserControl
{
    public StudentView()
    {
        InitializeComponent();
    }
}
```

### 2.3. ViewModel

**ViewModel** chứa presentation logic, commands, và properties cho View.

```csharp
// ViewModels/StudentViewModel.cs
using System.Collections.ObjectModel;
using System.ComponentModel;
using System.Runtime.CompilerServices;
using System.Windows.Input;

public class StudentViewModel : INotifyPropertyChanged
{
    // Properties
    private Student selectedStudent;
    private ObservableCollection<Student> students;

    public Student SelectedStudent
    {
        get => selectedStudent;
        set
        {
            selectedStudent = value;
            OnPropertyChanged();
            OnPropertyChanged(nameof(Classification));
        }
    }

    public ObservableCollection<Student> Students
    {
        get => students;
        set
        {
            students = value;
            OnPropertyChanged();
        }
    }

    public string Classification => SelectedStudent?.GetClassification() ?? "";

    // Commands
    public ICommand AddCommand { get; }
    public ICommand UpdateCommand { get; }
    public ICommand DeleteCommand { get; }
    public ICommand ClearCommand { get; }

    // Constructor
    public StudentViewModel()
    {
        // Initialize data
        Students = new ObservableCollection<Student>
        {
            new Student { Id = 1, Name = "John Doe", Email = "john@example.com", Age = 20, GPA = 3.5 },
            new Student { Id = 2, Name = "Jane Smith", Email = "jane@example.com", Age = 21, GPA = 3.8 }
        };

        SelectedStudent = new Student();

        // Initialize commands
        AddCommand = new RelayCommand(ExecuteAdd, CanExecuteAdd);
        UpdateCommand = new RelayCommand(ExecuteUpdate, CanExecuteUpdate);
        DeleteCommand = new RelayCommand(ExecuteDelete, CanExecuteDelete);
        ClearCommand = new RelayCommand(ExecuteClear);
    }

    // Add Command
    private void ExecuteAdd()
    {
        if (SelectedStudent.IsValid())
        {
            SelectedStudent.Id = Students.Count + 1;
            Students.Add(new Student
            {
                Id = SelectedStudent.Id,
                Name = SelectedStudent.Name,
                Email = SelectedStudent.Email,
                Age = SelectedStudent.Age,
                GPA = SelectedStudent.GPA
            });
            ExecuteClear();
        }
    }

    private bool CanExecuteAdd()
    {
        return SelectedStudent != null && SelectedStudent.IsValid();
    }

    // Update Command
    private void ExecuteUpdate()
    {
        var existing = Students.FirstOrDefault(s => s.Id == SelectedStudent.Id);
        if (existing != null && SelectedStudent.IsValid())
        {
            existing.Name = SelectedStudent.Name;
            existing.Email = SelectedStudent.Email;
            existing.Age = SelectedStudent.Age;
            existing.GPA = SelectedStudent.GPA;
            OnPropertyChanged(nameof(Students));
        }
    }

    private bool CanExecuteUpdate()
    {
        return SelectedStudent != null &&
               SelectedStudent.Id > 0 &&
               SelectedStudent.IsValid();
    }

    // Delete Command
    private void ExecuteDelete()
    {
        if (SelectedStudent != null)
        {
            Students.Remove(SelectedStudent);
            ExecuteClear();
        }
    }

    private bool CanExecuteDelete()
    {
        return SelectedStudent != null && SelectedStudent.Id > 0;
    }

    // Clear Command
    private void ExecuteClear()
    {
        SelectedStudent = new Student();
    }

    // INotifyPropertyChanged
    public event PropertyChangedEventHandler PropertyChanged;

    protected void OnPropertyChanged([CallerMemberName] string propertyName = null)
    {
        PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(propertyName));
    }
}
```

---

## 3. Data Binding trong MVVM

### 3.1. Binding Modes

```xml
<!-- OneWay: ViewModel -> View (read-only) -->
<TextBlock Text="{Binding Name, Mode=OneWay}" />

<!-- TwoWay: ViewModel <-> View (default cho TextBox.Text) -->
<TextBox Text="{Binding Name, Mode=TwoWay}" />

<!-- OneTime: ViewModel -> View (one time only) -->
<TextBlock Text="{Binding Title, Mode=OneTime}" />

<!-- OneWayToSource: View -> ViewModel -->
<Slider Value="{Binding Volume, Mode=OneWayToSource}" />
```

### 3.2. UpdateSourceTrigger

```xml
<!-- Default: Update khi lose focus -->
<TextBox Text="{Binding Name}" />

<!-- PropertyChanged: Update ngay khi gõ -->
<TextBox Text="{Binding Name, UpdateSourceTrigger=PropertyChanged}" />

<!-- LostFocus: Update khi lose focus -->
<TextBox Text="{Binding Name, UpdateSourceTrigger=LostFocus}" />

<!-- Explicit: Update khi gọi UpdateSource() -->
<TextBox x:Name="txtExplicit"
         Text="{Binding Name, UpdateSourceTrigger=Explicit}" />
```

### 3.3. String Formatting

```xml
<!-- Currency -->
<TextBlock Text="{Binding Price, StringFormat='{}{0:C}'}" />

<!-- Decimal -->
<TextBlock Text="{Binding GPA, StringFormat='{}{0:F2}'}" />

<!-- Date -->
<TextBlock Text="{Binding BirthDate, StringFormat='{}{0:dd/MM/yyyy}'}" />

<!-- Custom format -->
<TextBlock Text="{Binding Count, StringFormat='Total: {0} items'}" />
```

### 3.4. Multi-Binding

```xml
<TextBlock>
    <TextBlock.Text>
        <MultiBinding StringFormat="{}{0} {1}">
            <Binding Path="FirstName" />
            <Binding Path="LastName" />
        </MultiBinding>
    </TextBlock.Text>
</TextBlock>
```

---

## 4. INotifyPropertyChanged

### 4.1. Manual Implementation

```csharp
using System.ComponentModel;
using System.Runtime.CompilerServices;

public class ViewModelBase : INotifyPropertyChanged
{
    public event PropertyChangedEventHandler PropertyChanged;

    protected void OnPropertyChanged([CallerMemberName] string propertyName = null)
    {
        PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(propertyName));
    }

    protected bool SetProperty<T>(ref T field, T value, [CallerMemberName] string propertyName = null)
    {
        if (EqualityComparer<T>.Default.Equals(field, value))
            return false;

        field = value;
        OnPropertyChanged(propertyName);
        return true;
    }
}
```

### 4.2. Usage

```csharp
public class PersonViewModel : ViewModelBase
{
    private string firstName;
    private string lastName;
    private int age;

    // Method 1: Using OnPropertyChanged
    public string FirstName
    {
        get => firstName;
        set
        {
            firstName = value;
            OnPropertyChanged();
            OnPropertyChanged(nameof(FullName)); // Update dependent property
        }
    }

    // Method 2: Using SetProperty
    public string LastName
    {
        get => lastName;
        set
        {
            if (SetProperty(ref lastName, value))
            {
                OnPropertyChanged(nameof(FullName)); // Update dependent property
            }
        }
    }

    public int Age
    {
        get => age;
        set => SetProperty(ref age, value);
    }

    // Computed property
    public string FullName => $"{FirstName} {LastName}";
}
```

### 4.3. ObservableObject (CommunityToolkit.Mvvm)

```csharp
// Install: CommunityToolkit.Mvvm NuGet package

using CommunityToolkit.Mvvm.ComponentModel;

public partial class PersonViewModel : ObservableObject
{
    [ObservableProperty]
    private string firstName;

    [ObservableProperty]
    private string lastName;

    [ObservableProperty]
    private int age;

    // Compiler tự động generate properties với INotifyPropertyChanged!
}
```

---

## 5. ICommand Interface

### 5.1. ICommand Definition

```csharp
public interface ICommand
{
    event EventHandler CanExecuteChanged;
    bool CanExecute(object parameter);
    void Execute(object parameter);
}
```

### 5.2. Usage in ViewModel

```csharp
public class MyViewModel : ViewModelBase
{
    public ICommand SaveCommand { get; }
    public ICommand DeleteCommand { get; }
    public ICommand CancelCommand { get; }

    public MyViewModel()
    {
        SaveCommand = new RelayCommand(ExecuteSave, CanExecuteSave);
        DeleteCommand = new RelayCommand(ExecuteDelete, CanExecuteDelete);
        CancelCommand = new RelayCommand(ExecuteCancel); // Always enabled
    }

    private void ExecuteSave()
    {
        // Save logic
    }

    private bool CanExecuteSave()
    {
        // Return true if can save
        return !string.IsNullOrWhiteSpace(Name);
    }

    private void ExecuteDelete()
    {
        // Delete logic
    }

    private bool CanExecuteDelete()
    {
        return SelectedItem != null;
    }

    private void ExecuteCancel()
    {
        // Cancel logic
    }
}
```

### 5.3. Binding Commands in XAML

```xml
<!-- Simple command -->
<Button Content="Save" Command="{Binding SaveCommand}" />

<!-- Command with parameter -->
<Button Content="Delete"
        Command="{Binding DeleteCommand}"
        CommandParameter="{Binding SelectedItem}" />

<!-- Command in MenuItem -->
<MenuItem Header="Save" Command="{Binding SaveCommand}" />

<!-- Command in KeyBinding -->
<Window.InputBindings>
    <KeyBinding Key="S" Modifiers="Control" Command="{Binding SaveCommand}" />
    <KeyBinding Key="Delete" Command="{Binding DeleteCommand}" />
</Window.InputBindings>
```

---

## 6. RelayCommand Implementation

### 6.1. Basic RelayCommand

```csharp
using System;
using System.Windows.Input;

public class RelayCommand : ICommand
{
    private readonly Action execute;
    private readonly Func<bool> canExecute;

    public event EventHandler CanExecuteChanged
    {
        add { CommandManager.RequerySuggested += value; }
        remove { CommandManager.RequerySuggested -= value; }
    }

    public RelayCommand(Action execute, Func<bool> canExecute = null)
    {
        this.execute = execute ?? throw new ArgumentNullException(nameof(execute));
        this.canExecute = canExecute;
    }

    public bool CanExecute(object parameter)
    {
        return canExecute == null || canExecute();
    }

    public void Execute(object parameter)
    {
        execute();
    }
}
```

### 6.2. Generic RelayCommand

```csharp
public class RelayCommand<T> : ICommand
{
    private readonly Action<T> execute;
    private readonly Func<T, bool> canExecute;

    public event EventHandler CanExecuteChanged
    {
        add { CommandManager.RequerySuggested += value; }
        remove { CommandManager.RequerySuggested -= value; }
    }

    public RelayCommand(Action<T> execute, Func<T, bool> canExecute = null)
    {
        this.execute = execute ?? throw new ArgumentNullException(nameof(execute));
        this.canExecute = canExecute;
    }

    public bool CanExecute(object parameter)
    {
        return canExecute == null || canExecute((T)parameter);
    }

    public void Execute(object parameter)
    {
        execute((T)parameter);
    }
}
```

### 6.3. Usage Examples

```csharp
public class ProductViewModel : ViewModelBase
{
    private Product selectedProduct;

    public ICommand AddCommand { get; }
    public ICommand DeleteCommand { get; }
    public ICommand UpdatePriceCommand { get; }

    public ProductViewModel()
    {
        // Simple command
        AddCommand = new RelayCommand(ExecuteAdd, CanExecuteAdd);

        // Generic command with parameter
        DeleteCommand = new RelayCommand<Product>(ExecuteDelete, CanExecuteDelete);

        // Command with decimal parameter
        UpdatePriceCommand = new RelayCommand<decimal>(ExecuteUpdatePrice);
    }

    private void ExecuteAdd()
    {
        Products.Add(new Product());
    }

    private bool CanExecuteAdd()
    {
        return Products.Count < 100;
    }

    private void ExecuteDelete(Product product)
    {
        Products.Remove(product);
    }

    private bool CanExecuteDelete(Product product)
    {
        return product != null;
    }

    private void ExecuteUpdatePrice(decimal newPrice)
    {
        if (SelectedProduct != null)
        {
            SelectedProduct.Price = newPrice;
        }
    }
}
```

### 6.4. CommunityToolkit.Mvvm RelayCommand

```csharp
// Install: CommunityToolkit.Mvvm NuGet package

using CommunityToolkit.Mvvm.ComponentModel;
using CommunityToolkit.Mvvm.Input;

public partial class MyViewModel : ObservableObject
{
    [ObservableProperty]
    private string name;

    // Tự động generate SaveCommand
    [RelayCommand]
    private void Save()
    {
        // Save logic
    }

    // Tự động generate DeleteCommand với CanExecute
    [RelayCommand(CanExecute = nameof(CanDelete))]
    private void Delete()
    {
        // Delete logic
    }

    private bool CanDelete()
    {
        return !string.IsNullOrEmpty(Name);
    }

    // Generic command với parameter
    [RelayCommand]
    private void UpdatePrice(decimal newPrice)
    {
        // Update price logic
    }

    // Async command
    [RelayCommand]
    private async Task LoadDataAsync()
    {
        await Task.Delay(1000);
        // Load data...
    }
}
```

---

## 7. Dependency Injection

### 7.1. Service Interface

```csharp
// Services/IDataService.cs
public interface IDataService
{
    Task<List<Student>> GetStudentsAsync();
    Task<Student> GetStudentByIdAsync(int id);
    Task AddStudentAsync(Student student);
    Task UpdateStudentAsync(Student student);
    Task DeleteStudentAsync(int id);
}

// Services/StudentDataService.cs
public class StudentDataService : IDataService
{
    private List<Student> students = new List<Student>();

    public async Task<List<Student>> GetStudentsAsync()
    {
        await Task.Delay(100); // Simulate API call
        return students;
    }

    public async Task<Student> GetStudentByIdAsync(int id)
    {
        await Task.Delay(50);
        return students.FirstOrDefault(s => s.Id == id);
    }

    public async Task AddStudentAsync(Student student)
    {
        await Task.Delay(50);
        student.Id = students.Any() ? students.Max(s => s.Id) + 1 : 1;
        students.Add(student);
    }

    public async Task UpdateStudentAsync(Student student)
    {
        await Task.Delay(50);
        var existing = students.FirstOrDefault(s => s.Id == student.Id);
        if (existing != null)
        {
            existing.Name = student.Name;
            existing.Email = student.Email;
            existing.Age = student.Age;
            existing.GPA = student.GPA;
        }
    }

    public async Task DeleteStudentAsync(int id)
    {
        await Task.Delay(50);
        var student = students.FirstOrDefault(s => s.Id == id);
        if (student != null)
            students.Remove(student);
    }
}
```

### 7.2. ViewModel with DI

```csharp
public class StudentViewModel : ViewModelBase
{
    private readonly IDataService dataService;
    private ObservableCollection<Student> students;
    private bool isLoading;

    public ObservableCollection<Student> Students
    {
        get => students;
        set => SetProperty(ref students, value);
    }

    public bool IsLoading
    {
        get => isLoading;
        set => SetProperty(ref isLoading, value);
    }

    // Constructor injection
    public StudentViewModel(IDataService dataService)
    {
        this.dataService = dataService;

        LoadCommand = new RelayCommand(async () => await LoadDataAsync());
        AddCommand = new RelayCommand<Student>(async (s) => await AddStudentAsync(s));
        DeleteCommand = new RelayCommand<int>(async (id) => await DeleteStudentAsync(id));

        // Load initial data
        LoadCommand.Execute(null);
    }

    private async Task LoadDataAsync()
    {
        IsLoading = true;
        try
        {
            var data = await dataService.GetStudentsAsync();
            Students = new ObservableCollection<Student>(data);
        }
        finally
        {
            IsLoading = false;
        }
    }

    private async Task AddStudentAsync(Student student)
    {
        IsLoading = true;
        try
        {
            await dataService.AddStudentAsync(student);
            await LoadDataAsync();
        }
        finally
        {
            IsLoading = false;
        }
    }

    private async Task DeleteStudentAsync(int id)
    {
        IsLoading = true;
        try
        {
            await dataService.DeleteStudentAsync(id);
            await LoadDataAsync();
        }
        finally
        {
            IsLoading = false;
        }
    }

    public ICommand LoadCommand { get; }
    public ICommand AddCommand { get; }
    public ICommand DeleteCommand { get; }
}
```

### 7.3. DI Container Setup (Microsoft.Extensions.DependencyInjection)

```csharp
// App.xaml.cs
using Microsoft.Extensions.DependencyInjection;
using System.Windows;

public partial class App : Application
{
    private ServiceProvider serviceProvider;

    public App()
    {
        ServiceCollection services = new ServiceCollection();
        ConfigureServices(services);
        serviceProvider = services.BuildServiceProvider();
    }

    private void ConfigureServices(ServiceCollection services)
    {
        // Register services
        services.AddSingleton<IDataService, StudentDataService>();

        // Register ViewModels
        services.AddTransient<StudentViewModel>();
        services.AddTransient<ProductViewModel>();

        // Register Views
        services.AddTransient<MainWindow>();
    }

    protected override void OnStartup(StartupEventArgs e)
    {
        base.OnStartup(e);

        var mainWindow = serviceProvider.GetService<MainWindow>();
        mainWindow.Show();
    }
}
```

```csharp
// MainWindow.xaml.cs
public partial class MainWindow : Window
{
    public MainWindow(StudentViewModel viewModel)
    {
        InitializeComponent();
        DataContext = viewModel; // Injected ViewModel
    }
}
```

---

## 8. MVVM Frameworks

### 8.1. CommunityToolkit.Mvvm (Recommended)

**Installation:**
```bash
Install-Package CommunityToolkit.Mvvm
```

**Features:**
- Source generators
- `ObservableObject`
- `RelayCommand`
- `ObservableProperty` attribute
- Async commands

**Example:**
```csharp
using CommunityToolkit.Mvvm.ComponentModel;
using CommunityToolkit.Mvvm.Input;

public partial class PersonViewModel : ObservableObject
{
    [ObservableProperty]
    private string firstName;

    [ObservableProperty]
    private string lastName;

    [ObservableProperty]
    [NotifyPropertyChangedFor(nameof(FullName))]
    private string middleName;

    public string FullName => $"{FirstName} {MiddleName} {LastName}";

    [RelayCommand]
    private void Save()
    {
        // Save logic
    }

    [RelayCommand(CanExecute = nameof(CanDelete))]
    private void Delete()
    {
        // Delete logic
    }

    private bool CanDelete() => !string.IsNullOrEmpty(FirstName);

    [RelayCommand]
    private async Task LoadAsync()
    {
        await Task.Delay(1000);
        // Load data
    }
}
```

### 8.2. Prism

**Installation:**
```bash
Install-Package Prism.Wpf
Install-Package Prism.DryIoc
```

**Features:**
- Navigation
- Modules
- Event Aggregator
- Dialog Service
- DI Container

### 8.3. MVVM Light Toolkit (Deprecated)

Không còn được maintain, nên chuyển sang CommunityToolkit.Mvvm.

### 8.4. Caliburn.Micro

**Features:**
- Convention-based naming
- Action messages
- Coroutines
- Screen lifecycle

---

## 9. Best Practices

### 9.1. Do's ✅

```csharp
// ✅ Use ObservableCollection for collections
public ObservableCollection<Student> Students { get; set; }

// ✅ Implement INotifyPropertyChanged
public class MyViewModel : INotifyPropertyChanged { }

// ✅ Use Commands instead of Click events
public ICommand SaveCommand { get; }

// ✅ Use Dependency Injection
public MyViewModel(IDataService dataService) { }

// ✅ Keep ViewModel testable
[Test]
public void AddStudent_ShouldAddToCollection()
{
    var viewModel = new StudentViewModel(new MockDataService());
    var student = new Student { Name = "Test" };

    viewModel.AddCommand.Execute(student);

    Assert.That(viewModel.Students.Count, Is.EqualTo(1));
}

// ✅ Use async/await for long operations
private async Task LoadDataAsync()
{
    IsLoading = true;
    var data = await dataService.GetDataAsync();
    IsLoading = false;
}
```

### 9.2. Don'ts ❌

```csharp
// ❌ Don't reference View in ViewModel
public class MyViewModel
{
    private MainWindow window; // BAD!
}

// ❌ Don't use List<T> for binding
public List<Student> Students { get; set; } // BAD! Use ObservableCollection

// ❌ Don't put business logic in View
private void Button_Click(object sender, RoutedEventArgs e)
{
    // Business logic here // BAD!
}

// ❌ Don't forget to raise PropertyChanged
public string Name
{
    get => name;
    set { name = value; } // BAD! Missing OnPropertyChanged()
}

// ❌ Don't use code-behind for logic
public partial class MainWindow : Window
{
    private void SaveData() // BAD! Should be in ViewModel
    {
        // Save logic...
    }
}
```

### 9.3. Folder Structure

```
MyWPFApp/
├── Models/
│   ├── Student.cs
│   ├── Product.cs
│   └── Order.cs
├── ViewModels/
│   ├── ViewModelBase.cs
│   ├── StudentViewModel.cs
│   ├── ProductViewModel.cs
│   └── MainViewModel.cs
├── Views/
│   ├── StudentView.xaml
│   ├── ProductView.xaml
│   └── MainWindow.xaml
├── Services/
│   ├── IDataService.cs
│   ├── StudentDataService.cs
│   └── ApiService.cs
├── Commands/
│   ├── RelayCommand.cs
│   └── AsyncRelayCommand.cs
├── Converters/
│   ├── BoolToVisibilityConverter.cs
│   └── DateTimeFormatConverter.cs
└── Resources/
    ├── Styles.xaml
    └── Images/
```

---

## 10. Dự Án Thực Tế

### 10.1. Todo List App với MVVM

#### Model:
```csharp
// Models/TodoItem.cs
public class TodoItem : INotifyPropertyChanged
{
    private string title;
    private bool isCompleted;
    private DateTime dueDate;

    public int Id { get; set; }

    public string Title
    {
        get => title;
        set
        {
            title = value;
            OnPropertyChanged();
        }
    }

    public bool IsCompleted
    {
        get => isCompleted;
        set
        {
            isCompleted = value;
            OnPropertyChanged();
        }
    }

    public DateTime DueDate
    {
        get => dueDate;
        set
        {
            dueDate = value;
            OnPropertyChanged();
        }
    }

    public event PropertyChangedEventHandler PropertyChanged;
    protected void OnPropertyChanged([CallerMemberName] string name = null)
    {
        PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(name));
    }
}
```

#### ViewModel:
```csharp
// ViewModels/TodoViewModel.cs
using CommunityToolkit.Mvvm.ComponentModel;
using CommunityToolkit.Mvvm.Input;

public partial class TodoViewModel : ObservableObject
{
    [ObservableProperty]
    private ObservableCollection<TodoItem> todoItems;

    [ObservableProperty]
    private TodoItem selectedItem;

    [ObservableProperty]
    private string newTodoTitle;

    [ObservableProperty]
    private DateTime newTodoDueDate = DateTime.Today;

    public TodoViewModel()
    {
        TodoItems = new ObservableCollection<TodoItem>
        {
            new TodoItem { Id = 1, Title = "Learn MVVM", IsCompleted = false, DueDate = DateTime.Today },
            new TodoItem { Id = 2, Title = "Build WPF App", IsCompleted = false, DueDate = DateTime.Today.AddDays(1) }
        };
    }

    [RelayCommand]
    private void AddTodo()
    {
        if (!string.IsNullOrWhiteSpace(NewTodoTitle))
        {
            TodoItems.Add(new TodoItem
            {
                Id = TodoItems.Count + 1,
                Title = NewTodoTitle,
                IsCompleted = false,
                DueDate = NewTodoDueDate
            });

            NewTodoTitle = string.Empty;
            NewTodoDueDate = DateTime.Today;
        }
    }

    [RelayCommand(CanExecute = nameof(CanDeleteTodo))]
    private void DeleteTodo()
    {
        if (SelectedItem != null)
        {
            TodoItems.Remove(SelectedItem);
            SelectedItem = null;
        }
    }

    private bool CanDeleteTodo() => SelectedItem != null;

    [RelayCommand]
    private void ToggleComplete(TodoItem item)
    {
        if (item != null)
        {
            item.IsCompleted = !item.IsCompleted;
        }
    }

    [RelayCommand]
    private void ClearCompleted()
    {
        var completed = TodoItems.Where(t => t.IsCompleted).ToList();
        foreach (var item in completed)
        {
            TodoItems.Remove(item);
        }
    }
}
```

#### View:
```xml
<!-- Views/TodoView.xaml -->
<UserControl x:Class="TodoApp.Views.TodoView"
             xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="clr-namespace:TodoApp.ViewModels">

    <UserControl.DataContext>
        <vm:TodoViewModel />
    </UserControl.DataContext>

    <Grid Margin="20">
        <Grid.RowDefinitions>
            <RowDefinition Height="Auto" />
            <RowDefinition Height="*" />
            <RowDefinition Height="Auto" />
        </Grid.RowDefinitions>

        <!-- Add Todo Section -->
        <StackPanel Grid.Row="0" Margin="0,0,0,20">
            <TextBlock Text="Add New Todo" FontSize="18" FontWeight="Bold" Margin="0,0,0,10" />

            <Grid>
                <Grid.ColumnDefinitions>
                    <ColumnDefinition Width="*" />
                    <ColumnDefinition Width="Auto" />
                    <ColumnDefinition Width="Auto" />
                </Grid.ColumnDefinitions>

                <TextBox Grid.Column="0"
                         Text="{Binding NewTodoTitle, UpdateSourceTrigger=PropertyChanged}"
                         Margin="0,0,10,0" />

                <DatePicker Grid.Column="1"
                            SelectedDate="{Binding NewTodoDueDate}"
                            Margin="0,0,10,0" />

                <Button Grid.Column="2"
                        Content="Add"
                        Command="{Binding AddTodoCommand}"
                        Width="80" />
            </Grid>
        </StackPanel>

        <!-- Todo List -->
        <ListBox Grid.Row="1"
                 ItemsSource="{Binding TodoItems}"
                 SelectedItem="{Binding SelectedItem}">
            <ListBox.ItemTemplate>
                <DataTemplate>
                    <Grid Margin="5">
                        <Grid.ColumnDefinitions>
                            <ColumnDefinition Width="Auto" />
                            <ColumnDefinition Width="*" />
                            <ColumnDefinition Width="Auto" />
                        </Grid.ColumnDefinitions>

                        <CheckBox Grid.Column="0"
                                  IsChecked="{Binding IsCompleted}"
                                  Command="{Binding DataContext.ToggleCompleteCommand, RelativeSource={RelativeSource AncestorType=UserControl}}"
                                  CommandParameter="{Binding}"
                                  Margin="0,0,10,0" />

                        <StackPanel Grid.Column="1">
                            <TextBlock Text="{Binding Title}"
                                       FontSize="14">
                                <TextBlock.Style>
                                    <Style TargetType="TextBlock">
                                        <Style.Triggers>
                                            <DataTrigger Binding="{Binding IsCompleted}" Value="True">
                                                <Setter Property="TextDecorations" Value="Strikethrough" />
                                                <Setter Property="Foreground" Value="Gray" />
                                            </DataTrigger>
                                        </Style.Triggers>
                                    </Style>
                                </TextBlock.Style>
                            </TextBlock>

                            <TextBlock Text="{Binding DueDate, StringFormat='Due: {0:dd/MM/yyyy}'}"
                                       FontSize="10"
                                       Foreground="Gray" />
                        </StackPanel>
                    </Grid>
                </DataTemplate>
            </ListBox.ItemTemplate>
        </ListBox>

        <!-- Action Buttons -->
        <StackPanel Grid.Row="2" Orientation="Horizontal" HorizontalAlignment="Right" Margin="0,10,0,0">
            <Button Content="Delete Selected"
                    Command="{Binding DeleteTodoCommand}"
                    Width="120"
                    Margin="0,0,10,0" />

            <Button Content="Clear Completed"
                    Command="{Binding ClearCompletedCommand}"
                    Width="120" />
        </StackPanel>
    </Grid>
</UserControl>
```

---

## 📝 Tóm Tắt

### Key Points:

1. **MVVM** tách biệt UI, presentation logic, và business logic
2. **Model**: Business objects và data
3. **View**: XAML UI, ít hoặc không có code-behind
4. **ViewModel**: Presentation logic, commands, properties
5. **INotifyPropertyChanged** để notify UI khi data thay đổi
6. **ICommand** để handle user actions
7. **Dependency Injection** để inject services vào ViewModel
8. **CommunityToolkit.Mvvm** là framework MVVM hiện đại, recommended

### Best Practices:

- ✅ ViewModel không reference View
- ✅ Sử dụng Commands thay vì Events
- ✅ Implement INotifyPropertyChanged
- ✅ Sử dụng ObservableCollection
- ✅ Unit test ViewModels
- ✅ Sử dụng Dependency Injection
- ✅ Async/await cho long operations

---

**Next:** [05-Web-API-Integration.md](05-Web-API-Integration.md)
