function change_p_size()
{
    set_rating_font_size()
    window.addEventListener('resize', function (event)
    {
        set_rating_font_size()
    })

    function set_rating_font_size()
    {
        $('.mov_rating_text').css('font-size', '0').css("font-size",
            `${$('.one_star_container').first().height() - 5}`)
    }
}

change_p_size()