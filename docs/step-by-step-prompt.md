# Step-by-Step Prompts for Autoblog Implementation

Tài liệu này cung cấp các prompt chi tiết để hướng dẫn agent thực hiện từng bước trong việc triển khai dự án Autoblog. Mỗi prompt được thiết kế để hoàn thành một phần cụ thể của dự án với đầy đủ ngữ cảnh và điều kiện cần thiết.

## 1. Thiết lập môi trường phát triển

### Prompt 1.1: Cài đặt Frappe Framework
```prompt
Tôi muốn bắt đầu dự án Autoblog bằng Frappe Framework. Hãy thực hiện các bước sau:

1. Cài đặt tất cả các dependencies cần thiết cho Frappe Framework:
   - Python 3.6 trở lên
   - Node.js và npm
   - Redis
   - MariaDB/MySQL
   - Git
   - GCC và các thư viện cần thiết (libffi-dev, libssl-dev, etc.)
   - Các công cụ hệ thống như curl, wget

2. Cài đặt Bench tool để quản lý môi trường Frappe:
   - Cài đặt Bench bằng pip
   - Thêm Bench vào biến môi trường
   - Đảm bảo Bench hoạt động đúng với lệnh `bench --version`

3. Kiểm tra phiên bản đã cài đặt:
   - Python: `python3 --version`
   - Node.js: `node --version`
   - Redis: `redis-cli ping` (phản hồi "PONG")
   - MariaDB/MySQL: `mysql --version`


Sau khi cài đặt, tôi cần xác nhận rằng tất cả các thành phần đã được cài đặt đúng cách và không có lỗi.
```

### Prompt 1.2: Khởi tạo dự án
```prompt
Đã cài đặt xong Frappe Framework và các dependencies. Bây giờ hãy:
1. Khởi tạo một dự án mới tên là 'autoblog' ngay trong thư mục hiện tại
2. Tạo site mới với tên 'autoblog.local'
3. Tạo ứng dụng Frappe mới tên là 'autoblog'
4. Cài đặt ứng dụng vào site

Đảm bảo mỗi bước được thực hiện thành công và không có lỗi.
```

## 2. Thiết kế cấu trúc dữ liệu

# Prompt 2.1: Tạo Doctype Blog

Tôi cần tạo một Doctype mới cho Blog với các yêu cầu sau:

## Yêu cầu về fields:
1. **title (Data)**
   - Bắt buộc nhập
   - Độ dài: 5-150 ký tự
   - Đánh index
2. **content (Text Editor)**
   - Rich text
   - Độ dài tối thiểu 10 ký tự
3. **author (Link)**
   - Link to: BlogUser doctype
   - Bắt buộc nhập
4. **published_date (Date)**
   - Mặc định: ngày hiện tại
5. **is_published (Check)**
   - Mặc định: 0
6. **is_deleted (Check)**
   - Hỗ trợ soft delete
   - Mặc định: 0

## Yêu cầu về permissions:
- **Role: "System Manager"**
  - Read: Yes
  - Write: Yes
  - Create: Yes
  - Delete: Yes
- **Role: "Blog Editor"**
  - Read: Yes
  - Write: Yes
  - Create: Yes
  - Delete: No -->

Sau đó chạy lệnh bench --site autoblog.local migrate để đồng bộ tất cả các thay đổi về cấu trúc dữ liệu

## 3. Thiết kế API RESTful

### Prompt 3.1: Cấu hình API cho Blog
```prompt
Cần thiết lập API endpoints cho Blog với các yêu cầu sau:

1. GET /api/resource/Blog
   - Lấy danh sách blog
   - Lọc theo is_published và is_deleted
   - Giới hạn 10 bài mỗi trang
   - Sắp xếp theo ngày xuất bản mới nhất

2. POST /api/resource/Blog
   - Tạo blog mới
   - Validate độ dài title và content
   - Tự động gán author là blogUser hiện tại

3. PUT /api/resource/Blog/{name}
   - Cập nhật blog
   - Chỉ author mới được sửa

4. Soft delete
   - Không xóa thật, chỉ đánh dấu is_deleted

Hãy thực hiện cấu hình API và thêm các validation cần thiết, viết logs đầy đủ để sử dụng cho debug.
```

## 4. Tạo giao diện người dùng

### Prompt 4.1: Xây dựng giao diện quản lý Blog
```prompt
Cần xây dựng giao diện quản lý Blog với các yêu cầu sau:

HTML (blog_management.html):
1. Form thêm blog mới
   - Input cho tiêu đề
   - Textarea cho nội dung
   - Nút submit
2. Vùng hiển thị danh sách blog
3. Nút xem, chỉnh sửa và xoá blog
4. Khi nhấn nút xem, chỉnh sửa sẽ hiển thị ra một modal hiển thị thông tin blog (title, content) tuy nhiên chỉ khi nhấn nút chỉnh sửa mới cho thay đổi trưc tiếp và lưu, nếu xem thì không được thay đổi và lưu
5. Link đến CSS và JS

JavaScript (blog.js):
1. Hàm loadBlogs(): tải và hiển thị danh sách
2. Hàm setupForm(): xử lý submit form
3. Validation dữ liệu trước khi gửi
4. Xử lý lỗi và thông báo
5. Sử dụng CSRF token

Sử dụng các api được tạo từ doctype blog
Hãy tạo các file với code đầy đủ và đảm bảo hoạt động đúng.
```

### Prompt 4.2: Tạo và tùy chỉnh CSS
```prompt
Cần tạo file CSS chung cho toàn bộ ứng dụng với các yêu cầu sau:

1. Thiết lập biến CSS cho:
   - Màu sắc chính (--primary-color: #007bff)
   - Màu danger (--danger-color: #dc3545)
   - Màu text (--text-color: #333)
   - Màu border (--border-color: #ddd)

2. Định dạng cho:
   - Body: font-family Arial, margin 20px
   - Forms: max-width 400px, centered
   - Inputs: full width, padding, border radius
   - Buttons: full width, color scheme, hover effects
   - Links: color scheme, hover effects
   - Responsive design

3. Các styles cụ thể cho:
   - Form quản lý blog
   - Danh sách blog
   - Error messages

4. Media queries cho mobile:
   - Điều chỉnh margin (10px)
   - Full-width inputs
   - Stack buttons
   - Responsive padding
```



