from django.urls import path
from .views import RegistrationPageView, LoginPageView, ProfilePageView

urlpatterns = [
    path('register/', RegistrationPageView.as_view(), name='register_page'),
    path('login/', LoginPageView.as_view(), name='login_page'),
    path('profile/', ProfilePageView.as_view(), name='profile_page'),

]
