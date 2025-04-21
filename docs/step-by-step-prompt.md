# Step-by-Step Prompts for Autoblog Implementation

Tài liệu này cung cấp các prompt chi tiết để hướng dẫn agent thực hiện từng bước trong việc triển khai dự án Autoblog. Mỗi prompt được thiết kế để hoàn thành một phần cụ thể của dự án với đầy đủ ngữ cảnh và điều kiện cần thiết.

## 1. Thiết lập môi trường phát triển

### Prompt 1.1: Cài đặt Frappe Framework
```prompt
Tôi muốn bắt đầu dự án Autoblog bằng Frappe Framework. Hãy:
1. Cài đặt tất cả các dependencies cần thiết cho Frappe Framework
2. Cài đặt Bench tool để quản lý môi trường Frappe
3. Kiểm tra phiên bản đã cài đặt

Yêu cầu hệ thống:
- Hệ điều hành: Linux
- Python 3.6 trở lên
- Node.js và npm
- Redis
- MariaDB/MySQL

Sau khi cài đặt, tôi cần xác nhận rằng tất cả các thành phần đã được cài đặt đúng cách.
```

### Prompt 1.2: Khởi tạo dự án
```prompt
Đã cài đặt xong Frappe Framework và các dependencies. Bây giờ hãy:
1. Khởi tạo một dự án mới tên là 'autoblog'
2. Tạo site mới với tên 'autoblog.local'
3. Tạo ứng dụng Frappe mới tên là 'autoblog'
4. Cài đặt ứng dụng vào site

Đảm bảo mỗi bước được thực hiện thành công và không có lỗi.
```

## 2. Thiết kế cấu trúc dữ liệu

### Prompt 2.1: Tạo Doctype Blog
```prompt
Tôi cần tạo một Doctype mới cho Blog với các yêu cầu sau:

Fields cần có:
1. title (Data)
   - Bắt buộc nhập
   - Độ dài: 5-150 ký tự
   - Đánh index
2. content (Text Editor)
   - Rich text
   - Độ dài tối thiểu 10 ký tự
3. author (Link)
   - Link to: User doctype
   - Bắt buộc nhập
4. published_date (Date)
   - Mặc định: ngày hiện tại
5. is_published (Check)
   - Mặc định: 0
6. is_deleted (Check)
   - Hỗ trợ soft delete
   - Mặc định: 0

Cần thêm validation cho:
- Độ dài tiêu đề
- Độ dài nội dung
- Kiểm tra author hợp lệ

Vui lòng tạo Doctype với các cấu hình trên và thêm các validation cần thiết.
```

## 3. Thiết kế API RESTful

### Prompt 3.1: Cấu hình API cho User
```prompt
Cần thiết lập API endpoints cho quản lý User với các yêu cầu sau:

1. GET /api/resource/User
   - Lấy danh sách user
   - Cần lọc theo trường enabled
   - Giới hạn 20 kết quả mỗi trang
   - Sắp xếp theo tên

2. POST /api/resource/User
   - Tạo user mới
   - Validate email và password
   - Tự động gán role cơ bản

3. PUT /api/resource/User/{name}
   - Cập nhật thông tin user
   - Không cho phép thay đổi email

4. DELETE /api/resource/User/{name}
   - Xóa user
   - Kiểm tra quyền trước khi xóa

Hãy thực hiện cấu hình và kiểm tra các API endpoints này.
```

### Prompt 3.2: Cấu hình API cho Blog
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
   - Tự động gán author là user hiện tại

3. PUT /api/resource/Blog/{name}
   - Cập nhật blog
   - Chỉ author mới được sửa

4. Soft delete
   - Không xóa thật, chỉ đánh dấu is_deleted

Hãy thực hiện cấu hình API và thêm các validation cần thiết.
```

## 4. Tạo giao diện người dùng

### Prompt 4.1: Thiết lập cấu trúc frontend
```prompt
Cần tạo cấu trúc thư mục và files cho phần frontend trong thư mục www của ứng dụng autoblog:

Cấu trúc cần có:
1. user_management.html
2. blog_management.html
3. style.css
4. js/
   - user.js
   - blog.js

Hãy tạo cấu trúc thư mục và các file trống với cấu trúc cơ bản.
```

### Prompt 4.2: Xây dựng giao diện quản lý User
```prompt
Cần xây dựng giao diện quản lý User với các yêu cầu sau:

HTML (user_management.html):
1. Tiêu đề trang
2. Vùng hiển thị danh sách user
3. Link đến CSS

JavaScript (user.js):
1. Hàm loadUsers(): tải và hiển thị danh sách
2. Hàm deleteUser(): xác nhận và xóa user
3. Xử lý lỗi và hiển thị thông báo
4. Sử dụng CSRF token cho các request

CSS đã có sẵn trong style.css

Hãy tạo các file với code đầy đủ và đảm bảo hoạt động đúng.
```

### Prompt 4.3: Xây dựng giao diện quản lý Blog
```prompt
Cần xây dựng giao diện quản lý Blog với các yêu cầu sau:

HTML (blog_management.html):
1. Form thêm blog mới
   - Input cho tiêu đề
   - Textarea cho nội dung
   - Nút submit
