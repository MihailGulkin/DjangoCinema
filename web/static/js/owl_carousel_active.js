$("#movie_slider").owlCarousel(
    {
        loop: true,
        margin: 30,
        nav: true,
        slideBy: 2,
        dots: false,
        navText: ["<div class='nav-btn prev-slide'></div>", "<div class='nav-btn next-slide'></div>"],
        responsive: {
            0: {
                items: 2,
                nav: false,
            },
            500:
                {
                    items: 2,
                    nav: false,
                },
            768: {
                items: 3,
                nav: false,
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
        slideBy: 2,
        dots: false,
        navText: ["<div class='nav-btn prev-slide'></div>", "<div class='nav-btn next-slide'></div>"],
        responsive: {
            0: {
                items: 2,
                nav: false,
            },
            500:
                {
                    items: 2,
                    nav: false,
                },
            768: {
                items: 3,
                nav: false,
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