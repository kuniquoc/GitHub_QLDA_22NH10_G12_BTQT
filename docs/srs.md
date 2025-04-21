# Software Requirement Specification (SRS) cho AutoBlog

## 1. Giới thiệu

### 1.1 Mục đích

Hệ thống AutoBlog được phát triển nhằm mục đích tự động hóa quá trình quản lý và đăng bài blog, tích hợp trí tuệ nhân tạo (AI) để giảm thiểu 50% thời gian và công sức cần thiết cho việc quản lý nội dung thủ công. Mục tiêu chính là cung cấp một nền tảng thân thiện, hiệu quả cho các blogger, nhà sáng tạo nội dung và doanh nghiệp để tạo, quản lý và xuất bản nội dung một cách tự động và tối ưu.

### 1.2 Phạm vi

Hệ thống AutoBlog bao gồm các tính năng sau:

- **Tự động hóa nội dung**: Sử dụng AI để tạo bài viết dựa trên từ khóa và chủ đề do người dùng cung cấp.
- **Lên lịch đăng bài**: Cho phép đặt lịch đăng bài tự động lên các nền tảng blog.
- **Quản lý nội dung**: Hỗ trợ tạo, chỉnh sửa, xóa và phân loại bài viết theo danh mục và thẻ tag.
- **Tích hợp đa nền tảng**: Đăng bài lên ít nhất 3 nền tảng blog như WordPress, Blogger và Medium.
- **Quản lý tài khoản**: Đăng ký, đăng nhập, khôi phục mật khẩu và quản lý thông tin người dùng.
- **Tìm kiếm**: Tìm kiếm bài viết theo từ khóa, danh mục hoặc ngày tháng.
- **Báo cáo và thống kê**: Cung cấp số liệu về lượt xem và tương tác với bài viết.

Các tính năng không bao gồm trong phiên bản đầu tiên:

- Ứng dụng di động riêng biệt (dù giao diện web sẽ đáp ứng trên thiết bị di động).
- Hỗ trợ đa ngôn ngữ (chỉ hỗ trợ tiếng Anh ban đầu).
- Tính năng AI phức tạp như chatbot hoặc phân tích cảm xúc.
- Công cụ tiếp thị hoặc quảng bá blog.
- Thanh toán trực tuyến hoặc bán hàng.
- Phát trực tiếp video/âm thanh.
- Quản lý cộng đồng phức tạp.

### 1.3 Định nghĩa, Từ viết tắt và Thuật ngữ

- **AI**: Trí tuệ nhân tạo (Artificial Intelligence).
- **API**: Giao diện lập trình ứng dụng (Application Programming Interface).
- **CMS**: Hệ thống quản lý nội dung (Content Management System).
- **CRUD**: Tạo (Create), Đọc (Read), Cập nhật (Update), Xóa (Delete).
- **SEO**: Tối ưu hóa công cụ tìm kiếm (Search Engine Optimization).
- **UI**: Giao diện người dùng (User Interface).
- **UX**: Trải nghiệm người dùng (User Experience).
- **SRS**: Tài liệu Đặc tả Yêu cầu Phần mềm (Software Requirement Specification).

### 1.4 Tài liệu tham khảo

