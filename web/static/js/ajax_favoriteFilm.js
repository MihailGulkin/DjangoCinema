`
Favorite film/serial heart_svg
`
function ajax_favoriteFilm()
{
    const elems = $('.svg_heart_container')
    for (let ele of elems)
    {
        $(ele).children('svg').on('click', function (event)
        {
            event.preventDefault()
            sendFavoriteData($(ele).attr('data-value'), $(ele).attr('data-value-type'))
        })
    }
    const sendFavoriteData = (query, cinema_type) =>
    {
        $.ajax({
            type: 'POST',
            url: '/favorite_film',
            data: {
                'csrfmiddlewaretoken': $('[name="csrfmiddlewaretoken"]')[0].value,
                'slug': query,
                'cinema_type': cinema_type,
            },
            success: (res) =>
            {
                if (res.url)
                {
                    window.location = res.url
                }
                if (res.dataAdd)
                {
                    for (let ele of $(`.${res.dataAdd.slug}_cls_favorite`))
                    {
                        $(ele).children('svg').addClass('favourite_film')
                    }
                }
                if (res.dataRemove)
                {
                    for (let ele of $(`.${res.dataRemove.slug}_cls_favorite`))
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
