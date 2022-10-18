`
Function to close big text review and add open text btn
`
function btn_text_open_active()
{
    $(".content-block-text").each(function ()
    {
        let th = $(this);
        if (th.prop('scrollHeight') > th.height())
        {
            let more = th.next(".show-all-container").find(".show-all");
            th.next(".show-all-container").show();

            more.click(function ()
            {
                th.toggleClass(" content-block-text-open");
                th.next(".show-all-container").remove()
            });
        }
    });
}

btn_text_open_active()