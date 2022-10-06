const ele = $('#button_review_send')
const title_input = $('#input_title')
const area_review = $('#textarea_form_review')

$(ele).click(function ()
    {
        if ($(title_input)[0].checkValidity() && $(area_review)[0].checkValidity())
        {
            const relative_url = $('#form_view_submit').attr('name')
            const _type = $('#button_review_send').attr('data-cinema-type')
            sendReviewData(_type, relative_url)
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
                $(write_review_block).before(`
                    <div class="row m-20px">
                        <h2 class="mov_rating_text text-start">Users Review</h2>
                    </div>
                    <div class="row">
                        <div class="col-md-10 order-md-1 col-sm-12 order-last">
                            <div id="users_review" class="m-20px">

                            </div>
                        </div>
                        <div class="col-md-2 order-md-1 col-sm-12 order-first m-20px">
                            <div id="review_type_block">
                                 <div data-type="Total"
                                                 class="rating_bar_select_total rating_bar_select_cls active_rating_bar_block">
                                    <h1>${res.data.calculated.total}</h1>
                                    <h4 class="total_text">Total</h4>
                                 </div>
                                ${generate_html_review_type(res.data.calculated)}                                                                                
                            </div>
                        </div>
                    </div>
                `)
            } else
            {

                $('#review_type_block').html('').append(`
                 <div data-type="Total"
                                 class="rating_bar_select_total rating_bar_select_cls active_rating_bar_block">
                    <h1>${res.data.calculated.total}</h1>
                    <h4 class="total_text">Total</h4>
                 </div>
                 ${generate_html_review_type(res.data.calculated)}
                                `)
            }
            const review_users_block = $('#users_review')
            review_users_block.append(`
                <div data-type="${res.data.review_type}"
                                     class="border_style_form user_review_container ${res.data.review_type.toLowerCase()}_border m-20px">
                                    <div class="${res.data.review_type.toLowerCase()}_user_bottom user_info d-flex">
                                        <div>
                                            <a href="/profile/${res.data.user}">${res.data.user}</a>
                                        </div>
                                        <div class="created_review_date">
                                            <p class="mov_rating_text">${res.data.created}</p>
                                        </div>
                                    </div>
                                    <div class="user_review title_form_review_container">
                                        <h4 class="mov_rating_text text-start">${res.data.title}</h4>
                                        <div class="content-block-text">
                                            <p class="mov_rating_text text-start">${res.data.text}</p>
                                        </div>
                                        <div class="show-all-container">
                                            <button class="show-all">Show all review</button>
                                        </div>
                                    </div>
                                </div>
            `)

            $(write_review_block).remove()
            btn_text_open_active()
            filtering_data_review_func()
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
        html_code += `<div data-type="Positive" class=" rating_bar_select_cls">
                                    <div class="d-flex align-content-center align-items-end">
                                        <h1 class="m-0 positive_rating_bar">${calculated.Positives.Positive}</h1>
                                        <h6 class="percent_style">${calculated.Positives.total}%</h6>
                                    </div>
                                    <h4 class="text-start">Positives</h4>
                                </div>`
    }
    if (calculated.Neutrals)
    {
        html_code += ` <div data-type="Neutral" class=" rating_bar_select_cls">
                                    <div class="d-flex align-content-center align-items-end">
                                        <h1 class="m-0 neutral_rating_bar">${calculated.Neutrals.Neutral}</h1>
                                        <h6 class="percent_style">${calculated.Neutrals.total}%</h6>
                                    </div>
                                    <h4 class="text-start">Neutrals</h4>
                                </div>`
    }
    if (calculated.Negatives)
    {
        html_code += ` <div data-type="Negative" class=" rating_bar_select_cls">
                                    <div class="d-flex align-content-center align-items-end">
                                        <h1 class="m-0 negative_rating_bar">${calculated.Negatives.Negative}</h1>
                                        <h6 class="percent_style">${calculated.Negatives.total}%</h6>
                                    </div>
                                    <h4 class="text-start">Negatives</h4>
                                </div>`
    }
    return html_code
}