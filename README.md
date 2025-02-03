# 📌 Marco Doctor - Portfolio Website

## 🚀 About the Project
This is a **personal portfolio website** built using **Vue.js**. It showcases projects, skills, and achievements, providing visitors with an overview of Marco Doctor's work as a web developer.

## 🛠 Tech Stack
- **Frontend:** Vue.js 3, HTML5, CSS3, JavaScript
- **Styling:** Custom CSS, Tailwind CSS
- **Backend (Future Enhancement):** Node.js, Express.js
- **Database (Future Enhancement):** MongoDB, Firebase
- **Deployment:** Nginx + Docker, Vercel, Netlify
- **Build Tool:** Vite

## 🎨 Features
✅ **Responsive Design** - Works on all devices (desktop, tablet, mobile).  
✅ **Dark Mode Toggle** - Switch between light and dark themes.  
✅ **Dynamic Project Showcase** - Display projects using Vue's dynamic rendering.  
✅ **Modals for Project Details** - Click to view project descriptions.  
✅ **Contact Form** - Integrated with [Formspree](https://formspree.io) for easy email communication.  
✅ **SEO Optimization** - Meta tags and structured data for better search engine rankings.  
✅ **Lazy Loading Images** - Improves performance and page speed.  
✅ **Progressive Web App (PWA) Support** - Future enhancement to allow offline access.  
✅ **Blog Section** - Future addition to share articles and tutorials.

## 📂 Project Structure
```
📦 mrcdctr-portfolio
├── 📂 public
│   ├── 📂 assets
│   │   ├── 📂 images
│   │   │   ├── 🖼️ ID_COVER.png
├── 📂 src
│   ├── 📂 assets (Vue processed assets)
│   ├── 📂 components
│   │   ├── 📄 PythonProjects.vue
│   ├── 📂 views
│   ├── 📄 App.vue
│   ├── 📄 main.js
├── 📄 package.json
├── 📄 README.md
```

## 🛠 Installation & Setup
1️⃣ **Clone the repository**:
```sh
git clone https://github.com/mrcdctr/mrcdctr-portfolio.git
cd mrcdctr-portfolio
```

2️⃣ **Install dependencies**:
```sh
npm install
```

3️⃣ **Run the development server**:
```sh
npm run dev
```
👉 The project will be available at: `http://localhost:5173/`

## 📦 Build & Deployment
To create a production build:
```sh
npm run build
```
To deploy with Docker & Nginx:
1. **Build the Docker image**:
```sh
docker build -t portfolio .
```
2. **Run the container**:
```sh
docker run -d -p 80:80 --name portfolio-container portfolio
```
👉 The portfolio will be accessible at `http://localhost/`

[(Live Demo)](https://mrcdctr-portfolio-website.netlify.app/)

## 🚀 Future Enhancements
- 🔹 **Admin Dashboard** - Manage portfolio content dynamically.  
- 🔹 **Backend API** - Implement Node.js + Express API for storing project data.  
- 🔹 **CMS Integration** - Use a lightweight CMS for easy content management.  
- 🔹 **User Authentication** - Secure login system for updating portfolio.  
- 🔹 **Portfolio Analytics** - Track visitor statistics using Google Analytics.  
- 🔹 **Multilingual Support** - Translate the site into different languages.  
- 🔹 **Animated Transitions** - Improve UI/UX with Vue animations.

## 🐞 Troubleshooting
### **Image Not Loading?**
- **Check if the image is inside `public/assets/images/`**
- Open in the browser: `http://localhost:5173/assets/images/id_cover.png`
- If missing, move the image to `public/assets/images/`

### **Common Fixes**
Restart the development server:
```sh
npm run dev
```
Clear cache and reload the page:
- **Windows/Linux:** `Ctrl + Shift + R`
- **Mac:** `Cmd + Shift + R`

## 📬 Contact
📧 Email: [Gmail](mailto:mrcdctr@gmail.com)  
🔗 GitHub: [mrcdctr](https://github.com/mrcdctr)  
🌐 Portfolio: [https://mrcdctr.dev](https://mrcdctr.dev)

## ⭐ Contribute
Feel free to fork this repository, create a feature branch, and submit a PR! 😊

