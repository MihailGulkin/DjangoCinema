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
            const write_review_block = $('#write_review_user')
            if (!res.data.bool)
            {
                console.log()
                $(write_review_block).before(`
                    <div class="row">
                        <h2 class="mov_rating_text" style="text-align: start">Users Review</h2>
                    </div>
                    <div class="row">
                        <div class="col-md-10 order-md-1 col-sm-12 order-last">
                            <div id="users_review" style="margin-top: 40px">

                            </div>
                        </div>
                        <div class="col-md-2 order-md-1 col-sm-12 order-first" style="margin-top: 40px;">
                        <div style="position: sticky; top: 100px">
                            <h4 data-type="Total" class="mov_rating_text rating_bar_select_cls">
                                Total: ${res.data.calculated.total}
                            </h4>
                            ${generate_html_review_type(res.data.calculated)}
                        </div>
                    </div>
                    </div>
                `)
                select_menu()
            }
            const review_users_block = $('#users_review')
            review_users_block.append(`
                <div data-type="${res.data.review_type}" class="border_style_form user_review_container" style="margin-top: 20px">
                                    <div class="user_info">
                                        <a href="/profile/${res.data.user}">${res.data.user}</a>
                                        <h4 class="mov_rating_text">${res.data.created}</h4>
                                    </div>
                                    <div class="user_review">
                                        <div class="title_form_review_container">
                                            <h4 class="mov_rating_text">${res.data.title}</h4>
                                            <h4 class="mov_rating_text">${res.data.review_type}</h4>
                                        </div>
                                        <div class="text_form_review_container">
                                            <p class="mov_rating_text">${res.data.text}</p>
                                        </div>
                                    </div>
                </div>
            `)
            $(write_review_block).remove()
            console.log(res.data)
        },
        error: (err) =>
        {
        }
    })
}

function generate_html_review_type(calculated)
{
    let html_code = ''
    if (calculated.Positives)
    {
        html_code += `<h4 data-type="Positive" class="mov_rating_text rating_bar_select_cls">
                                Positive: ${calculated.Positives.Positive}</h4>`
    }
    if (calculated.Neutrals)
    {
        html_code += `<h4 data-type="Positive" class="mov_rating_text rating_bar_select_cls">
                                Positive: ${calculated.Neutrals.Neutrals}</h4>`
    }
    if (calculated.Negatives)
    {
        html_code += `<h4 data-type="Positive" class="mov_rating_text rating_bar_select_cls">
                                Positive: ${calculated.Negatives.Negative}</h4>`
    }
    return html_code
}