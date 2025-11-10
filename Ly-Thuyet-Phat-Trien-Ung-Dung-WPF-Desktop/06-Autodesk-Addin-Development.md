# AUTODESK ADD-IN DEVELOPMENT VỚI C#

## 📚 Mục Lục

1. [Giới Thiệu Autodesk API](#1-giới-thiệu-autodesk-api)
2. [AutoCAD .NET API](#2-autocad-net-api)
3. [Revit API](#3-revit-api)
4. [Inventor API](#4-inventor-api)
5. [WPF UI trong Add-ins](#5-wpf-ui-trong-add-ins)
6. [Ribbon Customization](#6-ribbon-customization)
7. [Best Practices](#7-best-practices)
8. [Debugging](#8-debugging)
9. [Deployment](#9-deployment)
10. [Tài Nguyên Học Tập](#10-tài-nguyên-học-tập)

---

## 1. Giới Thiệu Autodesk API

### 1.1. Các Loại API

**Autodesk** cung cấp .NET API cho các sản phẩm:

- **AutoCAD** - CAD 2D/3D general purpose
- **Revit** - BIM (Building Information Modeling)
- **Inventor** - 3D CAD for mechanical design
- **Civil 3D** - Infrastructure design
- **Navisworks** - Project review
- **Advance Steel** - Structural engineering

### 1.2. Yêu Cầu

```
- Visual Studio 2019/2022
- .NET Framework 4.8 (AutoCAD, Revit)
- C# programming knowledge
- WPF knowledge (for UI)
- Autodesk software installed (AutoCAD, Revit, Inventor)
```

### 1.3. Cấu Trúc Add-in Project

```
MyAddin/
├── Commands/
│   ├── Command1.cs
│   └── Command2.cs
├── UI/
│   ├── MainWindow.xaml
│   └── MainWindow.xaml.cs
├── Models/
│   └── MyData.cs
├── Services/
│   └── DataService.cs
├── Resources/
│   ├── Icons/
│   └── Styles.xaml
├── Properties/
│   └── AssemblyInfo.cs
└── PackageContents.xml (Revit)
    or addin.bundle/ (AutoCAD)
```

---

## 2. AutoCAD .NET API

### 2.1. Setup Project

**1. Tạo Class Library Project (.NET Framework 4.8)**

**2. Add References:**
```
acdbmgd.dll       - Database management
acmgd.dll         - Application services
accoremgd.dll     - Core functionality
AcWindows.dll     - Windows integration
```

**3. Set Copy Local = False** cho tất cả Autodesk DLLs

### 2.2. Basic Command

```csharp
using Autodesk.AutoCAD.Runtime;
using Autodesk.AutoCAD.ApplicationServices;
using Autodesk.AutoCAD.DatabaseServices;
using Autodesk.AutoCAD.EditorInput;
using Autodesk.AutoCAD.Geometry;

[assembly: CommandClass(typeof(MyAddin.Commands))]

namespace MyAddin
{
    public class Commands
    {
        [CommandMethod("HelloAutoCAD")]
        public void HelloAutoCAD()
        {
            // Get the current document and editor
            Document doc = Application.DocumentManager.MdiActiveDocument;
            Editor ed = doc.Editor;

            // Display a message
            ed.WriteMessage("\nHello from AutoCAD .NET API!");
        }
    }
}
```

### 2.3. Drawing Entities

```csharp
[CommandMethod("DrawCircle")]
public void DrawCircle()
{
    Document doc = Application.DocumentManager.MdiActiveDocument;
    Database db = doc.Database;
    Editor ed = doc.Editor;

    // Prompt for center point
    PromptPointResult ppr = ed.GetPoint("\nSpecify center point: ");
    if (ppr.Status != PromptStatus.OK)
        return;

    Point3d center = ppr.Value;

    // Prompt for radius
    PromptDoubleResult pdr = ed.GetDouble("\nSpecify radius: ");
    if (pdr.Status != PromptStatus.OK)
        return;

    double radius = pdr.Value;

    // Start a transaction
    using (Transaction tr = db.TransactionManager.StartTransaction())
    {
        try
        {
            // Open the Block table for read
            BlockTable bt = tr.GetObject(db.BlockTableId, OpenMode.ForRead) as BlockTable;

            // Open the Block table record Model space for write
            BlockTableRecord btr = tr.GetObject(bt[BlockTableRecord.ModelSpace], OpenMode.ForWrite) as BlockTableRecord;

            // Create a circle
            using (Circle circle = new Circle())
            {
                circle.Center = center;
                circle.Radius = radius;
                circle.ColorIndex = 1; // Red

                // Add to the database
                btr.AppendEntity(circle);
                tr.AddNewlyCreatedDBObject(circle, true);
            }

            // Commit the transaction
            tr.Commit();

            ed.WriteMessage($"\nCircle created at {center} with radius {radius}");
        }
        catch (System.Exception ex)
        {
            ed.WriteMessage($"\nError: {ex.Message}");
            tr.Abort();
        }
    }
}
```

### 2.4. Entity Selection

```csharp
[CommandMethod("SelectEntities")]
public void SelectEntities()
{
    Document doc = Application.DocumentManager.MdiActiveDocument;
    Database db = doc.Database;
    Editor ed = doc.Editor;

    // Create a selection filter for circles only
    TypedValue[] filterList = new TypedValue[]
    {
        new TypedValue((int)DxfCode.Start, "CIRCLE")
    };
    SelectionFilter filter = new SelectionFilter(filterList);

    // Prompt for selection
    PromptSelectionResult psr = ed.GetSelection(filter);

    if (psr.Status != PromptStatus.OK)
        return;

    SelectionSet ss = psr.Value;

    using (Transaction tr = db.TransactionManager.StartTransaction())
    {
        foreach (SelectedObject so in ss)
        {
            if (so != null)
            {
                Entity ent = tr.GetObject(so.ObjectId, OpenMode.ForRead) as Entity;

                if (ent is Circle circle)
                {
                    ed.WriteMessage($"\nCircle at {circle.Center}, radius: {circle.Radius}");
                }
            }
        }

        tr.Commit();
    }
}
```

### 2.5. Modify Entities

```csharp
[CommandMethod("ChangeColor")]
public void ChangeColor()
{
    Document doc = Application.DocumentManager.MdiActiveDocument;
    Database db = doc.Database;
    Editor ed = doc.Editor;

    PromptSelectionResult psr = ed.GetSelection();
    if (psr.Status != PromptStatus.OK)
        return;

    SelectionSet ss = psr.Value;

    using (Transaction tr = db.TransactionManager.StartTransaction())
    {
        foreach (SelectedObject so in ss)
        {
            Entity ent = tr.GetObject(so.ObjectId, OpenMode.ForWrite) as Entity;
            if (ent != null)
            {
                ent.ColorIndex = 3; // Green
            }
        }

        tr.Commit();
        ed.WriteMessage($"\n{ss.Count} entities changed to green");
    }
}
```

---

## 3. Revit API

### 3.1. Setup Project

**1. Tạo Class Library Project (.NET Framework 4.8)**

**2. Add References:**
```
RevitAPI.dll
RevitAPIUI.dll
```

**3. Tạo Manifest File** (.addin)

### 3.2. External Command

```csharp
using Autodesk.Revit.Attributes;
using Autodesk.Revit.DB;
using Autodesk.Revit.UI;
using System;

namespace MyRevitAddin
{
    [Transaction(TransactionMode.Manual)]
    public class HelloRevit : IExternalCommand
    {
        public Result Execute(ExternalCommandData commandData, ref string message, ElementSet elements)
        {
            try
            {
                // Get application and document
                UIApplication uiApp = commandData.Application;
                UIDocument uiDoc = uiApp.ActiveUIDocument;
                Document doc = uiDoc.Document;

                // Show message
                TaskDialog.Show("Hello Revit", $"Document: {doc.Title}\nElements: {new FilteredElementCollector(doc).GetElementCount()}");

                return Result.Succeeded;
            }
            catch (Exception ex)
            {
                message = ex.Message;
                return Result.Failed;
            }
        }
    }
}
```

### 3.3. Manifest File (.addin)

```xml
<?xml version="1.0" encoding="utf-8"?>
<RevitAddIns>
  <AddIn Type="Command">
    <Name>Hello Revit</Name>
    <Assembly>MyRevitAddin.dll</Assembly>
    <AddInId>12345678-1234-1234-1234-123456789ABC</AddInId>
    <FullClassName>MyRevitAddin.HelloRevit</FullClassName>
    <Text>Hello Revit</Text>
    <Description>My first Revit add-in</Description>
    <VendorId>MYCO</VendorId>
    <VendorDescription>My Company</VendorDescription>
  </AddIn>
</RevitAddIns>
```

**Location:** `C:\ProgramData\Autodesk\Revit\Addins\2024\MyAddin.addin`

### 3.4. Create Wall

```csharp
[Transaction(TransactionMode.Manual)]
public class CreateWall : IExternalCommand
{
    public Result Execute(ExternalCommandData commandData, ref string message, ElementSet elements)
    {
        UIDocument uiDoc = commandData.Application.ActiveUIDocument;
        Document doc = uiDoc.Document;

        try
        {
            // Create two points
            XYZ point1 = new XYZ(0, 0, 0);
            XYZ point2 = new XYZ(10, 0, 0);

            // Create a line
            Line line = Line.CreateBound(point1, point2);

            // Start a transaction
            using (Transaction trans = new Transaction(doc, "Create Wall"))
            {
                trans.Start();

                // Get a wall type
                FilteredElementCollector collector = new FilteredElementCollector(doc);
                WallType wallType = collector.OfClass(typeof(WallType)).FirstElement() as WallType;

                // Get a level
                Level level = new FilteredElementCollector(doc)
                    .OfClass(typeof(Level))
                    .FirstElement() as Level;

                // Create the wall
                Wall wall = Wall.Create(doc, line, level.Id, false);

                trans.Commit();

                TaskDialog.Show("Success", "Wall created successfully!");
                return Result.Succeeded;
            }
        }
        catch (Exception ex)
        {
            message = ex.Message;
            return Result.Failed;
        }
    }
}
```

### 3.5. Filter Elements

```csharp
[Transaction(TransactionMode.ReadOnly)]
public class CountWalls : IExternalCommand
{
    public Result Execute(ExternalCommandData commandData, ref string message, ElementSet elements)
    {
        Document doc = commandData.Application.ActiveUIDocument.Document;

        // Get all walls
        FilteredElementCollector collector = new FilteredElementCollector(doc);
        ICollection<Element> walls = collector.OfClass(typeof(Wall)).ToElements();

        // Count by wall type
        var wallsByType = walls
            .GroupBy(w => w.Name)
            .Select(g => new { Type = g.Key, Count = g.Count() });

        string result = "Walls in document:\n\n";
        foreach (var item in wallsByType)
        {
            result += $"{item.Type}: {item.Count}\n";
        }

        TaskDialog.Show("Wall Count", result);
        return Result.Succeeded;
    }
}
```

### 3.6. External Application (Ribbon)

```csharp
using Autodesk.Revit.UI;
using System;
using System.Reflection;
using System.Windows.Media.Imaging;

namespace MyRevitAddin
{
    public class Application : IExternalApplication
    {
        public Result OnStartup(UIControlledApplication application)
        {
            try
            {
                // Create ribbon tab
                string tabName = "My Tools";
                application.CreateRibbonTab(tabName);

                // Create ribbon panel
                RibbonPanel panel = application.CreateRibbonPanel(tabName, "Commands");

                // Add button
                string assemblyPath = Assembly.GetExecutingAssembly().Location;

                PushButtonData buttonData = new PushButtonData(
                    "HelloRevit",
                    "Hello\nRevit",
                    assemblyPath,
                    "MyRevitAddin.HelloRevit"
                );

                // Add icon (optional)
                // buttonData.LargeImage = new BitmapImage(new Uri("pack://application:,,,/MyRevitAddin;component/Resources/icon32.png"));

                PushButton button = panel.AddItem(buttonData) as PushButton;
                button.ToolTip = "Say hello to Revit";

                return Result.Succeeded;
            }
            catch (Exception ex)
            {
                TaskDialog.Show("Error", ex.Message);
                return Result.Failed;
            }
        }

        public Result OnShutdown(UIControlledApplication application)
        {
            return Result.Succeeded;
        }
    }
}
```

---

## 4. Inventor API

### 4.1. Setup Project

**1. Tạo Class Library Project**

**2. Add References:**
```
Autodesk.Inventor.Interop.dll
```

### 4.2. Basic Add-in

```csharp
using Inventor;
using System;
using System.Runtime.InteropServices;

namespace MyInventorAddin
{
    [Guid("YOUR-GUID-HERE")]
    public class StandardAddInServer : ApplicationAddInServer
    {
        private Inventor.Application inventorApp;
        private ButtonDefinition button;

        public void Activate(ApplicationAddInSite addInSiteObject, bool firstTime)
        {
            // Get Inventor application object
            inventorApp = addInSiteObject.Application;

            // Create button
            if (firstTime)
            {
                ControlDefinitions controlDefs = inventorApp.CommandManager.ControlDefinitions;

                button = controlDefs.AddButtonDefinition(
                    "Hello Inventor",
                    "HelloInventor",
                    CommandTypesEnum.kShapeEditCmdType,
                    AddInClientID()
                );

                // Add event handler
                button.OnExecute += Button_OnExecute;
            }
        }

        private void Button_OnExecute(NameValueMap context)
        {
            inventorApp.StatusBarText = "Hello from Inventor Add-in!";
        }

        public void Deactivate()
        {
            // Cleanup
            Marshal.ReleaseComObject(inventorApp);
            inventorApp = null;

            GC.Collect();
            GC.WaitForPendingFinalizers();
        }

        public void ExecuteCommand(int commandID)
        {
            // Not used
        }

        public object Automation
        {
            get { return null; }
        }
    }
}
```

### 4.3. Create Part

```csharp
private void CreateBox()
{
    // Create a new part document
    PartDocument partDoc = (PartDocument)inventorApp.Documents.Add(
        DocumentTypeEnum.kPartDocumentObject,
        inventorApp.FileManager.GetTemplateFile(DocumentTypeEnum.kPartDocumentObject)
    );

    // Get component definition
    PartComponentDefinition compDef = partDoc.ComponentDefinition;

    // Create a sketch on the XY plane
    PlanarSketch sketch = compDef.Sketches.Add(compDef.WorkPlanes[3]);

    // Draw a rectangle
    TransientGeometry tg = inventorApp.TransientGeometry;
    Point2d point1 = tg.CreatePoint2d(0, 0);
    Point2d point2 = tg.CreatePoint2d(10, 10);

    sketch.SketchLines.AddAsTwoPointRectangle(point1, point2);

    // Create profile
    Profile profile = sketch.Profiles.AddForSolid();

    // Extrude
    ExtrudeDefinition extrudeDef = compDef.Features.ExtrudeFeatures.CreateExtrudeDefinition(
        profile,
        PartFeatureOperationEnum.kJoinOperation
    );

    extrudeDef.SetDistanceExtent(5, PartFeatureExtentDirectionEnum.kPositiveExtentDirection);

    ExtrudeFeature extrude = compDef.Features.ExtrudeFeatures.Add(extrudeDef);
}
```

---

## 5. WPF UI trong Add-ins

### 5.1. AutoCAD - Show WPF Window

```csharp
using Autodesk.AutoCAD.Runtime;
using Autodesk.AutoCAD.ApplicationServices;

[CommandMethod("ShowUI")]
public void ShowUI()
{
    Document doc = Application.DocumentManager.MdiActiveDocument;

    try
    {
        // Create and show WPF window
        MyWindow window = new MyWindow();

        // Show as modal dialog
        Application.ShowModalDialog(window);

        // Or show modeless
        // Application.ShowModelessDialog(window);
    }
    catch (System.Exception ex)
    {
        doc.Editor.WriteMessage($"\nError: {ex.Message}");
    }
}
```

### 5.2. Revit - Show WPF Window

```csharp
[Transaction(TransactionMode.Manual)]
public class ShowUICommand : IExternalCommand
{
    public Result Execute(ExternalCommandData commandData, ref string message, ElementSet elements)
    {
        try
        {
            MyWindow window = new MyWindow(commandData);
            window.ShowDialog();

            return Result.Succeeded;
        }
        catch (Exception ex)
        {
            message = ex.Message;
            return Result.Failed;
        }
    }
}
```

### 5.3. WPF Window with MVVM

```xml
<!-- MyWindow.xaml -->
<Window x:Class="MyAddin.MyWindow"
        xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        xmlns:vm="clr-namespace:MyAddin.ViewModels"
        Title="My Addin Tool"
        Height="400"
        Width="600">

    <Window.DataContext>
        <vm:MyViewModel />
    </Window.DataContext>

    <Grid Margin="20">
        <Grid.RowDefinitions>
            <RowDefinition Height="Auto" />
            <RowDefinition Height="*" />
            <RowDefinition Height="Auto" />
        </Grid.RowDefinitions>

        <TextBlock Grid.Row="0" Text="Elements in Document" FontSize="18" FontWeight="Bold" />

        <DataGrid Grid.Row="1"
                  ItemsSource="{Binding Elements}"
                  AutoGenerateColumns="True"
                  Margin="0,10,0,10" />

        <StackPanel Grid.Row="2" Orientation="Horizontal" HorizontalAlignment="Right">
            <Button Content="Refresh" Command="{Binding RefreshCommand}" Width="100" Margin="5" />
            <Button Content="Close" Command="{Binding CloseCommand}" Width="100" Margin="5" />
        </StackPanel>
    </Grid>
</Window>
```

---

## 6. Ribbon Customization

### 6.1. AutoCAD Ribbon (CUI)

AutoCAD sử dụng CUI (Customization User Interface) files để customize ribbon.

**Programmatically:**
```csharp
// Load ribbon using CUI file
// This is typically done through CUI editor, not code
```

### 6.2. Revit Ribbon

```csharp
public Result OnStartup(UIControlledApplication app)
{
    // Create ribbon tab
    string tabName = "My Company";
    app.CreateRibbonTab(tabName);

    // Create ribbon panel
    RibbonPanel panel = app.CreateRibbonPanel(tabName, "Tools");

    // Add push button
    string assemblyPath = Assembly.GetExecutingAssembly().Location;

    PushButtonData button1Data = new PushButtonData(
        "Button1",
        "Tool 1",
        assemblyPath,
        "MyAddin.Command1"
    );

    PushButton button1 = panel.AddItem(button1Data) as PushButton;
    button1.ToolTip = "Description of Tool 1";
    button1.LargeImage = GetImage("icon32.png");

    // Add pulldown button
    PulldownButtonData pulldownData = new PulldownButtonData("Pulldown1", "More Tools");
    PulldownButton pulldown = panel.AddItem(pulldownData) as PulldownButton;

    pulldown.AddPushButton(new PushButtonData("Sub1", "Sub Tool 1", assemblyPath, "MyAddin.SubCommand1"));
    pulldown.AddPushButton(new PushButtonData("Sub2", "Sub Tool 2", assemblyPath, "MyAddin.SubCommand2"));

    return Result.Succeeded;
}

private BitmapImage GetImage(string imageName)
{
    return new BitmapImage(new Uri($"pack://application:,,,/MyAddin;component/Resources/{imageName}"));
}
```

---

## 7. Best Practices

### 7.1. Do's ✅

```csharp
// ✅ Always use transactions
using (Transaction trans = doc.TransactionManager.StartTransaction())
{
    // Modify entities
    trans.Commit();
}

// ✅ Dispose objects properly
using (Circle circle = new Circle()) { }

// ✅ Check for null
if (entity != null) { }

// ✅ Use try-catch
try { }
catch (Exception ex) { ed.WriteMessage($"Error: {ex.Message}"); }

// ✅ Set Copy Local = False for Autodesk DLLs

// ✅ Use appropriate transaction modes in Revit
[Transaction(TransactionMode.Manual)]
```

### 7.2. Don'ts ❌

```csharp
// ❌ Don't modify entities outside transaction
entity.Color = Color.Red; // Error!

// ❌ Don't forget to commit transaction
trans.Start();
// ... modifications ...
// Missing: trans.Commit();

// ❌ Don't keep entities open longer than needed

// ❌ Don't hardcode paths
string path = "C:\\Users\\..."; // Bad!

// ❌ Don't show modal dialogs on document events
```

---

## 8. Debugging

### 8.1. AutoCAD Debugging

**1. Project Properties**
- Debug tab
- Start external program: `C:\Program Files\Autodesk\AutoCAD 2024\acad.exe`

**2. Load Add-in**
```
NETLOAD command
Browse to your DLL
```

**3. Attach to Process**
- Debug → Attach to Process
- Select acad.exe

### 8.2. Revit Debugging

**1. Project Properties**
- Debug tab
- Start external program: `C:\Program Files\Autodesk\Revit 2024\Revit.exe`

**2. Copy .addin and .dll**
```
Post-build event:
copy "$(TargetPath)" "C:\ProgramData\Autodesk\Revit\Addins\2024\"
copy "$(ProjectDir)MyAddin.addin" "C:\ProgramData\Autodesk\Revit\Addins\2024\"
```

---

## 9. Deployment

### 9.1. AutoCAD Bundle Structure

```
MyAddin.bundle/
├── Contents/
│   ├── Windows/
│   │   └── MyAddin.dll
│   └── PackageContents.xml
```

**PackageContents.xml:**
```xml
<?xml version="1.0" encoding="utf-8"?>
<ApplicationPackage>
  <Components>
    <RuntimeRequirements OS="Win64" Platform="AutoCAD" />
    <ComponentEntry AppName="MyAddin" Version="1.0" ModuleName="./MyAddin.dll">
      <Commands>
        <Command Local="MYADDIN" Global="MYADDIN" />
      </Commands>
    </ComponentEntry>
  </Components>
</ApplicationPackage>
```

### 9.2. Revit Deployment

**Copy files to:**
```
C:\ProgramData\Autodesk\Revit\Addins\2024\
```

---

## 10. Tài Nguyên Học Tập

### 10.1. Documentation

- **AutoCAD .NET**: https://www.autodesk.com/developer-network/platform-technologies/autocad
- **Revit API**: https://www.revitapidocs.com/
- **Inventor API**: https://help.autodesk.com/view/INVNTOR/2024/ENU/?guid=GUID-API_Welcome

### 10.2. Communities

- **Autodesk Forums**: https://forums.autodesk.com/
- **RevitAPI.dll Blog**: https://thebuildingcoder.typepad.com/
- **Stack Overflow**: Tag [autocad], [revit-api]

### 10.3. Sample Code

- **AutoCAD .NET Samples**: https://github.com/ADN-DevTech/AutoCAD-DotNet-Samples
- **Revit SDK**: Installed with Revit

---

## 📝 Tóm Tắt

### Key Points:

1. **AutoCAD API** - Transaction-based, Entity manipulation
2. **Revit API** - Element-based, BIM-focused
3. **Inventor API** - COM-based, Part/Assembly modeling
4. **WPF UI** - Hiển thị dialogs trong add-ins
5. **Ribbon** - Customize UI
6. **Debugging** - Attach to process
7. **Deployment** - Bundle structure

### Best Practices:

- ✅ Always use transactions
- ✅ Dispose objects properly
- ✅ Handle exceptions
- ✅ Set Copy Local = False
- ✅ Test thoroughly
- ✅ Follow naming conventions
- ✅ Document your code

---

**Hoàn thành bộ tài liệu!** 🎉

Bạn đã có đầy đủ kiến thức để phát triển ứng dụng WPF Desktop và Autodesk Add-ins.
