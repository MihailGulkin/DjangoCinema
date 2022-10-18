from django.http import JsonResponse
from web.models import Movie, Serial


class DeleteProfileDataMixin:
    """
    Mixin for Delete model entry in movie/serial rating, later
    and favorite actions
    """

    def _delete_profile_data_film_serial(
            self,
            delete_model_obj,
            films_serials_model):
        delete_model_obj.delete()
        return self.__return_json_data(films_serials_model)

    def __return_json_data(self, model):
        return JsonResponse({'data': {
            'count': len(model),
        }})

    def _return_movie_obj(self, slug):
        return Movie.objects.get(slug=slug)

    def _return_serial_obj(self, slug):
        return Serial.objects.get(slug=slug)
