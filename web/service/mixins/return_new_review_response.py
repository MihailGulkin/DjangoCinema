from django.http import JsonResponse


class GetNewUserReviewMixin():
    def new_review_response(self, cinema_model, review_model,
                            _review_flt):

        _bool = _review_flt.exists()

        if self.cinema_type == 'film':
            new_review = review_model.objects.create(
                user=self.request.user,
                movie=cinema_model,
                review_type=self.review_type,
                title=self.title,
                text=self.text_data
            )
        else:
            new_review = review_model.objects.create(
                user=self.request.user,
                serial=cinema_model,
                review_type=self.review_type,
                title=self.title,
                text=self.text_data
            )

        return JsonResponse({'data': {
            'user': self.request.user.username,
            'review_type': new_review.review_type,
            'title': new_review.title,
            'text': new_review.text,
            'bool': _bool,
            'calculated': self.calculate_review(_review_flt),
            'created': new_review.created.strftime('%#d %B %Y at %#H:%#M')
        }})
