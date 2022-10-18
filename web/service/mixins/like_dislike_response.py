from django.http import JsonResponse


class GetUsersLikeDis:
    """
    Contains general method to not duplicate code in LikeDislikeView.
    """
    def _return_like_dis_response(self, _review_model, like_dis_model):
        review_obj = _review_model.objects.get(pk=self.pk)

        model_obj = like_dis_model.objects.filter(
            user=self.user,
            review=review_obj
        ).first()

        if model_obj:
            model_obj.like_dislike = self.like_dislike
            model_obj.save()
            return JsonResponse({'data': {
                'created': False
            }})
        like_dis_model.objects.create(
            user=self.user,
            review=review_obj,
            like_dislike=self.like_dislike
        )

        return JsonResponse({'data': {
            'created': True
        }})
