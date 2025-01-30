// Toggle Mobile Navigation Menu
document.querySelector('.menu-toggle').addEventListener('click', () => {
    document.querySelector('.nav-links').classList.toggle('show');
});

// Dark Mode Toggle
document.querySelector('#dark-mode-toggle').addEventListener('click', () => {
    document.body.toggleAttribute('data-theme', 'dark');
    localStorage.setItem('theme', document.body.hasAttribute('data-theme') ? 'dark' : 'light');
});

// Load Dark Mode Preference
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