from django.urls import path, include

from accounts.views import AccountsListView

urlpatterns = [
    path("", AccountsListView.as_view(), name="accounts-list"),
]
