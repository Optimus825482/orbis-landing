// ═══════════════════════════════════════════════════════════════
// ORBIS LANDING PAGE - JAVASCRIPT
// ═══════════════════════════════════════════════════════════════

// Mobile Menu Toggle
function toggleMobileMenu() {
  const menu = document.getElementById("mobileMenu");
  menu.classList.toggle("active");
}

function closeMobileMenu() {
  const menu = document.getElementById("mobileMenu");
  menu.classList.remove("active");
}

// Navbar scroll effect
window.addEventListener("scroll", () => {
  const navbar = document.querySelector(".navbar");
  if (window.scrollY > 50) {
    navbar.style.background = "rgba(10, 1, 24, 0.95)";
    navbar.style.boxShadow = "0 4px 30px rgba(0, 0, 0, 0.3)";
  } else {
    navbar.style.background = "rgba(10, 1, 24, 0.8)";
    navbar.style.boxShadow = "none";
  }
});

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
  anchor.addEventListener("click", function (e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute("href"));
    if (target) {
      target.scrollIntoView({
        behavior: "smooth",
        block: "start",
      });
    }
  });
});

// Intersection Observer for animations
const observerOptions = {
  threshold: 0.1,
  rootMargin: "0px 0px -50px 0px",
};

const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.classList.add("animate-in");
    }
  });
}, observerOptions);

// Observe elements for animation
document.addEventListener("DOMContentLoaded", () => {
  // Add animation classes
  const animateElements = document.querySelectorAll(
    ".feature-card, .step, .screenshot-card, .analysis-item"
  );

  animateElements.forEach((el, index) => {
    el.style.opacity = "0";
    el.style.transform = "translateY(30px)";
    el.style.transition = `opacity 0.6s ease ${
      index * 0.1
    }s, transform 0.6s ease ${index * 0.1}s`;
    observer.observe(el);
  });
});

// Animation class
document.head.insertAdjacentHTML(
  "beforeend",
  `
    <style>
        .animate-in {
            opacity: 1 !important;
            transform: translateY(0) !important;
        }
    </style>
`
);

// Parallax effect for stars
window.addEventListener("mousemove", (e) => {
  const stars = document.querySelector(".stars");
  const stars2 = document.querySelector(".stars2");
  const stars3 = document.querySelector(".stars3");

  const x = e.clientX / window.innerWidth;
  const y = e.clientY / window.innerHeight;

  if (stars) stars.style.transform = `translate(${x * 20}px, ${y * 20}px)`;
  if (stars2) stars2.style.transform = `translate(${x * -15}px, ${y * -15}px)`;
  if (stars3) stars3.style.transform = `translate(${x * 10}px, ${y * 10}px)`;
});

// Console Easter Egg
console.log(`
✧ ORBIS - Kaderin Geometrisi ✧
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Yapay Zeka Destekli Astroloji
© 2026 ORBIS by Erkan ERDEM
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
`);
