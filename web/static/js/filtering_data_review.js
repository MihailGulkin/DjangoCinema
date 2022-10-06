function filtering_data_review_func()
{
    const elems = $('.rating_bar_select_cls')

    for (let ele of elems)
    {
        $(ele).click(function ()
            {
                remove_all_active_cls()
                open_all_reviews()

                $(ele).addClass('active_rating_bar_block')

                if ($(ele).attr('data-type') !== 'Total')
                {
                    hide_all_reviews($(ele).attr('data-type'))
                }
            }
        )
    }

    function remove_all_active_cls()
    {
        for (let ele of elems)
        {
            $(ele).removeClass('active_rating_bar_block')

        }
    }

    function open_all_reviews()
    {
        for (let ele of $('.user_review_container'))
        {
            $(ele).css('display', '')
        }


    }

    function hide_all_reviews(reviews_type)
    {
        for (let ele of $('.user_review_container'))
        {
            if ($(ele).attr('data-type') !== reviews_type)
            {
                $(ele).css('display', 'none')
            }

        }
    }
}
filtering_data_review_func()