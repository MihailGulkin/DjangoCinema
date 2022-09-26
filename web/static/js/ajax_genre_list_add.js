`
Add genres on navbar when page loading
`

const csrf = $('[name="csrfmiddlewaretoken"]')[0].value
const dropdown_menu = $('#dropdown_genres_menu')

$(document).ready(function ()
{
    sendGenresData()
})
const sendGenresData = () =>
{
    $.ajax({
        type: "POST",
        url: '/genres_menu',
        data: {
            csrfmiddlewaretoken: csrf,
        },
        success: function (resp)
        {
            if (!$(dropdown_menu).children().length)
            {

                resp.data.forEach(genre =>
                    $(dropdown_menu).append(`
                 <li class="nav_item_header"><a class="dropdown-item"
                                                               href="/${genre.slug}">${genre.name}</a>
                                </li>
                `)
                )
            }
        },
        error: function ()
        {
        }
    });
}