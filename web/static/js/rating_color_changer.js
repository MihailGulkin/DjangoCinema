function rating_color_change()
{
    const select = $('.mov_rating_text')
    const value = $(select).text()
    select.each(function ()
    {
        if (value > 7)
        {
            $(this).css('color', 'rgb(47, 128, 237)')
        } else if (value >= 5)
        {
            $(this).css('color', '#a9b0b0')

        } else
        {
            $(this).css('color', '#a11418')

        }
    })


}

rating_color_change()