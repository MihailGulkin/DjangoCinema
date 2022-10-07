function change_p_size()
{
    set_rating_font_size()
    window.addEventListener('resize', function ()
    {
        set_rating_font_size()
    })


}

function set_rating_font_size()
{
    $('#true_rating_cinema').css('font-size', '0').css('font-size',
        `${$('.many_star_container').first().height() - 5}px`)
}

change_p_size()