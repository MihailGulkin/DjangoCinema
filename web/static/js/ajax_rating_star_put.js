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

            },
            error: (err) =>
            {
                // console.log(err)
            }
        })
    }
}
ajax_rating_put()