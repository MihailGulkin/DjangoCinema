// one_star_container
`
Favorite film/serial heart_svg
`

function ajax_rating_put()
{
    const ele = $('#delete_user_rating')
    if(ele)
    {
         $(ele).on('click', function (event)
        {
            event.preventDefault()
            sendDeleteData($(ele).attr('name'), $(ele).attr('data-type'))
        })
    }

    const sendDeleteData = (cinema_name, type) =>
    {
        $.ajax({
            type: 'POST',
            url: '/delete_user_rating',
            data: {
                'csrfmiddlewaretoken': $('[name="csrfmiddlewaretoken"]')[0].value,
                'name': cinema_name,
                'type':type,

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