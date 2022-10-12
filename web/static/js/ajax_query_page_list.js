`
Many page list on one page without loading
`

function ajax_start()
{
    $('.page_number').click(function (event)
    {
            console.log('dsf')

        event.preventDefault();
        let page_n = $(this).attr('href');

        $.ajax({
            type: "POST",
            url: '',
            data: {
                'page_n': page_n,
                'csrfmiddlewaretoken': $('[name="csrfmiddlewaretoken"]')[0].value,
            },
            success: function (resp)
            {
                current_active_number_change(page_n)

                change_pages_active(page_n)

                arrow_changer(page_n)

                $('#movie_list_container_card').html('')

                $.each(resp.results, function (i, val)
                {
                    $('#movie_list_container_card').append(`
                            <div class="col-12 col-md-6 col-xl-4">
                                <div class="card сard_big">
                                    <a href="/movie/${val.slug}/" class="card_cover">
                                            <img class="card_img" src="/media/${val.poster}" alt="">
                                            <svg  class="card_svg_play" version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
\t viewBox="0 0 512 512" style="enable-background:new 0 0 512 512;" xml:space="preserve">
<g>
\t<g>
\t\t<path d="M256,0C114.841,0,0,114.841,0,256s114.841,256,256,256s256-114.841,256-256S397.159,0,256,0z M256,492.308
\t\t\tc-130.298,0-236.308-106.01-236.308-236.308S125.702,19.692,256,19.692S492.308,125.702,492.308,256S386.298,492.308,256,492.308z
\t\t\t"/>
\t</g>
</g>
<g>
\t<g>
\t\t<path d="M246.154,118.154c-21.582,0-41.721,8.564-56.707,24.106c-3.774,3.913-3.664,10.144,0.255,13.918
\t\t\tc3.909,3.774,10.144,3.664,13.918-0.254c11.24-11.655,26.346-18.078,42.534-18.078c32.577,0,59.077,26.501,59.077,59.077
\t\t\tc0,20.275-9.447,26.712-26.601,38.394c-9.039,6.159-19.288,13.135-29.759,23.543c-28.111,27.923-19.394,59.044-10.861,71.597
\t\t\tc1.899,2.792,4.971,4.289,8.106,4.289c1.885,0,3.793-0.543,5.481-1.669c4.495-3,5.707-9.1,2.745-13.624
\t\t\tc-1.553-2.371-14.529-23.837,8.404-46.621c9.187-9.125,18.635-15.561,26.971-21.24c18.106-12.331,35.207-23.981,35.207-54.668
\t\t\tC324.923,153.49,289.586,118.154,246.154,118.154z"/>
\t</g>
</g>
<g>
\t<g>
\t\t<path d="M245.135,364.308c-5.438,0-9.846,4.41-9.846,9.846V384c0,5.438,4.409,9.846,9.846,9.846c5.438,0,9.846-4.409,9.846-9.846
\t\t\tv-9.846C254.981,368.718,250.572,364.308,245.135,364.308z"/>
\t</g>
</g>
                                        </svg>
    
                                            <span class="navbar_rating_hover">
                                                <span class="card_rating">
                                                    <svg class="card_svg_star" version="1.1" id="Capa_1"
                                                         xmlns="http://www.w3.org/2000/svg"
                                                         xmlns:xlink="http://www.w3.org/1999/xlink"
                                                         x="0px"
                                                         y="0px"
                                                         width="36.09px" height="36.09px" viewBox="0 0 36.09 36.09"
                                                         style="enable-background:new 0 0 36.09 36.09;"
                                                         xml:space="preserve"
                                                    >
        <g>
            <path d="M36.042,13.909c-0.123-0.377-0.456-0.646-0.85-0.688l-11.549-1.172L18.96,1.43c-0.16-0.36-0.519-0.596-0.915-0.596
                s-0.755,0.234-0.915,0.598L12.446,12.05L0.899,13.221c-0.394,0.04-0.728,0.312-0.85,0.688c-0.123,0.377-0.011,0.791,0.285,1.055
                l8.652,7.738L6.533,34.045c-0.083,0.387,0.069,0.787,0.39,1.02c0.175,0.127,0.381,0.191,0.588,0.191
                c0.173,0,0.347-0.045,0.503-0.137l10.032-5.84l10.03,5.84c0.342,0.197,0.77,0.178,1.091-0.059c0.32-0.229,0.474-0.633,0.391-1.02
                l-2.453-11.344l8.653-7.737C36.052,14.699,36.165,14.285,36.042,13.909z M25.336,21.598c-0.268,0.24-0.387,0.605-0.311,0.957
                l2.097,9.695l-8.574-4.99c-0.311-0.182-0.695-0.182-1.006,0l-8.576,4.99l2.097-9.695c0.076-0.352-0.043-0.717-0.311-0.957
                l-7.396-6.613l9.87-1.002c0.358-0.035,0.668-0.264,0.814-0.592l4.004-9.077l4.003,9.077c0.146,0.328,0.456,0.557,0.814,0.592
                l9.87,1.002L25.336,21.598z"/>
        </g>
                                                        <g>
        </g>
                                                        <g>
        </g>
                                                        <g>
        </g>
                                                        <g>
        </g>
                                                        <g>
        </g>
                                                        <g>
        </g>
                                                        <g>
        </g>
                                                        <g>
        </g>
                                                        <g>
        </g>
                                                        <g>
        </g>
                                                        <g>
        </g>
                                                        <g>
        </g>
                                                        <g>
        </g>
                                                        <g>
        </g>
                                                        <g>
        </g>
        </svg>
                                                    ${val.IMDb_RATING}
                                                </span>
                                                <div data-value="${val.slug}" data-value-type="film" class="svg_heart_container ${val.slug}_cls_favorite">
                                                    ${generate_html_svg_heart(resp.favorite[i])}
                                                </div>
                                                <div data-value="${val.slug}" data-value-type="film" class="svg_bookmark_container ${val.slug}_cls_bookmark">
                                                    ${generate_html_svg_book(resp.later[i])}
                                   
                                                </div>
                                            </span>
                                        </a>
                                    <div class="card_content">
                                        <h3 class="card_title_word_wrap card_title_wrap"><a href="/movie/${val.slug}/">${val.title}</a></h3>
                                        <h5 class="card_content_title_h5">Genres</h5>
                                        <ul class="card_list_big card_test_some flex-row">
                                                    ${generate_html_li(resp.film_genres, val)}
                                        </ul>
                                        <ul class="card_list_big">
                                            <li class="card_list_li">Release Date : ${val.release_date}</li>
                                            <li class="card_list_li">
                                                Director: <a class="card_director" href="">${resp.directors[val.director_id - 1]}</a>
                                            </li>
                                        </ul>
                                        <p class="card_content_title_h5 card_content_p">
                                            «${val.summary.substring(0, 99)}…»</p>
                                    </div>
                                </div>
                            </div>`)
                });
                start()
                ajax_favoriteFilm()
                ajax_lateFilm()
            },
            error: function ()
            {
            }
        });

    })
}

