# GitHub_QLDA_22NH10_G12_BTQT# 📘 S-Blog

**S-Blog** is a personal blogging platform built entirely with **React**. Each user becomes their own **blogger** within the site — they can create, edit, delete posts, explore content from others, follow users, and share blog posts to social media.

> ⚠️ **Note**: This repository only contains the **frontend** of the project. It communicates with a pre-existing **REST API** (not included in this repo).

---

## 🚀 Features

-   📝 **Full CRUD for blog posts** — create, update, delete, and view posts.
-   🔍 **Search for posts** by keywords.
-   👥 **View posts from other users**.
-   ❤️ **Follow / Unfollow users** to keep up with their content.
-   🔗 **Share blog posts** to social platforms like Facebook, Twitter, etc.
-   🌐 **Multilingual support** with i18n.
-   📱 **Responsive design** for all screen sizes.
-   👤 **User profile page** with personal blog management.

---

## 🛠️ Tech Stack

| Category            | Technology                                                                                                              |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| ⚛️ Framework        | React                                                                                                                   |
| 🎨 UI / CSS         | [SCSS module]                                                                                                           |
| 🔄 State Management | [React Query](https://tanstack.com/query) (async), [React Context](https://reactjs.org/docs/context.html) (local state) |
| 📑 Form Handling    | [React Hook Form](https://react-hook-form.com/)                                                                         |
| 🧭 Routing          | [React Router](https://reactrouter.com/)                                                                                |
| ⚙️ Build Tool       | [Vite](https://vitejs.dev/)                                                                                             |
| 🌐 i18n             | [react-i18next](https://react.i18next.com/)                                                                             |
| 🔍 SEO              | [React Helmet](https://github.com/nfl/react-helmet)                                                                     |
| 🧪 Unit Testing     | (Optional — can be integrated with Jest or React Testing Library)                                                       |
| 📖 UI Documentation | [Storybook](https://storybook.js.org/)                                                                                  |
| 🔌 API Integration  | REST API (provided separately by your own backend)                                                                      |

---

## 📦 Getting Started

```bash
# Clone the project
git clone https://github.com/your-username/s-blog.git
cd s-blog

# Install dependencies
npm install

# Start the development server
npm run dev
```

---

## 📁 Project Structure

```
src/
├── components/     # Shared UI components
├── pages/          # Application pages
├── hooks/          # Custom React hooks
├── context/        # React Context for global state
├── services/       # API interaction logic
├── locales/        # i18n translation files
├── routes/         # Route definitions
└── utils/          # Utility functions
```

---

## 🤝 Contributing

-   Feel free to open Issues or submit a Pull Request if you find bugs or have feature suggestions.

---

## 📄 License

-   MIT License — see the LICENSE file for details.
