`
Add header bottom line when user scroll it
`
function add_header_line()
{
    $(document).ready(function ()
    {
        __add_style()

        $(window).on('scroll', function ()
        {
            __add_style()
        });
    })

    function __add_style()
    {
        if ($(window).scrollTop() > 0)
        {
            $('.header--fixed').addClass('header--active');
        } else
        {
            $('.header--fixed').removeClass('header--active');
        }
    }

}
add_header_line()