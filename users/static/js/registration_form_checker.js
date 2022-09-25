function form_validation_check()
{
    const sendRegData = () =>
    {
        $.ajax({
            type: 'POST',
            url: '/register/',
            data: get_data(),

            success: (res) =>
            {
                $('#error_username').remove()
                $('#error_email').remove()
                $('#error_pwd2').remove()

                $(username).attr('data-value', true)
                $(email).attr('data-value', true)
                $(pwd2).attr('data-value', true)

                if (res.errors.username !== undefined)
                {
                    $(username).after(`<h4 class="error_field" id="error_username">${res.errors.username}</h4>
                         `)
                    $(username).attr('data-value', false)

                }
                if (res.errors.email !== undefined)
                {
                    $(email).after(
                        `<h4 class="error_field" id="error_email">${res.errors.email}</h4>`
                    )
                    $(email).attr('data-value', false)
                }
                if (res.errors.password2 !== undefined)
                {
                    $(pwd2).after(
                        `<h4 class="error_field" id="error_pwd2">${res.errors.password2}</h4>`
                    )
                    $(pwd2).attr('data-value', false)
                }
                errors_check()
            },
            error: (err) =>
            {
            }
        })
    }

    const box_form = $('.form_input_reg')

    const username = $('#username_reg')
    const email = $('#email_reg')
    const pwd1 = $('#pwd1_reg')
    const pwd2 = $('#pwd2_reg')


    for (let ele of box_form)
    {
        $(ele).keyup(function ()
            {
                sendRegData()
            }
        )
    }

    function set_regex_on_input()
    {
        $(username).on('input', function ()
        {
            if (!(/[A-Za-z\d]/.test($(username).val().at(-1))))
            {
                $(username).val($(username).val().substring(0, $(username).val().length - 1))
            }
        })
    }

    function get_data()
    {
        return {
            'csrfmiddlewaretoken': document.getElementsByName('csrfmiddlewaretoken')[0].value,
            'username': $(username).val(),
            'email': $(email).val(),
            'password1': $(pwd1).val(),
            'password2': $(pwd2).val()
        }
    }

    function errors_check()
    {

        if (check_data_value() && check_value_fill())
        {
            $('#submit_btn').removeClass('disable_btn')
        } else
        {
            $('#submit_btn').addClass('disable_btn')

        }

        function check_value_fill()
        {
            const temp = Array()
            for (let ele of box_form)
            {
                temp.push(!!$(ele).val())
            }
            return temp.every(function (value)
            {
                return value
            })
        }

        function check_data_value()
        {
            return parse_string_boolean(username.attr('data-value')) &&
                parse_string_boolean(email.attr('data-value')) &&
                parse_string_boolean(pwd2.attr('data-value'))

            function parse_string_boolean(element)
            {
                return element !== 'false'
            }
        }
    }

    set_regex_on_input()
}

form_validation_check()

