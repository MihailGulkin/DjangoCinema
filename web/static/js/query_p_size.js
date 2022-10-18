`
Change p size text when width height change
`
function start()
{

    const array_content_p = []

    const selector_p = $('.card_content_p')

    for (let ele of selector_p)
    {
        array_content_p.push(ele.innerText)
    }

    function set_text(number_word)
    {
        selector_p.each(function (i)
            {
                $(this).text((number_word !== 100) ?
                    `${array_content_p[i].substring(0, number_word)}...»` : `${array_content_p[i]}`)
            }
        )
    }

    const mediaQuery_320 = window.matchMedia('(max-width: 320px)')
    const mediaQuery_500 = window.matchMedia('(max-width:500px)')
    const mediaQuery_1024 = window.matchMedia('(min-width:500px) and (max-width: 1400px)')
    const mediaQuery_more_than_1400 = window.matchMedia('(min-width: 1400px)')

    if (window.screen.width <= 320)
    {

        set_text(15)
    } else if (320 < window.screen.width && window.screen.width <= 500)
    {
        set_text(25)
    } else if (500 < window.screen.width && window.screen.width <= 1400)
    {
        set_text(50)
    } else if (window.screen.width > 1400)
    {
        set_text(100)
    }

    mediaQuery_320.addListener(function (e)
    {
        if (e.matches)
        {
            set_text(15)
        } else
        {
            set_text(25)

        }
    })
    mediaQuery_500.addListener(function (e)
    {
        if(e.matches)
        {
            set_text(25)
        }
    })
    mediaQuery_1024.addListener(function (e)
    {

        if (e.matches)
        {
            set_text(50)
        }
    })
    mediaQuery_more_than_1400.addListener(function (e)
    {
        if (e.matches)
        {
            set_text(100)
        }
    })
}

start()