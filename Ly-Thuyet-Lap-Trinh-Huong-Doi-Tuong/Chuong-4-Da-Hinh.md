# CHƯƠNG 4: ĐA HÌNH (POLYMORPHISM)

## 📚 Mục Lục

1. [Khái niệm đa hình](#1-khái-niệm-đa-hình)
2. [Gắn kết động và gắn kết tĩnh](#2-gắn-kết-động-và-gắn-kết-tĩnh)
3. [Toán tử typeof/instanceof](#3-toán-tử-typeofinstanceof)
4. [Lớp và phương thức trừu tượng](#4-lớp-và-phương-thức-trừu-tượng)
5. [Giao diện (Interface)](#5-giao-diện-interface)
6. [Các giao diện thông dụng](#6-các-giao-diện-thông-dụng)
7. [Biểu thức Lambda](#7-biểu-thức-lambda)
8. [Lập trình tổng quát (Generic Programming)](#8-lập-trình-tổng-quát-generic-programming)
9. [Ký hiệu UML](#9-ký-hiệu-uml)

---

## 1. Khái niệm đa hình

### 1.1. Đa hình là gì?

**Đa hình (Polymorphism)** nghĩa là "nhiều hình thái". Trong OOP, đa hình cho phép:
- Một method có thể có nhiều implementations khác nhau
- Một object có thể có nhiều hình thái
- Code linh hoạt và dễ mở rộng

**Phân loại**:
1. **Compile-time Polymorphism** (Static): Method Overloading, Operator Overloading
2. **Runtime Polymorphism** (Dynamic): Method Overriding, Virtual Functions

---

### 1.2. Compile-time Polymorphism

**Đã học ở Chương 2: Method Overloading**

**Ví dụ C++**:
```cpp
class Calculator {
public:
    int add(int a, int b) {
        return a + b;
    }

    double add(double a, double b) {
        return a + b;
    }

    int add(int a, int b, int c) {
        return a + b + c;
    }
};
```

**Đặc điểm**:
- Compiler quyết định method nào được gọi (compile time)
- Dựa vào số lượng và kiểu tham số
- Không liên quan đến inheritance

---

### 1.3. Runtime Polymorphism

**Method Overriding với Virtual Functions**

**Ví dụ C++**:
```cpp
#include <iostream>
#include <vector>
using namespace std;

class Animal {
public:
    virtual void makeSound() {  // Virtual function
        cout << "Animal makes a sound" << endl;
    }

    virtual ~Animal() {}  // Virtual destructor
};

class Dog : public Animal {
public:
    void makeSound() override {
        cout << "Dog says: Woof!" << endl;
    }
};

class Cat : public Animal {
public:
    void makeSound() override {
        cout << "Cat says: Meow!" << endl;
    }
};

int main() {
    // Polymorphism - base class pointer
    vector<Animal*> animals;
    animals.push_back(new Dog());
    animals.push_back(new Cat());
    animals.push_back(new Dog());

    // Runtime polymorphism
    for (Animal* animal : animals) {
        animal->makeSound();  // Gọi method tương ứng
    }

    // Cleanup
    for (Animal* animal : animals) {
        delete animal;
    }

    return 0;
}
```

**Ví dụ C#**:
```csharp
using System;
using System.Collections.Generic;

class Animal
{
    public virtual void MakeSound()  // Virtual method
    {
        Console.WriteLine("Animal makes a sound");
    }
}

class Dog : Animal
{
    public override void MakeSound()
    {
        Console.WriteLine("Dog says: Woof!");
    }
}

class Cat : Animal
{
    public override void MakeSound()
    {
        Console.WriteLine("Cat says: Meow!");
    }
}

class Program
{
    static void Main()
    {
        // Polymorphism - base class reference
        List<Animal> animals = new List<Animal>
        {
            new Dog(),
            new Cat(),
            new Dog()
        };

        // Runtime polymorphism
        foreach (Animal animal in animals)
        {
            animal.MakeSound();  // Gọi method tương ứng
        }
    }
}
```

**Lợi ích**:
- ✅ Code linh hoạt, dễ mở rộng
- ✅ Giảm code duplication
- ✅ Tăng tính tái sử dụng
- ✅ Dễ maintain

---

## 2. Gắn kết động và gắn kết tĩnh

### 2.1. Static Binding (Gắn kết tĩnh)

**Định nghĩa**: Method call được quyết định tại compile time.

**Đặc điểm**:
- Nhanh hơn dynamic binding
- Sử dụng cho non-virtual functions
- Dựa vào type của pointer/reference

**Ví dụ C++**:
```cpp
#include <iostream>
using namespace std;

class Base {
public:
    void show() {  // Non-virtual
        cout << "Base::show()" << endl;
    }
};

class Derived : public Base {
public:
    void show() {  // Hiding
        cout << "Derived::show()" << endl;
    }
};

int main() {
    Derived d;
    Base* b = &d;

    b->show();  // Base::show() - Static binding
    d.show();   // Derived::show()

    return 0;
}
```

---

### 2.2. Dynamic Binding (Gắn kết động)

**Định nghĩa**: Method call được quyết định tại runtime.

**Đặc điểm**:
- Chậm hơn static binding (vtable lookup)
- Sử dụng cho virtual functions
- Dựa vào actual type của object

**Ví dụ C++**:
```cpp
#include <iostream>
using namespace std;

class Base {
public:
    virtual void show() {  // Virtual
        cout << "Base::show()" << endl;
    }

    virtual ~Base() {}
};

class Derived : public Base {
public:
    void show() override {
        cout << "Derived::show()" << endl;
    }
};

int main() {
    Derived d;
    Base* b = &d;

    b->show();  // Derived::show() - Dynamic binding
    d.show();   // Derived::show()

    return 0;
}
```

**Ví dụ C#**:
```csharp
using System;

class Base
{
    public virtual void Show()  // Virtual
    {
        Console.WriteLine("Base::Show()");
    }
}

class Derived : Base
{
    public override void Show()
    {
        Console.WriteLine("Derived::Show()");
    }
}

class Program
{
    static void Main()
    {
        Derived d = new Derived();
        Base b = d;

        b.Show();  // Derived::Show() - Dynamic binding
        d.Show();  // Derived::Show()
    }
}
```

---

### 2.3. So sánh Static vs Dynamic Binding

| Tiêu chí | Static Binding | Dynamic Binding |
|----------|----------------|-----------------|
| **Thời điểm** | Compile time | Runtime |
| **Tốc độ** | Nhanh hơn | Chậm hơn |
| **Từ khóa** | Non-virtual | virtual/override |
| **Type** | Pointer/Reference type | Object type |
| **Overhead** | Không | vtable lookup |
| **Flexibility** | Thấp | Cao |

---

## 3. Toán tử typeof/instanceof

### 3.1. typeof/typeid trong C++

**typeid operator**: Trả về type information

```cpp
#include <iostream>
#include <typeinfo>
using namespace std;

class Animal {
public:
    virtual ~Animal() {}
};

class Dog : public Animal {};
class Cat : public Animal {};

int main() {
    Animal* a1 = new Dog();
    Animal* a2 = new Cat();

    // typeid - lấy type information
    cout << "a1 type: " << typeid(*a1).name() << endl;
    cout << "a2 type: " << typeid(*a2).name() << endl;

    // So sánh type
    if (typeid(*a1) == typeid(Dog)) {
        cout << "a1 is a Dog" << endl;
    }

    if (typeid(*a2) == typeid(Cat)) {
        cout << "a2 is a Cat" << endl;
    }

    delete a1;
    delete a2;

    return 0;
}
```

---

### 3.2. dynamic_cast trong C++

**dynamic_cast**: Ép kiểu an toàn cho polymorphic types

```cpp
#include <iostream>
using namespace std;

class Animal {
public:
    virtual void makeSound() = 0;
    virtual ~Animal() {}
};

class Dog : public Animal {
public:
    void makeSound() override {
        cout << "Woof!" << endl;
    }

    void fetch() {
        cout << "Dog is fetching" << endl;
    }
};

class Cat : public Animal {
public:
    void makeSound() override {
        cout << "Meow!" << endl;
    }

    void scratch() {
        cout << "Cat is scratching" << endl;
    }
};

void processAnimal(Animal* animal) {
    // Kiểm tra và ép kiểu
    Dog* dog = dynamic_cast<Dog*>(animal);
    if (dog != nullptr) {
        cout << "This is a dog: ";
        dog->fetch();
        return;
    }

    Cat* cat = dynamic_cast<Cat*>(animal);
    if (cat != nullptr) {
        cout << "This is a cat: ";
        cat->scratch();
        return;
    }

    cout << "Unknown animal type" << endl;
}

int main() {
    Animal* a1 = new Dog();
    Animal* a2 = new Cat();

    processAnimal(a1);
    processAnimal(a2);

    delete a1;
    delete a2;

    return 0;
}
```

---

### 3.3. is và as trong C#

**is operator**: Kiểm tra type

**as operator**: Ép kiểu an toàn

```csharp
using System;

class Animal
{
    public virtual void MakeSound() { }
}

class Dog : Animal
{
    public override void MakeSound()
    {
        Console.WriteLine("Woof!");
    }

    public void Fetch()
    {
        Console.WriteLine("Dog is fetching");
    }
}

class Cat : Animal
{
    public override void MakeSound()
    {
        Console.WriteLine("Meow!");
    }

    public void Scratch()
    {
        Console.WriteLine("Cat is scratching");
    }
}

class Program
{
    static void ProcessAnimal(Animal animal)
    {
        // is operator - kiểm tra type
        if (animal is Dog)
        {
            Console.Write("This is a dog: ");
            ((Dog)animal).Fetch();
            return;
        }

        if (animal is Cat)
        {
            Console.Write("This is a cat: ");
            ((Cat)animal).Scratch();
            return;
        }

        // Pattern matching (C# 7.0+)
        switch (animal)
        {
            case Dog dog:
                Console.Write("Dog detected: ");
                dog.Fetch();
                break;
            case Cat cat:
                Console.Write("Cat detected: ");
                cat.Scratch();
                break;
            default:
                Console.WriteLine("Unknown animal");
                break;
        }

        // as operator - ép kiểu an toàn
        Dog d = animal as Dog;
        if (d != null)
        {
            d.Fetch();
        }
    }

    static void Main()
    {
        Animal a1 = new Dog();
        Animal a2 = new Cat();

        ProcessAnimal(a1);
        ProcessAnimal(a2);

        // typeof operator
        Console.WriteLine($"Type of a1: {a1.GetType().Name}");
        Console.WriteLine($"Type of a2: {a2.GetType().Name}");
    }
}
```

---

## 4. Lớp và phương thức trừu tượng

### 4.1. Abstract Class (Lớp trừu tượng)

**Định nghĩa**: Lớp không thể khởi tạo trực tiếp, dùng làm base class.

**Đặc điểm**:
- Có thể có abstract methods (không có implementation)
- Có thể có concrete methods (có implementation)
- Có thể có fields, constructors
- Class con bắt buộc implement tất cả abstract methods

---

### 4.2. Abstract Class trong C++

```cpp
#include <iostream>
#include <string>
#include <cmath>
using namespace std;

// Abstract class
class Shape {
protected:
    string name;

public:
    Shape(string n) : name(n) {}

    // Pure virtual functions - abstract methods
    virtual double calculateArea() = 0;
    virtual double calculatePerimeter() = 0;

    // Virtual function - có implementation
    virtual void display() {
        cout << "Shape: " << name << endl;
        cout << "Area: " << calculateArea() << endl;
        cout << "Perimeter: " << calculatePerimeter() << endl;
    }

    // Normal function
    string getName() const {
        return name;
    }

    virtual ~Shape() {}
};

class Circle : public Shape {
private:
    double radius;

public:
    Circle(double r) : Shape("Circle"), radius(r) {}

    // Implement abstract methods
    double calculateArea() override {
        return M_PI * radius * radius;
    }

    double calculatePerimeter() override {
        return 2 * M_PI * radius;
    }

    void display() override {
        Shape::display();
        cout << "Radius: " << radius << endl;
    }
};

class Rectangle : public Shape {
private:
    double width, height;

public:
    Rectangle(double w, double h)
        : Shape("Rectangle"), width(w), height(h) {}

    double calculateArea() override {
        return width * height;
    }

    double calculatePerimeter() override {
        return 2 * (width + height);
    }

    void display() override {
        Shape::display();
        cout << "Width: " << width << ", Height: " << height << endl;
    }
};

int main() {
    // Không thể khởi tạo abstract class
    // Shape s("Test");  // ERROR!

    // Sử dụng polymorphism
    Shape* shapes[] = {
        new Circle(5),
        new Rectangle(4, 6),
        new Circle(3)
    };

    for (int i = 0; i < 3; i++) {
        shapes[i]->display();
        cout << endl;
    }

    // Cleanup
    for (int i = 0; i < 3; i++) {
        delete shapes[i];
    }

    return 0;
}
```

---

### 4.3. Abstract Class trong C#

```csharp
using System;

// Abstract class
abstract class Shape
{
    protected string name;

    public Shape(string n)
    {
        name = n;
    }

    // Abstract methods - không có implementation
    public abstract double CalculateArea();
    public abstract double CalculatePerimeter();

    // Virtual method - có implementation
    public virtual void Display()
    {
        Console.WriteLine($"Shape: {name}");
        Console.WriteLine($"Area: {CalculateArea():F2}");
        Console.WriteLine($"Perimeter: {CalculatePerimeter():F2}");
    }

    // Normal method
    public string GetName()
    {
        return name;
    }
}

class Circle : Shape
{
    private double radius;

    public Circle(double r) : base("Circle")
    {
        radius = r;
    }

    // Implement abstract methods
    public override double CalculateArea()
    {
        return Math.PI * radius * radius;
    }

    public override double CalculatePerimeter()
    {
        return 2 * Math.PI * radius;
    }

    public override void Display()
    {
        base.Display();
        Console.WriteLine($"Radius: {radius}");
    }
}

class Rectangle : Shape
{
    private double width, height;

    public Rectangle(double w, double h) : base("Rectangle")
    {
        width = w;
        height = h;
    }

    public override double CalculateArea()
    {
        return width * height;
    }

    public override double CalculatePerimeter()
    {
        return 2 * (width + height);
    }

    public override void Display()
    {
        base.Display();
        Console.WriteLine($"Width: {width}, Height: {height}");
    }
}

class Program
{
    static void Main()
    {
        // Không thể khởi tạo abstract class
        // Shape s = new Shape("Test");  // ERROR!

        // Sử dụng polymorphism
        Shape[] shapes = {
            new Circle(5),
            new Rectangle(4, 6),
            new Circle(3)
        };

        foreach (Shape shape in shapes)
        {
            shape.Display();
            Console.WriteLine();
        }
    }
}
```

---

## 5. Giao diện (Interface)

### 5.1. Khái niệm

**Interface** là contract định nghĩa tập hợp các methods mà class phải implement.

**Đặc điểm**:
- Chỉ định nghĩa signatures, không có implementation (trước C# 8.0, C++20)
- Class có thể implement nhiều interfaces
- Tất cả members đều public
- Không có fields (chỉ có constants)

---

### 5.2. Interface trong C++ (Abstract Class)

C++ không có interface keyword, sử dụng abstract class:

```cpp
#include <iostream>
#include <string>
using namespace std;

// Interface (Pure abstract class)
class IDrawable {
public:
    virtual void draw() = 0;
    virtual ~IDrawable() {}
};

class IResizable {
public:
    virtual void resize(int width, int height) = 0;
    virtual ~IResizable() {}
};

// Class implement nhiều interfaces
class Image : public IDrawable, public IResizable {
private:
    string name;
    int width, height;

public:
    Image(string n, int w, int h)
        : name(n), width(w), height(h) {}

    // Implement IDrawable
    void draw() override {
        cout << "Drawing image: " << name
             << " (" << width << "x" << height << ")" << endl;
    }

    // Implement IResizable
    void resize(int w, int h) override {
        width = w;
        height = h;
        cout << "Resized to " << width << "x" << height << endl;
    }
};

class Button : public IDrawable {
private:
    string label;

public:
    Button(string lbl) : label(lbl) {}

    void draw() override {
        cout << "Drawing button: " << label << endl;
    }
};

int main() {
    Image img("photo.jpg", 800, 600);
    Button btn("Click Me");

    // Polymorphism với interface
    IDrawable* drawables[] = { &img, &btn };

    for (int i = 0; i < 2; i++) {
        drawables[i]->draw();
    }

    // IResizable
    IResizable* resizable = &img;
    resizable->resize(1024, 768);

    return 0;
}
```

---

### 5.3. Interface trong C#

```csharp
using System;

// Interface
interface IDrawable
{
    void Draw();
}

interface IResizable
{
    void Resize(int width, int height);
}

interface IRotatable
{
    void Rotate(double angle);
}

// Class implement nhiều interfaces
class Image : IDrawable, IResizable, IRotatable
{
    private string name;
    private int width, height;
    private double angle;

    public Image(string n, int w, int h)
    {
        name = n;
        width = w;
        height = h;
        angle = 0;
    }

    // Implement IDrawable
    public void Draw()
    {
        Console.WriteLine($"Drawing image: {name} ({width}x{height}) at {angle}°");
    }

    // Implement IResizable
    public void Resize(int w, int h)
    {
        width = w;
        height = h;
        Console.WriteLine($"Resized to {width}x{height}");
    }

    // Implement IRotatable
    public void Rotate(double a)
    {
        angle = a;
        Console.WriteLine($"Rotated to {angle}°");
    }
}

class Button : IDrawable
{
    private string label;

    public Button(string lbl)
    {
        label = lbl;
    }

    public void Draw()
    {
        Console.WriteLine($"Drawing button: {label}");
    }
}

class Program
{
    static void Main()
    {
        Image img = new Image("photo.jpg", 800, 600);
        Button btn = new Button("Click Me");

        // Polymorphism với interface
        IDrawable[] drawables = { img, btn };

        foreach (IDrawable drawable in drawables)
        {
            drawable.Draw();
        }

        // IResizable
        IResizable resizable = img;
        resizable.Resize(1024, 768);

        // IRotatable
        IRotatable rotatable = img;
        rotatable.Rotate(45);

        img.Draw();
    }
}
```

---

### 5.4. Interface vs Abstract Class

| Tiêu chí | Interface | Abstract Class |
|----------|-----------|----------------|
| **Implementation** | Không có (C#) | Có thể có |
| **Multiple Inheritance** | Có | Không (C++) / Không (C#) |
| **Fields** | Không | Có |
| **Constructor** | Không | Có |
| **Access Modifiers** | Public (default) | Có thể có |
| **Khi nào dùng** | Define contract | Share code |

---

## 6. Các giao diện thông dụng

### 6.1. IComparable trong C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Person {
private:
    string name;
    int age;

public:
    Person(string n, int a) : name(n), age(a) {}

    string getName() const { return name; }
    int getAge() const { return age; }

    // Operator< cho sorting
    bool operator<(const Person& other) const {
        return age < other.age;
    }

    // Operator== cho comparison
    bool operator==(const Person& other) const {
        return name == other.name && age == other.age;
    }

    friend ostream& operator<<(ostream& os, const Person& p) {
        os << p.name << " (" << p.age << ")";
        return os;
    }
};

int main() {
    vector<Person> people = {
        Person("Alice", 25),
        Person("Bob", 20),
        Person("Charlie", 30)
    };

    // Sort using operator<
    sort(people.begin(), people.end());

    cout << "Sorted by age:" << endl;
    for (const auto& p : people) {
        cout << p << endl;
    }

    return 0;
}
```

---

### 6.2. IComparable trong C#

```csharp
using System;
using System.Collections.Generic;
using System.Linq;

class Person : IComparable<Person>
{
    public string Name { get; set; }
    public int Age { get; set; }

    public Person(string name, int age)
    {
        Name = name;
        Age = age;
    }

    // Implement IComparable
    public int CompareTo(Person other)
    {
        if (other == null) return 1;
        return Age.CompareTo(other.Age);
    }

    public override string ToString()
    {
        return $"{Name} ({Age})";
    }
}

class Program
{
    static void Main()
    {
        List<Person> people = new List<Person>
        {
            new Person("Alice", 25),
            new Person("Bob", 20),
            new Person("Charlie", 30)
        };

        // Sort using IComparable
        people.Sort();

        Console.WriteLine("Sorted by age:");
        foreach (var p in people)
        {
            Console.WriteLine(p);
        }
    }
}
```

---

### 6.3. ICloneable/Copyable

**C++**:
```cpp
#include <iostream>
#include <string>
using namespace std;

class Student {
private:
    string name;
    int age;
    double* grades;
    int numGrades;

public:
    Student(string n, int a, int num)
        : name(n), age(a), numGrades(num) {
        grades = new double[numGrades];
    }

    // Copy constructor - deep copy
    Student(const Student& other)
        : name(other.name), age(other.age), numGrades(other.numGrades) {
        grades = new double[numGrades];
        for (int i = 0; i < numGrades; i++) {
            grades[i] = other.grades[i];
        }
    }

    // Clone method
    Student* clone() const {
        return new Student(*this);
    }

    ~Student() {
        delete[] grades;
    }

    void setGrade(int index, double grade) {
        if (index >= 0 && index < numGrades) {
            grades[index] = grade;
        }
    }

    void display() const {
        cout << "Name: " << name << ", Age: " << age << endl;
        cout << "Grades: ";
        for (int i = 0; i < numGrades; i++) {
            cout << grades[i] << " ";
        }
        cout << endl;
    }
};

int main() {
    Student s1("John", 20, 3);
    s1.setGrade(0, 8.5);
    s1.setGrade(1, 9.0);
    s1.setGrade(2, 7.5);

    // Clone
    Student* s2 = s1.clone();

    cout << "Original:" << endl;
    s1.display();

    cout << "\nCloned:" << endl;
    s2->display();

    delete s2;
    return 0;
}
```

**C#**:
```csharp
using System;

class Student : ICloneable
{
    public string Name { get; set; }
    public int Age { get; set; }
    public double[] Grades { get; set; }

    public Student(string name, int age, int numGrades)
    {
        Name = name;
        Age = age;
        Grades = new double[numGrades];
    }

    // Implement ICloneable - shallow copy
    public object Clone()
    {
        return MemberwiseClone();
    }

    // Deep copy method
    public Student DeepClone()
    {
        Student clone = (Student)MemberwiseClone();
        clone.Grades = (double[])Grades.Clone();
        return clone;
    }

    public void Display()
    {
        Console.WriteLine($"Name: {Name}, Age: {Age}");
        Console.Write("Grades: ");
        foreach (var grade in Grades)
        {
            Console.Write($"{grade} ");
        }
        Console.WriteLine();
    }
}

class Program
{
    static void Main()
    {
        Student s1 = new Student("John", 20, 3);
        s1.Grades[0] = 8.5;
        s1.Grades[1] = 9.0;
        s1.Grades[2] = 7.5;

        // Shallow clone
        Student s2 = (Student)s1.Clone();

        // Deep clone
        Student s3 = s1.DeepClone();

        Console.WriteLine("Original:");
        s1.Display();

        Console.WriteLine("\nShallow Clone:");
        s2.Display();

        Console.WriteLine("\nDeep Clone:");
        s3.Display();

        // Modify original
        s1.Grades[0] = 10.0;

        Console.WriteLine("\nAfter modifying original:");
        Console.WriteLine("Original:");
        s1.Display();
        Console.WriteLine("Shallow Clone (affected):");
        s2.Display();
        Console.WriteLine("Deep Clone (not affected):");
        s3.Display();
    }
}
```

---

## 7. Biểu thức Lambda

### 7.1. Lambda trong C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    vector<int> numbers = {5, 2, 8, 1, 9, 3, 7, 4, 6};

    // Lambda expression - basic
    auto print = [](int n) {
        cout << n << " ";
    };

    cout << "Numbers: ";
    for_each(numbers.begin(), numbers.end(), print);
    cout << endl;

    // Lambda - inline sorting
    sort(numbers.begin(), numbers.end(), [](int a, int b) {
        return a > b;  // Descending order
    });

    cout << "Sorted (desc): ";
    for_each(numbers.begin(), numbers.end(), print);
    cout << endl;

    // Lambda - capture variables
    int threshold = 5;
    auto count = count_if(numbers.begin(), numbers.end(),
        [threshold](int n) {  // Capture by value
            return n > threshold;
        });

    cout << "Count > " << threshold << ": " << count << endl;

    // Lambda - capture by reference
    int sum = 0;
    for_each(numbers.begin(), numbers.end(),
        [&sum](int n) {  // Capture by reference
            sum += n;
        });

    cout << "Sum: " << sum << endl;

    // Lambda - generic (C++14)
    auto multiply = [](auto a, auto b) {
        return a * b;
    };

    cout << "3 * 4 = " << multiply(3, 4) << endl;
    cout << "3.5 * 2.5 = " << multiply(3.5, 2.5) << endl;

    return 0;
}
```

---

### 7.2. Lambda trong C#

```csharp
using System;
using System.Collections.Generic;
using System.Linq;

class Program
{
    static void Main()
    {
        List<int> numbers = new List<int> { 5, 2, 8, 1, 9, 3, 7, 4, 6 };

        // Lambda expression - basic
        Action<int> print = n => Console.Write($"{n} ");

        Console.Write("Numbers: ");
        numbers.ForEach(print);
        Console.WriteLine();

        // Lambda - sorting
        var sortedDesc = numbers.OrderByDescending(n => n);

        Console.Write("Sorted (desc): ");
        foreach (var n in sortedDesc)
        {
            Console.Write($"{n} ");
        }
        Console.WriteLine();

        // Lambda - filtering
        int threshold = 5;
        var filtered = numbers.Where(n => n > threshold);

        Console.Write($"Numbers > {threshold}: ");
        foreach (var n in filtered)
        {
            Console.Write($"{n} ");
        }
        Console.WriteLine();

        // Lambda - aggregation
        int sum = numbers.Aggregate(0, (acc, n) => acc + n);
        Console.WriteLine($"Sum: {sum}");

        // Lambda - transformation
        var squared = numbers.Select(n => n * n);

        Console.Write("Squared: ");
        foreach (var n in squared)
        {
            Console.Write($"{n} ");
        }
        Console.WriteLine();

        // Lambda with custom objects
        List<Person> people = new List<Person>
        {
            new Person { Name = "Alice", Age = 25 },
            new Person { Name = "Bob", Age = 20 },
            new Person { Name = "Charlie", Age = 30 }
        };

        // Filter and sort
        var adults = people
            .Where(p => p.Age >= 21)
            .OrderBy(p => p.Name)
            .Select(p => p.Name);

        Console.WriteLine("\nAdults:");
        foreach (var name in adults)
        {
            Console.WriteLine(name);
        }
    }
}

class Person
{
    public string Name { get; set; }
    public int Age { get; set; }
}
```

---

## 8. Lập trình tổng quát (Generic Programming)

### 8.1. Templates trong C++

```cpp
#include <iostream>
#include <vector>
using namespace std;

// Generic function template
template<typename T>
T getMax(T a, T b) {
    return (a > b) ? a : b;
}

// Generic class template
template<typename T>
class Stack {
private:
    vector<T> elements;

public:
    void push(T element) {
        elements.push_back(element);
    }

    T pop() {
        if (elements.empty()) {
            throw runtime_error("Stack is empty");
        }
        T top = elements.back();
        elements.pop_back();
        return top;
    }

    T peek() const {
        if (elements.empty()) {
            throw runtime_error("Stack is empty");
        }
        return elements.back();
    }

    bool isEmpty() const {
        return elements.empty();
    }

    int size() const {
        return elements.size();
    }
};

// Generic class with multiple type parameters
template<typename K, typename V>
class Pair {
private:
    K key;
    V value;

public:
    Pair(K k, V v) : key(k), value(v) {}

    K getKey() const { return key; }
    V getValue() const { return value; }

    void display() const {
        cout << "(" << key << ", " << value << ")" << endl;
    }
};

int main() {
    // Generic function
    cout << "Max(10, 20) = " << getMax(10, 20) << endl;
    cout << "Max(10.5, 20.3) = " << getMax(10.5, 20.3) << endl;
    cout << "Max('A', 'Z') = " << getMax('A', 'Z') << endl;

    // Generic Stack
    Stack<int> intStack;
    intStack.push(10);
    intStack.push(20);
    intStack.push(30);

    cout << "\nInt Stack:" << endl;
    while (!intStack.isEmpty()) {
        cout << intStack.pop() << " ";
    }
    cout << endl;

    Stack<string> stringStack;
    stringStack.push("Hello");
    stringStack.push("World");

    cout << "\nString Stack:" << endl;
    while (!stringStack.isEmpty()) {
        cout << stringStack.pop() << " ";
    }
    cout << endl;

    // Generic Pair
    Pair<string, int> p1("Age", 25);
    Pair<int, double> p2(1, 3.14);

    cout << "\nPairs:" << endl;
    p1.display();
    p2.display();

    return 0;
}
```

---

### 8.2. Generics trong C#

```csharp
using System;
using System.Collections.Generic;

// Generic method
class Utils
{
    public static T GetMax<T>(T a, T b) where T : IComparable<T>
    {
        return a.CompareTo(b) > 0 ? a : b;
    }

    public static void Swap<T>(ref T a, ref T b)
    {
        T temp = a;
        a = b;
        b = temp;
    }
}

// Generic class
class Stack<T>
{
    private List<T> elements = new List<T>();

    public void Push(T element)
    {
        elements.Add(element);
    }

    public T Pop()
    {
        if (elements.Count == 0)
        {
            throw new InvalidOperationException("Stack is empty");
        }
        T top = elements[elements.Count - 1];
        elements.RemoveAt(elements.Count - 1);
        return top;
    }

    public T Peek()
    {
        if (elements.Count == 0)
        {
            throw new InvalidOperationException("Stack is empty");
        }
        return elements[elements.Count - 1];
    }

    public bool IsEmpty => elements.Count == 0;

    public int Size => elements.Count;
}

// Generic class with constraints
class Repository<T> where T : class, new()
{
    private List<T> items = new List<T>();

    public void Add(T item)
    {
        items.Add(item);
    }

    public T GetById(int id)
    {
        return items[id];
    }

    public List<T> GetAll()
    {
        return items;
    }

    public T CreateNew()
    {
        return new T();  // Requires new() constraint
    }
}

// Generic class with multiple type parameters
class Pair<K, V>
{
    public K Key { get; set; }
    public V Value { get; set; }

    public Pair(K key, V value)
    {
        Key = key;
        Value = value;
    }

    public override string ToString()
    {
        return $"({Key}, {Value})";
    }
}

class Program
{
    static void Main()
    {
        // Generic methods
        Console.WriteLine($"Max(10, 20) = {Utils.GetMax(10, 20)}");
        Console.WriteLine($"Max(10.5, 20.3) = {Utils.GetMax(10.5, 20.3)}");
        Console.WriteLine($"Max('A', 'Z') = {Utils.GetMax('A', 'Z')}");

        int x = 10, y = 20;
        Utils.Swap(ref x, ref y);
        Console.WriteLine($"After swap: x={x}, y={y}");

        // Generic Stack
        Stack<int> intStack = new Stack<int>();
        intStack.Push(10);
        intStack.Push(20);
        intStack.Push(30);

        Console.WriteLine("\nInt Stack:");
        while (!intStack.IsEmpty)
        {
            Console.Write($"{intStack.Pop()} ");
        }
        Console.WriteLine();

        Stack<string> stringStack = new Stack<string>();
        stringStack.Push("Hello");
        stringStack.Push("World");

        Console.WriteLine("\nString Stack:");
        while (!stringStack.IsEmpty)
        {
            Console.Write($"{stringStack.Pop()} ");
        }
        Console.WriteLine();

        // Generic Pair
        Pair<string, int> p1 = new Pair<string, int>("Age", 25);
        Pair<int, double> p2 = new Pair<int, double>(1, 3.14);

        Console.WriteLine("\nPairs:");
        Console.WriteLine(p1);
        Console.WriteLine(p2);

        // Generic collections
        List<int> numbers = new List<int> { 1, 2, 3, 4, 5 };
        Dictionary<string, int> ages = new Dictionary<string, int>
        {
            { "Alice", 25 },
            { "Bob", 30 }
        };

        Console.WriteLine("\nGeneric Collections:");
        Console.Write("Numbers: ");
        numbers.ForEach(n => Console.Write($"{n} "));
        Console.WriteLine();

        Console.WriteLine("Ages:");
        foreach (var kvp in ages)
        {
            Console.WriteLine($"{kvp.Key}: {kvp.Value}");
        }
    }
}
```

---

## 9. Ký hiệu UML

### 9.1. Abstract Class trong UML

```
┌─────────────────────────────┐
│ <<abstract>>                │
│      Shape                  │
├─────────────────────────────┤
│ # name: string              │
├─────────────────────────────┤
│ + Shape(name)               │
│ + calculateArea(): double   │
│   {abstract}                │
│ + calculatePerimeter(): d   │
│   {abstract}                │
│ + display()                 │
│   {virtual}                 │
└────────────▲────────────────┘
             │
      ┌──────┴──────┐
      │             │
┌─────┴──────┐ ┌────┴────────┐
│  Circle    │ │  Rectangle  │
├────────────┤ ├─────────────┤
│ - radius   │ │ - width     │
│            │ │ - height    │
├────────────┤ ├─────────────┤
│ + calcArea │ │ + calcArea  │
│ + calcPeri │ │ + calcPeri  │
└────────────┘ └─────────────┘
```

---

### 9.2. Interface trong UML

```
┌─────────────────────────┐
│ <<interface>>           │
│    IDrawable            │
├─────────────────────────┤
│ + draw()                │
└───────────▲─────────────┘
            │
            │ implements
            │
    ┌───────┴───────┐
    │               │
┌───┴──────┐  ┌─────┴─────┐
│  Image   │  │  Button   │
├──────────┤  ├───────────┤
│ - name   │  │ - label   │
├──────────┤  ├───────────┤
│ + draw() │  │ + draw()  │
└──────────┘  └───────────┘

Ký hiệu implements: ········▷
```

---

## 📝 Tóm tắt Chương 4

### Các điểm chính:

1. **Đa hình (Polymorphism)**:
   - Compile-time: Overloading
   - Runtime: Overriding
   - Tăng tính linh hoạt

2. **Binding**:
   - Static binding: Compile time
   - Dynamic binding: Runtime
   - Virtual functions

3. **Abstract Class**:
   - Không thể khởi tạo
   - Có abstract methods
   - Dùng làm base class

4. **Interface**:
   - Define contract
   - Multiple implementation
   - Polymorphism

5. **Generic Programming**:
   - Templates (C++)
   - Generics (C#)
   - Type safety

### Bài tập:

1. Implement hierarchy `Animal` với abstract methods và polymorphism
2. Tạo interface `IPayment` với các implementations: `CreditCard`, `PayPal`, `BankTransfer`
3. Viết generic class `LinkedList<T>` với các operations cơ bản
4. Sử dụng lambda expressions để filter và transform collections
5. Vẽ UML cho hệ thống với abstract classes và interfaces

---

**Hoàn thành**: Bạn đã học xong 4 chương lý thuyết OOP! 🎉
