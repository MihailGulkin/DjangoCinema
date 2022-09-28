`
Later film/serial bookmark_svg
`
function ajax_lateFilm()
{
    const elems = $('.svg_bookmark_container')
    for (let ele of elems)
    {
        $(ele).children('svg').on('click', function (event)
        {
            event.preventDefault()
            sendLaterData($(ele).attr('data-value'), $(ele).attr('data-value-type'))
        })
    }
    const sendLaterData = (query, cinema_type) =>
    {
        $.ajax({
            type: 'POST',
            url: '/later_film',
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
                    for (let ele of $(`.${res.dataAdd.slug}_cls_bookmark`))
                    {
                        $(ele).children('svg').addClass('later_film')
                    }
                }
                if (res.dataRemove)
                {
                    for (let ele of $(`.${res.dataRemove.slug}_cls_bookmark`))
                    {
                        $(ele).children('svg').removeClass('later_film')
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