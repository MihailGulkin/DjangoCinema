from django.http import JsonResponse


def create_serial_film_model_response(
        model_cinema,
        favorite_cinema,
        chooses,
        request,
        slug):
    _obj = model_cinema.objects.get(slug=slug)

    if film_obj := favorite_cinema.objects.filter(
            user=request.user,
            cinema_type=_obj,
            choose_favorite_later=chooses)\
            .first():
        film_obj.delete()
        return JsonResponse({'dataRemove': {'slug': slug}})

    favorite_cinema.objects.create(
        user=request.user,
        cinema_type=_obj,
        choose_favorite_later=chooses)

    return JsonResponse({'dataAdd': {'slug': slug}})
