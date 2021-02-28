$(document).ready(function () {

    $(window).scroll(function () {

        const height = $('.newsletter_parallax').height() / 2;
        const scrollTop = $(window).scrollTop();

        if ($(document).width() >= 800) {

            if (scrollTop >= height - 40)
                $('.nav-container').addClass('solid-nav');
            else
                $('.nav-container').removeClass('solid-nav');
        }
    });
});