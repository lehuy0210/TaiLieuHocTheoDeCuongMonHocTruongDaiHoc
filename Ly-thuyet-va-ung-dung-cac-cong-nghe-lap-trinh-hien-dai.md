# LÝ THUYẾT VÀ ỨNG DỤNG CÁC CÔNG NGHỆ LẬP TRÌNH HIỆN ĐẠI

## MỤC LỤC

1. [Các xu hướng lập trình hiện đại](#chương-1-các-xu-hướng-lập-trình-hiện-đại)
2. [Phát triển Restful API](#chương-2-phát-triển-restful-api)
3. [Phát triển WebApp](#chương-3-phát-triển-webapp)
4. [Phát triển HybridApp](#chương-4-phát-triển-hybridapp)

---

## CHƯƠNG 1: CÁC XU HƯỚNG LẬP TRÌNH HIỆN ĐẠI

### 1.1. Kiến trúc Client-Server

#### Lý thuyết
**Kiến trúc Client-Server** là mô hình phân tán trong đó các nhiệm vụ được chia giữa các nhà cung cấp dịch vụ (server) và các bên yêu cầu dịch vụ (client).

**Đặc điểm chính:**
- **Client**: Gửi yêu cầu đến server, hiển thị giao diện người dùng
- **Server**: Xử lý logic nghiệp vụ, quản lý dữ liệu, trả về kết quả
- **Giao thức truyền thông**: HTTP/HTTPS, WebSocket, gRPC

**Ưu điểm:**
- Tập trung hóa dữ liệu và logic
- Dễ bảo trì và nâng cấp
- Bảo mật tốt hơn
- Hỗ trợ đa nền tảng

**Nhược điểm:**
- Phụ thuộc vào kết nối mạng
- Server có thể trở thành điểm nghẽn (bottleneck)
- Chi phí cao cho hạ tầng server

#### Ứng dụng thực tế

**1. Hệ thống Ngân hàng trực tuyến**
```
Client (Web/Mobile App)
    ↓
Server (API Gateway)
    ↓
┌──────────────┬──────────────┬──────────────┐
│ Auth Service │ Transaction  │  Account     │
│              │   Service    │  Service     │
└──────────────┴──────────────┴──────────────┘
    ↓
Database (MySQL/PostgreSQL)
```

**2. Ứng dụng E-commerce**
- Client: Website/Mobile app hiển thị sản phẩm
- Server: Xử lý đặt hàng, thanh toán, quản lý kho
- Database: Lưu trữ thông tin sản phẩm, đơn hàng

**3. Hệ thống Quản lý Học sinh**
- Client: Giao diện cho giáo viên, học sinh, phụ huynh
- Server: Quản lý điểm, lịch học, thông báo
- Database: Lưu trữ thông tin học sinh, giáo viên

---

### 1.2. Web Services

#### Lý thuyết
**Web Services** là các dịch vụ phần mềm cung cấp chức năng thông qua giao thức web chuẩn, cho phép các ứng dụng khác nhau giao tiếp với nhau.

**Các loại Web Services:**

1. **SOAP (Simple Object Access Protocol)**
   - Sử dụng XML cho định dạng thông điệp
   - Có chuẩn WSDL (Web Services Description Language)
   - Bảo mật cao với WS-Security
   - Phức tạp, nặng nề

2. **REST (Representational State Transfer)**
   - Sử dụng HTTP methods (GET, POST, PUT, DELETE)
   - Định dạng JSON/XML
   - Đơn giản, nhẹ, dễ sử dụng
   - Stateless

#### Ứng dụng thực tế

**1. Tích hợp Thanh toán trực tuyến**
```javascript
// Ví dụ: Tích hợp VNPay, MoMo, ZaloPay
// Client gọi Web Service thanh toán
const createPayment = async (orderInfo) => {
  const response = await fetch('/api/payment/create', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      amount: orderInfo.total,
      orderId: orderInfo.id,
      returnUrl: 'https://myapp.com/payment/result'
    })
  });

  const data = await response.json();
  window.location.href = data.paymentUrl;
};
```

**2. Tích hợp Google Maps API**
```javascript
// Hiển thị bản đồ trên website
const initMap = () => {
  const map = new google.maps.Map(document.getElementById('map'), {
    center: { lat: 10.762622, lng: 106.660172 },
    zoom: 15
  });

  // Thêm marker
  new google.maps.Marker({
    position: { lat: 10.762622, lng: 106.660172 },
    map: map,
    title: 'Trường Đại học Mở TP.HCM'
  });
};
```

**3. Dịch vụ Email (SendGrid, AWS SES)**
```python
# Python - Gửi email thông qua Web Service
import requests

def send_email(to_email, subject, content):
    url = "https://api.sendgrid.com/v3/mail/send"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "personalizations": [{"to": [{"email": to_email}]}],
        "from": {"email": "noreply@myapp.com"},
        "subject": subject,
        "content": [{"type": "text/html", "value": content}]
    }

    response = requests.post(url, json=data, headers=headers)
    return response.status_code == 202
```

---

### 1.3. RESTful API

#### Lý thuyết
**RESTful API** là một kiến trúc API tuân theo các nguyên tắc của REST, sử dụng HTTP methods để thực hiện các thao tác CRUD.

**Nguyên tắc REST:**
1. **Stateless**: Mỗi request độc lập, không lưu trạng thái
2. **Client-Server**: Tách biệt client và server
3. **Cacheable**: Có thể cache để tăng hiệu suất
4. **Uniform Interface**: Giao diện thống nhất
5. **Layered System**: Hệ thống phân lớp

**HTTP Methods:**
- **GET**: Lấy dữ liệu
- **POST**: Tạo mới
- **PUT**: Cập nhật toàn bộ
- **PATCH**: Cập nhật một phần
- **DELETE**: Xóa

**HTTP Status Codes:**
- **200 OK**: Thành công
- **201 Created**: Tạo mới thành công
- **400 Bad Request**: Yêu cầu không hợp lệ
- **401 Unauthorized**: Chưa xác thực
- **403 Forbidden**: Không có quyền
- **404 Not Found**: Không tìm thấy
- **500 Internal Server Error**: Lỗi server

#### Ứng dụng thực tế

**1. API Quản lý Sản phẩm**
```
GET    /api/products          - Lấy danh sách sản phẩm
GET    /api/products/:id      - Lấy chi tiết sản phẩm
POST   /api/products          - Tạo sản phẩm mới
PUT    /api/products/:id      - Cập nhật sản phẩm
DELETE /api/products/:id      - Xóa sản phẩm
```

**2. Ví dụ thực tế - API Blog**
```javascript
// Client-side: Gọi API bằng Fetch/Axios
const BlogAPI = {
  // Lấy danh sách bài viết
  async getAllPosts(page = 1, limit = 10) {
    const response = await fetch(
      `/api/posts?page=${page}&limit=${limit}`
    );
    return response.json();
  },

  // Lấy chi tiết bài viết
  async getPostById(id) {
    const response = await fetch(`/api/posts/${id}`);
    if (!response.ok) throw new Error('Post not found');
    return response.json();
  },

  // Tạo bài viết mới
  async createPost(postData) {
    const response = await fetch('/api/posts', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify(postData)
    });
    return response.json();
  },

  // Cập nhật bài viết
  async updatePost(id, postData) {
    const response = await fetch(`/api/posts/${id}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify(postData)
    });
    return response.json();
  },

  // Xóa bài viết
  async deletePost(id) {
    const response = await fetch(`/api/posts/${id}`, {
      method: 'DELETE',
      headers: {
        'Authorization': `Bearer ${token}`
      }
    });
    return response.ok;
  }
};
```

**3. API Hệ thống Đặt phòng khách sạn**
```
Endpoints:

