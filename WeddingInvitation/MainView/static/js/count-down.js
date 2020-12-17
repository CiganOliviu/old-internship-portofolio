const second = 1000,
      minute = second * 60,
      hour = minute * 60,
      day = hour * 24;

let countDown = new Date('Nov 12, 2027 00:00:00').getTime(),
    x = setInterval(function() {

      let now = new Date().getTime(),
          distance = countDown - now;

        document.getElementById('Days').innerText = Math.floor(distance / (day)),
        document.getElementById('Hours').innerText = Math.floor((distance % (day)) / (hour)),
        document.getElementById('Minutes').innerText = Math.floor((distance % (hour)) / (minute)),
        document.getElementById('Seconds').innerText = Math.floor((distance % (minute)) / second);

    }, second)
