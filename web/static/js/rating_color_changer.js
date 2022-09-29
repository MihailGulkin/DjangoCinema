function rating_color_change()
{
    const select = $('.rating_cinema_color')
    select.each(function ()
    {
        const value = $(this).text()
        if (value >= 7)
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