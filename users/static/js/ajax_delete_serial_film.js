`
Ajax function to delete film/serial rating in profile
`
function delete_serial_film()
{
    const elems = $('.film_serial_cls')
    elems.click(function ()
    {
        const th = $(this)
        sendDeleteFilmSerial(th.attr('data-type'), th.attr('data-slug'))
    })
    const sendDeleteFilmSerial = (type_, slug_) =>
    {
        $.ajax({
                type: 'POST',
                url: '/delete_film_serial/',
                data: {
                    'csrfmiddlewaretoken': document.getElementsByName('csrfmiddlewaretoken')[0].value,
                    'type': type_,
                    'slug': slug_
                },
                success: (res) =>
                {
                    $(`#${slug_}_rating`).remove()
                    if (res.data.count === 0)
                    {
                        $(`#table_rating_${type_}`).remove()
                        $(`#rating_${type_}_tab`).after(`
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

delete_serial_film()