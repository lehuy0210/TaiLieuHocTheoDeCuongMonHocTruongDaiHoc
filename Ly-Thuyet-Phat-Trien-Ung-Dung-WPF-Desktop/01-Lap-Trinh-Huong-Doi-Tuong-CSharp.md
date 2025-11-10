# LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG TRONG C#

## 📚 Mục Lục

1. [Giới Thiệu OOP](#1-giới-thiệu-oop)
2. [4 Tính Chất OOP](#2-bốn-tính-chất-oop)
3. [Class và Object](#3-class-và-object)
4. [Properties và Methods](#4-properties-và-methods)
5. [Constructors và Destructors](#5-constructors-và-destructors)
6. [Interface](#6-interface)
7. [Abstract Class](#7-abstract-class)
8. [SOLID Principles](#8-solid-principles)
9. [Design Patterns Cơ Bản](#9-design-patterns-cơ-bản)
10. [Bài Tập Thực Hành](#10-bài-tập-thực-hành)

---

## 1. Giới Thiệu OOP

### 1.1. OOP Là Gì?

**Lập trình hướng đối tượng (Object-Oriented Programming - OOP)** là một mô hình lập trình dựa trên khái niệm "đối tượng", có chứa dữ liệu (thuộc tính) và mã nguồn (phương thức).

### 1.2. Tại Sao Sử Dụng OOP?

- ✅ **Tái sử dụng code**: Giảm duplicate code
- ✅ **Dễ bảo trì**: Code có cấu trúc rõ ràng
- ✅ **Dễ mở rộng**: Thêm tính năng mới dễ dàng
- ✅ **Bảo mật tốt**: Encapsulation che giấu thông tin
- ✅ **Mô phỏng thế giới thực**: Gần với tư duy con người

### 1.3. So Sánh OOP vs Procedural Programming

| Procedural Programming | Object-Oriented Programming |
|------------------------|------------------------------|
| Tập trung vào functions | Tập trung vào objects |
| Data và functions tách biệt | Data và functions gắn liền |
| Top-down approach | Bottom-up approach |
| Khó bảo trì với dự án lớn | Dễ bảo trì và mở rộng |

---

## 2. Bốn Tính Chất OOP

### 2.1. Encapsulation (Tính Đóng Gói)

**Định nghĩa**: Che giấu thông tin bên trong object, chỉ cho phép truy cập qua các phương thức public.

#### Access Modifiers trong C#:

```csharp
public    // Truy cập từ mọi nơi
private   // Chỉ truy cập trong class
protected // Truy cập trong class và class con
internal  // Truy cập trong cùng assembly
protected internal // Kết hợp protected và internal
private protected  // Kết hợp private và protected (C# 7.2+)
```

#### Ví Dụ Encapsulation:

```csharp
public class BankAccount
{
    // Private field - không thể truy cập trực tiếp từ bên ngoài
    private decimal balance;

    // Public property - truy cập có kiểm soát
    public decimal Balance
    {
        get { return balance; }
        private set // Chỉ set được trong class
        {
            if (value >= 0)
                balance = value;
            else
                throw new ArgumentException("Balance không thể âm");
        }
    }

    // Constructor
    public BankAccount(decimal initialBalance)
    {
        Balance = initialBalance;
    }

    // Public method
    public void Deposit(decimal amount)
    {
        if (amount <= 0)
            throw new ArgumentException("Số tiền phải > 0");

        Balance += amount;
        Console.WriteLine($"Đã nạp {amount:C}. Số dư: {Balance:C}");
    }

    public bool Withdraw(decimal amount)
    {
        if (amount <= 0)
            throw new ArgumentException("Số tiền phải > 0");

        if (amount > Balance)
        {
            Console.WriteLine("Số dư không đủ!");
            return false;
        }

        Balance -= amount;
        Console.WriteLine($"Đã rút {amount:C}. Số dư: {Balance:C}");
        return true;
    }
}

// Sử dụng
class Program
{
    static void Main()
    {
        BankAccount account = new BankAccount(1000);

        // OK - sử dụng public method
        account.Deposit(500);
        account.Withdraw(200);

        // OK - đọc balance
        Console.WriteLine($"Số dư hiện tại: {account.Balance:C}");

        // ERROR - không thể set Balance từ bên ngoài
        // account.Balance = -100; // Compile error

        // ERROR - không thể truy cập private field
        // account.balance = 5000; // Compile error
    }
}
```

**Lợi ích**:
- Bảo vệ dữ liệu khỏi truy cập trái phép
- Kiểm soát cách dữ liệu được thay đổi
- Dễ maintain và debug

---

### 2.2. Inheritance (Tính Kế Thừa)

**Định nghĩa**: Class con kế thừa thuộc tính và phương thức từ class cha.

#### Ví Dụ Inheritance:

```csharp
// Base class (class cha)
public class Animal
{
    public string Name { get; set; }
    public int Age { get; set; }

    public Animal(string name, int age)
    {
        Name = name;
        Age = age;
    }

    public virtual void MakeSound()
    {
        Console.WriteLine("Animal makes a sound");
    }

    public void Sleep()
    {
        Console.WriteLine($"{Name} is sleeping");
    }
}

// Derived class (class con)
public class Dog : Animal
{
    public string Breed { get; set; }

    // Constructor gọi constructor của base class
    public Dog(string name, int age, string breed) : base(name, age)
    {
        Breed = breed;
    }

    // Override method của base class
    public override void MakeSound()
    {
        Console.WriteLine($"{Name} says: Woof! Woof!");
    }

    // Method riêng của Dog
    public void Fetch()
    {
        Console.WriteLine($"{Name} is fetching the ball");
    }
}

public class Cat : Animal
{
    public Cat(string name, int age) : base(name, age)
    {
    }

    public override void MakeSound()
    {
        Console.WriteLine($"{Name} says: Meow!");
    }

    public void Scratch()
    {
        Console.WriteLine($"{Name} is scratching");
    }
}

// Sử dụng
class Program
{
    static void Main()
    {
        Dog dog = new Dog("Buddy", 3, "Golden Retriever");
        Cat cat = new Cat("Whiskers", 2);

        // Sử dụng method từ base class
        dog.Sleep();  // Output: Buddy is sleeping
        cat.Sleep();  // Output: Whiskers is sleeping

        // Sử dụng overridden method
        dog.MakeSound();  // Output: Buddy says: Woof! Woof!
        cat.MakeSound();  // Output: Whiskers says: Meow!

        // Sử dụng method riêng
        dog.Fetch();      // Output: Buddy is fetching the ball
        cat.Scratch();    // Output: Whiskers is scratching

        // Polymorphism
        Animal animal1 = new Dog("Max", 5, "Labrador");
        Animal animal2 = new Cat("Fluffy", 1);

        animal1.MakeSound();  // Output: Max says: Woof! Woof!
        animal2.MakeSound();  // Output: Fluffy says: Meow!
    }
}
```

#### Sealed Class (Ngăn Kế Thừa):

```csharp
// Sealed class - không thể kế thừa
public sealed class FinalDog : Animal
{
    public FinalDog(string name, int age) : base(name, age)
    {
    }

    public override void MakeSound()
    {
        Console.WriteLine("Final dog barks!");
    }
}

// ERROR - không thể kế thừa từ sealed class
// public class SuperDog : FinalDog { } // Compile error
```

**Lợi ích**:
- Tái sử dụng code
- Tạo hierarchy rõ ràng
- Dễ mở rộng chức năng

---

### 2.3. Polymorphism (Tính Đa Hình)

**Định nghĩa**: Một method có thể có nhiều hình thái khác nhau.

#### 2.3.1. Compile-time Polymorphism (Method Overloading)

```csharp
public class Calculator
{
    // Overloading - cùng tên, khác parameters
    public int Add(int a, int b)
    {
        return a + b;
    }

    public double Add(double a, double b)
    {
        return a + b;
    }

    public int Add(int a, int b, int c)
    {
        return a + b + c;
    }

    public string Add(string a, string b)
    {
        return a + b;
    }
}

// Sử dụng
Calculator calc = new Calculator();
Console.WriteLine(calc.Add(5, 3));           // Output: 8
Console.WriteLine(calc.Add(5.5, 3.2));       // Output: 8.7
Console.WriteLine(calc.Add(1, 2, 3));        // Output: 6
Console.WriteLine(calc.Add("Hello", " World")); // Output: Hello World
```

#### 2.3.2. Runtime Polymorphism (Method Overriding)

```csharp
public class Shape
{
    public virtual double CalculateArea()
    {
        return 0;
    }

    public virtual void Draw()
    {
        Console.WriteLine("Drawing a shape");
    }
}

public class Circle : Shape
{
    public double Radius { get; set; }

    public Circle(double radius)
    {
        Radius = radius;
    }

    public override double CalculateArea()
    {
        return Math.PI * Radius * Radius;
    }

    public override void Draw()
    {
        Console.WriteLine("Drawing a circle");
    }
}

public class Rectangle : Shape
{
    public double Width { get; set; }
    public double Height { get; set; }

    public Rectangle(double width, double height)
    {
        Width = width;
        Height = height;
    }

    public override double CalculateArea()
    {
        return Width * Height;
    }

    public override void Draw()
    {
        Console.WriteLine("Drawing a rectangle");
    }
}

// Sử dụng - Runtime Polymorphism
class Program
{
    static void Main()
    {
        // Array of shapes
        Shape[] shapes = new Shape[]
        {
            new Circle(5),
            new Rectangle(4, 6),
            new Circle(3)
        };

        // Polymorphic behavior
        foreach (Shape shape in shapes)
        {
            shape.Draw();
            Console.WriteLine($"Area: {shape.CalculateArea():F2}\n");
        }

        // Output:
        // Drawing a circle
        // Area: 78.54
        //
        // Drawing a rectangle
        // Area: 24.00
        //
        // Drawing a circle
        // Area: 28.27
    }
}
```

**Lợi ích**:
- Code linh hoạt hơn
- Dễ mở rộng
- Giảm code duplication

---

### 2.4. Abstraction (Tính Trừu Tượng)

**Định nghĩa**: Ẩn đi chi tiết implementation, chỉ hiển thị những gì cần thiết.

#### Ví Dụ với Abstract Class:

```csharp
// Abstract class - không thể khởi tạo trực tiếp
public abstract class Vehicle
{
    public string Brand { get; set; }
    public string Model { get; set; }

    // Abstract method - bắt buộc override
    public abstract void Start();
    public abstract void Stop();

    // Virtual method - có thể override
    public virtual void Honk()
    {
        Console.WriteLine("Beep beep!");
    }

    // Normal method
    public void DisplayInfo()
    {
        Console.WriteLine($"Brand: {Brand}, Model: {Model}");
    }
}

public class Car : Vehicle
{
    public int NumberOfDoors { get; set; }

    public override void Start()
    {
        Console.WriteLine("Car engine started");
    }

    public override void Stop()
    {
        Console.WriteLine("Car engine stopped");
    }
}

public class Motorcycle : Vehicle
{
    public bool HasSidecar { get; set; }

    public override void Start()
    {
        Console.WriteLine("Motorcycle engine started");
    }

    public override void Stop()
    {
        Console.WriteLine("Motorcycle engine stopped");
    }

    public override void Honk()
    {
        Console.WriteLine("Beep beep beep!"); // Custom honk
    }
}

// Sử dụng
class Program
{
    static void Main()
    {
        // ERROR - không thể khởi tạo abstract class
        // Vehicle vehicle = new Vehicle(); // Compile error

        Car car = new Car { Brand = "Toyota", Model = "Camry", NumberOfDoors = 4 };
        Motorcycle bike = new Motorcycle { Brand = "Honda", Model = "CBR", HasSidecar = false };

        car.DisplayInfo();
        car.Start();
        car.Honk();
        car.Stop();

        Console.WriteLine();

        bike.DisplayInfo();
        bike.Start();
        bike.Honk();
        bike.Stop();
    }
}
```

**Lợi ích**:
- Giảm complexity
- Tập trung vào chức năng chính
- Dễ maintain

---

## 3. Class và Object

### 3.1. Class

**Class** là blueprint (bản thiết kế) để tạo ra objects.

```csharp
public class Student
{
    // Fields (private)
    private string studentId;

    // Properties (public)
    public string Name { get; set; }
    public int Age { get; set; }
    public double GPA { get; set; }

    // Auto-implemented property
    public string Email { get; set; }

    // Property with backing field
    public string StudentId
    {
        get { return studentId; }
        set
        {
            if (string.IsNullOrWhiteSpace(value))
                throw new ArgumentException("Student ID không được rỗng");
            studentId = value;
        }
    }

    // Constructor
    public Student(string id, string name, int age)
    {
        StudentId = id;
        Name = name;
        Age = age;
        GPA = 0.0;
    }

    // Method
    public void DisplayInfo()
    {
        Console.WriteLine($"ID: {StudentId}");
        Console.WriteLine($"Name: {Name}");
        Console.WriteLine($"Age: {Age}");
        Console.WriteLine($"GPA: {GPA:F2}");
    }

    public string GetClassification()
    {
        if (GPA >= 3.6) return "Xuất sắc";
        if (GPA >= 3.2) return "Giỏi";
        if (GPA >= 2.5) return "Khá";
        if (GPA >= 2.0) return "Trung bình";
        return "Yếu";
    }
}
```

### 3.2. Object

**Object** là instance của class.

```csharp
// Tạo object
Student student1 = new Student("SV001", "Nguyễn Văn A", 20);
student1.Email = "nva@university.edu";
student1.GPA = 3.5;

Student student2 = new Student("SV002", "Trần Thị B", 21);
student2.Email = "ttb@university.edu";
student2.GPA = 3.8;

// Sử dụng object
student1.DisplayInfo();
Console.WriteLine($"Xếp loại: {student1.GetClassification()}");

// Object initializer (C# 3.0+)
Student student3 = new Student("SV003", "Lê Văn C", 19)
{
    Email = "lvc@university.edu",
    GPA = 2.8
};
```

---

## 4. Properties và Methods

### 4.1. Properties

#### Auto-implemented Properties:

```csharp
public class Person
{
    // Auto-implemented properties
    public string FirstName { get; set; }
    public string LastName { get; set; }

    // Read-only auto-property (C# 6.0+)
    public DateTime BirthDate { get; }

    // Property with default value (C# 6.0+)
    public string Country { get; set; } = "Vietnam";

    // Computed property
    public string FullName => $"{FirstName} {LastName}";

    public int Age => DateTime.Now.Year - BirthDate.Year;

    public Person(DateTime birthDate)
    {
        BirthDate = birthDate; // Chỉ set được trong constructor
    }
}
```

#### Properties with Validation:

```csharp
public class Product
{
    private decimal price;
    private int quantity;

    public string Name { get; set; }

    public decimal Price
    {
        get => price;
        set
        {
            if (value < 0)
                throw new ArgumentException("Giá không thể âm");
            price = value;
        }
    }

    public int Quantity
    {
        get => quantity;
        set
        {
            if (value < 0)
                throw new ArgumentException("Số lượng không thể âm");
            quantity = value;
        }
    }

    public decimal TotalValue => Price * Quantity;
}
```

### 4.2. Methods

#### Method Types:

```csharp
public class MathOperations
{
    // Instance method
    public int Add(int a, int b)
    {
        return a + b;
    }

    // Static method
    public static int Multiply(int a, int b)
    {
        return a * b;
    }

    // Method with optional parameters
    public int Calculate(int a, int b = 10, int c = 5)
    {
        return a + b + c;
    }

    // Method with params keyword
    public int Sum(params int[] numbers)
    {
        return numbers.Sum();
    }

    // Method with ref parameter
    public void Swap(ref int a, ref int b)
    {
        int temp = a;
        a = b;
        b = temp;
    }

    // Method with out parameter
    public bool TryDivide(int a, int b, out double result)
    {
        if (b == 0)
        {
            result = 0;
            return false;
        }
        result = (double)a / b;
        return true;
    }

    // Extension method (must be static in static class)
}

// Extension methods
public static class StringExtensions
{
    public static bool IsValidEmail(this string email)
    {
        return email.Contains("@") && email.Contains(".");
    }

    public static string Capitalize(this string text)
    {
        if (string.IsNullOrEmpty(text))
            return text;
        return char.ToUpper(text[0]) + text.Substring(1).ToLower();
    }
}

// Sử dụng
class Program
{
    static void Main()
    {
        MathOperations math = new MathOperations();

        // Instance method
        Console.WriteLine(math.Add(5, 3));

        // Static method
        Console.WriteLine(MathOperations.Multiply(5, 3));

        // Optional parameters
        Console.WriteLine(math.Calculate(1));        // 1 + 10 + 5 = 16
        Console.WriteLine(math.Calculate(1, 2));     // 1 + 2 + 5 = 8
        Console.WriteLine(math.Calculate(1, 2, 3));  // 1 + 2 + 3 = 6

        // Params
        Console.WriteLine(math.Sum(1, 2, 3, 4, 5));  // 15

        // Ref
        int x = 10, y = 20;
        math.Swap(ref x, ref y);
        Console.WriteLine($"x={x}, y={y}");  // x=20, y=10

        // Out
        if (math.TryDivide(10, 2, out double result))
            Console.WriteLine($"Result: {result}");

        // Extension method
        string email = "test@example.com";
        Console.WriteLine(email.IsValidEmail());  // True

        string name = "JOHN";
        Console.WriteLine(name.Capitalize());  // John
    }
}
```

---

## 5. Constructors và Destructors

### 5.1. Constructors

```csharp
public class Employee
{
    public string Name { get; set; }
    public string Department { get; set; }
    public decimal Salary { get; set; }

    // Default constructor
    public Employee()
    {
        Name = "Unknown";
        Department = "Unassigned";
        Salary = 0;
    }

    // Parameterized constructor
    public Employee(string name, string department)
    {
        Name = name;
        Department = department;
        Salary = 10000; // Default salary
    }

    // Constructor with all parameters
    public Employee(string name, string department, decimal salary)
    {
        Name = name;
        Department = department;
        Salary = salary;
    }

    // Constructor chaining
    public Employee(string name) : this(name, "General", 10000)
    {
    }

    // Static constructor
    static Employee()
    {
        Console.WriteLine("Static constructor called once");
    }
}

// Sử dụng
Employee emp1 = new Employee();
Employee emp2 = new Employee("John");
Employee emp3 = new Employee("Jane", "IT");
Employee emp4 = new Employee("Bob", "HR", 15000);
```

### 5.2. Destructors (Finalizers)

```csharp
public class FileManager
{
    private string filePath;

    public FileManager(string path)
    {
        filePath = path;
        Console.WriteLine($"FileManager created for {filePath}");
    }

    // Destructor
    ~FileManager()
    {
        // Cleanup code
        Console.WriteLine($"FileManager destroyed for {filePath}");
        // NOTE: Trong thực tế, nên sử dụng IDisposable thay vì destructor
    }
}

// Sử dụng IDisposable (Best Practice)
public class DatabaseConnection : IDisposable
{
    private bool disposed = false;

    public void Connect()
    {
        Console.WriteLine("Connected to database");
    }

    public void Disconnect()
    {
        Console.WriteLine("Disconnected from database");
    }

    public void Dispose()
    {
        Dispose(true);
        GC.SuppressFinalize(this);
    }

    protected virtual void Dispose(bool disposing)
    {
        if (!disposed)
        {
            if (disposing)
            {
                // Cleanup managed resources
                Disconnect();
            }
            // Cleanup unmanaged resources
            disposed = true;
        }
    }

    ~DatabaseConnection()
    {
        Dispose(false);
    }
}

// Sử dụng với using statement
using (DatabaseConnection db = new DatabaseConnection())
{
    db.Connect();
    // Do work...
} // Tự động gọi Dispose()
```

---

## 6. Interface

### 6.1. Định Nghĩa Interface

```csharp
// Interface - chỉ định nghĩa contract, không có implementation
public interface ILogger
{
    void Log(string message);
    void LogError(string error);
    void LogWarning(string warning);
}

public interface IRepository<T>
{
    void Add(T item);
    void Update(T item);
    void Delete(int id);
    T GetById(int id);
    IEnumerable<T> GetAll();
}
```

### 6.2. Implement Interface

```csharp
// Implement interface
public class FileLogger : ILogger
{
    private string logFilePath;

    public FileLogger(string filePath)
    {
        logFilePath = filePath;
    }

    public void Log(string message)
    {
        WriteToFile($"[INFO] {message}");
    }

    public void LogError(string error)
    {
        WriteToFile($"[ERROR] {error}");
    }

    public void LogWarning(string warning)
    {
        WriteToFile($"[WARNING] {warning}");
    }

    private void WriteToFile(string text)
    {
        File.AppendAllText(logFilePath, $"{DateTime.Now}: {text}\n");
    }
}

public class ConsoleLogger : ILogger
{
    public void Log(string message)
    {
        Console.ForegroundColor = ConsoleColor.White;
        Console.WriteLine($"[INFO] {message}");
        Console.ResetColor();
    }

    public void LogError(string error)
    {
        Console.ForegroundColor = ConsoleColor.Red;
        Console.WriteLine($"[ERROR] {error}");
        Console.ResetColor();
    }

    public void LogWarning(string warning)
    {
        Console.ForegroundColor = ConsoleColor.Yellow;
        Console.WriteLine($"[WARNING] {warning}");
        Console.ResetColor();
    }
}

// Generic Repository implementation
public class StudentRepository : IRepository<Student>
{
    private List<Student> students = new List<Student>();

    public void Add(Student item)
    {
        students.Add(item);
    }

    public void Update(Student item)
    {
        var existing = students.FirstOrDefault(s => s.StudentId == item.StudentId);
        if (existing != null)
        {
            existing.Name = item.Name;
            existing.Age = item.Age;
            existing.GPA = item.GPA;
        }
    }

    public void Delete(int id)
    {
        var student = students.FirstOrDefault(s => s.StudentId == id.ToString());
        if (student != null)
            students.Remove(student);
    }

    public Student GetById(int id)
    {
        return students.FirstOrDefault(s => s.StudentId == id.ToString());
    }

    public IEnumerable<Student> GetAll()
    {
        return students;
    }
}
```

### 6.3. Multiple Interface Implementation

```csharp
public interface IDrawable
{
    void Draw();
}

public interface IResizable
{
    void Resize(int width, int height);
}

public interface IRotatable
{
    void Rotate(double angle);
}

// Class implement nhiều interfaces
public class Image : IDrawable, IResizable, IRotatable
{
    public int Width { get; set; }
    public int Height { get; set; }
    public double Angle { get; set; }

    public void Draw()
    {
        Console.WriteLine($"Drawing image {Width}x{Height} at {Angle}°");
    }

    public void Resize(int width, int height)
    {
        Width = width;
        Height = height;
        Console.WriteLine($"Resized to {Width}x{Height}");
    }

    public void Rotate(double angle)
    {
        Angle = angle;
        Console.WriteLine($"Rotated to {Angle}°");
    }
}
```

### 6.4. Interface vs Abstract Class

| Interface | Abstract Class |
|-----------|----------------|
| Chỉ có method signatures (trước C# 8.0) | Có thể có implementation |
| Multiple implementation | Single inheritance |
| Không có fields | Có thể có fields |
| Không có constructor | Có constructor |
| Public by default | Có access modifiers |

---

## 7. Abstract Class

### 7.1. Khi Nào Dùng Abstract Class

✅ Sử dụng Abstract Class khi:
- Muốn share code giữa các related classes
- Có common functionality
- Muốn define common fields/properties

❌ Không dùng Abstract Class khi:
- Cần multiple inheritance
- Classes không related
- Chỉ cần define contract

### 7.2. Ví Dụ Abstract Class

```csharp
public abstract class Document
{
    // Properties
    public string Title { get; set; }
    public string Author { get; set; }
    public DateTime CreatedDate { get; protected set; }

    // Constructor
    protected Document(string title, string author)
    {
        Title = title;
        Author = author;
        CreatedDate = DateTime.Now;
    }

    // Abstract methods - bắt buộc implement
    public abstract void Open();
    public abstract void Save();
    public abstract void Print();

    // Virtual method - có thể override
    public virtual void Close()
    {
        Console.WriteLine($"Closing document: {Title}");
    }

    // Normal method - không override được
    public void DisplayInfo()
    {
        Console.WriteLine($"Title: {Title}");
        Console.WriteLine($"Author: {Author}");
        Console.WriteLine($"Created: {CreatedDate}");
    }
}

public class WordDocument : Document
{
    public int PageCount { get; set; }

    public WordDocument(string title, string author) : base(title, author)
    {
        PageCount = 1;
    }

    public override void Open()
    {
        Console.WriteLine($"Opening Word document: {Title}");
    }

    public override void Save()
    {
        Console.WriteLine($"Saving Word document: {Title}");
    }

    public override void Print()
    {
        Console.WriteLine($"Printing {PageCount} pages of {Title}");
    }
}

public class PdfDocument : Document
{
    public bool IsProtected { get; set; }

    public PdfDocument(string title, string author, bool isProtected = false)
        : base(title, author)
    {
        IsProtected = isProtected;
    }

    public override void Open()
    {
        if (IsProtected)
            Console.WriteLine($"Opening protected PDF: {Title} (requires password)");
        else
            Console.WriteLine($"Opening PDF: {Title}");
    }

    public override void Save()
    {
        Console.WriteLine($"Saving PDF: {Title}");
    }

    public override void Print()
    {
        if (IsProtected)
            Console.WriteLine("Cannot print protected PDF");
        else
            Console.WriteLine($"Printing PDF: {Title}");
    }

    public override void Close()
    {
        if (IsProtected)
            Console.WriteLine("Closing and locking PDF");
        else
            base.Close();
    }
}
```

---

## 8. SOLID Principles

### 8.1. Single Responsibility Principle (SRP)

**Nguyên tắc**: Một class chỉ nên có một lý do để thay đổi.

❌ **Bad Example**:
```csharp
public class Employee
{
    public string Name { get; set; }
    public decimal Salary { get; set; }

    // Tính lương - OK
    public decimal CalculatePay()
    {
        return Salary * 1.1m; // Bonus
    }

    // Lưu vào DB - Vi phạm SRP
    public void SaveToDatabase()
    {
        // Database code...
    }

    // Gửi email - Vi phạm SRP
    public void SendEmail()
    {
        // Email code...
    }
}
```

✅ **Good Example**:
```csharp
// Class chỉ quản lý data
public class Employee
{
    public string Name { get; set; }
    public decimal Salary { get; set; }

    public decimal CalculatePay()
    {
        return Salary * 1.1m;
    }
}

// Class chịu trách nhiệm lưu database
public class EmployeeRepository
{
    public void Save(Employee employee)
    {
        // Database code...
    }
}

// Class chịu trách nhiệm gửi email
public class EmailService
{
    public void SendWelcomeEmail(Employee employee)
    {
        // Email code...
    }
}
```

### 8.2. Open/Closed Principle (OCP)

**Nguyên tắc**: Open for extension, closed for modification.

❌ **Bad Example**:
```csharp
public class AreaCalculator
{
    public double CalculateArea(object shape)
    {
        if (shape is Circle circle)
            return Math.PI * circle.Radius * circle.Radius;
        else if (shape is Rectangle rectangle)
            return rectangle.Width * rectangle.Height;
        // Mỗi lần thêm shape mới phải modify class này
        return 0;
    }
}
```

✅ **Good Example**:
```csharp
public abstract class Shape
{
    public abstract double CalculateArea();
}

public class Circle : Shape
{
    public double Radius { get; set; }

    public override double CalculateArea()
    {
        return Math.PI * Radius * Radius;
    }
}

public class Rectangle : Shape
{
    public double Width { get; set; }
    public double Height { get; set; }

    public override double CalculateArea()
    {
        return Width * Height;
    }
}

// Thêm shape mới không cần modify code cũ
public class Triangle : Shape
{
    public double Base { get; set; }
    public double Height { get; set; }

    public override double CalculateArea()
    {
        return 0.5 * Base * Height;
    }
}

public class AreaCalculator
{
    public double CalculateTotalArea(IEnumerable<Shape> shapes)
    {
        return shapes.Sum(s => s.CalculateArea());
    }
}
```

### 8.3. Liskov Substitution Principle (LSP)

**Nguyên tắc**: Derived class phải có thể thay thế base class.

❌ **Bad Example**:
```csharp
public class Bird
{
    public virtual void Fly()
    {
        Console.WriteLine("Flying...");
    }
}

public class Penguin : Bird
{
    public override void Fly()
    {
        throw new NotSupportedException("Penguins can't fly!");
        // Vi phạm LSP - không thể thay thế Bird
    }
}
```

✅ **Good Example**:
```csharp
public abstract class Bird
{
    public abstract void Move();
}

public class FlyingBird : Bird
{
    public override void Move()
    {
        Fly();
    }

    protected virtual void Fly()
    {
        Console.WriteLine("Flying...");
    }
}

public class Penguin : Bird
{
    public override void Move()
    {
        Swim();
    }

    private void Swim()
    {
        Console.WriteLine("Swimming...");
    }
}
```

### 8.4. Interface Segregation Principle (ISP)

**Nguyên tắc**: Không nên bắt client implement interface mà nó không dùng.

❌ **Bad Example**:
```csharp
public interface IWorker
{
    void Work();
    void Eat();
    void Sleep();
}

public class Robot : IWorker
{
    public void Work() { /* OK */ }
    public void Eat() { throw new NotImplementedException(); } // Robot không eat
    public void Sleep() { throw new NotImplementedException(); } // Robot không sleep
}
```

✅ **Good Example**:
```csharp
public interface IWorkable
{
    void Work();
}

public interface IFeedable
{
    void Eat();
}

public interface ISleepable
{
    void Sleep();
}

public class Human : IWorkable, IFeedable, ISleepable
{
    public void Work() { /* ... */ }
    public void Eat() { /* ... */ }
    public void Sleep() { /* ... */ }
}

public class Robot : IWorkable
{
    public void Work() { /* ... */ }
    // Không cần implement Eat và Sleep
}
```

### 8.5. Dependency Inversion Principle (DIP)

**Nguyên tắc**: Depend on abstractions, not concretions.

❌ **Bad Example**:
```csharp
public class EmailService
{
    public void SendEmail(string message)
    {
        Console.WriteLine($"Email sent: {message}");
    }
}

public class Notification
{
    private EmailService emailService; // Phụ thuộc vào concrete class

    public Notification()
    {
        emailService = new EmailService();
    }

    public void Send(string message)
    {
        emailService.SendEmail(message);
    }
}
```

✅ **Good Example**:
```csharp
// Abstraction
public interface IMessageService
{
    void Send(string message);
}

// Implementations
public class EmailService : IMessageService
{
    public void Send(string message)
    {
        Console.WriteLine($"Email sent: {message}");
    }
}

public class SmsService : IMessageService
{
    public void Send(string message)
    {
        Console.WriteLine($"SMS sent: {message}");
    }
}

// Phụ thuộc vào abstraction
public class Notification
{
    private readonly IMessageService messageService;

    // Dependency Injection
    public Notification(IMessageService messageService)
    {
        this.messageService = messageService;
    }

    public void Send(string message)
    {
        messageService.Send(message);
    }
}

// Sử dụng
var emailNotification = new Notification(new EmailService());
emailNotification.Send("Hello via Email");

var smsNotification = new Notification(new SmsService());
smsNotification.Send("Hello via SMS");
```

---

## 9. Design Patterns Cơ Bản

### 9.1. Singleton Pattern

**Mục đích**: Đảm bảo chỉ có 1 instance của class.

```csharp
public sealed class DatabaseConnection
{
    private static DatabaseConnection instance = null;
    private static readonly object lockObject = new object();

    private DatabaseConnection()
    {
        Console.WriteLine("Database connection initialized");
    }

    public static DatabaseConnection Instance
    {
        get
        {
            lock (lockObject)
            {
                if (instance == null)
                {
                    instance = new DatabaseConnection();
                }
                return instance;
            }
        }
    }

    public void Query(string sql)
    {
        Console.WriteLine($"Executing: {sql}");
    }
}

// Sử dụng
var db1 = DatabaseConnection.Instance;
var db2 = DatabaseConnection.Instance;
Console.WriteLine(db1 == db2); // True - cùng instance
```

### 9.2. Factory Pattern

**Mục đích**: Tạo objects mà không cần specify exact class.

```csharp
public interface IPayment
{
    void ProcessPayment(decimal amount);
}

public class CreditCardPayment : IPayment
{
    public void ProcessPayment(decimal amount)
    {
        Console.WriteLine($"Processing credit card payment: {amount:C}");
    }
}

public class PayPalPayment : IPayment
{
    public void ProcessPayment(decimal amount)
    {
        Console.WriteLine($"Processing PayPal payment: {amount:C}");
    }
}

public class BankTransferPayment : IPayment
{
    public void ProcessPayment(decimal amount)
    {
        Console.WriteLine($"Processing bank transfer: {amount:C}");
    }
}

public enum PaymentMethod
{
    CreditCard,
    PayPal,
    BankTransfer
}

public class PaymentFactory
{
    public static IPayment CreatePayment(PaymentMethod method)
    {
        switch (method)
        {
            case PaymentMethod.CreditCard:
                return new CreditCardPayment();
            case PaymentMethod.PayPal:
                return new PayPalPayment();
            case PaymentMethod.BankTransfer:
                return new BankTransferPayment();
            default:
                throw new ArgumentException("Invalid payment method");
        }
    }
}

// Sử dụng
var payment = PaymentFactory.CreatePayment(PaymentMethod.PayPal);
payment.ProcessPayment(100.50m);
```

### 9.3. Repository Pattern

**Mục đích**: Abstraction layer giữa data layer và business logic.

```csharp
public interface IRepository<T> where T : class
{
    T GetById(int id);
    IEnumerable<T> GetAll();
    void Add(T entity);
    void Update(T entity);
    void Delete(int id);
}

public class ProductRepository : IRepository<Product>
{
    private List<Product> products = new List<Product>();

    public Product GetById(int id)
    {
        return products.FirstOrDefault(p => p.Id == id);
    }

    public IEnumerable<Product> GetAll()
    {
        return products;
    }

    public void Add(Product entity)
    {
        products.Add(entity);
    }

    public void Update(Product entity)
    {
        var existing = GetById(entity.Id);
        if (existing != null)
        {
            existing.Name = entity.Name;
            existing.Price = entity.Price;
        }
    }

    public void Delete(int id)
    {
        var product = GetById(id);
        if (product != null)
            products.Remove(product);
    }
}
```

### 9.4. Observer Pattern

**Mục đích**: Notify nhiều objects khi có sự thay đổi.

```csharp
public interface IObserver
{
    void Update(string message);
}

public interface ISubject
{
    void Attach(IObserver observer);
    void Detach(IObserver observer);
    void Notify(string message);
}

public class NewsAgency : ISubject
{
    private List<IObserver> observers = new List<IObserver>();

    public void Attach(IObserver observer)
    {
        observers.Add(observer);
    }

    public void Detach(IObserver observer)
    {
        observers.Remove(observer);
    }

    public void Notify(string message)
    {
        foreach (var observer in observers)
        {
            observer.Update(message);
        }
    }

    public void PublishNews(string news)
    {
        Console.WriteLine($"Publishing: {news}");
        Notify(news);
    }
}

public class NewsChannel : IObserver
{
    private string name;

    public NewsChannel(string name)
    {
        this.name = name;
    }

    public void Update(string message)
    {
        Console.WriteLine($"{name} received: {message}");
    }
}

// Sử dụng
var agency = new NewsAgency();
var channel1 = new NewsChannel("VTV");
var channel2 = new NewsChannel("HTV");

agency.Attach(channel1);
agency.Attach(channel2);

agency.PublishNews("Breaking news!");
```

---

## 10. Bài Tập Thực Hành

### Bài 1: Quản Lý Thư Viện

Xây dựng hệ thống quản lý thư viện với các yêu cầu:

1. Tạo abstract class `LibraryItem` với properties: Id, Title, Author, PublishYear
2. Tạo các class `Book`, `Magazine`, `DVD` kế thừa từ `LibraryItem`
3. Implement interface `IBorrowable` với methods: Borrow(), Return()
4. Tạo class `Library` quản lý danh sách items
5. Áp dụng SOLID principles

### Bài 2: Hệ Thống Banking

Xây dựng hệ thống ngân hàng:

1. Tạo class `BankAccount` với Encapsulation đúng cách
2. Tạo các loại tài khoản: `SavingsAccount`, `CheckingAccount`, `BusinessAccount`
3. Implement interface `ITransferable` cho chuyển khoản
4. Sử dụng Singleton cho `Bank` class
5. Sử dụng Factory pattern để tạo accounts

### Bài 3: Shape Calculator

1. Tạo abstract class `Shape` với abstract method `CalculateArea()` và `CalculatePerimeter()`
2. Implement các shapes: Circle, Rectangle, Triangle, Square
3. Tạo class `ShapeCalculator` tính tổng diện tích
4. Áp dụng OCP - dễ dàng thêm shape mới

### Bài 4: E-commerce System

1. Tạo interface `IProduct` và các implementations
2. Implement Repository pattern cho `ProductRepository`
3. Tạo `ShoppingCart` class với add, remove, calculate total
4. Implement Observer pattern cho price changes
5. Sử dụng Factory pattern cho payment methods

---

## 📝 Tóm Tắt

### Key Points:

1. **OOP** giúp code dễ maintain, mở rộng và tái sử dụng
2. **4 tính chất OOP**: Encapsulation, Inheritance, Polymorphism, Abstraction
3. **Interface** define contract, **Abstract class** share code
4. **SOLID principles** giúp design code tốt hơn
5. **Design patterns** là solutions cho common problems

### Best Practices:

- ✅ Luôn sử dụng Encapsulation
- ✅ Prefer composition over inheritance
- ✅ Code to interfaces, not implementations
- ✅ Follow SOLID principles
- ✅ Sử dụng meaningful names
- ✅ Keep classes small and focused
- ✅ Write unit tests

---

**Next:** [02-WPF-Va-XAML-Co-Ban.md](02-WPF-Va-XAML-Co-Ban.md)
