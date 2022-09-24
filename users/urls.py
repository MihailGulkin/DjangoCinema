from django.urls import path
from .views import RegistrationPageView, LoginPageView
urlpatterns = [
    path('register/', RegistrationPageView.as_view(), name='register_page'),
    path('login/', LoginPageView.as_view(), name='login_page'),

]