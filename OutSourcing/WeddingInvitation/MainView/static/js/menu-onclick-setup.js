var counter = 0;

function SetActivityIfOddCounter(counter) {

  if (counter % 2 == 1) {

    $('label a').removeClass('deactivate-click');
    $('label a').addClass('activate-click');
  }
}

function SetActivityIfEvenCounter() {

  if (counter % 2 == 0) {

    $('label a').removeClass('activate-click');
    $('label a').addClass('deactivate-click');
  }
}

$(document).ready(function() {
    $('label .menu ').click(function() {

        counter++;

        SetActivityIfOddCounter(counter);
        SetActivityIfEvenCounter(counter);
    });
});
