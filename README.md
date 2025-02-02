# 📌 Marco Doctor - Portfolio Website

## 🚀 About the Project
This is a **personal portfolio website** built using **Vue.js**. It showcases projects, skills, and achievements, providing visitors with an overview of Marco Doctor's work as a web developer.

## 🛠 Tech Stack
- **Frontend:** Vue.js 3, HTML5, CSS3, JavaScript
- **Styling:** Custom CSS
- **Deployment:** Nginx + Docker
- **Build Tool:** Vite

## 🎨 Features
✅ **Responsive Design** - Works on all devices (desktop, tablet, mobile).  
✅ **Dark Mode Toggle** - Switch between light and dark themes.  
✅ **Dynamic Project Showcase** - Display projects using Vue's dynamic rendering.  
✅ **Modals for Project Details** - Click to view project descriptions.  
✅ **Contact Form** - Integrated with [Formspree](https://formspree.io) for easy email communication.

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

## 🐞 Troubleshooting
### **Image Not Loading?**
- **Check if the image is inside `public/assets/images/`**
- Open in the browser: `http://localhost:5173/assets/images/ID_COVER.png`
- If missing, move the image to `public/assets/images/`

### **Common Fixes**
Restart the development server:
```sh
npm run dev
```
Clear cache and reload the page:
- **Windows/Linux:** `Ctrl + Shift + R`
- **Mac:** `Cmd + Shift + R`


