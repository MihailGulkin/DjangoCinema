`
Delete user Rating button click
`

function ajax_delete_rating()
{
    const ele = $('#delete_user_rating')
    if (ele)
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
                'type': type,

            },
            success: (res) =>
            {
                $('#user_rating').html('')

                const rating = $('#true_rating_cinema')
                rating.attr('name', `${rating.text()}`)

                colors.number = colors._get_two_numbers(rating.attr('name'))
                colors.star_fill_change()

            },
            error: (err) =>
            {
                // console.log(err)
            }
        })
    }
}

ajax_delete_rating()