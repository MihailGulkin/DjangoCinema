`
Ajax function to delete review film/serial
`
function delete_serial_film_review()
{
    const elems = $('.review_film_cls')
    elems.click(function ()
    {
        const th = $(this)
        sendDeleteFilmSerialReview(th.attr('data-type'), th.attr('data-slug'))
    })
    const sendDeleteFilmSerialReview = (type_, slug_) =>
    {
        $.ajax({
                type: 'POST',
                url: '/delete_film_serial_review/',
                data: {
                    'csrfmiddlewaretoken': document.getElementsByName('csrfmiddlewaretoken')[0].value,
                    'type': type_,
                    'slug': slug_
                },
                success: (res) =>
                {
                    $(`#${slug_}_review`).remove()
                    if (res.data.count === 0)
                    {
                        $(`#table_review_${type_}`).remove()
                        $(`#review_${type_}_tab`).after(`
                        <h3 class="empty_field">Empty</h3>

                    `)
                    }

                },
                error: (err) =>
                {
                }
            }
        )
    }
}

delete_serial_film_review()