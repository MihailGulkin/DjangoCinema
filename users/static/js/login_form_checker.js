function form_validation_check()
{
    const sendLoginData = () =>
    {
        $.ajax({
            type: 'POST',
            url: '/login/',
            data: get_data(),

            success: (res) =>
            {
                $('#error_username').remove()
                $('#error_pwd').remove()
                $('#error_all').remove()

                if (res.errors)
                {

                    if (res.errors.username !== undefined)
                    {
                        $(username).after(`<h4 class="error_field" id="error_username">${res.errors.username}</h4>
                         `)

                    }
                    if (res.errors.password !== undefined)
                    {
                        $(pwd).after(
                            `<h4 class="error_field" id="error_pwd">${res.errors.password}</h4>`
                        )
                    }
                    if (res.errors.__all__ !== undefined)
                    {
                        $(pwd).after(`<h4 class="error_field" id="error_all">${res.errors.__all__}</h4>
                         `)
                    }

                } else
                {
                    window.location = res.url
                }

            },
            error: (err) =>
            {
            }
        })
    }


    const username = $('#email_log')
    const pwd = $('#pwd_log')

    const btn = $('#login_btn')

    $(username).on('input', function ()
    {
        $('#error_username').remove()
        $('#error_all').remove()

    })
    $(pwd).on('input', function ()
    {
        $('#error_pwd').remove()
        $('#error_all').remove()

    })

    $(btn).click(function ()
    {
        sendLoginData()
    })

    function get_data()
    {
        return {
            'csrfmiddlewaretoken': document.getElementsByName('csrfmiddlewaretoken')[0].value,
            'username': $(username).val(),
            'password': $(pwd).val()
        }
    }
}

form_validation_check()

