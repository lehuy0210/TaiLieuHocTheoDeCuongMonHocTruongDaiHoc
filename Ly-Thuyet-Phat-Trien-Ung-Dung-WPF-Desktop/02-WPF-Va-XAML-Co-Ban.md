# WPF VÀ XAML CƠ BẢN

## 📚 Mục Lục

1. [Giới Thiệu WPF](#1-giới-thiệu-wpf)
2. [XAML Basics](#2-xaml-basics)
3. [Layout Controls](#3-layout-controls)
4. [Common Controls](#4-common-controls)
5. [Data Binding](#5-data-binding)
6. [Event Handling](#6-event-handling)
7. [Resources](#7-resources)
8. [Styles](#8-styles)
9. [Commands](#9-commands)
10. [Bài Tập Thực Hành](#10-bài-tập-thực-hành)

---

## 1. Giới Thiệu WPF

### 1.1. WPF Là Gì?

**Windows Presentation Foundation (WPF)** là framework của Microsoft để xây dựng ứng dụng desktop Windows với UI phong phú, hiện đại.

### 1.2. Đặc Điểm WPF

✅ **Vector-based graphics**: UI scale tốt ở mọi resolution
✅ **XAML**: Declarative UI design
✅ **Data Binding**: Tự động sync data giữa UI và code
✅ **Styling và Templating**: Customize UI dễ dàng
✅ **Rich Controls**: Nhiều controls built-in
✅ **Multimedia support**: Video, audio, animations

### 1.3. WPF vs WinForms

| WPF | WinForms |
|-----|----------|
| Vector-based | Pixel-based |
| XAML + C# | C# only |
| Rich styling | Limited styling |
| Modern look | Traditional look |
| Data binding mạnh | Data binding hạn chế |
| Learning curve cao hơn | Dễ học hơn |

### 1.4. Kiến Trúc WPF Application

```
MyWPFApp/
├── App.xaml              # Application-level resources
├── App.xaml.cs           # Application entry point
├── MainWindow.xaml       # Main window XAML
├── MainWindow.xaml.cs    # Main window code-behind
├── Views/                # Other windows/pages
├── Models/               # Data models
├── ViewModels/           # ViewModels (MVVM)
└── Resources/            # Images, icons, etc.
```

---

## 2. XAML Basics

### 2.1. XAML Là Gì?

**XAML (Extensible Application Markup Language)** là ngôn ngữ markup XML-based để define UI.

### 2.2. XAML Syntax

#### Basic Structure:

```xml
<Window x:Class="MyApp.MainWindow"
        xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        Title="My Application"
        Height="450"
        Width="800">

    <Grid>
        <!-- UI elements here -->
    </Grid>

</Window>
```

#### Elements và Attributes:

```xml
<!-- Element -->
<Button>Click Me</Button>

<!-- Element with attributes -->
<Button Content="Click Me"
        Width="100"
        Height="30" />

<!-- Element with property syntax -->
<Button>
    <Button.Content>Click Me</Button.Content>
    <Button.Width>100</Button.Width>
</Button>

<!-- Nested elements -->
<StackPanel>
    <TextBlock Text="Label" />
    <TextBox Width="200" />
</StackPanel>
```

### 2.3. Namespaces

```xml
<!-- Default WPF namespace -->
xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"

<!-- XAML language namespace -->
xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"

<!-- Custom namespace -->
xmlns:local="clr-namespace:MyApp"
xmlns:vm="clr-namespace:MyApp.ViewModels"

<!-- Sử dụng custom namespace -->
<local:MyCustomControl />
<vm:MyViewModel />
```

### 2.4. XAML vs C# Code

#### XAML:
```xml
<Button x:Name="myButton"
        Content="Click Me"
        Width="100"
        Height="30"
        Click="MyButton_Click" />
```

#### Equivalent C#:
```csharp
Button myButton = new Button();
myButton.Content = "Click Me";
myButton.Width = 100;
myButton.Height = 30;
myButton.Click += MyButton_Click;
```

---

## 3. Layout Controls

### 3.1. Grid

**Grid** là layout phổ biến nhất, chia UI thành rows và columns.

```xml
<Grid>
    <!-- Define rows -->
    <Grid.RowDefinitions>
        <RowDefinition Height="Auto" />        <!-- Chiều cao tự động -->
        <RowDefinition Height="*" />           <!-- Chiếm phần còn lại -->
        <RowDefinition Height="2*" />          <!-- Gấp 2 lần row trên -->
        <RowDefinition Height="50" />          <!-- Fixed height -->
    </Grid.RowDefinitions>

    <!-- Define columns -->
    <Grid.ColumnDefinitions>
        <ColumnDefinition Width="200" />       <!-- Fixed width -->
        <ColumnDefinition Width="*" />         <!-- Chiếm phần còn lại -->
        <ColumnDefinition Width="Auto" />      <!-- Width tự động -->
    </Grid.ColumnDefinitions>

    <!-- Place elements -->
    <TextBlock Grid.Row="0" Grid.Column="0" Text="Top Left" />
    <TextBlock Grid.Row="0" Grid.Column="1" Text="Top Center" />
    <TextBlock Grid.Row="1" Grid.Column="0" Grid.ColumnSpan="2"
               Text="Span 2 columns" />
</Grid>
```

#### Ví Dụ: Login Form

```xml
<Grid Margin="20">
    <Grid.RowDefinitions>
        <RowDefinition Height="Auto" />
        <RowDefinition Height="Auto" />
        <RowDefinition Height="Auto" />
        <RowDefinition Height="Auto" />
    </Grid.RowDefinitions>

    <Grid.ColumnDefinitions>
        <ColumnDefinition Width="Auto" />
        <ColumnDefinition Width="*" />
    </Grid.ColumnDefinitions>

    <!-- Username -->
    <TextBlock Grid.Row="0" Grid.Column="0"
               Text="Username:"
               VerticalAlignment="Center"
               Margin="0,0,10,10" />
    <TextBox Grid.Row="0" Grid.Column="1"
             x:Name="txtUsername"
             Margin="0,0,0,10" />

    <!-- Password -->
    <TextBlock Grid.Row="1" Grid.Column="0"
               Text="Password:"
               VerticalAlignment="Center"
               Margin="0,0,10,10" />
    <PasswordBox Grid.Row="1" Grid.Column="1"
                 x:Name="txtPassword"
                 Margin="0,0,0,10" />

    <!-- Remember Me -->
    <CheckBox Grid.Row="2" Grid.Column="1"
              Content="Remember Me"
              Margin="0,0,0,10" />

    <!-- Login Button -->
    <Button Grid.Row="3" Grid.Column="1"
            Content="Login"
            Width="100"
            HorizontalAlignment="Right"
            Click="LoginButton_Click" />
</Grid>
```

### 3.2. StackPanel

**StackPanel** xếp các elements theo chiều ngang hoặc dọc.

```xml
<!-- Vertical StackPanel (default) -->
<StackPanel Orientation="Vertical" Margin="10">
    <TextBlock Text="Item 1" Background="LightBlue" Margin="5" />
    <TextBlock Text="Item 2" Background="LightGreen" Margin="5" />
    <TextBlock Text="Item 3" Background="LightCoral" Margin="5" />
</StackPanel>

<!-- Horizontal StackPanel -->
<StackPanel Orientation="Horizontal" Margin="10">
    <Button Content="Button 1" Margin="5" />
    <Button Content="Button 2" Margin="5" />
    <Button Content="Button 3" Margin="5" />
</StackPanel>
```

### 3.3. WrapPanel

**WrapPanel** tự động wrap elements khi hết chỗ.

```xml
<WrapPanel Orientation="Horizontal" Margin="10">
    <Button Content="Button 1" Width="100" Height="30" Margin="5" />
    <Button Content="Button 2" Width="100" Height="30" Margin="5" />
    <Button Content="Button 3" Width="100" Height="30" Margin="5" />
    <Button Content="Button 4" Width="100" Height="30" Margin="5" />
    <Button Content="Button 5" Width="100" Height="30" Margin="5" />
    <!-- Tự động wrap sang dòng mới nếu không đủ chỗ -->
</WrapPanel>
```

### 3.4. DockPanel

**DockPanel** dock elements vào các cạnh.

```xml
<DockPanel LastChildFill="True">
    <Menu DockPanel.Dock="Top" Background="LightGray">
        <MenuItem Header="File" />
        <MenuItem Header="Edit" />
        <MenuItem Header="View" />
    </Menu>

    <StatusBar DockPanel.Dock="Bottom" Background="LightGray">
        <TextBlock Text="Ready" />
    </StatusBar>

    <TreeView DockPanel.Dock="Left" Width="200" Background="WhiteSmoke">
        <TreeViewItem Header="Folder 1" />
        <TreeViewItem Header="Folder 2" />
    </TreeView>

    <TextBox AcceptsReturn="True"
             VerticalScrollBarVisibility="Auto" />
    <!-- LastChildFill=True: Element cuối cùng chiếm phần còn lại -->
</DockPanel>
```

### 3.5. Canvas

**Canvas** cho phép positioning tuyệt đối.

```xml
<Canvas>
    <Rectangle Canvas.Left="50" Canvas.Top="50"
               Width="100" Height="100"
               Fill="Blue" />

    <Ellipse Canvas.Left="200" Canvas.Top="100"
             Width="80" Height="80"
             Fill="Red" />

    <TextBlock Canvas.Left="100" Canvas.Top="200"
               Text="Hello WPF"
               FontSize="20" />
</Canvas>
```

### 3.6. UniformGrid

**UniformGrid** chia đều space cho tất cả cells.

```xml
<UniformGrid Rows="2" Columns="3" Margin="10">
    <Button Content="1" />
    <Button Content="2" />
    <Button Content="3" />
    <Button Content="4" />
    <Button Content="5" />
    <Button Content="6" />
    <!-- Tất cả buttons có kích thước giống nhau -->
</UniformGrid>
```

---

## 4. Common Controls

### 4.1. TextBlock và Label

```xml
<!-- TextBlock - lightweight, read-only -->
<TextBlock Text="This is a TextBlock"
           FontSize="16"
           FontWeight="Bold"
           Foreground="Blue" />

<!-- TextBlock with multiple styles -->
<TextBlock>
    <Run Text="Normal " />
    <Run Text="Bold " FontWeight="Bold" />
    <Run Text="Italic " FontStyle="Italic" />
    <Run Text="Red" Foreground="Red" />
</TextBlock>

<!-- Label - supports mnemonics -->
<Label Content="_Name:" Target="{Binding ElementName=txtName}" />
<TextBox x:Name="txtName" />
<!-- Alt+N sẽ focus vào TextBox -->
```

### 4.2. TextBox

```xml
<!-- Simple TextBox -->
<TextBox x:Name="txtSimple"
         Width="200"
         Text="Enter text here" />

<!-- Multiline TextBox -->
<TextBox AcceptsReturn="True"
         TextWrapping="Wrap"
         VerticalScrollBarVisibility="Auto"
         Height="100" />

<!-- Password Box -->
<PasswordBox x:Name="txtPassword"
             Width="200" />

<!-- TextBox with Placeholder (Watermark) -->
<TextBox x:Name="txtSearch" Width="200">
    <TextBox.Style>
        <Style TargetType="TextBox">
            <Style.Triggers>
                <Trigger Property="Text" Value="">
                    <Setter Property="Background">
                        <Setter.Value>
                            <VisualBrush Stretch="None" AlignmentX="Left">
                                <VisualBrush.Visual>
                                    <TextBlock Text="Search..."
                                               Foreground="Gray"
                                               Margin="5,0,0,0" />
                                </VisualBrush.Visual>
                            </VisualBrush>
                        </Setter.Value>
                    </Setter>
                </Trigger>
            </Style.Triggers>
        </Style>
    </TextBox.Style>
</TextBox>
```

### 4.3. Button

```xml
<!-- Simple Button -->
<Button Content="Click Me"
        Width="100"
        Height="30"
        Click="Button_Click" />

<!-- Button with Image -->
<Button Width="100" Height="40">
    <StackPanel Orientation="Horizontal">
        <Image Source="icon.png" Width="16" Height="16" Margin="0,0,5,0" />
        <TextBlock Text="Save" VerticalAlignment="Center" />
    </StackPanel>
</Button>

<!-- Custom styled button -->
<Button Content="Custom Button"
        Background="DodgerBlue"
        Foreground="White"
        FontSize="16"
        Padding="20,10"
        BorderThickness="0"
        Cursor="Hand">
    <Button.Effect>
        <DropShadowEffect ShadowDepth="2" BlurRadius="5" />
    </Button.Effect>
</Button>
```

### 4.4. CheckBox và RadioButton

```xml
<StackPanel Margin="10">
    <!-- CheckBox -->
    <CheckBox Content="Option 1" IsChecked="True" />
    <CheckBox Content="Option 2" />
    <CheckBox Content="Option 3" IsThreeState="True" />

    <!-- RadioButton (chỉ chọn 1) -->
    <RadioButton Content="Male" GroupName="Gender" IsChecked="True" />
    <RadioButton Content="Female" GroupName="Gender" />
    <RadioButton Content="Other" GroupName="Gender" />
</StackPanel>
```

### 4.5. ComboBox

```xml
<!-- Simple ComboBox -->
<ComboBox x:Name="cboCountry" Width="200">
    <ComboBoxItem Content="Vietnam" IsSelected="True" />
    <ComboBoxItem Content="Thailand" />
    <ComboBoxItem Content="Singapore" />
    <ComboBoxItem Content="Malaysia" />
</ComboBox>

<!-- Editable ComboBox -->
<ComboBox IsEditable="True" Width="200">
    <ComboBoxItem Content="Item 1" />
    <ComboBoxItem Content="Item 2" />
</ComboBox>
```

### 4.6. ListBox

```xml
<ListBox x:Name="lstItems" Width="200" Height="150">
    <ListBoxItem Content="Item 1" />
    <ListBoxItem Content="Item 2" />
    <ListBoxItem Content="Item 3" />
    <ListBoxItem Content="Item 4" />
</ListBox>

<!-- Multiple selection -->
<ListBox SelectionMode="Multiple" Width="200" Height="150">
    <ListBoxItem Content="Apple" />
    <ListBoxItem Content="Banana" />
    <ListBoxItem Content="Orange" />
</ListBox>
```

### 4.7. DataGrid

```xml
<DataGrid x:Name="dgData"
          AutoGenerateColumns="True"
          CanUserAddRows="False"
          CanUserDeleteRows="False"
          IsReadOnly="True"
          AlternatingRowBackground="LightGray"
          GridLinesVisibility="None">
</DataGrid>
```

```csharp
// Code-behind
public partial class MainWindow : Window
{
    public MainWindow()
    {
        InitializeComponent();
        LoadData();
    }

    private void LoadData()
    {
        var students = new List<Student>
        {
            new Student { Id = 1, Name = "Nguyen Van A", Age = 20, GPA = 3.5 },
            new Student { Id = 2, Name = "Tran Thi B", Age = 21, GPA = 3.8 },
            new Student { Id = 3, Name = "Le Van C", Age = 19, GPA = 3.2 }
        };

        dgData.ItemsSource = students;
    }
}

public class Student
{
    public int Id { get; set; }
    public string Name { get; set; }
    public int Age { get; set; }
    public double GPA { get; set; }
}
```

### 4.8. ListView

```xml
<ListView x:Name="lvProducts" Height="200">
    <ListView.View>
        <GridView>
            <GridViewColumn Header="ID" DisplayMemberBinding="{Binding Id}" Width="50" />
            <GridViewColumn Header="Name" DisplayMemberBinding="{Binding Name}" Width="150" />
            <GridViewColumn Header="Price" DisplayMemberBinding="{Binding Price}" Width="100" />
        </GridView>
    </ListView.View>
</ListView>
```

### 4.9. Menu

```xml
<Menu>
    <MenuItem Header="_File">
        <MenuItem Header="_New" InputGestureText="Ctrl+N" Click="New_Click" />
        <MenuItem Header="_Open" InputGestureText="Ctrl+O" Click="Open_Click" />
        <MenuItem Header="_Save" InputGestureText="Ctrl+S" Click="Save_Click" />
        <Separator />
        <MenuItem Header="E_xit" Click="Exit_Click" />
    </MenuItem>

    <MenuItem Header="_Edit">
        <MenuItem Header="_Cut" InputGestureText="Ctrl+X" />
        <MenuItem Header="_Copy" InputGestureText="Ctrl+C" />
        <MenuItem Header="_Paste" InputGestureText="Ctrl+V" />
    </MenuItem>

    <MenuItem Header="_Help">
        <MenuItem Header="_About" Click="About_Click" />
    </MenuItem>
</Menu>
```

### 4.10. ProgressBar

```xml
<!-- Determinate ProgressBar -->
<ProgressBar x:Name="pbProgress"
             Width="300"
             Height="25"
             Minimum="0"
             Maximum="100"
             Value="50" />

<!-- Indeterminate ProgressBar (loading animation) -->
<ProgressBar IsIndeterminate="True"
             Width="300"
             Height="25" />
```

---

## 5. Data Binding

### 5.1. Data Binding Là Gì?

**Data Binding** tự động sync data giữa UI (View) và data source.

### 5.2. Binding Modes

```csharp
OneWay      // Source -> Target (read-only)
TwoWay      // Source <-> Target (read-write)
OneTime     // Source -> Target (one time only)
OneWayToSource // Target -> Source
```

### 5.3. Simple Binding

#### XAML:
```xml
<StackPanel Margin="10">
    <TextBox x:Name="txtInput" Width="200" Margin="5" />

    <!-- Binding to another element -->
    <TextBlock Text="{Binding ElementName=txtInput, Path=Text}"
               FontSize="16"
               Margin="5" />

    <!-- TwoWay Binding -->
    <Slider x:Name="slider"
            Minimum="0"
            Maximum="100"
            Width="200"
            Margin="5" />
    <TextBlock Text="{Binding ElementName=slider, Path=Value, StringFormat='{}{0:F2}'}"
               Margin="5" />
</StackPanel>
```

### 5.4. Binding to DataContext

#### XAML:
```xml
<Window x:Class="MyApp.MainWindow"
        xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        Title="Data Binding Demo"
        Height="300"
        Width="400">

    <StackPanel Margin="20">
        <TextBlock Text="Name:" />
        <TextBox Text="{Binding Name, Mode=TwoWay, UpdateSourceTrigger=PropertyChanged}"
                 Width="200"
                 Margin="5" />

        <TextBlock Text="Age:" />
        <TextBox Text="{Binding Age, Mode=TwoWay}"
                 Width="200"
                 Margin="5" />

        <TextBlock Text="Email:" />
        <TextBox Text="{Binding Email, Mode=TwoWay}"
                 Width="200"
                 Margin="5" />

        <Button Content="Show Info"
                Click="ShowInfo_Click"
                Width="100"
                Margin="10" />
    </StackPanel>
</Window>
```

#### Code-behind:
```csharp
public partial class MainWindow : Window
{
    private Person person;

    public MainWindow()
    {
        InitializeComponent();

        person = new Person
        {
            Name = "John Doe",
            Age = 25,
            Email = "john@example.com"
        };

        // Set DataContext
        this.DataContext = person;
    }

    private void ShowInfo_Click(object sender, RoutedEventArgs e)
    {
        MessageBox.Show($"Name: {person.Name}\nAge: {person.Age}\nEmail: {person.Email}");
    }
}

public class Person
{
    public string Name { get; set; }
    public int Age { get; set; }
    public string Email { get; set; }
}
```

### 5.5. INotifyPropertyChanged

Để UI tự động update khi data thay đổi trong code:

```csharp
using System.ComponentModel;
using System.Runtime.CompilerServices;

public class Person : INotifyPropertyChanged
{
    private string name;
    private int age;
    private string email;

    public string Name
    {
        get => name;
        set
        {
            if (name != value)
            {
                name = value;
                OnPropertyChanged();
            }
        }
    }

    public int Age
    {
        get => age;
        set
        {
            if (age != value)
            {
                age = value;
                OnPropertyChanged();
            }
        }
    }

    public string Email
    {
        get => email;
        set
        {
            if (email != value)
            {
                email = value;
                OnPropertyChanged();
            }
        }
    }

    public event PropertyChangedEventHandler PropertyChanged;

    protected void OnPropertyChanged([CallerMemberName] string propertyName = null)
    {
        PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(propertyName));
    }
}
```

### 5.6. ObservableCollection

Để ListBox/DataGrid tự động update khi add/remove items:

```csharp
using System.Collections.ObjectModel;

public class MainViewModel : INotifyPropertyChanged
{
    private ObservableCollection<Student> students;

    public ObservableCollection<Student> Students
    {
        get => students;
        set
        {
            students = value;
            OnPropertyChanged();
        }
    }

    public MainViewModel()
    {
        Students = new ObservableCollection<Student>
        {
            new Student { Id = 1, Name = "John", GPA = 3.5 },
            new Student { Id = 2, Name = "Jane", GPA = 3.8 }
        };
    }

    public void AddStudent(Student student)
    {
        Students.Add(student); // UI tự động update
    }

    public void RemoveStudent(Student student)
    {
        Students.Remove(student); // UI tự động update
    }

    // INotifyPropertyChanged implementation
    public event PropertyChangedEventHandler PropertyChanged;
    protected void OnPropertyChanged([CallerMemberName] string propertyName = null)
    {
        PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(propertyName));
    }
}
```

```xml
<!-- XAML -->
<ListBox ItemsSource="{Binding Students}">
    <ListBox.ItemTemplate>
        <DataTemplate>
            <StackPanel Orientation="Horizontal">
                <TextBlock Text="{Binding Id}" Width="50" />
                <TextBlock Text="{Binding Name}" Width="150" />
                <TextBlock Text="{Binding GPA}" />
            </StackPanel>
        </DataTemplate>
    </ListBox.ItemTemplate>
</ListBox>
```

---

## 6. Event Handling

### 6.1. Click Event

```xml
<Button Content="Click Me" Click="Button_Click" />
```

```csharp
private void Button_Click(object sender, RoutedEventArgs e)
{
    MessageBox.Show("Button clicked!");
}
```

### 6.2. TextChanged Event

```xml
<TextBox TextChanged="TextBox_TextChanged" />
```

```csharp
private void TextBox_TextChanged(object sender, TextChangedEventArgs e)
{
    TextBox textBox = sender as TextBox;
    Debug.WriteLine($"Text changed: {textBox.Text}");
}
```

### 6.3. SelectionChanged Event

```xml
<ComboBox SelectionChanged="ComboBox_SelectionChanged">
    <ComboBoxItem Content="Option 1" />
    <ComboBoxItem Content="Option 2" />
</ComboBox>
```

```csharp
private void ComboBox_SelectionChanged(object sender, SelectionChangedEventArgs e)
{
    ComboBox comboBox = sender as ComboBox;
    ComboBoxItem selected = comboBox.SelectedItem as ComboBoxItem;
    MessageBox.Show($"Selected: {selected.Content}");
}
```

### 6.4. Mouse Events

```xml
<Border Width="200" Height="200" Background="LightBlue"
        MouseEnter="Border_MouseEnter"
        MouseLeave="Border_MouseLeave"
        MouseDown="Border_MouseDown"
        MouseUp="Border_MouseUp">
    <TextBlock Text="Hover Me"
               HorizontalAlignment="Center"
               VerticalAlignment="Center" />
</Border>
```

```csharp
private void Border_MouseEnter(object sender, MouseEventArgs e)
{
    Border border = sender as Border;
    border.Background = Brushes.LightGreen;
}

private void Border_MouseLeave(object sender, MouseEventArgs e)
{
    Border border = sender as Border;
    border.Background = Brushes.LightBlue;
}
```

### 6.5. Keyboard Events

```xml
<TextBox KeyDown="TextBox_KeyDown"
         KeyUp="TextBox_KeyUp"
         PreviewKeyDown="TextBox_PreviewKeyDown" />
```

```csharp
private void TextBox_KeyDown(object sender, KeyEventArgs e)
{
    if (e.Key == Key.Enter)
    {
        MessageBox.Show("Enter pressed!");
        e.Handled = true; // Prevent further processing
    }
}
```

---

## 7. Resources

### 7.1. Static Resources

```xml
<Window.Resources>
    <!-- Brush Resource -->
    <SolidColorBrush x:Key="PrimaryBrush" Color="#2196F3" />

    <!-- System Double -->
    <System:Double x:Key="StandardFontSize">16</System:Double>

    <!-- Thickness -->
    <Thickness x:Key="StandardMargin">10</Thickness>
</Window.Resources>

<StackPanel>
    <Button Content="Button 1"
            Background="{StaticResource PrimaryBrush}"
            FontSize="{StaticResource StandardFontSize}"
            Margin="{StaticResource StandardMargin}" />

    <Button Content="Button 2"
            Background="{StaticResource PrimaryBrush}"
            FontSize="{StaticResource StandardFontSize}"
            Margin="{StaticResource StandardMargin}" />
</StackPanel>
```

### 7.2. Dynamic Resources

```xml
<Window.Resources>
    <SolidColorBrush x:Key="DynamicBrush" Color="Red" />
</Window.Resources>

<Button Content="Change Color"
        Background="{DynamicResource DynamicBrush}"
        Click="ChangeColor_Click" />
```

```csharp
private void ChangeColor_Click(object sender, RoutedEventArgs e)
{
    // Change resource at runtime
    this.Resources["DynamicBrush"] = new SolidColorBrush(Colors.Blue);
}
```

### 7.3. Application Resources (App.xaml)

```xml
<Application x:Class="MyApp.App"
             xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             StartupUri="MainWindow.xaml">
    <Application.Resources>
        <!-- Global resources -->
        <SolidColorBrush x:Key="AppPrimaryColor" Color="#2196F3" />
        <SolidColorBrush x:Key="AppSecondaryColor" Color="#FFC107" />
        <System:Double x:Key="AppFontSize">14</System:Double>
    </Application.Resources>
</Application>
```

---

## 8. Styles

### 8.1. Inline Style

```xml
<Button Content="Styled Button">
    <Button.Style>
        <Style TargetType="Button">
            <Setter Property="Background" Value="DodgerBlue" />
            <Setter Property="Foreground" Value="White" />
            <Setter Property="FontSize" Value="16" />
            <Setter Property="Padding" Value="20,10" />
        </Style>
    </Button.Style>
</Button>
```

### 8.2. Named Style

```xml
<Window.Resources>
    <Style x:Key="PrimaryButtonStyle" TargetType="Button">
        <Setter Property="Background" Value="DodgerBlue" />
        <Setter Property="Foreground" Value="White" />
        <Setter Property="FontSize" Value="16" />
        <Setter Property="Padding" Value="20,10" />
        <Setter Property="BorderThickness" Value="0" />
        <Setter Property="Cursor" Value="Hand" />
    </Style>
</Window.Resources>

<StackPanel>
    <Button Content="Save" Style="{StaticResource PrimaryButtonStyle}" />
    <Button Content="Delete" Style="{StaticResource PrimaryButtonStyle}" />
</StackPanel>
```

### 8.3. Implicit Style (Auto-apply)

```xml
<Window.Resources>
    <!-- Tự động apply cho tất cả TextBlock -->
    <Style TargetType="TextBlock">
        <Setter Property="FontSize" Value="14" />
        <Setter Property="Margin" Value="5" />
    </Style>

    <!-- Tự động apply cho tất cả Button -->
    <Style TargetType="Button">
        <Setter Property="MinWidth" Value="80" />
        <Setter Property="Margin" Value="5" />
    </Style>
</Window.Resources>
```

### 8.4. Style Inheritance

```xml
<Window.Resources>
    <!-- Base style -->
    <Style x:Key="BaseButtonStyle" TargetType="Button">
        <Setter Property="FontSize" Value="14" />
        <Setter Property="Padding" Value="10,5" />
        <Setter Property="Margin" Value="5" />
    </Style>

    <!-- Inherited style -->
    <Style x:Key="PrimaryButton"
           TargetType="Button"
           BasedOn="{StaticResource BaseButtonStyle}">
        <Setter Property="Background" Value="DodgerBlue" />
        <Setter Property="Foreground" Value="White" />
    </Style>

    <Style x:Key="DangerButton"
           TargetType="Button"
           BasedOn="{StaticResource BaseButtonStyle}">
        <Setter Property="Background" Value="Red" />
        <Setter Property="Foreground" Value="White" />
    </Style>
</Window.Resources>
```

### 8.5. Style Triggers

```xml
<Style x:Key="HoverButtonStyle" TargetType="Button">
    <Setter Property="Background" Value="LightGray" />
    <Setter Property="Foreground" Value="Black" />

    <!-- Property Trigger -->
    <Style.Triggers>
        <Trigger Property="IsMouseOver" Value="True">
            <Setter Property="Background" Value="DodgerBlue" />
            <Setter Property="Foreground" Value="White" />
        </Trigger>

        <Trigger Property="IsPressed" Value="True">
            <Setter Property="Background" Value="DarkBlue" />
        </Trigger>

        <Trigger Property="IsEnabled" Value="False">
            <Setter Property="Opacity" Value="0.5" />
        </Trigger>
    </Style.Triggers>
</Style>
```

---

## 9. Commands

### 9.1. Built-in Commands

```xml
<Window.CommandBindings>
    <CommandBinding Command="ApplicationCommands.New"
                    Executed="New_Executed"
                    CanExecute="New_CanExecute" />
    <CommandBinding Command="ApplicationCommands.Open"
                    Executed="Open_Executed" />
    <CommandBinding Command="ApplicationCommands.Save"
                    Executed="Save_Executed" />
</Window.CommandBindings>

<Menu>
    <MenuItem Header="_File">
        <MenuItem Header="_New" Command="ApplicationCommands.New" />
        <MenuItem Header="_Open" Command="ApplicationCommands.Open" />
        <MenuItem Header="_Save" Command="ApplicationCommands.Save" />
    </MenuItem>
</Menu>
```

```csharp
private void New_Executed(object sender, ExecutedRoutedEventArgs e)
{
    MessageBox.Show("New command executed");
}

private void New_CanExecute(object sender, CanExecuteRoutedEventArgs e)
{
    e.CanExecute = true; // Enable command
}

private void Open_Executed(object sender, ExecutedRoutedEventArgs e)
{
    MessageBox.Show("Open command executed");
}

private void Save_Executed(object sender, ExecutedRoutedEventArgs e)
{
    MessageBox.Show("Save command executed");
}
```

### 9.2. Custom Commands

```csharp
public static class CustomCommands
{
    public static readonly RoutedCommand RefreshCommand = new RoutedCommand(
        "Refresh",
        typeof(CustomCommands),
        new InputGestureCollection()
        {
            new KeyGesture(Key.F5)
        }
    );
}
```

```xml
<Window.CommandBindings>
    <CommandBinding Command="local:CustomCommands.RefreshCommand"
                    Executed="Refresh_Executed" />
</Window.CommandBindings>

<Button Content="Refresh" Command="local:CustomCommands.RefreshCommand" />
```

---

## 10. Bài Tập Thực Hành

### Bài 1: Calculator App

Xây dựng ứng dụng máy tính đơn giản:
- Sử dụng Grid layout
- Các nút số 0-9, +, -, *, /, =
- TextBox hiển thị kết quả
- Xử lý các phép tính cơ bản

### Bài 2: Todo List App

- TextBox nhập task mới
- Button "Add Task"
- ListBox hiển thị danh sách tasks
- Button "Delete Selected"
- CheckBox đánh dấu completed

### Bài 3: Student Management

- Form nhập thông tin sinh viên (ID, Name, Age, GPA)
- Button Add/Update/Delete
- DataGrid hiển thị danh sách
- Implement INotifyPropertyChanged
- Sử dụng ObservableCollection

### Bài 4: Login Form

- TextBox Username
- PasswordBox Password
- CheckBox "Remember Me"
- Button "Login"
- Validation và error messages
- Style cho UI đẹp

---

## 📝 Tóm Tắt

### Key Points:

1. **WPF** là framework mạnh mẽ để xây dựng desktop apps
2. **XAML** là declarative language để define UI
3. **Layout Controls**: Grid, StackPanel, DockPanel, Canvas, WrapPanel
4. **Data Binding** tự động sync UI với data
5. **INotifyPropertyChanged** để notify UI khi data thay đổi
6. **ObservableCollection** cho collections
7. **Resources** để tái sử dụng values
8. **Styles** để customize UI
9. **Commands** để implement logic

### Best Practices:

- ✅ Sử dụng Grid cho complex layouts
- ✅ Implement INotifyPropertyChanged cho data binding
- ✅ Sử dụng ObservableCollection cho lists
- ✅ Define resources và styles trong App.xaml
- ✅ Sử dụng Commands thay vì Click events
- ✅ Separate UI (XAML) và logic (C#)

---

**Next:** [03-WPF-Nang-Cao.md](03-WPF-Nang-Cao.md)
