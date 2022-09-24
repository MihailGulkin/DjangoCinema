from django.urls import path
from .views import RegistrationPageView
urlpatterns = [
    path('register/', RegistrationPageView.as_view(), name='register_page'),

]