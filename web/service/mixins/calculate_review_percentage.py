from django.db.models import QuerySet


class CalculateReviewsTypeMixin:
    def calculate_review(self, reviews_obj):
        result_dict = {'total': reviews_obj.__len__()}
        self.total = result_dict['total']
        for ele in reviews_obj:
            if f'{ele.review_type}s' not in result_dict:
                result_dict[f'{ele.review_type}s'] = {
                    ele.review_type: 1,
                    'total': self.__fraction_part_check()
                }
            else:
                result_dict[f'{ele.review_type}s'][ele.review_type] += 1
                temp = result_dict[f'{ele.review_type}s'][ele.review_type]
                result_dict[f'{ele.review_type}s'][
                    'total'] = self.__fraction_part_check(temp=temp)
        print(result_dict)
        return result_dict

    def __fraction_part_check(self, temp=1):
        return f'{(temp / self.total * 100):.2f}' \
               if (temp / self.total * 100) % 1 != 0 \
               else f'{(temp / self.total * 100):.0f}'
