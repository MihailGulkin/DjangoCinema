from django.shortcuts import render
from django.http import JsonResponse


class GetResponseMixin:
    def get_response_film_serial(self, request, model_obj, filter_model):
        if not request.user.is_authenticated:
            return render(request, self.template,
                          {'content': model_obj,
                           'rating': model_obj.IMDb_RATING})
        return render(request, self.template,
                      {'content': model_obj,
                       'rating':
                           filter_model.get(
                               user=request.user)
                           if filter_model.filter(
                               user=request.user).exists()
                           else model_obj.IMDb_RATING
                       }
                      )

    def post_response_film_serial(self, request, model_obj, filter_model):
        if not request.user.is_authenticated:
            return JsonResponse(
                {'url': f'{request.build_absolute_uri("/register/")}'})

        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            if rating_obj := filter_model.filter(
                    user=request.user).first():
                rating_obj.rating = request.POST['rating']
                rating_obj.save()
            else:
                rating_obj = self._create_rating_model(request, model_obj)

            return JsonResponse({'data': {
                'rating': rating_obj.rating,
                'name': rating_obj.movie.title if self._type == 'film'
                else rating_obj.serial.serial_name,
                'create': rating_obj.created.strftime('%Y-%m-%d %H:%M'),
                'type': self._type,
            }})
