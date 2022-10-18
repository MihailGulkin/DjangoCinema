`
Ajax like dislike review button
`
function ajax_like_dislike_set_func()
{
    const csrf = $('[name="csrfmiddlewaretoken"]')[0].value
    const btn_s = $('.like_dislike_btn')


    btn_s.each(function ()
    {
        $(this).click(function ()
        {
            const this_ = $(this)
            const pk = this_.parent().attr('data-id')
            const cinema_type = $('#like_dislike_btn_container')

            sendLikeDisData(this_.attr('data-value'), pk, cinema_type.attr('data-type'))
        })
    })
    const sendLikeDisData = (value, review_pk, cinema_type) =>
    {
        $.ajax({
            type: "POST",
            url: '/user_review_like_dislike',
            data: {
                'csrfmiddlewaretoken': csrf,
                value: value,
                pk: review_pk,
                cinema_type: cinema_type
            },
            success: function (resp)
            {
                if (resp.url)
                {
                    window.location = resp.url
                    return
                }

                const btn = $(`#${value.toLowerCase()}_${review_pk}_btn`)

                if (!btn.hasClass('active_btn_status'))
                {
                    $(`#like_${review_pk}_btn`).removeClass('active_btn_status')
                    $(`#dislike_${review_pk}_btn`).removeClass('active_btn_status')

                    const reverse_value = {
                        'Like': 'dislike',
                        'Dislike': 'like'
                    }
                    btn.addClass('active_btn_status')
                    const _span = btn.children('span')

                    if (resp.data.created)
                    {
                        _span.text(`${parseInt(_span.text()) + 1}`)
                    } else
                    {
                        const _rev_btn = $(`#${reverse_value[value]}_${review_pk}_btn`)
                        const _rev_span = _rev_btn.children('span')
                        _rev_span.text(`${parseInt(_rev_span.text()) - 1}`)
                        _span.text(`${parseInt(_span.text()) + 1}`)
                    }
                }


            },
            error: function ()
            {
            }
        });
    }
}
