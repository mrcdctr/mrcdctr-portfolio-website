// Toggle Mobile Navigation Menu
document.querySelector('.menu-toggle').addEventListener('click', () => {
    document.querySelector('.nav-links').classList.toggle('show');
});

// Dark Mode Toggle
document.querySelector('#dark-mode-toggle').addEventListener('click', () => {
    if (document.body.getAttribute('data-theme') === 'dark') {
        document.body.removeAttribute('data-theme');
        localStorage.setItem('theme', 'light');
    } else {
        document.body.setAttribute('data-theme', 'dark');
        localStorage.setItem('theme', 'dark');
    }
});

// Load Dark Mode Preference on Page Load
if (localStorage.getItem('theme') === 'dark') {
    document.body.setAttribute('data-theme', 'dark');
}

// Handle Modal Popups for Projects
document.querySelectorAll('.modal-btn').forEach(button => {
    button.addEventListener('click', event => {
        const modalId = event.target.getAttribute('data-modal');
        document.getElementById(modalId).style.display = 'flex';
    });
});

document.querySelectorAll('.close-btn').forEach(button => {
    button.addEventListener('click', event => {
        const modalId = event.target.getAttribute('data-modal');
        document.getElementById(modalId).style.display = 'none';
    });
});

window.addEventListener('click', event => {
    if (event.target.classList.contains('modal')) {
        event.target.style.display = 'none';
    }
});
const projects = [
    {
        title: "Content Management System (CMS) 🏗",
        description: "Coming soon...",
        link: "#"
    },
    {
        title: "E-commerce Website 🛒",
        description: "Coming soon...",
        link: "#"
    },
    {
        title: "Chat Application 💬",
        description: "Coming soon...",
        link: "#"
    }
];

const projectsContainer = document.querySelector(".projects");
projects.forEach(project => {
    const projectCard = document.createElement("div");
    projectCard.classList.add("project-card");
    projectCard.innerHTML = `
        <h3>${project.title}</h3>
        <p>${project.description}</p>
        <a href="${project.link}" class="btn btn-primary">View More</a>
    `;
    projectsContainer.appendChild(projectCard);
});
