from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),
    path("banks/", include("banks.urls")),
    path("api/banks/", include("banks.apis.urls")),
    path("accounts/", include("accounts.urls")),
    path("api/accounts/", include("accounts.apis.urls")),
]
