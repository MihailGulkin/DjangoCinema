// one_star_container
`
Favorite film/serial heart_svg
`

function ajax_rating_put()
{
    const elems = $('.one_star_container')
    for (let ele of elems)
    {
        $(ele).on('click', function (event)
        {
            const relative_url = window.location.href.substring(window.location.origin.length)
            const user_rating = $(ele).attr('name')
            sendRatingData(relative_url, user_rating)
        })
    }
    const sendRatingData = (url, user_rating) =>
    {
        $.ajax({
            type: 'POST',
            url: url,
            data: {
                'csrfmiddlewaretoken': $('[name="csrfmiddlewaretoken"]')[0].value,
                'rating': user_rating

            },
            success: (res) =>
            {
                if (res.url)
                {
                    window.location = res.url

                }
                if (res.rating)
                {
                    colors.number = {
                        integer: parseInt(res.rating),
                        fraction: 0,
                    }
                    colors.star_fill_change()
                    const ele = $('#user_rating')
                    if ($(ele).length)
                    {
                        $(ele).html('')
                        $(ele).append(`
                        <h4 class="my-5 mov_rating_text">Your evaluation <span class="rating_cinema_color">${res.rating}</span></h4>
                        `
                        )
                    } else
                    {
                        $('#cinema_bar_rating_system').after(`
                        <div class="d-flex justify-content-start" id="user_rating">
                            <h2 class="mov_rating_text">Your evaluation<span class="rating_cinema_color">${res.rating}</h2>
                        </div>`)
                    }
                    rating_color_change()

                }
            },
            error: (err) =>
            {
                // console.log(err)
            }
        })
    }
}

ajax_rating_put()