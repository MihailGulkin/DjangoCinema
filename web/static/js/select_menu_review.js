`
Styles select menu in review form
`
function select_menu()
{
       $('select').each(function ()
        {
            let $this = $(this)

            $this.addClass('select-hidden');
            $this.wrap('<div class="select"></div>');
            $this.after('<div id="selected_review_type" class="select-styled"></div>');

            let $styledSelect = $this.next('div.select-styled');
            $styledSelect.text($this.children('option').eq(0).text());

            let $list = $('<ul />', {
                'class': 'select-options'
            }).insertAfter($styledSelect);



            for(let ele of $this.children('option'))
            {
                $('<li />', {
                    text: $(ele).text(),
                    rel: $(ele).val()
                }).appendTo($list)
            }

            let $listItems = $list.children('li');

            // event on click select area
            $styledSelect.click(function (e)
            {
                e.stopPropagation();
                $('div.select-styled.active').not(this).each(function ()
                {
                    $(this).removeClass('active').next('ul.select-options').hide();
                });
                $(this).toggleClass('active').next('ul.select-options').toggle();
            });

            // event on select item in selected list
            $listItems.click(function (e)
            {
                $('#button_review_send').removeClass('disable_btn')
                e.stopPropagation();
                $styledSelect.text($(this).text()).removeClass('active');
                $this.val($(this).attr('rel'));
                $list.hide();
            });

            // hide selector when click on non-select area
            $(document).click(function ()
            {
                $styledSelect.removeClass('active');
                $list.hide();
            });

        });
}
select_menu()