# Phòng
GET    /api/rooms                    - Danh sách phòng
GET    /api/rooms/:id                - Chi tiết phòng
GET    /api/rooms/available          - Phòng trống

# Đặt phòng
POST   /api/bookings                 - Tạo đặt phòng
GET    /api/bookings/:id             - Chi tiết đặt phòng
GET    /api/bookings/user/:userId    - Lịch sử đặt phòng
PUT    /api/bookings/:id/cancel      - Hủy đặt phòng

# Thanh toán
POST   /api/payments                 - Thanh toán
GET    /api/payments/:id             - Chi tiết thanh toán
```

---

### 1.4. Native App vs Hybrid App

#### Lý thuyết

**Native App:**
- Phát triển riêng cho từng nền tảng (iOS: Swift/Objective-C, Android: Java/Kotlin)
- Hiệu năng cao nhất
- Truy cập đầy đủ tính năng thiết bị
- Chi phí phát triển cao
- Thời gian phát triển lâu

**Hybrid App:**
- Một mã nguồn chạy trên nhiều nền tảng
- Sử dụng web technologies (HTML, CSS, JavaScript)
- Đóng gói trong native container
- Hiệu năng trung bình
- Chi phí thấp hơn, phát triển nhanh hơn

**So sánh chi tiết:**

| Tiêu chí | Native App | Hybrid App |
|----------|-----------|------------|
| Ngôn ngữ | Swift/Kotlin | JavaScript/Dart |
| Hiệu năng | Rất cao ⭐⭐⭐⭐⭐ | Trung bình ⭐⭐⭐ |
| Trải nghiệm UX | Tốt nhất | Tốt |
| Chi phí | Cao | Thấp hơn |
| Thời gian | Lâu | Nhanh |
| Bảo trì | Khó | Dễ hơn |

**Công nghệ Hybrid App phổ biến:**
- React Native (Facebook)
- Flutter (Google)
- Ionic
- Apache Cordova/PhoneGap

#### Ứng dụng thực tế

**1. Khi nào dùng Native App?**
- Game đòi hỏi đồ họa cao (PUBG Mobile, Liên Quân Mobile)
- Ứng dụng cần hiệu năng cao (Camera360, PicsArt)
- Ứng dụng cần tính năng đặc thù của nền tảng
- Ứng dụng ngân hàng, bảo mật cao

**2. Khi nào dùng Hybrid App?**
- Startup cần MVP nhanh chóng
- Ngân sách hạn chế
- Ứng dụng đơn giản, CRUD cơ bản
- Ứng dụng nội dung (tin tức, blog)

**3. Ví dụ thực tế**

**Native Apps:**
- Facebook (iOS: Swift, Android: Kotlin)
- Instagram
- Google Maps
- Zalo

**Hybrid Apps:**
- Airbnb (React Native - trước đây)
- Walmart (React Native)
- Bloomberg (React Native)
- Alibaba (Flutter)

---

### 1.5. Các thư viện và Framework JavaScript nổi bật

#### Lý thuyết

**1. Frontend Frameworks**

**React (Facebook)**
- Library cho UI
- Virtual DOM
- Component-based
- Unidirectional data flow
- Ecosystem lớn

**Vue.js**
- Progressive framework
- Dễ học
- Two-way data binding
- Single File Components

**Angular (Google)**
- Full-featured framework
- TypeScript
- MVC architecture
- Enterprise-level

**2. Backend Frameworks**

**Node.js + Express**
- JavaScript trên server
- Non-blocking I/O
- NPM ecosystem
- Microservices

**NestJS**
- TypeScript
- Modular architecture
- Inspired by Angular

#### Ứng dụng thực tế

**1. React - Xây dựng Dashboard Admin**
```javascript
// Component Dashboard
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Dashboard = () => {
  const [stats, setStats] = useState({
    users: 0,
    orders: 0,
    revenue: 0
  });

  useEffect(() => {
    const fetchStats = async () => {
      const response = await axios.get('/api/dashboard/stats');
      setStats(response.data);
    };

    fetchStats();
  }, []);

  return (
    <div className="dashboard">
      <h1>Dashboard</h1>
      <div className="stats-grid">
        <div className="stat-card">
          <h3>Người dùng</h3>
          <p>{stats.users}</p>
        </div>
        <div className="stat-card">
          <h3>Đơn hàng</h3>
          <p>{stats.orders}</p>
        </div>
        <div className="stat-card">
          <h3>Doanh thu</h3>
          <p>{stats.revenue.toLocaleString()} VNĐ</p>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
```

**2. Express.js - Xây dựng REST API**
```javascript
const express = require('express');
const app = express();

// Middleware
app.use(express.json());

// Routes
app.get('/api/products', async (req, res) => {
  try {
    const products = await Product.find();
    res.json(products);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

app.post('/api/products', async (req, res) => {
  try {
    const product = new Product(req.body);
    await product.save();
    res.status(201).json(product);
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
});

app.listen(3000, () => {
  console.log('Server running on port 3000');
});
```

---

### 1.6. Vấn đề an toàn trong phát triển ứng dụng

#### Lý thuyết

**Các mối đe dọa phổ biến (OWASP Top 10):**

1. **SQL Injection**
   - Chèn mã SQL độc hại
   - Phòng chống: Parameterized queries, ORM

2. **XSS (Cross-Site Scripting)**
   - Chèn JavaScript độc hại
   - Phòng chống: Escape output, Content Security Policy

3. **CSRF (Cross-Site Request Forgery)**
   - Giả mạo request từ người dùng
   - Phòng chống: CSRF token, SameSite cookies

4. **Broken Authentication**
   - Xác thực yếu
   - Phòng chống: JWT, OAuth2, 2FA

5. **Sensitive Data Exposure**
   - Lộ thông tin nhạy cảm
   - Phòng chống: HTTPS, encryption, hashing

#### Ứng dụng thực tế

**1. Phòng chống SQL Injection**
```python
# ❌ KHÔNG AN TOÀN
query = f"SELECT * FROM users WHERE username = '{username}'"

# ✅ AN TOÀN - Sử dụng parameterized query
query = "SELECT * FROM users WHERE username = %s"
cursor.execute(query, (username,))

# ✅ AN TOÀN - Sử dụng ORM (Django)
user = User.objects.get(username=username)
```

**2. Phòng chống XSS**
```javascript
// ❌ KHÔNG AN TOÀN
element.innerHTML = userInput;

// ✅ AN TOÀN - Escape HTML
element.textContent = userInput;

// React tự động escape
return <div>{userInput}</div>

// Hoặc sử dụng thư viện
import DOMPurify from 'dompurify';
const clean = DOMPurify.sanitize(userInput);
```

**3. Authentication với JWT**
```javascript
// Server - Tạo JWT token
const jwt = require('jsonwebtoken');

const generateToken = (user) => {
  return jwt.sign(
    {
      id: user.id,
      email: user.email
    },
    process.env.JWT_SECRET,
    { expiresIn: '7d' }
  );
};

// Middleware xác thực
const authenticateToken = (req, res, next) => {
  const token = req.headers['authorization']?.split(' ')[1];

  if (!token) {
    return res.status(401).json({ error: 'Access denied' });
  }

  try {
    const verified = jwt.verify(token, process.env.JWT_SECRET);
    req.user = verified;
    next();
  } catch (error) {
    res.status(403).json({ error: 'Invalid token' });
  }
};
```

**4. Mã hóa mật khẩu**
```javascript
const bcrypt = require('bcrypt');

// Mã hóa mật khẩu khi đăng ký
const hashPassword = async (password) => {
  const salt = await bcrypt.genSalt(10);
  return await bcrypt.hash(password, salt);
};

// Kiểm tra mật khẩu khi đăng nhập
const verifyPassword = async (password, hashedPassword) => {
  return await bcrypt.compare(password, hashedPassword);
};

// Sử dụng
app.post('/register', async (req, res) => {
  const hashedPassword = await hashPassword(req.body.password);
  const user = new User({
    email: req.body.email,
    password: hashedPassword
  });
  await user.save();
  res.status(201).json({ message: 'User created' });
});
```

---

## CHƯƠNG 2: PHÁT TRIỂN RESTFUL API

### 2.1. Giới thiệu Python Django

#### Lý thuyết

**Django** là một high-level Python web framework khuyến khích phát triển nhanh và thiết kế sạch, thực dụng.

**Đặc điểm chính:**
- **MTV Pattern** (Model-Template-View)
- **ORM mạnh mẽ**: Django ORM
- **Admin interface** tự động
- **Security**: CSRF, XSS, SQL injection protection
- **Scalable**: Được sử dụng bởi Instagram, Pinterest

**Cấu trúc Django Project:**
```
myproject/
├── manage.py
├── myproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── myapp/
    ├── migrations/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── views.py
    └── urls.py
```

#### Ứng dụng thực tế

**1. Tạo Django Project đầu tiên**
```bash
# Cài đặt Django
pip install django

# Tạo project
django-admin startproject bookstore

# Tạo app
cd bookstore
python manage.py startapp books

# Chạy server
python manage.py runserver
```

**2. Định nghĩa Models**
```python
# books/models.py
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='books'
    )
    description = models.TextField()
    cover_image = models.ImageField(upload_to='books/', blank=True)
    stock = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
```

**3. Tạo và chạy migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 2.2. Django Rest Framework (DRF)

#### Lý thuyết

**Django Rest Framework** là thư viện mạnh mẽ để xây dựng Web APIs.

**Tính năng chính:**
- **Serialization**: Chuyển đổi dữ liệu Django models sang JSON
- **Authentication**: Token, JWT, OAuth
- **Permissions**: Phân quyền chi tiết
- **ViewSets**: Tự động tạo CRUD operations
- **Browsable API**: Giao diện web để test API

#### Ứng dụng thực tế

**1. Cài đặt và cấu hình**
```bash
pip install djangorestframework
pip install djangorestframework-simplejwt
```

```python
# settings.py
INSTALLED_APPS = [
    # ...
    'rest_framework',
    'rest_framework_simplejwt',
    'books',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}
```

**2. Serializers**
```python
# books/serializers.py
from rest_framework import serializers
from .models import Book, Category

class CategorySerializer(serializers.ModelSerializer):
    books_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'books_count']

    def get_books_count(self, obj):
        return obj.books.count()

class BookSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(
        source='category.name',
        read_only=True
    )

    class Meta:
        model = Book
        fields = [
            'id', 'title', 'author', 'isbn', 'price',
            'category', 'category_name', 'description',
            'cover_image', 'stock', 'created_at'
        ]
        read_only_fields = ['created_at']

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError(
                "Giá không thể âm"
            )
        return value

    def validate_isbn(self, value):
        if len(value) != 13:
            raise serializers.ValidationError(
                "ISBN phải có 13 ký tự"
            )
        return value
```

**3. Views và ViewSets**
```python
# books/views.py
from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book, Category
from .serializers import BookSerializer, CategorySerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    filterset_fields = ['category', 'author']
    search_fields = ['title', 'author', 'isbn']
    ordering_fields = ['price', 'created_at']

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return [IsAuthenticated()]

    @action(detail=False, methods=['get'])
    def bestsellers(self, request):
        """Lấy sách bán chạy"""
        books = self.queryset.order_by('-stock')[:10]
        serializer = self.get_serializer(books, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def purchase(self, request, pk=None):
        """Mua sách"""
        book = self.get_object()
        quantity = request.data.get('quantity', 1)

        if book.stock < quantity:
            return Response(
                {'error': 'Không đủ hàng trong kho'},
                status=status.HTTP_400_BAD_REQUEST
            )

        book.stock -= quantity
        book.save()

        return Response({
            'message': 'Mua hàng thành công',
            'remaining_stock': book.stock
        })

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
```

**4. URLs**
```python
# books/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

# myproject/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('books.urls')),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
]
```

**5. Sử dụng API**
```bash
# Lấy danh sách sách
GET http://localhost:8000/api/books/

# Tìm kiếm sách
GET http://localhost:8000/api/books/?search=python

# Lọc theo category
GET http://localhost:8000/api/books/?category=1

# Sắp xếp theo giá
GET http://localhost:8000/api/books/?ordering=-price

# Lấy sách bán chạy
GET http://localhost:8000/api/books/bestsellers/

# Đăng nhập lấy token
POST http://localhost:8000/api/token/
{
  "username": "admin",
  "password": "password"
}

# Tạo sách mới (cần authentication)
POST http://localhost:8000/api/books/
Authorization: Bearer <token>
{
  "title": "Python Programming",
  "author": "John Doe",
  "isbn": "1234567890123",
  "price": 299000,
  "category": 1,
  "description": "Learn Python",
  "stock": 100
}
```

---

### 2.3. Authentication & Authorization

#### Lý thuyết

**Authentication (Xác thực)**: Xác minh danh tính người dùng

**Authorization (Phân quyền)**: Xác định quyền truy cập của người dùng

**Các phương thức Authentication trong DRF:**
1. **Session Authentication**: Dùng session của Django
2. **Token Authentication**: Token cố định
3. **JWT (JSON Web Token)**: Token có thời hạn, bảo mật cao
4. **OAuth2**: Đăng nhập qua bên thứ 3

#### Ứng dụng thực tế

**1. JWT Authentication**
```python
# settings.py
from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
}

# views.py - Custom User Registration
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')

    if User.objects.filter(username=username).exists():
        return Response(
            {'error': 'Username đã tồn tại'},
            status=status.HTTP_400_BAD_REQUEST
        )

    user = User.objects.create_user(
        username=username,
        password=password,
        email=email
    )

    refresh = RefreshToken.for_user(user)

    return Response({
        'user': {
            'id': user.id,
            'username': user.username,
            'email': user.email
        },
        'tokens': {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
    }, status=status.HTTP_201_CREATED)
```

**2. Custom Permissions**
```python
# permissions.py
from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Chỉ cho phép owner chỉnh sửa object
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions cho tất cả
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions chỉ cho owner
        return obj.owner == request.user

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Chỉ admin mới được chỉnh sửa
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user and request.user.is_staff

# Sử dụng trong ViewSet
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrReadOnly]
```

---

## CHƯƠNG 3: PHÁT TRIỂN WEBAPP

### 3.1. JavaScript Cơ bản

#### Lý thuyết

**JavaScript** là ngôn ngữ lập trình chạy trên trình duyệt, cho phép tạo nội dung động.

**Các khái niệm quan trọng:**
- Variables: let, const, var
- Data types: String, Number, Boolean, Array, Object
- Functions: Function declaration, Arrow function
- DOM Manipulation
- Events
- Promises & Async/Await

#### Ứng dụng thực tế

**1. ES6+ Features**
```javascript
// 1. Arrow Functions
const greet = (name) => `Hello, ${name}!`;

// 2. Destructuring
const user = { name: 'John', age: 25, email: 'john@mail.com' };
const { name, age } = user;

const numbers = [1, 2, 3, 4, 5];
const [first, second, ...rest] = numbers;

// 3. Spread Operator
const arr1 = [1, 2, 3];
const arr2 = [...arr1, 4, 5];

const obj1 = { a: 1, b: 2 };
const obj2 = { ...obj1, c: 3 };

// 4. Template Literals
const message = `User ${name} is ${age} years old`;

// 5. Promises
const fetchData = () => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve({ data: 'Success' });
    }, 1000);
  });
};

