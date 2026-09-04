(function () {
  "use strict";

  var MAX_RESULTS = 12;
  var NAME_WEIGHT = 100;
  var SLUG_WEIGHT = 60;
  var TAGLINE_WEIGHT = 30;
  var CATEGORY_WEIGHT = 15;

  var root = document.querySelector(".catalog-search");
  if (!root) return;

  var input = root.querySelector("#catalog-search-input");
  var panel = root.querySelector("#catalog-search-panel");
  var status = root.querySelector("#catalog-search-status");
  var listbox = root.querySelector("#catalog-search-listbox");
  if (!input || !panel || !status || !listbox) return;

  var indexUrl = root.getAttribute("data-index-url") || "";
  var baseurl = root.getAttribute("data-baseurl") || "";
  var records = null;
  var loadPromise = null;
  var loadError = "";
  var activeIndex = -1;
  var open = false;
  var renderFrame = 0;
  var lastMatches = [];

  function tokenize(query) {
    return query.toLowerCase().trim().split(/\s+/).filter(Boolean);
  }

  function contains(haystack, token) {
    return haystack.indexOf(token) !== -1;
  }

  function prepareIndex(payload) {
    var labels = payload.categories || {};
    var services = payload.services || [];
    var prepared = new Array(services.length);
    for (var i = 0; i < services.length; i++) {
      var item = services[i];
      var label = labels[item.category] || String(item.category || "").replace(/-/g, " ");
      var name = item.name || "";
      var slug = item.slug || "";
      var tagline = item.tagline || "";
      var category = item.category || "";
      prepared[i] = {
        id: item.id,
        slug: slug,
        name: name,
        tagline: tagline,
        category: category,
        categoryLabel: label,
        dossier: item.dossier || "",
        mcp: item.mcp_status === "available" || item.mcp_status === "optional",
        urlOnboarding: !!item.url_onboarding,
        nameLc: name.toLowerCase(),
        slugLc: slug.toLowerCase(),
        taglineLc: tagline.toLowerCase(),
        categoryLc: (category + " " + label).toLowerCase(),
        haystack: item.haystack || [name, slug, item.id, tagline, category, label].join(" ").toLowerCase()
      };
    }
    return prepared;
  }

  function scoreItem(item, tokens) {
    for (var i = 0; i < tokens.length; i++) {
      if (!contains(item.haystack, tokens[i])) return -1;
    }
    var score = 0;
    for (var j = 0; j < tokens.length; j++) {
      var token = tokens[j];
      if (contains(item.nameLc, token)) {
        score += NAME_WEIGHT;
        if (item.nameLc === token) score += 50;
        else if (item.nameLc.indexOf(token) === 0) score += 25;
      } else if (contains(item.slugLc, token)) {
        score += SLUG_WEIGHT;
      } else if (contains(item.taglineLc, token)) {
        score += TAGLINE_WEIGHT;
      } else if (contains(item.categoryLc, token)) {
        score += CATEGORY_WEIGHT;
      } else {
        score += 1;
      }
    }
    return score;
  }

  function search(query) {
    var tokens = tokenize(query);
    if (!tokens.length || !records) return [];
    var ranked = [];
    for (var i = 0; i < records.length; i++) {
      var item = records[i];
      var score = scoreItem(item, tokens);
      if (score >= 0) ranked.push({ item: item, score: score });
    }
    ranked.sort(function (a, b) {
      if (b.score !== a.score) return b.score - a.score;
      if (a.item.nameLc < b.item.nameLc) return -1;
      if (a.item.nameLc > b.item.nameLc) return 1;
      return 0;
    });
    var limit = Math.min(MAX_RESULTS, ranked.length);
    var out = new Array(limit);
    for (var j = 0; j < limit; j++) out[j] = ranked[j].item;
    return out;
  }

  function snippet(tagline, tokens) {
    if (!tagline) return "";
    var lower = tagline.toLowerCase();
    var idx = 0;
    for (var i = 0; i < tokens.length; i++) {
      var found = lower.indexOf(tokens[i]);
      if (found !== -1) {
        idx = Math.max(0, found - 18);
        break;
      }
    }
    var end = Math.min(tagline.length, idx + 92);
    var text = tagline.slice(idx, end).trim();
    if (idx > 0) text = "…" + text;
    if (end < tagline.length) text += "…";
    return text;
  }

  function collectionUrl(category) {
    return baseurl + "/categories/" + encodeURIComponent(category) + "/";
  }

  function setExpanded(expanded) {
    open = expanded;
    input.setAttribute("aria-expanded", expanded ? "true" : "false");
    panel.hidden = !expanded;
    root.classList.toggle("is-open", expanded);
    if (!expanded) {
      input.removeAttribute("aria-activedescendant");
      activeIndex = -1;
    }
  }

  function setStatus(text, visible) {
    status.textContent = text;
    status.hidden = !visible;
    status.classList.remove("visually-hidden");
  }

  function optionId(index) {
    return "catalog-search-opt-" + index;
  }

  function markActive(next) {
    var options = listbox.querySelectorAll('[role="option"]');
    if (!options.length) {
      activeIndex = -1;
      input.removeAttribute("aria-activedescendant");
      return;
    }
    if (next < 0) next = 0;
    if (next >= options.length) next = options.length - 1;
    activeIndex = next;
    for (var i = 0; i < options.length; i++) {
      var selected = i === activeIndex;
      options[i].setAttribute("aria-selected", selected ? "true" : "false");
      options[i].classList.toggle("is-active", selected);
    }
    input.setAttribute("aria-activedescendant", optionId(activeIndex));
    options[activeIndex].scrollIntoView({ block: "nearest" });
  }

  function render() {
    var query = input.value;
    var tokens = tokenize(query);

    if (!open) return;

    if (loadError) {
      lastMatches = [];
      listbox.replaceChildren();
      setStatus(loadError, true);
      input.removeAttribute("aria-activedescendant");
      return;
    }

    if (!records) {
      lastMatches = [];
      listbox.replaceChildren();
      setStatus("Loading catalog…", true);
      input.removeAttribute("aria-activedescendant");
      return;
    }

    if (!tokens.length) {
      lastMatches = [];
      listbox.replaceChildren();
      setStatus("Search " + records.length + " services. Try a name, collection, or capability.", true);
      input.removeAttribute("aria-activedescendant");
      return;
    }

    var matches = search(query);
    lastMatches = matches;
    if (!matches.length) {
      listbox.replaceChildren();
      setStatus("No services match “" + query.trim() + "”.", true);
      input.removeAttribute("aria-activedescendant");
      return;
    }

    var fragment = document.createDocumentFragment();
    for (var i = 0; i < matches.length; i++) {
      var item = matches[i];
      var option = document.createElement("li");
      option.className = "catalog-search__option";
      option.id = optionId(i);
      option.setAttribute("role", "option");
      option.setAttribute("aria-selected", i === 0 ? "true" : "false");

      var primary = document.createElement("a");
      primary.className = "catalog-search__primary";
      primary.href = collectionUrl(item.category);
      primary.tabIndex = -1;

      var name = document.createElement("span");
      name.className = "catalog-search__name";
      name.textContent = item.name;
      primary.appendChild(name);

      var meta = document.createElement("span");
      meta.className = "catalog-search__meta";
      var category = document.createElement("span");
      category.className = "catalog-search__category";
      category.textContent = item.categoryLabel;
      meta.appendChild(category);
      if (item.mcp) {
        var mcp = document.createElement("span");
        mcp.className = "catalog-search__badge";
        mcp.textContent = "MCP";
        meta.appendChild(mcp);
      }
      if (item.urlOnboarding) {
        var urlBadge = document.createElement("span");
        urlBadge.className = "catalog-search__badge catalog-search__badge--star";
        urlBadge.textContent = "URL";
        meta.appendChild(urlBadge);
      }
      primary.appendChild(meta);

      var excerpt = snippet(item.tagline, tokens);
      if (excerpt) {
        var line = document.createElement("span");
        line.className = "catalog-search__snippet";
        line.textContent = excerpt;
        primary.appendChild(line);
      }
      option.appendChild(primary);

      if (item.dossier) {
        var dossier = document.createElement("a");
        dossier.className = "catalog-search__dossier";
        dossier.href = item.dossier;
        dossier.tabIndex = -1;
        dossier.rel = "noopener noreferrer";
        dossier.textContent = "Dossier ↗";
        option.appendChild(dossier);
      }

      fragment.appendChild(option);
    }

    listbox.replaceChildren(fragment);
    setStatus(matches.length + " match" + (matches.length === 1 ? "" : "es"), true);
    status.classList.add("visually-hidden");
    markActive(0);
  }

  function scheduleRender() {
    if (renderFrame) return;
    renderFrame = window.requestAnimationFrame(function () {
      renderFrame = 0;
      render();
    });
  }

  function loadIndex() {
    if (records) return Promise.resolve(records);
    if (loadPromise) return loadPromise;
    loadPromise = fetch(indexUrl, { credentials: "same-origin", cache: "force-cache" })
      .then(function (response) {
        if (!response.ok) throw new Error("Could not load the catalog index.");
        return response.json();
      })
      .then(function (payload) {
        records = prepareIndex(payload);
        loadError = "";
        if (open) scheduleRender();
        return records;
      })
      .catch(function () {
        loadPromise = null;
        loadError = "Catalog search is unavailable.";
        if (open) scheduleRender();
        throw new Error(loadError);
      });
    return loadPromise;
  }

  function openSearch() {
    setExpanded(true);
    input.focus();
    loadIndex().catch(function () {});
    scheduleRender();
  }

  function closeSearch() {
    setExpanded(false);
    listbox.replaceChildren();
    setStatus("", false);
  }

  function isEditable(target) {
    if (!target || target === input) return false;
    var tag = target.tagName;
    if (tag === "INPUT" || tag === "TEXTAREA" || tag === "SELECT") return true;
    return !!target.isContentEditable;
  }

  function activateSelection(event) {
    if (!lastMatches.length) return;
    var item = lastMatches[activeIndex] || lastMatches[0];
    if (!item) return;
    if (event) event.preventDefault();
    window.location.assign(collectionUrl(item.category));
  }

  input.addEventListener("focus", function () {
    openSearch();
  });

  input.addEventListener("input", function () {
    if (!open) setExpanded(true);
    loadIndex().catch(function () {});
    scheduleRender();
  });

  input.addEventListener("keydown", function (event) {
    if (event.key === "Escape") {
      event.preventDefault();
      input.value = "";
      closeSearch();
      input.blur();
      return;
    }
    if (event.key === "ArrowDown") {
      event.preventDefault();
      if (!open) openSearch();
      else markActive(activeIndex + 1);
      return;
    }
    if (event.key === "ArrowUp") {
      event.preventDefault();
      if (!open) openSearch();
      else markActive(activeIndex <= 0 ? 0 : activeIndex - 1);
      return;
    }
    if (event.key === "Enter") {
      if (open && lastMatches.length) activateSelection(event);
    }
  });

  panel.addEventListener("mousedown", function (event) {
    event.preventDefault();
  });

  panel.addEventListener("click", function (event) {
    var dossier = event.target.closest(".catalog-search__dossier");
    if (dossier && dossier.href) {
      event.preventDefault();
      window.open(dossier.href, "_blank", "noopener,noreferrer");
      return;
    }
    var option = event.target.closest(".catalog-search__option");
    if (!option) return;
    var options = listbox.querySelectorAll('[role="option"]');
    for (var i = 0; i < options.length; i++) {
      if (options[i] === option) {
        activeIndex = i;
        activateSelection(event);
        return;
      }
    }
  });

  document.addEventListener("keydown", function (event) {
    if (event.defaultPrevented || event.altKey) return;
    if (isEditable(event.target)) return;
    if (event.key === "/" && !event.metaKey && !event.ctrlKey) {
      event.preventDefault();
      openSearch();
      return;
    }
    if ((event.key === "k" || event.key === "K") && (event.metaKey || event.ctrlKey)) {
      event.preventDefault();
      openSearch();
    }
  });

  document.addEventListener("pointerdown", function (event) {
    if (!open) return;
    if (!root.contains(event.target)) closeSearch();
  });

  if ("requestIdleCallback" in window) {
    window.requestIdleCallback(function () { loadIndex().catch(function () {}); }, { timeout: 2000 });
  } else {
    window.setTimeout(function () { loadIndex().catch(function () {}); }, 1);
  }
})();