- Wireframe Design: [Link đến Wireframe](#).
- Prototype Design: [Link đến Prototype](#).
- Các sơ đồ thiết kế: Sơ đồ ERD, Usecase, Lớp, Hoạt động, Tuần tự (xem Phụ lục).

### 1.5 Tổng quan

AutoBlog là một nền tảng web tích hợp AI, xây dựng với React.js cho frontend và Frappe Framework cho backend, cho phép người dùng tự động hóa việc tạo và quản lý nội dung blog, lên lịch đăng bài và tích hợp với các nền tảng blog bên ngoài. Hệ thống nhắm đến việc tối ưu hóa quy trình làm việc, tăng hiệu suất và cung cấp trải nghiệm người dùng trực quan, dễ sử dụng.

---

## 2. Mô tả Tổng quan

### 2.1 Quan điểm Sản phẩm

AutoBlog là một hệ thống web tập trung, hoạt động như một trung tâm quản lý nội dung blog. Nó tích hợp với các API AI (như Hugging Face) để tạo nội dung và kết nối với các nền tảng blog bên ngoài thông qua API (như WordPress REST API). Hệ thống được thiết kế để mở rộng, hỗ trợ số lượng người dùng và bài viết ngày càng tăng.

### 2.2 Chức năng Sản phẩm

Các chức năng chính của AutoBlog bao gồm:

- Đăng ký, đăng nhập và quản lý tài khoản người dùng.
- Tạo, chỉnh sửa, xóa và phân loại bài viết blog.
- Lên lịch và đăng bài tự động lên các nền tảng blog.
- Tích hợp AI để gợi ý tiêu đề và nội dung bài viết.
- Tìm kiếm bài viết theo từ khóa, danh mục hoặc ngày tháng.
- Cung cấp báo cáo và thống kê về hiệu suất bài viết.
- Tích hợp với ít nhất 3 nền tảng blog bên ngoài.

### 2.3 Đặc điểm Người dùng

Hệ thống phục vụ hai nhóm người dùng chính:

- **Người dùng (User)**: Bloggers hoặc nhà sáng tạo nội dung, có thể tạo, quản lý và đăng bài viết.
- **Quản trị viên (Admin)**: Quản lý tài khoản người dùng, danh mục và giám sát hoạt động hệ thống.

Người dùng được kỳ vọng có kỹ năng cơ bản về sử dụng máy tính và hiểu biết về blogging.

### 2.4 Ràng buộc

- Công nghệ: Backend sử dụng Frappe Framework (Python), frontend sử dụng React.js, cơ sở dữ liệu sử dụng MariaDB (theo mặc định của Frappe).
- Tích hợp AI phải sử dụng API hiện có như Hugging Face.
- Hỗ trợ ít nhất 3 nền tảng blog trong giai đoạn đầu.
- Hiệu suất phải xử lý ít nhất 1000 bài viết/ngày mà không bị gián đoạn.

### 2.5 Giả định và Phụ thuộc

- Người dùng có kết nối internet và trình duyệt hiện đại.
- Các API bên ngoài (Hugging Face, nền tảng blog) luôn sẵn sàng và đáng tin cậy.
- Hệ thống được triển khai trên nền tảng đám mây như Render và Vercel.

---

## 3. Yêu cầu Cụ thể

### 3.1 Yêu cầu Giao diện Bên ngoài

#### 3.1.1 Giao diện Người dùng

- Hệ thống cung cấp giao diện web đáp ứng trên cả máy tính để bàn và thiết bị di động.
- Giao diện được thiết kế bằng Figma, với wireframe và prototype tham khảo trong Phụ lục.

#### 3.1.2 Giao diện Phần cứng

- Không yêu cầu giao diện phần cứng đặc biệt ngoài máy chủ web và thiết bị người dùng tiêu chuẩn.

#### 3.1.3 Giao diện Phần mềm

- Hệ thống backend Frappe cung cấp REST API để quản lý người dùng, bài viết và lịch đăng.
- Frontend React.js kết nối với Frappe qua REST API để thực hiện các chức năng CRUD và scheduling.
- Tích hợp với API Hugging Face để tạo nội dung AI.
- Kết nối với API của WordPress, Blogger và Medium để đăng bài.
- Sử dụng SMTP (Gmail API hoặc SendGrid) để gửi thông báo qua email.

#### 3.1.4 Giao diện Truyền thông

- Sử dụng HTTPS để đảm bảo giao tiếp an toàn giữa client và server.
- Sử dụng RESTful API cho tích hợp với các dịch vụ bên ngoài.

### 3.2 Yêu cầu Chức năng

| ID  | Mô tả Yêu cầu                                                          | Mức độ Ưu tiên | Tiêu chí Chấp nhận                                                     |
| --- | ---------------------------------------------------------------------- | -------------- | ---------------------------------------------------------------------- |
| FR1 | Hệ thống cho phép đăng ký, đăng nhập, khôi phục mật khẩu               | Cao            | Người dùng có thể tạo tài khoản, đăng nhập và đặt lại mật khẩu khi cần |
| FR2 | Hệ thống cho phép tạo, chỉnh sửa, xóa bài viết                         | Cao            | Người dùng có thể tạo bài viết với tiêu đề, nội dung, hình ảnh         |
| FR3 | Hệ thống hỗ trợ đặt lịch đăng bài tự động                              | Cao            | Người dùng có thể đặt lịch và bài viết được đăng đúng giờ              |
| FR4 | Hệ thống đăng bài lên ít nhất 3 nền tảng (WordPress, Blogger, Medium)  | Cao            | Hệ thống đăng bài thành công lên ít nhất 3 nền tảng khác nhau          |
| FR5 | Hệ thống cho phép phân loại bài viết theo danh mục và tag              | Trung bình     | Người dùng có thể tạo, chỉnh sửa, xóa danh mục và gắn tag cho bài viết |
| FR6 | Hệ thống tích hợp AI để gợi ý tiêu đề và nội dung                      | Trung bình     | Hệ thống cung cấp nội dung gợi ý phù hợp với từ khóa/chủ đề nhập vào   |
| FR7 | Hệ thống cung cấp báo cáo và thống kê lượt xem, tương tác              | Thấp           | Người dùng có thể xem báo cáo tổng hợp về hiệu suất bài viết           |
| FR8 | Hệ thống cung cấp tìm kiếm bài viết theo từ khóa, danh mục, ngày tháng | Cao            | Người dùng có thể tìm kiếm và nhận kết quả phù hợp                     |

### 3.3 Yêu cầu Phi Chức năng

| ID   | Mô tả Yêu cầu                                             | Mức độ Ưu tiên | Tiêu chí Chấp nhận                                                      |
| ---- | --------------------------------------------------------- | -------------- | ----------------------------------------------------------------------- |
| NFR1 | Hệ thống xử lý ít nhất 1000 bài viết/ngày không gián đoạn | Cao            | Hệ thống hoạt động ổn định khi xử lý khối lượng lớn bài viết            |
| NFR2 | Hệ thống hỗ trợ xác thực hai lớp và mã hóa dữ liệu        | Cao            | Người dùng có thể bật 2FA, dữ liệu được mã hóa và bảo vệ                |
| NFR3 | Hệ thống có thể mở rộng để tích hợp thêm nền tảng blog    | Trung bình     | Hệ thống có API mở để thêm nền tảng mới mà không cần thay đổi lớn       |
| NFR4 | Giao diện trực quan, dễ sử dụng, không cần hướng dẫn dài  | Cao            | Người dùng có thể thao tác mà không gặp khó khăn                        |
| NFR5 | Hệ thống tương thích với nhiều thiết bị (desktop, mobile) | Trung bình     | Giao diện hiển thị tốt và hoạt động mượt mà trên các thiết bị khác nhau |

---

## 4. Phụ lục

- **Wireframe Design**: [Link đến Wireframe](#).
- **Prototype Design**: [Link đến Prototype](#).
- **Sơ đồ Thiết kế**:
  - Sơ đồ ERD (Trang 39).
  - Sơ đồ Usecase Tổng quan (Trang 40).
  - Sơ đồ Usecase Quản lý Danh mục (Trang 41).
  - Sơ đồ Usecase Quản lý Tài khoản (Trang 43).
  - Sơ đồ Usecase Tìm kiếm (Trang 45).
  - Sơ đồ Usecase Quản lý Bài viết (Trang 47).
  - Sơ đồ Usecase Xem Bài viết (Trang 50).
  - Sơ đồ Lớp (Trang 52).
  - Sơ đồ Hoạt động (Trang 52-53).
  - Sơ đồ Tuần tự (Trang 54-57).

---

### Ghi chú

File `SRS.md` này cung cấp đầy đủ thông tin cần thiết cho dự án AutoBlog, bao gồm yêu cầu chức năng, phi chức năng và các chi tiết kỹ thuật. Nếu cần thêm thông tin hoặc chỉnh sửa, vui lòng yêu cầu cụ thể để hoàn thiện.