// 6. Async/Await
const getData = async () => {
  try {
    const result = await fetchData();
    console.log(result);
  } catch (error) {
    console.error(error);
  }
};

// 7. Array Methods
const products = [
  { id: 1, name: 'Laptop', price: 1000 },
  { id: 2, name: 'Phone', price: 500 },
  { id: 3, name: 'Tablet', price: 300 }
];

// Map
const productNames = products.map(p => p.name);

// Filter
const expensiveProducts = products.filter(p => p.price > 400);

// Find
const laptop = products.find(p => p.name === 'Laptop');

// Reduce
const totalPrice = products.reduce((sum, p) => sum + p.price, 0);
```

**2. DOM Manipulation**
```javascript
// Lấy elements
const element = document.getElementById('myId');
const elements = document.querySelectorAll('.myClass');

// Tạo element
const div = document.createElement('div');
div.className = 'container';
div.textContent = 'Hello World';
document.body.appendChild(div);

// Event Listeners
button.addEventListener('click', () => {
  console.log('Button clicked');
});

// Form Handling
const form = document.getElementById('loginForm');
form.addEventListener('submit', (e) => {
  e.preventDefault();
  const username = document.getElementById('username').value;
  const password = document.getElementById('password').value;

  login(username, password);
});
```

---

### 3.2. ReactJS

#### Lý thuyết

**React** là thư viện JavaScript để xây dựng giao diện người dùng.

**Khái niệm cốt lõi:**
- **Components**: Khối xây dựng cơ bản
- **Props**: Truyền dữ liệu từ cha sang con
- **State**: Quản lý trạng thái component
- **Hooks**: useState, useEffect, useContext, etc.
- **Virtual DOM**: Tối ưu hiệu năng

#### Ứng dụng thực tế

**1. Todo App hoàn chỉnh**
```javascript
// App.js
import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [todos, setTodos] = useState([]);
  const [input, setInput] = useState('');
  const [filter, setFilter] = useState('all');

  // Load từ localStorage
  useEffect(() => {
    const saved = localStorage.getItem('todos');
    if (saved) {
      setTodos(JSON.parse(saved));
    }
  }, []);

  // Save vào localStorage
  useEffect(() => {
    localStorage.setItem('todos', JSON.stringify(todos));
  }, [todos]);

  const addTodo = (e) => {
    e.preventDefault();
    if (!input.trim()) return;

    setTodos([
      ...todos,
      {
        id: Date.now(),
        text: input,
        completed: false,
        createdAt: new Date().toISOString()
      }
    ]);
    setInput('');
  };

  const toggleTodo = (id) => {
    setTodos(todos.map(todo =>
      todo.id === id
        ? { ...todo, completed: !todo.completed }
        : todo
    ));
  };

  const deleteTodo = (id) => {
    setTodos(todos.filter(todo => todo.id !== id));
  };

  const filteredTodos = todos.filter(todo => {
    if (filter === 'active') return !todo.completed;
    if (filter === 'completed') return todo.completed;
    return true;
  });

  return (
    <div className="app">
      <h1>Todo List</h1>

      <form onSubmit={addTodo}>
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Thêm công việc..."
        />
        <button type="submit">Thêm</button>
      </form>

      <div className="filters">
        <button
          className={filter === 'all' ? 'active' : ''}
          onClick={() => setFilter('all')}
        >
          Tất cả ({todos.length})
        </button>
        <button
          className={filter === 'active' ? 'active' : ''}
          onClick={() => setFilter('active')}
        >
          Chưa xong ({todos.filter(t => !t.completed).length})
        </button>
        <button
          className={filter === 'completed' ? 'active' : ''}
          onClick={() => setFilter('completed')}
        >
          Đã xong ({todos.filter(t => t.completed).length})
        </button>
      </div>

      <ul className="todo-list">
        {filteredTodos.map(todo => (
          <li key={todo.id} className={todo.completed ? 'completed' : ''}>
            <input
              type="checkbox"
              checked={todo.completed}
              onChange={() => toggleTodo(todo.id)}
            />
            <span>{todo.text}</span>
            <button onClick={() => deleteTodo(todo.id)}>Xóa</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
```

**2. E-commerce Product List với API**
```javascript
// ProductList.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ProductList = () => {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [cart, setCart] = useState([]);

  useEffect(() => {
    fetchProducts();
  }, []);

  const fetchProducts = async () => {
    try {
      setLoading(true);
      const response = await axios.get('/api/products');
      setProducts(response.data);
    } catch (err) {
      setError('Không thể tải sản phẩm');
    } finally {
      setLoading(false);
    }
  };

  const addToCart = (product) => {
    const existing = cart.find(item => item.id === product.id);

    if (existing) {
      setCart(cart.map(item =>
        item.id === product.id
          ? { ...item, quantity: item.quantity + 1 }
          : item
      ));
    } else {
      setCart([...cart, { ...product, quantity: 1 }]);
    }
  };

  const getTotalPrice = () => {
    return cart.reduce((total, item) =>
      total + (item.price * item.quantity), 0
    );
  };

  if (loading) return <div>Đang tải...</div>;
  if (error) return <div>Lỗi: {error}</div>;

  return (
    <div className="product-page">
      <div className="products-grid">
        {products.map(product => (
          <div key={product.id} className="product-card">
            <img src={product.image} alt={product.name} />
            <h3>{product.name}</h3>
            <p className="price">
              {product.price.toLocaleString()} VNĐ
            </p>
            <button onClick={() => addToCart(product)}>
              Thêm vào giỏ
            </button>
          </div>
        ))}
      </div>

      <div className="cart">
        <h2>Giỏ hàng ({cart.length})</h2>
        {cart.map(item => (
          <div key={item.id} className="cart-item">
            <span>{item.name}</span>
            <span>x{item.quantity}</span>
            <span>{(item.price * item.quantity).toLocaleString()} VNĐ</span>
          </div>
        ))}
        <div className="total">
          <strong>Tổng: {getTotalPrice().toLocaleString()} VNĐ</strong>
        </div>
      </div>
    </div>
  );
};

export default ProductList;
```

**3. React Router - Navigation**
```javascript
// App.js với React Router
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
import Home from './pages/Home';
import Products from './pages/Products';
import ProductDetail from './pages/ProductDetail';
import Cart from './pages/Cart';
import Login from './pages/Login';

function App() {
  return (
    <BrowserRouter>
      <nav>
        <Link to="/">Trang chủ</Link>
        <Link to="/products">Sản phẩm</Link>
        <Link to="/cart">Giỏ hàng</Link>
        <Link to="/login">Đăng nhập</Link>
      </nav>

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/products" element={<Products />} />
        <Route path="/products/:id" element={<ProductDetail />} />
        <Route path="/cart" element={<Cart />} />
        <Route path="/login" element={<Login />} />
      </Routes>
    </BrowserRouter>
  );
}
```

---

### 3.3. State Management với Redux

#### Lý thuyết

**Redux** là thư viện quản lý state tập trung cho ứng dụng JavaScript.

**Nguyên tắc:**
- **Single Source of Truth**: Một store duy nhất
- **State is Read-only**: Chỉ thay đổi qua actions
- **Changes with Pure Functions**: Reducers là pure functions

#### Ứng dụng thực tế

**1. Setup Redux Toolkit**
```bash
npm install @reduxjs/toolkit react-redux
```

```javascript
// store.js
import { configureStore } from '@reduxjs/toolkit';
import cartReducer from './features/cartSlice';
import userReducer from './features/userSlice';

export const store = configureStore({
  reducer: {
    cart: cartReducer,
    user: userReducer,
  },
});

// features/cartSlice.js
import { createSlice } from '@reduxjs/toolkit';

const cartSlice = createSlice({
  name: 'cart',
  initialState: {
    items: [],
    total: 0,
  },
  reducers: {
    addToCart: (state, action) => {
      const existing = state.items.find(
        item => item.id === action.payload.id
      );

      if (existing) {
        existing.quantity += 1;
      } else {
        state.items.push({ ...action.payload, quantity: 1 });
      }

      state.total = state.items.reduce(
        (sum, item) => sum + (item.price * item.quantity),
        0
      );
    },
    removeFromCart: (state, action) => {
      state.items = state.items.filter(
        item => item.id !== action.payload
      );
      state.total = state.items.reduce(
        (sum, item) => sum + (item.price * item.quantity),
        0
      );
    },
    clearCart: (state) => {
      state.items = [];
      state.total = 0;
    },
  },
});

export const { addToCart, removeFromCart, clearCart } = cartSlice.actions;
export default cartSlice.reducer;

// App.js
import { Provider } from 'react-redux';
import { store } from './store';

function App() {
  return (
    <Provider store={store}>
      <YourApp />
    </Provider>
  );
}

// Component sử dụng Redux
import { useSelector, useDispatch } from 'react-redux';
import { addToCart } from './features/cartSlice';

function ProductCard({ product }) {
  const dispatch = useDispatch();
  const cartItems = useSelector(state => state.cart.items);

  const handleAddToCart = () => {
    dispatch(addToCart(product));
  };

  return (
    <div>
      <h3>{product.name}</h3>
      <button onClick={handleAddToCart}>Thêm vào giỏ</button>
    </div>
  );
}
```

---

## CHƯƠNG 4: PHÁT TRIỂN HYBRIDAPP

### 4.1. React Native

#### Lý thuyết

**React Native** cho phép xây dựng mobile app bằng JavaScript và React.

**Ưu điểm:**
- Code một lần, chạy cả iOS và Android
- Hot Reload: Xem thay đổi ngay lập tức
- Native Performance: Gần với native app
- Ecosystem lớn

**So với React Web:**
- Không có DOM, thay bằng native components
- Sử dụng StyleSheet thay vì CSS
- Navigation khác biệt

#### Ứng dụng thực tế

**1. Setup React Native**
```bash
# Cài đặt Expo CLI (cách dễ nhất)
npm install -g expo-cli

# Tạo project
expo init MyApp

# Chạy
cd MyApp
expo start
```

**2. Ứng dụng News App**
```javascript
// App.js
import React, { useState, useEffect } from 'react';
import {
  StyleSheet,
  Text,
  View,
  FlatList,
  Image,
  TouchableOpacity,
  ActivityIndicator
} from 'react-native';
import axios from 'axios';

export default function App() {
  const [news, setNews] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchNews();
  }, []);

  const fetchNews = async () => {
    try {
      const response = await axios.get(
        'https://newsapi.org/v2/top-headlines?country=vn'
      );
      setNews(response.data.articles);
    } catch (error) {
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  const renderItem = ({ item }) => (
    <TouchableOpacity style={styles.card}>
      {item.urlToImage && (
        <Image
          source={{ uri: item.urlToImage }}
          style={styles.image}
        />
      )}
      <View style={styles.content}>
        <Text style={styles.title}>{item.title}</Text>
        <Text style={styles.description}>
          {item.description}
        </Text>
        <Text style={styles.source}>{item.source.name}</Text>
      </View>
    </TouchableOpacity>
  );

  if (loading) {
    return (
      <View style={styles.loading}>
        <ActivityIndicator size="large" color="#0000ff" />
      </View>
    );
  }

  return (
    <View style={styles.container}>
      <Text style={styles.header}>Tin tức</Text>
      <FlatList
        data={news}
        renderItem={renderItem}
        keyExtractor={(item, index) => index.toString()}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f5f5f5',
    paddingTop: 50,
  },
  header: {
    fontSize: 24,
    fontWeight: 'bold',
    padding: 16,
    backgroundColor: '#fff',
  },
  loading: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  card: {
    backgroundColor: '#fff',
    marginVertical: 8,
    marginHorizontal: 16,
    borderRadius: 8,
    overflow: 'hidden',
    elevation: 3,
  },
  image: {
    width: '100%',
    height: 200,
  },
  content: {
    padding: 16,
  },
  title: {
    fontSize: 18,
    fontWeight: 'bold',
    marginBottom: 8,
  },
  description: {
    fontSize: 14,
    color: '#666',
    marginBottom: 8,
  },
  source: {
    fontSize: 12,
    color: '#999',
  },
});
```

**3. Navigation với React Navigation**
```javascript
// Cài đặt
npm install @react-navigation/native
npm install @react-navigation/stack
expo install react-native-screens react-native-safe-area-context

// App.js
import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import HomeScreen from './screens/HomeScreen';
import DetailsScreen from './screens/DetailsScreen';

const Stack = createStackNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator>
        <Stack.Screen
          name="Home"
          component={HomeScreen}
          options={{ title: 'Trang chủ' }}
        />
        <Stack.Screen
          name="Details"
          component={DetailsScreen}
          options={{ title: 'Chi tiết' }}
        />
      </Stack.Navigator>
    </NavigationContainer>
  );
}

