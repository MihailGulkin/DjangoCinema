from django.db.models import QuerySet


class CalculateReviewsTypeMixin:
    def calculate_review(self, film_obj):
        result_dict = {}
        reviews_obj: QuerySet = self.model_view.objects.filter(
            movie=film_obj)
        result_dict['total'] = reviews_obj.__len__()
        total = result_dict['total']
        for ele in reviews_obj:
            if f'{ele.review_type}s' not in result_dict:
                result_dict[f'{ele.review_type}s'] = {
                    ele.review_type: 1,
                    'total': f'{(1 / total):.2f}'
                }
            else:
                result_dict[f'{ele.review_type}s'][ele.review_type] += 1
                temp = result_dict[f'{ele.review_type}s'][ele.review_type]
                result_dict[f'{ele.review_type}s'][
                    'total'] = f'{(temp / total):.2f}'
        return result_dict
