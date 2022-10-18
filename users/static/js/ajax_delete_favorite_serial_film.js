`
Ajax function to delete favorite film/serial
`
function delete_serial_film_favorite()
{
    const elems = $('.favorite_film_cls')
    elems.click(function ()
    {
        const th = $(this)
        sendDeleteFilmSerialFavorite(th.attr('data-type'), th.attr('data-slug'))
    })
    const sendDeleteFilmSerialFavorite = (type_, slug_) =>
    {
        $.ajax({
                type: 'POST',
                url: '/delete_film_serial_favorite/',
                data: {
                    'csrfmiddlewaretoken': document.getElementsByName('csrfmiddlewaretoken')[0].value,
                    'type': type_,
                    'slug': slug_
                },
                success: (res) =>
                {
                    $(`#${slug_}_favorite`).remove()
                    if (res.data.count === 0)
                    {
                        $(`#table_favorite_${type_}`).remove()
                        $(`#favorite_${type_}_tab`).after(`
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

delete_serial_film_favorite()