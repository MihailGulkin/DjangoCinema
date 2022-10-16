function ajax_review_user_func()
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
            const relative_url = $('#form_view_submit').attr('name')
            const _type = $('#button_review_send').attr('data-cinema-type')
            sendReviewData(_type, relative_url)
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
                if (res.url)
                {
                    window.location = res.url
                    return
                }
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
                                            <a class="mov_rating_text" href="/profile/${res.data.user}">${res.data.user}</a>
                                            <h6 class="mov_rating_text text-start">${res.data.count_review} Reviews</h6>
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
                                        <div id="like_dislike_btn_container" data-type="${review_type}" class="d-flex" data-id="${res.data.pk}">
                                            <button id="like_${res.data.pk}_btn" data-value="Like" type="button"
                                                    class="like_dislike_btn m-left">
                                                <svg class="like_dislike_svg like_svg"
                                                     version="1.1" id="Capa_1"
                                                     xmlns="http://www.w3.org/2000/svg"
                                                     xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
                                                     viewBox="0 0 58 58" style="enable-background:new 0 0 58 58;"
                                                     xml:space="preserve">
                                                                                <g>
                                                                                    <path d="M9.5,43c-2.757,0-5,2.243-5,5s2.243,5,5,5s5-2.243,5-5S12.257,43,9.5,43z"/>
                                                                                    <path d="M56.5,35c0-2.495-1.375-3.662-2.715-4.233C54.835,29.85,55.5,28.501,55.5,27c0-2.757-2.243-5-5-5H36.134l0.729-3.41
                                                                                        c0.973-4.549,0.334-9.716,0.116-11.191C36.461,3.906,33.372,0,30.013,0h-0.239C28.178,0,25.5,0.909,25.5,7c0,14.821-6.687,15-7,15
                                                                                        h0h-1v-2h-16v38h16v-2h28c2.757,0,5-2.243,5-5c0-1.164-0.4-2.236-1.069-3.087C51.745,47.476,53.5,45.439,53.5,43
                                                                                        c0-1.164-0.4-2.236-1.069-3.087C54.745,39.476,56.5,37.439,56.5,35z M3.5,56V22h12v34H3.5z"/>
                                                                                </g>
                                                                                </svg>
                                                Useful
                                                <span class="number_btn_like_dis">0</span>
                                            </button>
                                            <button id="dislike_${res.data.pk}_btn" data-value="Dislike"
                                                type="button"
                                                class="like_dislike_btn">
                                                <svg class="like_dislike_svg dislike_svg" version="1.1" id="Capa_1"
                                                     xmlns="http://www.w3.org/2000/svg"
                                                     xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
                                                     viewBox="0 0 58 58" style="enable-background:new 0 0 58 58;"
                                                     xml:space="preserve">
                                                                                <g>
                                                                                    <path d="M40.5,0v2h-28c-2.757,0-5,2.243-5,5c0,1.164,0.4,2.236,1.069,3.087C6.255,10.524,4.5,12.561,4.5,15
                                                                                        c0,1.164,0.4,2.236,1.069,3.087C3.255,18.524,1.5,20.561,1.5,23c0,2.495,1.375,3.662,2.715,4.233C3.165,28.15,2.5,29.499,2.5,31
                                                                                        c0,2.757,2.243,5,5,5h14.366l-0.729,3.41c-0.973,4.551-0.334,9.717-0.116,11.191C21.539,54.094,24.628,58,27.987,58h0.239
                                                                                        c1.596,0,4.274-0.909,4.274-7c0-14.82,6.686-15,7-15h0h1v2h16V0H40.5z M54.5,36h-12V2h12V36z"/>
                                                                                    <path d="M48.5,15c2.757,0,5-2.243,5-5s-2.243-5-5-5s-5,2.243-5,5S45.743,15,48.5,15z"/>
                                                                                </g>
                                                                                </svg>
                                                Unuseful
                                                <span class="number_btn_like_dis">0</span>
                                            </button>
                                        </div>
                                    </div>
                                </div>
            `)

                $(write_review_block).remove()
                open_all_reviews()
                filtering_data_review_func()
                ajax_like_dislike_set_func()

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
}