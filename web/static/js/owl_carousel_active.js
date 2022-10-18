`
Active owl carousel slider for movie and serial
`
$("#movie_slider").owlCarousel(
    {
        loop: true,
        margin: 30,
        nav: true,
        autoplay: true,
        autoplayHoverPause: true,
        slideBy: 2,
        dots: false,
        navText: ["<div class='nav-btn prev-slide'></div>", "<div class='nav-btn next-slide'></div>"],
        responsive: {
            0: {
                items: 2,
                nav: false,
                dots: true,
            },
            500:
                {
                    items: 2,
                    nav: false,
                    dots: true,

                },
            768: {
                items: 3,
                nav: false,
                dots: true,

            },
            1000: {
                items: 4,

            },
            1440: {
                items: 5,

            },
        },
    }
);
$("#serial_slider").owlCarousel(
    {
        loop: true,
        margin: 30,
        nav: true,
        autoplay: true,
        autoplayHoverPause: true,
        slideBy: 2,
        dots: false,
        navText: ["<div class='nav-btn prev-slide'></div>", "<div class='nav-btn next-slide'></div>"],
        responsive: {
            0: {
                items: 2,
                nav: false,
                dots: true,
            },
            500:
                {
                    items: 2,
                    nav: false,
                    dots: true,

                },
            768: {
                items: 3,
                nav: false,
                dots: true,

            },
            1000: {
                items: 4,

            },
            1440: {
                items: 5,

            },
        },
    }
);