ajax_lateFilm()
ajax_favoriteFilm()
ajax_start()

function generate_html_svg_heart(bool)
{
    return bool
        ? `<svg class="card_svg_actions_with_film favourite_film" version="1.1"
                                                     id="Capa_1"
                                                     xmlns="http://www.w3.org/2000/svg"
                                                     xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
                                                     width="45.743px" height="45.743px" viewBox="0 0 45.743 45.743"
                                                     xml:space="preserve">
                                                    <g>
                                                        <path d="M34.199,3.83c-3.944,0-7.428,1.98-9.51,4.997c0,0-0.703,1.052-1.818,1.052c-1.114,0-1.817-1.052-1.817-1.052
                                                            c-2.083-3.017-5.565-4.997-9.51-4.997C5.168,3.83,0,8.998,0,15.376c0,1.506,0.296,2.939,0.82,4.258
                                                            c3.234,10.042,17.698,21.848,22.051,22.279c4.354-0.431,18.816-12.237,22.052-22.279c0.524-1.318,0.82-2.752,0.82-4.258
                                                            C45.743,8.998,40.575,3.83,34.199,3.83z"/>
                                                    </g>
                                                </svg>`
        : `<svg class="card_svg_actions_with_film" version="1.1"
                                                     id="Capa_1"
                                                     xmlns="http://www.w3.org/2000/svg"
                                                     xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
                                                     width="45.743px" height="45.743px" viewBox="0 0 45.743 45.743"
                                                     xml:space="preserve">
                                                    <g>
                                                        <path d="M34.199,3.83c-3.944,0-7.428,1.98-9.51,4.997c0,0-0.703,1.052-1.818,1.052c-1.114,0-1.817-1.052-1.817-1.052
                                                            c-2.083-3.017-5.565-4.997-9.51-4.997C5.168,3.83,0,8.998,0,15.376c0,1.506,0.296,2.939,0.82,4.258
                                                            c3.234,10.042,17.698,21.848,22.051,22.279c4.354-0.431,18.816-12.237,22.052-22.279c0.524-1.318,0.82-2.752,0.82-4.258
                                                            C45.743,8.998,40.575,3.83,34.199,3.83z"/>
                                                    </g>
                                                </svg>`
}
function generate_html_svg_book(bool)
{
    return bool
    ? `<svg class="card_svg_actions_with_film later_film" version="1.1"
                                                          id="Capa_1"
                                                          xmlns="http://www.w3.org/2000/svg"
                                                          xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
                                                          width="459px" height="459px" viewBox="0 0 459 459"
                                                          style="enable-background:new 0 0 459 459;"
                                                          xml:space="preserve">
                                                        <g>
                                                            <g id="bookmark">
                                                                <path d="M357,0H102C73.95,0,51,22.95,51,51v408l178.5-76.5L408,459V51C408,22.95,385.05,0,357,0z"/>
                                                            </g>
                                                        </g>
                                                        </svg>`
    : `<svg class="card_svg_actions_with_film" version="1.1"
                                                          id="Capa_1"
                                                          xmlns="http://www.w3.org/2000/svg"
                                                          xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
                                                          width="459px" height="459px" viewBox="0 0 459 459"
                                                          style="enable-background:new 0 0 459 459;"
                                                          xml:space="preserve">
                                                        <g>
                                                            <g id="bookmark">
                                                                <path d="M357,0H102C73.95,0,51,22.95,51,51v408l178.5-76.5L408,459V51C408,22.95,385.05,0,357,0z"/>
                                                            </g>
                                                        </g>
                                                        </svg>
`

}
function generate_html_li(film_genres, val)
{
    for (let ele of film_genres)
    {
        if (ele[val.title])
        {
            let html_code = ''
            for (let genre of ele[val.title])
            {
                if (ele[val.title].indexOf(genre) === 0)
                {
                    html_code += `<a href="/${genre.slug}">${genre}</a>
`
                }
                else if (ele[val.title].indexOf(genre) < 3)
                {

                    html_code += `<a href="/${genre.slug}"><span
                                                            class="span_color_card">, </span>${genre}</a>`
                }
            }
            return html_code

        }
    }

}

