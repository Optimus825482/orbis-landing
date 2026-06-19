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

// Parallax effect for stars (rAF-throttled, respects reduced-motion)
const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
if (!reducedMotion) {
  const stars = document.querySelector(".stars");
  const stars2 = document.querySelector(".stars2");
  const stars3 = document.querySelector(".stars3");
  let pendingX = 0;
  let pendingY = 0;
  let rafScheduled = false;

  function applyParallax() {
    if (stars) stars.style.transform = `translate(${pendingX * 20}px, ${pendingY * 20}px)`;
    if (stars2) stars2.style.transform = `translate(${pendingX * -15}px, ${pendingY * -15}px)`;
    if (stars3) stars3.style.transform = `translate(${pendingX * 10}px, ${pendingY * 10}px)`;
    rafScheduled = false;
  }

  window.addEventListener("mousemove", (e) => {
    pendingX = e.clientX / window.innerWidth;
    pendingY = e.clientY / window.innerHeight;
    if (!rafScheduled) {
      rafScheduled = true;
      requestAnimationFrame(applyParallax);
    }
  }, { passive: true });
}

// Console Easter Egg
console.log(`
✧ ORBIS - Kaderin Geometrisi ✧
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Yapay Zeka Destekli Astroloji
© 2026 ORBIS by Erkan ERDEM
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
`);

// ═══════════════════════════════════════════════════════════════
// KVKK / GDPR Cookie Consent
// ═══════════════════════════════════════════════════════════════

const COOKIE_CONSENT_KEY = "orbis_cookie_consent";

function getCookieConsent() {
  try {
    const raw = localStorage.getItem(COOKIE_CONSENT_KEY);
    if (!raw) return null;
    const parsed = JSON.parse(raw);
    if (parsed && typeof parsed === "object" && parsed.decision) return parsed;
  } catch (e) {
    // localStorage unavailable or corrupt
  }
  return null;
}

function setCookieConsent(decision) {
  try {
    localStorage.setItem(COOKIE_CONSENT_KEY, JSON.stringify({
      decision,
      timestamp: new Date().toISOString(),
      version: "1.0"
    }));
  } catch (e) {
    // ignore — banner still works for the session
  }
}

function disableNonEssentialScripts() {
  // Disable AdSense by removing the script element if present
  document.querySelectorAll('script[src*="googlesyndication.com"]').forEach((s) => {
    s.remove();
  });
  // Disable Google Analytics by stubbing dataLayer
  window.dataLayer = [];
  window.gtag = function () {
    // no-op when consent not granted
  };
}

function loadNonEssentialScripts() {
  // Reload page to re-execute deferred GA script with consent
  // (simpler than dynamically injecting after deferral has passed)
  location.reload();
}

function initCookieBanner() {
  const banner = document.getElementById("cookie-banner");
  if (!banner) return;

  const consent = getCookieConsent();

  if (!consent) {
    // First visit — show banner, block non-essential by default
    disableNonEssentialScripts();
    banner.hidden = false;
  } else if (consent.decision === "accept") {
    banner.hidden = true;
    // Consent given previously — scripts load normally via <head> defer
  } else {
    // Rejected — keep blocking
    banner.hidden = true;
    disableNonEssentialScripts();
  }

  banner.addEventListener("click", (e) => {
    const btn = e.target.closest("[data-cookie-action]");
    if (!btn) return;
    const action = btn.dataset.cookieAction;
    setCookieConsent(action);
    banner.hidden = true;
    if (action === "accept") {
      loadNonEssentialScripts();
    } else {
      disableNonEssentialScripts();
    }
  });

  // Keyboard support: Escape closes banner as "reject only"
  banner.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && !banner.hidden) {
      setCookieConsent("reject");
      banner.hidden = true;
      disableNonEssentialScripts();
    }
  });
}

// Initial gate — block GA/AdSense until consent decision
if (!getCookieConsent() || getCookieConsent().decision !== "accept") {
  disableNonEssentialScripts();
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", initCookieBanner);
} else {
  initCookieBanner();
}
