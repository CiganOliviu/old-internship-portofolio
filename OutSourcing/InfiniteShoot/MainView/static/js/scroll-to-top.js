const btn = $('#button-to-top');

$(window).scroll(function() {
  if ($(window).scrollTop() > 300) {
    btn.addClass('show');
  } else {
    btn.removeClass('show');
  }
});

btn.on('click', function(event) {
  event.preventDefault();
  $('html, body').animate({scrollTop:0}, '300');
});
