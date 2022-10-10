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
                                            <svg class="card_svg_play" version="1.0" xmlns="http://www.w3.org/2000/svg"
                                         width="512.000000pt" height="512.000000pt"
                                         viewBox="0 0 512.000000 512.000000"
                                         preserveAspectRatio="xMidYMid meet">
    
                                        <g transform="translate(0.000000,512.000000) scale(0.100000,-0.100000)"
                                           fill="#000000" stroke="none">
                                            <path d="M2330 5110 c-494 -48 -950 -230 -1350 -538 -195 -150 -448 -432 -594
    -662 -63 -99 -186 -351 -230 -471 -49 -134 -102 -340 -128 -499 -31 -195 -31
    -565 0 -760 45 -276 116 -498 237 -745 132 -269 269 -460 489 -681 221 -220
    412 -357 681 -489 247 -121 469 -192 745 -237 195 -31 565 -31 760 0 276 45
    498 116 745 237 269 132 460 269 681 489 220 221 357 412 489 681 88 179 132
    296 180 476 63 240 78 371 78 649 0 278 -15 409 -78 649 -48 180 -92 297 -180
    476 -132 269 -269 460 -489 681 -221 220 -412 357 -681 489 -246 121 -474 193
    -740 235 -147 23 -475 34 -615 20z m550 -226 c339 -49 662 -168 950 -352 253
    -161 541 -449 702 -702 144 -226 262 -507 317 -757 41 -185 53 -302 53 -513 0
    -275 -29 -467 -108 -713 -120 -371 -300 -663 -579 -942 -279 -279 -571 -459
    -942 -579 -246 -79 -438 -108 -713 -108 -275 0 -467 29 -713 108 -371 120
    -663 300 -942 579 -374 373 -589 803 -670 1340 -23 151 -23 479 0 630 54 355
    169 667 353 955 161 253 449 541 702 702 475 303 1045 429 1590 352z"/>
                                            <path d="M1983 3616 c-66 -30 -63 28 -63 -1058 0 -952 1 -984 19 -1014 28 -47
    78 -61 130 -37 78 35 1529 976 1542 1000 16 29 16 77 0 106 -10 18 -1218 806
    -1496 976 -64 38 -92 44 -132 27z m751 -676 c322 -206 585 -377 585 -380 0 -5
    -1162 -752 -1179 -758 -6 -2 -10 280 -10 758 0 478 4 760 10 758 5 -1 272
    -172 594 -378z"/>
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
