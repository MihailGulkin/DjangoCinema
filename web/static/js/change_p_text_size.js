function change_p_size_remove_star_bar()
{
    set_rating_font_size()
    set_star()
    window.addEventListener('resize', function (event)
    {
        set_rating_font_size()
        set_star()
    })

    function set_rating_font_size()
    {
        $('.mov_rating_text').css('font-size', '0').css("font-size",
            `${$('.one_star_container').first().height() - 5}`)
    }
    function set_star()
    {
        if(window.innerWidth < 768)
        {
            console.log('dfs')
        }
        `<div class="nav-item dropdown">
                            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button"
                               data-bs-toggle="dropdown" aria-expanded="false">
                                <div class="svg_star_container">
                                    <svg class="svg_star_mark" version="1.1" xmlns="http://www.w3.org/2000/svg"
                                         xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
                                         width="940.688px" height="940.688px" viewBox="0 0 940.688 940.688"
                                         style="enable-background:new 0 0 940.688 940.688;"
                                         xml:space="preserve">
                                        <defs>
                                            <lineargradient>
                                                <stop offset="50%" stop-color="yellow"></stop>
                                                <stop offset="50%" stop-color="grey"></stop>
                                            </lineargradient>
                                       </defs>
                                        <path d="M885.344,319.071l-258-3.8l-102.7-264.399c-19.8-48.801-88.899-48.801-108.6,0l-102.7,264.399l-258,3.8
                                                        c-53.4,3.101-75.1,70.2-33.7,103.9l209.2,181.4l-71.3,247.7c-14,50.899,41.1,92.899,86.5,65.899l224.3-122.7l224.3,122.601
                                                        c45.4,27,100.5-15,86.5-65.9l-71.3-247.7l209.2-181.399C960.443,389.172,938.744,322.071,885.344,319.071z"/>
                                    </svg>
                                </div>
                            </a>

                            <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="navbarDropdown">
                                {% for i in 10|for_range %}
                                    <li>
                                        <div class="one_star_div">
                                            <a name="{{ i }}" class="one_star_container d-flex" href="#">
                                                <div class="svg_star_container">
                                                    <svg class="svg_star_mark" version="1.1"
                                                         xmlns="http://www.w3.org/2000/svg"
                                                         xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
                                                         width="940.688px" height="940.688px"
                                                         viewBox="0 0 940.688 940.688"
                                                         style="enable-background:new 0 0 940.688 940.688;"
                                                         xml:space="preserve">
                                        <defs>
                                            <lineargradient id="grad_{{ i }}">
                                                <stop offset="50%" stop-color="yellow"></stop>
                                                <stop offset="50%" stop-color="grey"></stop>
                                            </lineargradient>
                                       </defs>
                                                        <path d="M885.344,319.071l-258-3.8l-102.7-264.399c-19.8-48.801-88.899-48.801-108.6,0l-102.7,264.399l-258,3.8
                                                        c-53.4,3.101-75.1,70.2-33.7,103.9l209.2,181.4l-71.3,247.7c-14,50.899,41.1,92.899,86.5,65.899l224.3-122.7l224.3,122.601
                                                        c45.4,27,100.5-15,86.5-65.9l-71.3-247.7l209.2-181.399C960.443,389.172,938.744,322.071,885.344,319.071z"/>
                                    </svg>
                                                </div>
                                                <p class="my-0 p_star_text">{{ i |add:1 }}</p>
                                            </a>
                                        </div>
                                    </li>
                                {% endfor %}
                            </ul>
                        </div>`
    }
}

change_p_size_remove_star_bar()