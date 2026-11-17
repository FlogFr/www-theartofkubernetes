// The site works without JavaScript. This file only enhances it:
// 1. the mobile menu toggle;
// 2. the look of the Sender.net embedded forms (newsletter, contact).

// ---- 1. Mobile navigation ---------------------------------------------------
// Opens/closes the mobile menu and closes it after a link is followed.
(function () {
  var toggle = document.querySelector("[data-menu-toggle]");
  var menu = document.getElementById("menu-mobile");
  if (!toggle || !menu) return;

  function setOpen(open) {
    toggle.setAttribute("aria-expanded", open ? "true" : "false");
    toggle.classList.toggle("menu-is-open", open);
    menu.classList.toggle("hidden", !open);
  }

  toggle.addEventListener("click", function () {
    setOpen(toggle.getAttribute("aria-expanded") !== "true");
  });
  menu.querySelectorAll("[data-menu-link]").forEach(function (link) {
    link.addEventListener("click", function () { setOpen(false); });
  });
  document.addEventListener("keydown", function (event) {
    if (event.key === "Escape") setOpen(false);
  });
})();

// ---- 2. Sender.net embedded forms --------------------------------------------
// Sender's universal.js (loaded by base.html) renders each form in an about:blank
// iframe written by the page, so the iframe is same-origin and can be styled:
// we load assets/css/sender-forms.css inside it (site fonts and colours), make it
// fluid, keep its height in sync with the form and improve the fields:
//   - a message field becomes a multi-line <textarea> (same name: Sender's
//     serializer and validator read any [name] / textarea);
//   - labels are tied to their field, and email/name fields allow autofill.
// The form is hidden from the moment Sender inserts it until the stylesheet is
// loaded ("sender-styling" class, before the first paint), and always revealed,
// even if the stylesheet fails. Texts and fields are set in Sender, not here.
(function () {
  var containers = document.querySelectorAll(".sender-form-field[data-sender-form-id]");
  if (!containers.length || !window.MutationObserver) return;
  var STYLESHEET = "/theme/assets/css/sender-forms.css";
  var AUTOCOMPLETE = { email: "email", firstname: "given-name", lastname: "family-name" };

  function reveal(container) {
    container.classList.remove("sender-styling");
  }

  function improveFields(doc, formId) {
    var message = doc.querySelector('input.sender-form-input[type="text"][name*="message" i]');
    if (message) {
      var area = doc.createElement("textarea");
      Array.prototype.forEach.call(message.attributes, function (attr) {
        if (attr.name !== "type" && attr.name !== "value") area.setAttribute(attr.name, attr.value);
      });
      area.rows = 5;
      message.parentNode.replaceChild(area, message);
    }
    doc.querySelectorAll(".sender-form-inputs .sender-form-field").forEach(function (field, i) {
      var label = field.querySelector("label.sender-form-label");
      var input = field.querySelector("input, textarea, select");
      if (!label || !input) return;
      input.id = input.id || "sender-" + formId + "-" + i;
      label.htmlFor = input.id;
      if (AUTOCOMPLETE[input.name]) input.setAttribute("autocomplete", AUTOCOMPLETE[input.name]);
    });
  }

  function style(container) {
    var iframe = container.querySelector("iframe");
    if (!iframe || iframe.hasAttribute("data-styled")) return;
    var doc, form;
    try {
      doc = iframe.contentDocument;
      form = doc && doc.querySelector("form");
    } catch (e) {
      reveal(container);
      return;
    }
    if (!form) return;
    iframe.setAttribute("data-styled", "");
    container.classList.add("sender-styling");
    setTimeout(function () { reveal(container); }, 3000);
    doc.documentElement.lang = document.documentElement.lang;
    improveFields(doc, container.getAttribute("data-sender-form-id"));

    function fit() {
      var height = form.getBoundingClientRect().height;
      if (height) iframe.style.height = Math.ceil(height) + "px";
    }
    function done() {
      container.classList.add("sender-styled");
      fit();
      reveal(container);
    }
    var link = doc.createElement("link");
    link.rel = "stylesheet";
    link.href = STYLESHEET;
    link.onload = done;
    link.onerror = function () { reveal(container); };
    doc.body.appendChild(link);
    // Follow the form's height (validation errors, success message, web fonts).
    if (iframe.contentWindow.ResizeObserver) new iframe.contentWindow.ResizeObserver(fit).observe(form);
    if (doc.fonts && doc.fonts.ready) doc.fonts.ready.then(fit);
  }

  containers.forEach(function (container) {
    style(container);
    new MutationObserver(function () { style(container); })
      .observe(container, { childList: true, subtree: true });
  });
})();
