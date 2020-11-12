$(function() {
  $('.scroll-down').click (function() {
    $('html, body').animate({scrollTop: $('#brands').offset().top }, 'slow');
    return false;
  });
});
