$(function() {
  $('.scroll-down').click (function() {
    $('html, body').animate({scrollTop: $('#about-me').offset().top }, 'slow');
    return false;
  });
});

$(function() {
  $('.scroll-down-books').click (function() {
    $('html, body').animate({scrollTop: $('#books').offset().top }, 'slow');
    return false;
  });
});


$(function() {
  $('.scroll-down-blog').click (function() {
    $('html, body').animate({scrollTop: $('#blog').offset().top }, 'slow');
    return false;
  });
});
