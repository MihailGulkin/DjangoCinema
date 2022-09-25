function favoriteFilm()
{
    const elems = $('.svg_heart_container')
    const csrf = $('[name="csrfmiddlewaretoken"]')[0].value
    for (let ele of elems)
    {
        $(ele).children('svg').on('click', function (event)
        {
            event.preventDefault()
            sendFavoriteData($(ele).attr('data-value'))
        })
    }
    const sendFavoriteData = (query) =>
    {
        $.ajax({
            type: 'POST',
            url: '/favorite_film',
            data: {
                'csrfmiddlewaretoken': csrf,
                'slug': query
            },
            success: (res) =>
            {
                if (res.url)
                {
                    window.location = res.url
                }
                if (res.dataAdd)
                {
                    for (let ele of $(`.${res.dataAdd.slug}_cls`))
                    {
                        $(ele).children('svg').addClass('favourite_film')
                    }
                }
                if (res.dataRemove)
                {
                    for (let ele of $(`.${res.dataRemove.slug}_cls`))
                    {
                        $(ele).children('svg').removeClass('favourite_film')
                    }

                }
            },
            error: (err) =>
            {
                // console.log(err)
            }
        })
    }
}