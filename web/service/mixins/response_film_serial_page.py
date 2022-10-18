from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone


class GetResponseMixin:
    """
    View have get and post method to use in Movie/Serial.
    """
    def get_response_film_serial(self, request, model_obj, model_review,
                                 filter_model):
        if not request.user.is_authenticated:
            return render(request, self.template,
                          {'content': model_obj,
                           'cinema_reviews': model_review,
                           'have_review': False,
                           'rating': model_obj.IMDb_RATING,
                           'calculated': self.calculate_review(model_review)})
        return render(request, self.template,
                      {'content': model_obj,
                       'cinema_reviews': model_review,
                       'have_review': model_review.filter(
                           user=request.user).exists(),
                       'rating':
                           filter_model.get(
                               user=request.user)
                           if filter_model.filter(
                               user=request.user).exists()
                           else model_obj.IMDb_RATING,
                       'calculated': self.calculate_review(model_review)
                       }
                      )

    def post_response_film_serial(self, request, model_obj,
                                  filter_model):
        if not request.user.is_authenticated:
            return JsonResponse(
                {'url': f'{request.build_absolute_uri("/register/")}'})

        if request.META.get(
                'HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            if rating_obj := filter_model.filter(
                    user=request.user).first():
                rating_obj.created = timezone.now()
                rating_obj.rating = request.POST['rating']
                rating_obj.save()
            else:
                rating_obj = self._create_rating_model(request,
                                                       model_obj)

            return JsonResponse({'data': {
                'rating': rating_obj.rating,
                'name': rating_obj.movie.title if self._type == 'film'
                else rating_obj.serial.serial_name,
                'create': rating_obj.created.strftime(
                    '%Y-%m-%d %H:%M'),
                'type': self._type,
            }})
