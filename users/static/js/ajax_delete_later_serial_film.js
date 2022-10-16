function delete_serial_film_later()
{
    const elems = $('.later_film_cls')
    elems.click(function ()
    {
        const th = $(this)
        sendDeleteFilmSerialLater(th.attr('data-type'), th.attr('data-slug'))
    })
    const sendDeleteFilmSerialLater = (type_, slug_) =>
    {
        $.ajax({
                type: 'POST',
                url: '/delete_film_serial_later/',
                data: {
                    'csrfmiddlewaretoken': document.getElementsByName('csrfmiddlewaretoken')[0].value,
                    'type': type_,
                    'slug': slug_
                },
                success: (res) =>
                {
                    $(`#${slug_}_later`).remove()
                    if (res.data.count === 0)
                    {
                        $(`#table_later_${type_}`).remove()
                        $(`#later_${type_}_tab`).after(`
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

delete_serial_film_later()