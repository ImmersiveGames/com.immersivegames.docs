(function () {
  const root = document.documentElement;
  const topbar = document.querySelector(".docs-topbar");
  const sidebar = document.querySelector("#docs-sidebar");
  const toc = document.querySelector("#docs-toc");

  function updateTopbarHeight() {
    if (!topbar) return;
    const height = Math.ceil(topbar.getBoundingClientRect().height);
    root.style.setProperty("--docs-layout-topbar-height", `${height}px`);
  }

  function safeGetTheme() {
    try {
      return localStorage.getItem("docs-theme");
    } catch (error) {
      return null;
    }
  }

  function safeSetTheme(theme) {
    try {
      localStorage.setItem("docs-theme", theme);
    } catch (error) {
      // The template remains usable without localStorage.
    }
  }

  const savedTheme = safeGetTheme();
  if (savedTheme === "dark" || savedTheme === "light") {
    root.dataset.theme = savedTheme;
  }

  updateTopbarHeight();
  window.addEventListener("resize", updateTopbarHeight);

  if ("ResizeObserver" in window && topbar) {
    const topbarObserver = new ResizeObserver(updateTopbarHeight);
    topbarObserver.observe(topbar);
  }

  document.addEventListener("click", (event) => {
    const themeButton = event.target.closest("[data-action='toggle-theme']");
    if (themeButton) {
      const next = root.dataset.theme === "dark" ? "light" : "dark";
      root.dataset.theme = next;
      safeSetTheme(next);
      updateTopbarHeight();
    }

    const sidebarButton = event.target.closest("[data-action='toggle-sidebar']");
    if (sidebarButton && sidebar) {
      const open = !sidebar.classList.contains("is-open");
      sidebar.classList.toggle("is-open", open);
      sidebarButton.setAttribute("aria-expanded", String(open));
    }

    const tocButton = event.target.closest("[data-action='toggle-toc']");
    if (tocButton && toc) {
      const open = !toc.classList.contains("is-open");
      toc.classList.toggle("is-open", open);
      tocButton.setAttribute("aria-expanded", String(open));
    }
  });
})();
