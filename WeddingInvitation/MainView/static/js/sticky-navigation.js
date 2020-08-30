// Sticky Header
$(window).scroll(function() {
  if ($(window).scrollTop() > 12) {
    $(".header").addClass("sticky");
  } else {
    $(".header").removeClass("sticky");
  }
});

// Mobile Navigation
$(".mobile-toggle").click(function() {
  if ($(".header").hasClass("open-nav")) {
    $(".header").removeClass("open-nav");
  } else {
    $(".header").addClass("open-nav");
  }
});

$(".header li a").click(function() {
  if ($(".header").hasClass("open-nav")) {
    $(".navigation").removeClass("open-nav");
    $(".header").removeClass("open-nav");
  }
});

// Navigation Scroll
$("nav a").click(function(event) {
  var id = $(this).attr("href");
  var offset = 70;
  var target = $(id).offset().top - offset;
  $("html, body").animate(
    {
      scrollTop: target
    },
    500
  );
  event.preventDefault();
});
