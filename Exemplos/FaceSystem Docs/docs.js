(function () {
  "use strict";

  var tabs = Array.from(document.querySelectorAll(".tab"));
  var documents = Array.from(document.querySelectorAll("[data-document]"));
  var tocLists = Array.from(document.querySelectorAll("[data-toc]"));
  var sidebar = document.querySelector(".sidebar");
  var sidebarToggle = document.querySelector(".sidebar-toggle");
  var searchInput = document.querySelector("#docs-search");
  var searchStatus = document.querySelector("#search-status");
  var activeDocument = "technical";
  var observer = null;

  function normalizeText(value) {
    return value.toLocaleLowerCase().replace(/\s+/g, " ").trim();
  }

  function resetSearch() {
    if (searchInput) {
      searchInput.value = "";
    }

    documents.forEach(function (documentPanel) {
      documentPanel.querySelectorAll("section[hidden]").forEach(function (section) {
        section.hidden = false;
      });
    });

    tocLists.forEach(function (toc) {
      toc.querySelectorAll("a[hidden]").forEach(function (link) {
        link.hidden = false;
      });
    });

    if (searchStatus) {
      searchStatus.textContent = "";
      searchStatus.classList.remove("is-empty");
    }
  }

  function runSearch() {
    if (!searchInput || !searchStatus) {
      return;
    }

    var query = normalizeText(searchInput.value);
    var activePanel = document.querySelector('[data-document="' + activeDocument + '"]');
    var activeToc = document.querySelector('[data-toc="' + activeDocument + '"]');

    if (!activePanel || !activeToc) {
      return;
    }

    var sections = Array.from(activePanel.querySelectorAll("section[id]"));
    var visibleSections = 0;

    sections.forEach(function (section) {
      var matches = !query || normalizeText(section.textContent).includes(query);
      section.hidden = !matches;
      if (matches) {
        visibleSections += 1;
      }
    });

    activeToc.querySelectorAll("a").forEach(function (link) {
      var target = document.querySelector(link.getAttribute("href"));
      var section = target ? target.closest("section[id]") : null;
      link.hidden = Boolean(query) && (!section || section.hidden);
    });

    searchStatus.classList.toggle("is-empty", Boolean(query) && visibleSections === 0);

    if (!query) {
      searchStatus.textContent = "";
    } else if (visibleSections === 0) {
      searchStatus.textContent = "No results found.";
    } else {
      searchStatus.textContent = visibleSections + (visibleSections === 1 ? " section found." : " sections found.");
    }

    if (observer) {
      observer.disconnect();
    }
    if (!query) {
      observeSections();
    }
  }

  function setActiveSection(id) {
    var activeToc = document.querySelector('[data-toc="' + activeDocument + '"]');
    if (!activeToc) {
      return;
    }

    activeToc.querySelectorAll("a").forEach(function (link) {
      link.classList.toggle("is-current", link.getAttribute("href") === "#" + id);
    });
  }

  function observeSections() {
    if (observer) {
      observer.disconnect();
    }

    var activePanel = document.querySelector('[data-document="' + activeDocument + '"]');
    if (!activePanel || !("IntersectionObserver" in window)) {
      return;
    }

    observer = new IntersectionObserver(function (entries) {
      var visible = entries
        .filter(function (entry) { return entry.isIntersecting; })
        .sort(function (a, b) { return b.intersectionRatio - a.intersectionRatio; });

      if (visible.length) {
        setActiveSection(visible[0].target.id);
      }
    }, {
      rootMargin: "-18% 0px -68% 0px",
      threshold: [0, 0.1, 0.35]
    });

    activePanel.querySelectorAll("section[id], h4[id]").forEach(function (section) {
      observer.observe(section);
    });
  }

  function activateDocument(name, moveFocus) {
    activeDocument = name;
    resetSearch();

    tabs.forEach(function (tab) {
      var isActive = tab.dataset.doc === name;
      tab.classList.toggle("is-active", isActive);
      tab.setAttribute("aria-selected", String(isActive));
      tab.tabIndex = isActive ? 0 : -1;
      if (isActive && moveFocus) {
        tab.focus();
      }
    });

    documents.forEach(function (documentPanel) {
      var isActive = documentPanel.dataset.document === name;
      documentPanel.hidden = !isActive;
      documentPanel.classList.toggle("is-active", isActive);
    });

    tocLists.forEach(function (toc) {
      var isActive = toc.dataset.toc === name;
      toc.hidden = !isActive;
      toc.classList.toggle("is-active", isActive);
    });

    if (sidebar) {
      sidebar.classList.remove("is-open");
    }
    if (sidebarToggle) {
      sidebarToggle.setAttribute("aria-expanded", "false");
    }

    window.scrollTo({ top: 0, behavior: "auto" });
    observeSections();
  }

  function openDocumentLink(link) {
    var documentName = link.dataset.docTarget;
    var targetId = link.getAttribute("href").slice(1);

    activateDocument(documentName, false);
    window.requestAnimationFrame(function () {
      var target = document.getElementById(targetId);
      if (target) {
        target.scrollIntoView();
        setActiveSection(targetId);
      }
    });
  }

  tabs.forEach(function (tab, index) {
    tab.addEventListener("click", function () {
      activateDocument(tab.dataset.doc, false);
    });

    tab.addEventListener("keydown", function (event) {
      if (event.key !== "ArrowLeft" && event.key !== "ArrowRight") {
        return;
      }

      event.preventDefault();
      var direction = event.key === "ArrowRight" ? 1 : -1;
      var nextIndex = (index + direction + tabs.length) % tabs.length;
      activateDocument(tabs[nextIndex].dataset.doc, true);
    });
  });

  tocLists.forEach(function (toc) {
    toc.addEventListener("click", function (event) {
      if (!event.target.matches("a")) {
        return;
      }

      var targetId = event.target.getAttribute("href").slice(1);
      setActiveSection(targetId);
      if (sidebar) {
        sidebar.classList.remove("is-open");
      }
      if (sidebarToggle) {
        sidebarToggle.setAttribute("aria-expanded", "false");
      }
    });
  });

  document.addEventListener("click", function (event) {
    var documentLink = event.target.closest("a[data-doc-target]");
    if (!documentLink) {
      return;
    }

    event.preventDefault();
    openDocumentLink(documentLink);
  });

  if (sidebarToggle && sidebar) {
    sidebarToggle.addEventListener("click", function () {
      var isOpen = sidebar.classList.toggle("is-open");
      sidebarToggle.setAttribute("aria-expanded", String(isOpen));
    });
  }

  if (searchInput) {
    searchInput.addEventListener("input", runSearch);
    searchInput.addEventListener("keydown", function (event) {
      if (event.key === "Escape" && searchInput.value) {
        resetSearch();
        observeSections();
      }
    });
  }

  setActiveSection("technical-architecture");
  observeSections();
}());
