// Mobile navigation toggle. The site works without JavaScript; this only
// opens/closes the mobile menu and closes it after a link is followed.
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
