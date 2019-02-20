$(function() {
  $('[data-toggle="tooltip"]').tooltip({ trigger: "manual" }).tooltip("show");
});

$( window ).scroll(function() {
  var el = document.getElementById('bar-wrap');
if(isScrolledIntoView(el)){  // scroll down abit and get the action
$(".progress-bar").each(function() {
  each_bar_width = $(this).attr("aria-valuenow");
  $(this).width(each_bar_width + "%");
})
}});

function isScrolledIntoView(el) {
  var elemTop = el.getBoundingClientRect().top;
  var elemBottom = el.getBoundingClientRect().bottom;

  var isVisible = (elemTop >= 0) && (elemBottom <= window.innerHeight);
  return isVisible;
}
