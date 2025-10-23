from django.urls import path, include

from accounts.views import AccountsCreateListGenericAPIView, AccountsRetrieveUpdateDestroyAPIView

urlpatterns = [
    path("", AccountsCreateListGenericAPIView.as_view(), name="accounts-create-list"),
    path("<int:pk>/", AccountsRetrieveUpdateDestroyAPIView.as_view(), name="accounts-detail"),
]