// screens/HomeScreen.js
import React from 'react';
import { View, Button } from 'react-native';

function HomeScreen({ navigation }) {
  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Button
        title="Xem chi tiết"
        onPress={() => navigation.navigate('Details', {
          itemId: 86,
          otherParam: 'anything you want here',
        })}
      />
    </View>
  );
}

export default HomeScreen;

// screens/DetailsScreen.js
import React from 'react';
import { View, Text, Button } from 'react-native';

function DetailsScreen({ route, navigation }) {
  const { itemId, otherParam } = route.params;

  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Text>Item ID: {itemId}</Text>
      <Text>{otherParam}</Text>
      <Button
        title="Quay lại"
        onPress={() => navigation.goBack()}
      />
    </View>
  );
}

export default DetailsScreen;
```

---

## DỰ ÁN MẪU: HỆ THỐNG QUẢN LÝ THƯƠNG MẠI ĐIỆN TỬ

### Mô tả dự án
Xây dựng hệ thống e-commerce hoàn chỉnh với:
- Backend: Django + DRF
- Frontend Web: ReactJS
- Mobile App: React Native

### Kiến trúc hệ thống
```
┌─────────────────────────────────────────────┐
│           Client Applications                │
├──────────────┬──────────────┬───────────────┤
│   Web App    │  Mobile App  │  Admin Panel  │
│   (React)    │  (RN)        │  (React)      │
└──────────────┴──────────────┴───────────────┘
         │              │              │
         └──────────────┼──────────────┘
                        │
         ┌──────────────▼──────────────┐
         │      API Gateway             │
         │    (Django + DRF)            │
         └──────────────┬──────────────┘
                        │
         ┌──────────────▼──────────────┐
         │    Business Logic Layer      │
         ├──────────────┬───────────────┤
         │ Products     │ Orders        │
         │ Users        │ Payments      │
         └──────────────┴───────────────┘
                        │
         ┌──────────────▼──────────────┐
         │      Database Layer          │
         │      (PostgreSQL)            │
         └──────────────────────────────┘
