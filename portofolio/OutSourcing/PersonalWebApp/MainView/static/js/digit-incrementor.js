$(document).ready(function () {

    var counters = document.querySelectorAll('span.counter'),
      len =  counters.length,
      duration = 15000;

    $.extend($.easing, {

    easing: function (x, t, b, c, d) {
      return (t === d) ? b + c : c * (-Math.pow(2, -10 * t / d) + 1) + b;
    }
    });

    function animate() {
        var x, number;

        if (len !== 0) {
          len -= 1;
        }

        x = counters[len];
        number = 'number' + len;

        $(counters[len]).animate({opacity : 1}, {
          duration: duration,
          fade: true,
          easing: 'linear'
    });

    $({number: counters[len].getAttribute('data-from')}).animate({number: counters[len].getAttribute('data-to')}, {
      duration: duration,
      easing: 'easing',
      fade: true,
      queue: false,
      step: function (a) {
        a = Math.round(a);
        a = String(a);
        a = a.replace(/(\d)(?=(\d\d\d)+([^\d]|$))/g, '$1 ');

        $(x).html(a);
      }
    });
}

    function showAnimation() {

        var i;

        for (i = 0; i < 3; i += 1) {
          animate(i);
        }
    }

  showAnimation();
});
