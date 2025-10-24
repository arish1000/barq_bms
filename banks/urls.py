from django.urls import path, include

from banks.views import BankListView

urlpatterns = [
    path("", BankListView.as_view(), name="bank-list"),
]

