// 간다GO — lightweight interactions (no dependencies)
(function () {
  "use strict";

  // Mobile nav toggle
  var toggle = document.querySelector(".nav-toggle");
  var links = document.querySelector(".nav-links");
  if (toggle && links) {
    toggle.addEventListener("click", function () {
      var open = links.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    links.addEventListener("click", function (e) {
      if (e.target.tagName === "A") links.classList.remove("open");
    });
  }

  // Fire a lightweight event when the floating call button is tapped
  // (hook point for analytics; the tel: link handles the actual call).
  var call = document.querySelector(".float-call");
  if (call) {
    call.addEventListener("click", function () {
      if (window.dataLayer) window.dataLayer.push({ event: "tap_call" });
    });
  }
})();
