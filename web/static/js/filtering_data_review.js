const elems = $('.rating_bar_select_cls')

for (let ele of elems)
{
    $(ele).click(function ()
        {
            open_all_reviews()

            if ($(ele).attr('data-type') !== 'Total')
            {
                hide_all_reviews($(ele).attr('data-type'))
            }
        }
    )
}

function open_all_reviews(reviews_type)
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