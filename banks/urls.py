from django.urls import path

from banks.views import BankListView


urlpatterns = [
    path('', BankListView.as_view(), name="list-banks"),
]
