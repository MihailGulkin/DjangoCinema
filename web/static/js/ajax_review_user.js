const ele = $('#button_review_send')
const title_input = $('#input_title')
const area_review = $('#textarea_form_review')

$(ele).click(function ()
    {
        if ($(title_input)[0].checkValidity() && $(area_review)[0].checkValidity())
        {
            const relative_url = $('#form_view_submit').attr('name')
            sendReviewData('cinema', relative_url)
        }
    }
)
const sendReviewData = (review_type, slug) =>
{
    $.ajax({
        type: 'POST',
        url: '/review_user_send',
        data: {
            'type': review_type,
            'csrfmiddlewaretoken': $('[name="csrfmiddlewaretoken"]')[0].value,
            'title': $(title_input).val(),
            'review_type': $('#selected_review_type').text(),
            'text_data': $(area_review).val(),
            'slug': slug
        },

        success: (res) =>
        {
            const review_users_block = $('#users_review')
            review_users_block.append(`
                <div class="border_style_form" style="margin-top: 20px">
                                    <div class="user_info">
                                        <a href="/profile/${res.data.user}">${res.data.user}</a>
                                        <h4 class="mov_rating_text">${ res.data.created }</h4>
                                    </div>
                                    <div class="user_review">
                                        <div class="title_form_review_container">
                                            <h4 class="mov_rating_text">${res.data.title}</h4>
                                            <h4 class="mov_rating_text">${ res.data.review_type }</h4>
                                        </div>
                                        <div class="text_form_review_container">
                                            <p class="mov_rating_text">${ res.data.text }</p>
                                        </div>
                                    </div>
                </div>
            `)
            const review_send_block = $('#write_review_user')
            $(review_send_block).remove()
            console.log(res.data)
        },
        error: (err) =>
        {
        }
    })
}
