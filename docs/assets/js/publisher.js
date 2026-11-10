/*
 * Reserved AdSense placements stay empty unless every gate below is open.
 * publisher-config.json may name a client id for site verification and still
 * fail those gates. This file does not request an ad script unless enabled
 * is true, every reserved slot has an id, consentIntegration names a setup
 * other than "not_configured", and window.agentNativeAdConsent is "granted".
 * No consent popup ships with the site. A certified CMP has to set that
 * consent signal before ads may load for regions that require consent.
 */
(function () {
  "use strict";

  var CLIENT_ID = /^ca-pub-\d{16}$/;
  var SLOT_ID = /^\d{6,20}$/;
  var CONSENT_GRANTED = "granted";

  function slotId(value) {
    if (typeof value === "number" && isFinite(value)) {
      value = String(value);
    }
    return typeof value === "string" && SLOT_ID.test(value) ? value : "";
  }

  function adsMayLoad(config, consent, slotKeys) {
    if (!config || typeof config !== "object" || !config.adsense) return false;
    var adsense = config.adsense;
    if (adsense.enabled !== true) return false;
    if (typeof adsense.clientId !== "string" || !CLIENT_ID.test(adsense.clientId)) return false;
    if (typeof adsense.consentIntegration !== "string") return false;
    if (!adsense.consentIntegration || adsense.consentIntegration === "not_configured") return false;
    if (consent !== CONSENT_GRANTED) return false;
    if (!adsense.slots || typeof adsense.slots !== "object") return false;
    if (!slotKeys || !slotKeys.length) return false;
    for (var i = 0; i < slotKeys.length; i++) {
      if (!slotId(adsense.slots[slotKeys[i]])) return false;
    }
    return true;
  }

  function readConsent() {
    try {
      return window.agentNativeAdConsent === CONSENT_GRANTED ? CONSENT_GRANTED : "";
    } catch (error) {
      return "";
    }
  }

  function reservedSlots() {
    return Array.prototype.slice.call(document.querySelectorAll("[data-ad-slot-key]"));
  }

  function fillSlot(node, clientId, id) {
    var copy = node.querySelector(".ad-reserve__copy");
    if (!copy || !copy.parentNode) return false;
    var ins = document.createElement("ins");
    ins.className = "adsbygoogle";
    ins.setAttribute("data-ad-client", clientId);
    ins.setAttribute("data-ad-slot", id);
    ins.setAttribute("data-ad-format", "horizontal");
    ins.setAttribute("data-full-width-responsive", "false");
    ins.style.display = "block";
    copy.parentNode.replaceChild(ins, copy);
    node.setAttribute("data-ad-state", "loading");
    return true;
  }

  function requestAds(clientId) {
    var script = document.createElement("script");
    script.async = true;
    script.crossOrigin = "anonymous";
    script.src = "https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=" + encodeURIComponent(clientId);
    script.onload = function () {
      var units = document.querySelectorAll(".ad-reserve ins.adsbygoogle");
      for (var i = 0; i < units.length; i++) {
        try {
          (window.adsbygoogle = window.adsbygoogle || []).push({});
        } catch (error) {
          /* A failed unit must not unlock any other request path. */
        }
      }
    };
    document.head.appendChild(script);
  }

  function boot() {
    var holder = document.querySelector("script[data-publisher-config]");
    if (!holder || typeof fetch !== "function") return;
    var url = holder.getAttribute("data-publisher-config");
    if (!url) return;
    var nodes = reservedSlots();
    if (!nodes.length) return;

    fetch(url, { credentials: "same-origin", cache: "no-store" })
      .then(function (response) {
        if (!response.ok) throw new Error("config");
        return response.json();
      })
      .then(function (config) {
        var keys = nodes.map(function (node) {
          return node.getAttribute("data-ad-slot-key") || "";
        });
        if (!adsMayLoad(config, readConsent(), keys)) return;
        var clientId = config.adsense.clientId;
        var filled = 0;
        for (var i = 0; i < nodes.length; i++) {
          var id = slotId(config.adsense.slots[keys[i]]);
          if (id && fillSlot(nodes[i], clientId, id)) filled += 1;
        }
        if (filled) requestAds(clientId);
      })
      .catch(function () {
        /* Advertising stays on the reserved placeholder. */
      });
  }

  if (typeof document === "undefined") return;
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();
