from django.urls import path

from users.views import logout_view, token_login_view

urlpatterns = [
    path("login/", token_login_view, name="login"),
    path("logout/", logout_view, name="logout"),
]
