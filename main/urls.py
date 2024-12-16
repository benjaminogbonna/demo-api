from django.urls import path, include
from .views import RegisterUserView, UserProfileView
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'main'

urlpatterns = [
    path("login/", obtain_auth_token, name="login"),
    path("register/", RegisterUserView.as_view(), name="register"),
    path("profile/", UserProfileView.as_view(), name="profile"),
]
