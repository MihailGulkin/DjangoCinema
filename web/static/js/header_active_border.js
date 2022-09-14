$(document).ready(function ()
{

    $(window).on('scroll', function ()
    {
        if ($(window).scrollTop() > 0)
        {
            $('.header--fixed').addClass('header--active');
        } else
        {
            $('.header--fixed').removeClass('header--active');
        }
    });
})
