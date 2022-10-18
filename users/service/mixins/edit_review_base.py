from django.shortcuts import render, redirect
from users.models import CustomUser
from django.utils import timezone
from django.http import JsonResponse


class EditReviewBaseMixin:
    """
    Mixin for Film and Serial CBV review edit. Return GET response
    and POST response and save new review
    """
    template = 'users/edit_review_page_base.html'

    def _return_get_response(self, request, username, review_model):
        user_obj = CustomUser.objects.filter(username=username).first()
        if request.user.is_authenticated and username == request.user.username:
            review_obj = review_model.get(
                user=user_obj
            )
            return render(request, self.template,
                          {'review_obj': review_obj})
        return redirect('main_page')

    def _return_post_response(self, request, username, review_model):
        user_obj = CustomUser.objects.filter(username=username).first()

        title, text, review_type = (
            request.POST['title'],
            request.POST['text_data'],
            request.POST['review_type']
        )
        review_obj = review_model.get(
            user=user_obj
        )
        review_obj.title = title
        review_obj.text = text
        review_obj.review_type = review_type
        review_obj.created = timezone.now()
        review_obj.save()

        return JsonResponse(
            {'url': f'{request.build_absolute_uri("main_page")}'}
        )
