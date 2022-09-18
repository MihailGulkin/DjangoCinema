function start_query_search()
{
    const sendSearchData = (query) =>
    {
        $.ajax({
            type: 'POST',
            url: '/search_search_url_search_token/',
            data: {
                'csrfmiddlewaretoken': csrf,
                'query': query
            },
            success: (res) =>
            {
                const data = res.data

                $(result_box).html('')

                if (Array.isArray(data))
                {
                    data.forEach(element =>
                    {
                        $(result_box).append(`
                            <li class="block_li_search">
                                <a href='${element.title ? 'movie/':'serial/'}${element.slug}' class="d-flex row">
                                    <div class="col-3 img_search">
                                        <img src=/media/${element.poster} alt>
                                    </div>
                                    <div class="col-9 text_search">
                                        <p>${element.title ? element.title : element.serial_name}</p>
                                    </div>
                                </a>
                            </li>
                          `)
                    })
                } else
                {
                    if ($(search_input).val())
                    {
                        $(result_box).html(  `
                              <div class="w-100 search_text_error">
                                <h1>
                                    ${data}
                                </h1>
                              </div>
                              `)
                    } else
                    {
                        $(result_box).addClass('not_visible')
                    }
                }
            },
            error: (err) =>
            {
                console.log(err)
            }
        })
    }

    // const search_form = document.getElementById('search_form')

    const search_input = $('#search_input')
    console.log($(search_input).val())

    const result_box = $('#result_box')

    const csrf = $('[name="csrfmiddlewaretoken"]')[0].value

    search_input.keyup(function (event)
        {
            if ($(result_box).hasClass('not_visible') && event.target.value)
            {
                $(result_box).removeClass('not_visible')
            }

            sendSearchData(event.target.value)
        }
    )
}

start_query_search()