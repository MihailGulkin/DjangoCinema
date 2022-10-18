`
Ajax to edit user review
`
function ajax_edit_review_user_func()
{
    const ele = $('#button_review_send')
    const title_input = $('#input_title')
    const area_review = $('#textarea_form_review')

    $(ele).click(function ()
        {
            $('#area_error').remove()
            $('#title_error').remove()

            if (!$(title_input)[0].checkValidity())
            {
                title_input.after(`
                    <h4 id="title_error" class="error_field">Write on me ↑</h4>
                `)
                return
            }
            if (!area_review[0].checkValidity())
            {
                area_review.after(`
                    <h4 id="area_error" class="error_field">Write on me ↑</h4>
                `)
                return
            }
            const relative_url = window.location.href
            console.log(relative_url)
            sendEditReviewData(relative_url)
        }
    )
    const sendEditReviewData = (url) =>
    {
        $.ajax({
            type: 'POST',
            url: url,
            data: {
                'csrfmiddlewaretoken': $('[name="csrfmiddlewaretoken"]')[0].value,
                'title': $(title_input).val(),
                'review_type': $('#selected_review_type').text(),
                'text_data': $(area_review).val(),
            },

            success: (res) =>
            {
                if (res.url)
                {
                    window.location = res.url
                }
            },
            error: (err) =>
            {
            }
        })
    }

}

ajax_edit_review_user_func()