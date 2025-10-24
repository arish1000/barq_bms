from django.urls import path

from banks.apis.views import BankListCreateGenericView, BankRetrieveUpdateDestroyGenericView

urlpatterns = [
    path("", BankListCreateGenericView.as_view(), name="bank-list-create"),
    path("<int:pk>/", BankRetrieveUpdateDestroyGenericView.as_view(), name="bank-detail"),
]
