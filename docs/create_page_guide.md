✅ 1. Web Form — Giao diện nhập liệu đơn giản cho người dùng
Web Form là cách đơn giản nhất để tạo form public (người ngoài có thể điền).
📌 Dùng khi:
Bạn muốn người dùng tạo bản ghi (đăng ký, đặt hàng, gửi yêu cầu)


Giao diện chỉ cần form, không cần logic phức tạp


🛠️ Cách làm:
Vào Desk > Web Site > Web Form


Nhấn New


Đặt tên form, chọn Doctype có sẵn (vd: Customer, Lead, Contact,...)


Chọn các trường cần hiển thị


Chọn đường dẫn URL (vd: /dang-ky)


Tùy chỉnh thêm CSS hoặc đặt Published


👉 Truy cập website của bạn ở đường dẫn /dang-ky là có form ngay.

🌱 2. Web Page — Hiển thị nội dung từ Doctype bằng Jinja
Nếu bạn muốn hiển thị dữ liệu dạng danh sách, bảng, profile... thì dùng Web Page.
📌 Dùng khi:
Hiển thị danh sách, bảng dữ liệu (vd: danh sách sản phẩm, khách hàng, đơn hàng,...)


Có thể kết hợp HTML + Jinja để render giao diện


🛠️ Cách làm:
Vào Desk > Website > Web Page


Nhấn New


Điền title, route (vd: /san-pham)


Trong phần HTML, bạn có thể viết Jinja template:


html
Sao chépChỉnh sửa
{% set items = frappe.get_all('Item', fields=['item_name', 'item_code', 'image']) %}
<div class="grid grid-cols-3 gap-4">
  {% for i in items %}
    <div class="card">
      <img src="{{ i.image }}" />
      <h3>{{ i.item_name }}</h3>
      <p>{{ i.item_code }}</p>
    </div>
  {% endfor %}
</div>

💡 Giao diện được tạo bằng HTML, có thể chèn Tailwind CSS (Frappe đã hỗ trợ sẵn), hoặc CSS riêng.

🧙 3. Custom Page (JS + API) — Làm giao diện xịn như Single Page App
📌 Dùng khi:
Bạn muốn giao diện độc đáo, animation, fetch dữ liệu qua API, xử lý logic động (JS)


Làm một app riêng như portal, dashboard, hệ thống web tương tác


🛠️ Cách làm:
Tạo Page bằng command:


bash
Sao chépChỉnh sửa
bench --site your-site-name new-page your_app my_custom_page

Vào thư mục:


bash
Sao chépChỉnh sửa
apps/your_app/your_app/www/my_custom_page/index.js

Viết code:


js
Sao chépChỉnh sửa
frappe.pages['my_custom_page'].on_page_load = function(wrapper) {
  let page = frappe.ui.make_app_page({
    parent: wrapper,
    title: 'Trang khách hàng',
    single_column: true
  });

  frappe.call({
    method: 'frappe.client.get_list',
    args: {
      doctype: 'Customer',
      fields: ['name', 'customer_name']
    },
    callback: function(r) {
      let html = '<ul>';
      (r.message || []).forEach(c => {
        html += `<li>${c.customer_name}</li>`;
      });
      html += '</ul>';
      $(wrapper).find('.layout-main-section').html(html);
    }
  });
};

👉 Truy cập: http://your-site-name/my_custom_page
Bạn có toàn quyền viết giao diện bằng HTML, Tailwind, JS, Vue, React... tùy thích.