```

### Tính năng chính
1. **Quản lý sản phẩm**: CRUD, tìm kiếm, lọc, phân loại
2. **Giỏ hàng**: Thêm, xóa, cập nhật số lượng
3. **Đặt hàng**: Checkout, thanh toán
4. **Xác thực**: Đăng ký, đăng nhập, JWT
5. **Admin**: Quản lý đơn hàng, sản phẩm, người dùng

---

## KẾT LUẬN

Qua tài liệu này, bạn đã học được:

1. **Các xu hướng lập trình hiện đại**: Client-Server, RESTful API, Native vs Hybrid
2. **Backend với Django**: Models, Views, DRF, Authentication
3. **Frontend với React**: Components, Hooks, State Management
4. **Mobile với React Native**: Cross-platform development

### Lộ trình học tập tiếp theo
1. Hoàn thành bài tập lớn của môn học
2. Nghiên cứu sâu về một framework (React/Django/React Native)
3. Xây dựng portfolio với các dự án thực tế
4. Tham gia các dự án open source
5. Học các công nghệ nâng cao: Docker, CI/CD, Cloud (AWS/GCP)

### Tài nguyên học tập
- **Documentation**: Django Docs, React Docs, React Native Docs
- **Courses**: Udemy, Coursera, freeCodeCamp
- **Practice**: LeetCode, HackerRank, CodeWars
- **Community**: Stack Overflow, Reddit, Discord

---

**Chúc bạn học tốt!**
