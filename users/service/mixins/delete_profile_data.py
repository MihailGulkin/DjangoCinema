from django.http import JsonResponse
from web.models import Movie, Serial


class DeleteProfileDataMixin:
    def _delete_profile_data_film(self, delete_model_obj, films_model):
        delete_model_obj.delete()
        return self.__return_json_data(films_model)

    def _delete_profile_data_serial(self, delete_model_obj, serials_model):
        delete_model_obj.delete()
        return self.__return_json_data(serials_model)

    def __return_json_data(self, model):
        return JsonResponse({'data': {
            'count': len(model),
        }})

    def _return_movie_obj(self, slug):
        return Movie.objects.get(slug=slug)

    def _return_serial_obj(self, slug):
        return Serial.objects.get(slug=slug)
