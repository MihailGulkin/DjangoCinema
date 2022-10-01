// one_star_container
`
Ajax rating put film/serial
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
                if (res.data)
                {
                    colors.number = {
                        integer: parseInt(res.data.rating),
                        fraction: 0,
                    }
                    colors.star_fill_change()
                    const ele = $('#user_rating')
                    if ($(ele).length)
                    {
                        $(ele).html('')
                        $(ele).append(`
                            ${generate_html_rating_code(res)}
                        `
                        )
                    } else
                    {
                        $('#cinema_bar_rating_system').after(`
                        <div class="d-flex flex-column" id="user_rating">
                            ${generate_html_rating_code(res)} 
                        </div>`)
                    }
                    rating_color_change()
                    ajax_delete_rating()

                }
            },
            error: (err) =>
            {
                // console.log(err)
            }
        })
    }
}

function generate_html_rating_code(res)
{
    return `<div class="d-flex justify-content-start align-content-center align-items-center">
                                <h4 class="m-0 mov_rating_text font_class_style_rating">Your evaluation </h4>
                                <p class="m-0 rating_cinema_color font_class_style_rating">${res.data.rating}</p>
                                <a name="${res.data.name}" id="delete_user_rating" data-type="${res.data.type}"
                                    class="font_class_style_rating mov_rating_text" href="">Delete</a>
                            </div>
                            <p class="font_class_style_rating time_styles mov_rating_text">${res.data.create}</p>`
}

ajax_rating_put()