2. Vùng hiển thị danh sách blog
3. Link đến CSS và JS

JavaScript (blog.js):
1. Hàm loadBlogs(): tải và hiển thị danh sách
2. Hàm setupForm(): xử lý submit form
3. Validation dữ liệu trước khi gửi
4. Xử lý lỗi và thông báo
5. Sử dụng CSRF token

Hãy tạo các file với code đầy đủ và đảm bảo hoạt động đúng.
```

### Prompt 4.4: Tạo và tùy chỉnh CSS
```prompt
Cần tạo file CSS chung cho toàn bộ ứng dụng với các yêu cầu sau:

1. Thiết lập biến CSS cho:
   - Màu sắc chính
   - Màu danger
   - Màu text
   - Màu border

2. Định dạng cho:
   - Body và container
   - Forms và inputs
   - Buttons (primary và danger)
   - Responsive design

3. Media queries cho mobile:
   - Điều chỉnh margin
   - Full-width inputs
   - Stack buttons

Hãy tạo file style.css với đầy đủ các styles cần thiết.
```

## 5. Triển khai và kiểm thử

### Prompt 5.1: Kiểm tra validation
```prompt
Cần kiểm tra tất cả các validation trong hệ thống:

1. User validation:
   - Email hợp lệ
   - Mật khẩu đủ mạnh
   - Tên không trống

2. Blog validation:
   - Tiêu đề 5-150 ký tự
   - Nội dung ít nhất 10 ký tự
   - Author hợp lệ

Hãy thực hiện kiểm tra và đảm bảo tất cả validation hoạt động đúng.
```

### Prompt 5.2: Kiểm tra CRUD và phân quyền
```prompt
Cần kiểm tra đầy đủ các chức năng CRUD và phân quyền:

1. Tạo dữ liệu test:
   - 3 users với các role khác nhau
   - 5 blog posts với các trạng thái khác nhau

2. Kiểm tra quyền truy cập:
   - Chỉ admin được quản lý users
   - Author chỉ sửa được blog của mình
   - Guest chỉ xem được blog đã publish

3. Kiểm tra các chức năng:
   - Thêm, sửa, xóa user
   - Thêm, sửa, soft delete blog
   - Phân trang và sắp xếp

Hãy thực hiện các test case và báo cáo kết quả.
```

## 6. Bảo mật và tối ưu hóa

### Prompt 6.1: Thiết lập bảo mật
```prompt
Cần thiết lập các biện pháp bảo mật cho hệ thống:

1. API Security:
   - Cấu hình CSRF protection
   - Thiết lập rate limiting
   - Tạo và quản lý API keys

2. XSS Prevention:
   - Thêm CSP headers
   - Escape HTML trong rich text
   - Sử dụng textContent thay vì innerHTML

3. CORS:
   - Cấu hình whitelist domains
   - Thiết lập allow_cors

Hãy thực hiện các cấu hình bảo mật và kiểm tra hiệu quả.
```

### Prompt 6.2: Tối ưu hiệu năng
```prompt
Cần thực hiện tối ưu hiệu năng cho hệ thống:

1. Frontend:
   - Minify CSS/JS
   - Implement lazy loading
   - Sử dụng document fragments
   - Tối ưu event handlers

2. Backend:
   - Cấu hình Redis cache
   - Tối ưu queries
   - Implement connection pooling

3. Database:
   - Thêm indexes cho các trường tìm kiếm
   - Tối ưu query plan
   - Monitoring query performance

Hãy thực hiện các tối ưu và đo lường hiệu quả.
```

## 7. Deployment

### Prompt 7.1: Cấu hình Production
```prompt
Cần chuẩn bị hệ thống cho môi trường production:

1. Web Server:
   - Cài đặt và cấu hình Nginx
   - Setup reverse proxy
   - Cấu hình SSL với Let's Encrypt

2. Environment:
   - Tạo file cấu hình production
   - Thiết lập biến môi trường
   - Cấu hình logging

3. Database:
   - Backup strategy
   - Monitoring
   - Performance tuning

Hãy thực hiện các bước cấu hình và kiểm tra môi trường production.
```

### Prompt 7.2: Monitoring và Backup
```prompt
Cần thiết lập hệ thống monitoring và backup:

1. Logging:
   - Cấu hình log rotation
   - Error tracking
   - Performance monitoring

2. Backup:
   - Lịch backup tự động
   - Backup verification
   - Restore testing

3. Monitoring:
   - Setup Prometheus + Grafana
   - Cấu hình alerts
   - Resource monitoring

Hãy thực hiện cấu hình và kiểm tra hệ thống monitoring.
```

## Kết luận

Mỗi prompt trên được thiết kế để:
1. Cung cấp đầy đủ ngữ cảnh và yêu cầu
2. Chỉ rõ các điều kiện cần và đủ
3. Yêu cầu kiểm tra và xác nhận kết quả
4. Đảm bảo tính tuần tự và liên kết giữa các bước

Khi sử dụng các prompt này, hãy:
1. Thực hiện tuần tự từng bước
2. Đảm bảo hoàn thành và kiểm tra mỗi bước
3. Lưu lại log và kết quả thực hiện
4. Xử lý các lỗi nếu có trước khi chuyển sang bước tiếp theo