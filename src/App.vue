<template>
  <div id="app">
    <!-- Navigation -->
    <nav>
      <div>Marco Doctor</div>
      <button class="menu-toggle" @click="toggleMenu">☰</button>
      <div :class="{ 'nav-links': true, 'show': showMenu }">
        <a href="#about">About</a>
        <a href="#projects">Projects</a>
        <a href="#python-projects">Python Projects</a>
        <a href="#contact">Contact</a>
      </div>
      <button id="dark-mode-toggle" @click="toggleDarkMode" class="dark-mode-toggle">
        Toggle Dark Mode
      </button>
    </nav>

    <!-- Hero Section -->
    <section class="hero">
      <img src="/assets/images/id_cover.png" alt="Marco Doctor">
      <h1>Marco Doctor</h1>
      <p>Web Developer passionate about creating interactive and user-friendly applications.</p>
    </section>

    <!-- About Me -->
    <section id="about">
      <h2>About Me</h2>
      <p>
        Hi! I'm Marco Doctor, an aspiring Web Developer passionate about building user-friendly
        and interactive web applications. I enjoy solving problems, crafting clean designs, and
        developing efficient backend systems.
      </p>
    </section>

    <!-- Web Development Projects -->
    <section id="projects">
      <h2>Web Development Projects</h2>
      <div class="projects">
        <div v-for="(project, index) in projects" :key="index" class="project-card">
          <h3>{{ project.title }}</h3>
          <p>{{ project.description }}</p>
          <button v-if="project.modal" @click="openModal(index)">View More</button>
          <a v-else :href="project.link" target="_blank" class="btn btn-primary">Live Demo</a>
        </div>
      </div>
    </section>

    <!-- Python Projects Section -->
    <PythonProjects />

    <!-- Contact Section -->
    <section id="contact">
      <h2>Contact Me</h2>
      <form action="https://formspree.io/f/xvgzaeny" method="POST">
        <label>Name:</label>
        <input type="text" name="name" required>
        <label>Email:</label>
        <input type="email" name="email" required>
        <label>Message:</label>
        <textarea name="message" rows="5" required></textarea>
        <button type="submit">Send</button>
      </form>
    </section>

    <footer>&copy; 2025 Marco Doctor. All Rights Reserved.</footer>

    <!-- Modals -->
    <div v-if="modalOpen" class="modal">
      <div class="modal-content">
        <span class="close-btn" @click="closeModal">&times;</span>
        <h3>{{ modalContent.title }}</h3>
        <p>{{ modalContent.description }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import PythonProjects from "./components/PythonProjects.vue";

export default {
  components: {
    PythonProjects,
  },
  data() {
    return {
      coverImage: new URL("@/assets/images/id_cover.png", import.meta.url).href,
      showMenu: false,
      darkMode: localStorage.getItem("theme") === "dark",
      modalOpen: false,
      modalContent: {},
      projects: [
        {
          title: "Content Management System (CMS) 🏗",
          description: "Coming soon...",
          modal: true,
        },
        {
          title: "E-commerce Website 🛒",
          description: "Coming soon...",
          modal: true,
        },
        {
          title: "Chat Application 💬",
          description: "Coming soon...",
          modal: true,
        },
        {
          title: "GDP Dashboard 📊",
          description: "Interactive GDP visualization using Streamlit.",
          link: "https://gdp-dashboard-44b0eke58uz.streamlit.app/",
        },
        {
          title: "Movie Dataset 🎬",
          description: "A web application for analyzing movie datasets.",
          link: "https://movies-dataset-prn370gvp8.streamlit.app/",
        },
        {
          title: "AI Chatbot 🤖",
          description: "Conversational AI chatbot using LLM.",
          link: "https://chatbot-h5jilvj1nwi.streamlit.app/",
        },
      ],
    };
  },
  mounted() {
    if (this.darkMode) {
      document.body.setAttribute("data-theme", "dark");
    }
  },
  methods: {
    toggleMenu() {
      this.showMenu = !this.showMenu;
    },
    toggleDarkMode() {
      this.darkMode = !this.darkMode;
      document.body.setAttribute("data-theme", this.darkMode ? "dark" : "light");
      localStorage.setItem("theme", this.darkMode ? "dark" : "light");
    },
    openModal(index) {
      this.modalContent = this.projects[index];
      this.modalOpen = true;
    },
    closeModal() {
      this.modalOpen = false;
    },
  },
};
</script>
