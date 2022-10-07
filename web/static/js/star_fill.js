class Fill_Star
{
    constructor()
    {
        this.svg_star_marks = $('.svg_star_mark')
        this.star_arr = $('.one_star_container')
        this.number = this._get_two_numbers($('#true_rating_cinema').attr('name'))
    }

    star_fill_change()
    {

        this._remove_fill_on_all_star()
        Array.from(this.svg_star_marks).forEach((element, index) =>
        {

            if (index < this.number.integer)
            {
                $(element).css('fill', '#2f80ed')
            }
            if (index === this.number.integer)
            {
                this.half_star_element = {
                    element: element,
                    index: index
                }
                this._generate_fill_html_code(element)
            } else if (this.number.integer === 10)
            {
                $(element).css('fill', '#2f80ed')
                this.half_star_element = {
                    element: element,
                    index: index
                }
            }
        })
    }

    hover_fill_change()
    {
        let _this = this

        for (let ele of this.star_arr)
        {
            ele.addEventListener('mouseenter', function ()
            {
                _this._hover_all_star_before_active_deactivate(ele, true)
                _this._remove_half_color(_this.star_arr.index(ele))
                // _this._remove_fill_on_all_star()

            })
            ele.addEventListener('mouseleave', function ()
            {
                _this._hover_all_star_before_active_deactivate(ele)
                _this._add_half_color()

                // _this.star_fill_change()
            })
        }
    }

    _remove_fill_on_all_star()
    {
        Array.from(this.svg_star_marks).forEach((element, index) =>
        {

            $(element).css('fill', 'rgb(147, 145, 145)')
            $(element).children('path').removeAttr('fill')
        })

    }

    _generate_fill_html_code(html_block)
    {
        const [first_color, second_color] = $(`#grad_${this.number.integer}`).children()

        $(first_color).attr('offset', `${this.number.fraction}%`).attr('stop-color', '#2f80ed')
        $(second_color).attr('offset', `${this.number.fraction + 0.1}%`).attr('stop-color', 'rgb(147, 145, 145)')

        $(html_block).children('path').attr('fill', `url(#grad_${this.number.integer})`)
    }


    _get_two_numbers(rating_text)
    {
        const fractional_part = (rating_text % 1).toFixed(1)
        return {integer: Math.ceil(rating_text - fractional_part), fraction: Number(fractional_part) * 100}
    }

    _hover_all_star_before_active_deactivate(selector, flag)
    {
        for (let ele of this.star_arr)
        {
            if (Number(ele.name) <= Number(selector.name) && flag)
            {
                $(ele).addClass('active_star_fill')
            } else
            {
                $(ele).removeClass('active_star_fill')

            }
        }
    }

    _remove_half_color(eq_index)
    {
        if (eq_index >= this.half_star_element.index)
        {
            $(this.half_star_element.element).children('path').removeAttr('fill')
        }
    }

    _add_half_color()
    {
        if (this.number.integer !== 10)
        {
            $(this.half_star_element.element).children('path').attr('fill', `url(#grad_${this.half_star_element.index})`)

        }
    }
}

const colors = new Fill_Star()
colors.star_fill_change()
colors.hover_fill_change()

