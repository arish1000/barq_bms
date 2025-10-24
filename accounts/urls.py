from django.urls import path, include

from accounts.views import AccountsCreateListGenericAPIView, AccountsRetrieveUpdateDestroyAPIView, AccountBalanceUpdateAPIView

urlpatterns = [
    path("", AccountsCreateListGenericAPIView.as_view(), name="accounts-create-list"),
    path("<int:pk>/", AccountsRetrieveUpdateDestroyAPIView.as_view(), name="accounts-detail"),
    path("<int:pk>/balance/", AccountBalanceUpdateAPIView.as_view(), name="accounts-balance-update"),
]
