<template>
    <section id="python-projects">
      <h2>Python Projects</h2>
      <p>Here are some of the Python projects I've worked on:</p>
      <div class="projects">
        <div v-for="(project, index) in projects" :key="index" class="project-card">
          <h3>{{ project.title }}</h3>
          <p>{{ project.description }}</p>
          <a :href="project.link" class="btn btn-primary" target="_blank">View on GitHub</a>
        </div>
      </div>
    </section>
  </template>
  
  <script>
  export default {
    data() {
      return {
        projects: [
          {
            title: "Python Cheat Sheet",
            description: "A curated collection of Python syntax, tips, and examples for quick reference.",
            link: "https://github.com/mrcdctr/python-cheat-sheet"
          },
          {
            title: "Python Developer Course",
            description: "Resources and projects created while taking a Python developer course.",
            link: "https://github.com/mrcdctr/python-developer-course"
          },
          {
            title: "Meme Generator",
            description: "A Python application for generating memes with custom captions.",
            link: "https://github.com/mrcdctr/meme-generator"
          },
          {
            title: "Web Scraping App",
            description: "A tool for scraping and analyzing data from websites using Python.",
            link: "https://github.com/mrcdctr/web-scraping-app"
          },
          {
            title: "Password Vault",
            description: "A secure password management application built with Python.",
            link: "https://github.com/mrcdctr/password-vault"
          },
          {
            title: "Weather Notification System",
            description: "Fetches weather forecasts and sends alerts via SMS.",
            link: "https://github.com/mrcdctr/weather-notification-system"
          }
        ]
      };
    }
  };
  </script>
  