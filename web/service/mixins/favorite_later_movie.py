from web.models import ActionsWithMovie


class CheckFavLaterMovieMixin:
    def _favorite_later_movie(self, request, page_n, choose, paginator):
        if request.user.is_authenticated:
            return [ActionsWithMovie.objects.filter(
                cinema_type=film,
                user=request.user,
                choose_favorite_later=choose).exists()
                    for film in paginator.page(page_n).object_list]
        return [False for _ in range(len(page_n))]
