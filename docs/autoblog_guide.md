# Hướng dẫn triển khai dự án Autoblog

Hướng dẫn chi tiết step-by-step để triển khai dự án Autoblog sử dụng Frappe Framework, với giao diện người dùng được custom hoàn toàn bằng HTML/CSS và đặt trong thư mục www của ứng dụng Frappe. 

## Mục lục
1. [Thiết lập môi trường phát triển](#1-thiết-lập-môi-trường-phát-triển)
2. [Thiết kế cấu trúc dữ liệu](#2-thiết-kế-cấu-trúc-dữ-liệu)
3. [Thiết kế API RESTful](#3-thiết-kế-api-restful)
4. [Tạo giao diện người dùng](#4-tạo-giao-diện-người-dùng)
5. [Triển khai và kiểm thử](#5-triển-khai-và-kiểm-thử)
6. [Bảo mật và tối ưu hóa](#6-bảo-mật-và-tối-ưu-hóa)
7. [Deployment](#7-deployment)

## 1. Thiết lập môi trường phát triển

### Yêu cầu hệ thống
- Python 3.6 trở lên
- Git
- Redis
- Node.js và npm
- MariaDB/MySQL

### a. Cài đặt Frappe Framework

```bash
# Cài đặt các gói phụ thuộc
sudo apt-get update
sudo apt-get install git python3-pip python3-dev libffi-dev libssl-dev build-essential redis-server

# Cài đặt bench
pip3 install frappe-bench

# Kiểm tra phiên bản
bench --version
```

### b. Tạo project mới

```bash
# Khởi tạo project
bench init autoblog
cd autoblog

# Tạo site mới
bench new-site autoblog.local
bench use autoblog.local

# Tạo ứng dụng
bench new-app autoblog
bench --site autoblog.local install-app autoblog
```

### c. Cấu hình server

```bash
# Khởi động server mặc định (port 8000)
bench start

# Khởi động với port tùy chỉnh
bench start --port <new_port>

# Chạy trong background
bench start & disown
```

## 2. Thiết kế cấu trúc dữ liệu

### a. Doctype User (có sẵn)

Các trường chính:
- **name** (Text)
  - Primary key
  - Tên đăng nhập duy nhất
- **email** (Data)
  - Dùng làm tài khoản đăng nhập
  - Unique, required
- **first_name** (Data)
- **last_name** (Data)
- **password** (Password)
  - Được mã hóa tự động
- **enabled** (Check)
  - Trạng thái hoạt động
- **roles** (Table)
  - Danh sách vai trò

### b. Doctype Blog (tạo mới)

Các trường chính:
- **title** (Data)
  - Kiểu: Text
  - Required: Yes
  - Length: 5-150 ký tự
  - Indexed: Yes
- **content** (Text Editor)
  - Kiểu: Rich text
  - Min length: 10 ký tự
- **author** (Link)
  - Link to: User
  - Required: Yes
- **published_date** (Date)
  - Default: today()
- **is_published** (Check)
  - Default: 0
- **is_deleted** (Check)
  - Để hỗ trợ soft delete
  - Default: 0

### Validation và Indexing

```python
# Trong doctype Blog
validate_title_length(self):
    if len(self.title) < 5:
        frappe.throw("Tiêu đề phải có ít nhất 5 ký tự")

validate_content_length(self):
    if len(strip_html(self.content)) < 10:
        frappe.throw("Nội dung phải có ít nhất 10 ký tự")
```

## 3. Thiết kế API RESTful

### a. API cho User

1. Lấy danh sách user
```
GET /api/resource/User
```
Tham số:
- fields: ["name", "email", "first_name", "last_name", "enabled"]
- filters: {"enabled": 1}
- limit_page_length: 20
- order_by: "name asc"

2. Thêm user mới
```
POST /api/resource/User
```
Body:
```json
{
    "email": "user@example.com",
    "first_name": "John",
    "last_name": "Doe",
    "password": "securepassword"
}
```

3. Cập nhật user
```
PUT /api/resource/User/{name}
```
Body:
```json
{
    "first_name": "Jane",
    "last_name": "Smith"
}
```

4. Xóa user
```
DELETE /api/resource/User/{name}
```

### b. API cho Blog

1. Lấy danh sách blog
```
GET /api/resource/Blog
```
Tham số:
- fields: ["title", "author", "published_date", "is_published"]
- filters: {"is_published": 1, "is_deleted": 0}
- limit_page_length: 10
- order_by: "published_date desc"

2. Thêm blog mới
```
POST /api/resource/Blog
```
Body:
```json
{
    "title": "Bài viết đầu tiên",
    "content": "Nội dung bài viết...",
    "author": "user@example.com",
    "published_date": "2023-10-01",
    "is_published": 1
}
```

3. Cập nhật blog
```
PUT /api/resource/Blog/{name}
```

4. Xóa blog (soft delete)
```
PUT /api/resource/Blog/{name}
```
Body:
```json
{
    "is_deleted": 1
}
```

## 4. Tạo giao diện người dùng

### a. Cấu trúc thư mục
```
autoblog/www/
├── user_management.html
├── blog_management.html
├── style.css
└── js/
    ├── user.js
    └── blog.js
```

### b. Giao diện quản lý User

```html
<!-- user_management.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Quản lý User</title>
    <link rel="stylesheet" href="/files/style.css">
</head>
<body>
    <h1>Quản lý User</h1>
    <div id="user-list"></div>
    <script src="/files/js/user.js"></script>
</body>
</html>
```

```javascript
// user.js
document.addEventListener('DOMContentLoaded', () => {
    loadUsers();
});

async function loadUsers() {
    try {
        const response = await fetch('/api/resource/User');
        if (!response.ok) throw new Error('Network response was not ok');
        const data = await response.json();
        
        const userList = document.getElementById('user-list');
        const fragment = document.createDocumentFragment();
        
        data.data.forEach(user => {
            const div = document.createElement('div');
            div.innerHTML = `
                <strong>${user.name}</strong> - ${user.email}
                <button onclick="editUser('${user.name}')">Sửa</button>
                <button onclick="deleteUser('${user.name}')">Xoá</button>
            `;
            fragment.appendChild(div);
        });
        
        userList.appendChild(fragment);
    } catch (error) {
        console.error('Error:', error);
        alert('Không thể tải danh sách user');
    }
}

function deleteUser(name) {
    if (confirm(`Bạn có chắc chắn muốn xoá user ${name}?`)) {
        fetch(`/api/resource/User/${name}`, { 
            method: 'DELETE',
            headers: {
                'X-Frappe-CSRF-Token': frappe.csrf_token
            }
        })
        .then(response => {
            if (!response.ok) throw new Error('Delete failed');
            location.reload();
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Không thể xoá user');
        });
    }
}
```

### c. Giao diện quản lý Blog

```html
<!-- blog_management.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Quản lý Blog</title>
    <link rel="stylesheet" href="/files/style.css">
</head>
<body>
    <h1>Quản lý Blog</h1>
    <form id="blog-form">
        <input type="text" id="title" placeholder="Tiêu đề" required minlength="5" />
        <textarea id="content" placeholder="Nội dung" required minlength="10"></textarea>
        <button type="submit">Thêm Blog</button>
    </form>
    <div id="blog-list"></div>
    <script src="/files/js/blog.js"></script>
</body>
</html>
```

```javascript
// blog.js
document.addEventListener('DOMContentLoaded', () => {
    loadBlogs();
    setupForm();
});

async function loadBlogs() {
    try {
        const response = await fetch('/api/resource/Blog?fields=["title","author","published_date"]&filters={"is_published":1,"is_deleted":0}');
        if (!response.ok) throw new Error('Network response was not ok');
        const data = await response.json();
        
        const blogList = document.getElementById('blog-list');
        const fragment = document.createDocumentFragment();
        
        data.data.forEach(blog => {
            const div = document.createElement('div');
            div.textContent = `${blog.title} - ${blog.author}`;
            
            const editBtn = document.createElement('button');
            editBtn.textContent = 'Sửa';
            editBtn.onclick = () => editBlog(blog.name);
            
            const deleteBtn = document.createElement('button');
            deleteBtn.textContent = 'Xoá';
            deleteBtn.onclick = () => deleteBlog(blog.name);
            
            div.appendChild(editBtn);
            div.appendChild(deleteBtn);
            fragment.appendChild(div);
        });
        
        blogList.appendChild(fragment);
    } catch (error) {
        console.error('Error:', error);
        alert('Không thể tải danh sách blog');
    }
}

function setupForm() {
    document.getElementById('blog-form').addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const title = document.getElementById('title').value.trim();
        const content = document.getElementById('content').value.trim();
        
        try {
            const response = await fetch('/api/resource/Blog', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-Frappe-CSRF-Token': frappe.csrf_token
                },
                body: JSON.stringify({
                    title,
                    content,
                    author: frappe.session.user,
                    published_date: new Date().toISOString().split('T')[0],
                    is_published: 1
                })
            });
            
            if (!response.ok) throw new Error('Create failed');
            location.reload();
        } catch (error) {
            console.error('Error:', error);
            alert('Không thể tạo blog');
        }
    });
}
```

### d. CSS chung

```css
/* style.css */
:root {
    --primary-color: #007bff;
    --danger-color: #dc3545;
    --text-color: #333;
    --border-color: #ddd;
}

body {
    font-family: Arial, sans-serif;
    margin: 20px;
    color: var(--text-color);
}

h1 {
    color: var(--text-color);
    margin-bottom: 1.5rem;
}

form {
    margin-bottom: 2rem;
    padding: 1rem;
    border: 1px solid var(--border-color);
    border-radius: 4px;
}

input, textarea {
    display: block;
    width: 100%;
    margin: 0.5rem 0;
    padding: 0.5rem;
    border: 1px solid var(--border-color);
    border-radius: 4px;
}

button {
    padding: 0.5rem 1rem;
    margin: 0 0.25rem;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    background-color: var(--primary-color);
    color: white;
}

button:hover {
    opacity: 0.9;
}

button[onclick*="delete"] {
    background-color: var(--danger-color);
}

@media (max-width: 768px) {
    body {
        margin: 10px;
    }
    
    input, textarea {
        width: calc(100% - 1rem);
    }
    
    button {
        width: 100%;
        margin: 0.25rem 0;
    }
}
```

## 5. Triển khai và kiểm thử

### a. Kiểm tra validation

1. User validation:
- Email hợp lệ
- Mật khẩu đủ mạnh
- Tên không được trống

2. Blog validation:
- Tiêu đề 5-150 ký tự
- Nội dung ít nhất 10 ký tự
- Author phải là user hợp lệ

### b. Kiểm tra CRUD

1. Create:
- Tạo user mới
- Đăng bài blog mới

2. Read:
- Xem danh sách user
- Xem danh sách blog
- Phân trang hoạt động

3. Update:
- Cập nhật thông tin user
- Sửa nội dung blog

4. Delete:
- Xóa user
- Soft delete blog

## 6. Bảo mật và tối ưu hóa

### a. Bảo mật

1. API Security:
- Sử dụng CSRF token
- Rate limiting
- API key authentication

2. XSS Prevention:
- Sử dụng textContent thay vì innerHTML
- Escape HTML trong rich text
- CSP headers

3. CORS:
```python
# site_config.json
{
    "allow_cors": "*",
    "cors_whitelist": [
        "https://your-domain.com"
    ]
}
```

### b. Tối ưu hóa

1. Frontend:
- Minify CSS/JS
- Lazy loading
- Document fragments
- Event delegation

2. Backend:
- Query optimization
- Caching (Redis)
- Gzip compression

3. Database:
- Proper indexing
- Query optimization
- Connection pooling

## 7. Deployment

### a. Production Setup

1. Web Server (Nginx):
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

2. SSL Configuration:
```bash
# Install certbot
sudo apt install certbot python3-certbot-nginx

# Get SSL certificate
sudo certbot --nginx -d your-domain.com
```

### b. Monitoring & Backup

1. Logging:
```python
# site_config.json
{
    "logging": 1,
    "log_level": "debug",
    "log_file": "autoblog.log"
}
```

2. Automated Backup:
```bash
# Backup script
#!/bin/bash
bench --site autoblog.local backup

# Cron job (daily at 2 AM)
0 2 * * * /path/to/backup_script.sh
```

3. Monitoring:
- Setup Prometheus + Grafana
- Configure alerts
- Monitor system resources

## Lưu ý quan trọng

1. Phát triển:
- Tuân thủ coding standards
- Viết unit tests
- Code review

2. Bảo mật:
- Regular security audits
- Keep dependencies updated
- Monitor security alerts

3. Maintenance:
- Regular backups
- System updates
- Performance monitoring

## Kết luận

Dự án Autoblog là một ứng dụng web full-stack với:
- Backend mạnh mẽ bằng Frappe Framework
- Frontend tùy chỉnh bằng HTML/CSS/JS
- API RESTful cho tích hợp
- Bảo mật và tối ưu hóa đầy đủ
- Quy trình deployment chuyên nghiệp