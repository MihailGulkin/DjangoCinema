`
Ajax function to change username in profile
`
function ajax_change_username_func()
{
    const ele = $('#change_btn')
    const title_input = $('#username_log')

    ele.click(function ()
        {
            $('#username_error').remove()

            if (!$(title_input)[0].checkValidity())
            {
                title_input.after(`
                    <h4 id="username_error" class="error_field">Write on me ↑</h4>
                `)
                return
            }
            sendChangeData(title_input.val())
        }
    )
    const sendChangeData = (username) =>
    {
        $.ajax({
            type: 'POST',
            url: '/change_username_user/',
            data: {
                'username': username,
                'csrfmiddlewaretoken': $('[name="csrfmiddlewaretoken"]')[0].value,
            },

            success: (res) =>
            {
                $('#username_error').remove()

                if (res.data.url)
                {
                    window.location = res.data.url
                    return
                }
                if (res.data.error)
                {
                    title_input.after(`
                    <h4 id="username_error" class="error_field">${res.data.error}</h4>
                            `)
                }

            },
            error: (err) =>
            {
            }
        })
    }
}

ajax_change_username_func()