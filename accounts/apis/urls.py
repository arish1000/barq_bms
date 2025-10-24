from django.urls import path, include
from rest_framework.routers import DefaultRouter

from accounts.apis.views import AccountsViewSet

router = DefaultRouter()
router.register(r"", AccountsViewSet, basename="accounts")

urlpatterns = [
    path("", include(router.urls)),
]