function find_max_number()
{
    return Math.max(...$.map($('.page_number'), function (val, i)
    {
        return parseInt(val.innerHTML) ? parseInt(val.innerHTML) : 0
    }))
}

function find_min_number()
{
    return Math.min(...$.map($('.page_number'), function (val, i)
    {
        return parseInt(val.innerHTML) ? parseInt(val.innerHTML) : 100000
    }))
}

function current_active_number_change(page_number)
{
    const number_selector = $('.active_a')[0].innerHTML

    if (number_selector < page_number)
    {
        for (let ele of $('.page_number'))
        {
            if (parseInt(ele.innerHTML) && find_max_number() < $('.movie_list_page').data().number)
            {
                const number_plus = (parseInt(ele.innerHTML) + 1).toString()
                set_attr(ele, number_plus)
            }
        }
    } else if (number_selector > page_number)
    {
        if (find_min_number() > 1)
        {
            for (let ele of $('.page_number'))
            {
                if (parseInt(ele.innerHTML))
                {
                    const number_minus = (parseInt(ele.innerHTML) - 1).toString()
                    set_attr(ele, number_minus)
                }
            }
        }

    }

    function set_attr(ele, number)
    {
        ele.innerHTML = number
        $(ele).attr('href', number)
    }
}

function change_pages_active(page_number)
{
    for (let ele of $('.page_number').removeClass('active_a'))
    {
        if (page_number === ele.innerHTML)
        {
            $(ele).addClass('active_a')
        }
    }
}

function arrow_changer(page_number)
{
    const page_num = parseInt(page_number)
    const max_number = $('.movie_list_page').data().number

    const arrow_right = $('.page_arrow_right')
    const arrow_left = $('.page_arrow_left')


    arrow_right.attr('href', (page_num === max_number ? max_number : page_num + 1).toString())
    arrow_left.attr('href', (page_num === 1 ? 1 : page_num - 1).toString())
}
