const navToggle = document.getElementById("nav-toggle");
const nav = document.getElementById("nav");
const yearSpan = document.getElementById("year");

navToggle?.addEventListener("click", () => {
  nav.classList.toggle("open");
});

yearSpan.textContent = new Date().getFullYear();
