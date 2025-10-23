from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ReadOnlyModelViewSet

from accounts.models import Account
from accounts.serializers import AccountsListSerializer


@method_decorator(login_required(login_url="/users/login/"), name="dispatch")
class AccountsListView(View):
    def get(self, request, *args, **kwargs):
            accounts = Account.objects.select_related("branch__bank").filter(user=self.request.user)
            data = [ {
                "account_number": acc.account_number,
                "balance": acc.balance,
                "bank": acc.branch.bank.name,
            } for acc in accounts]
            
            return JsonResponse({"data": data})


class AccountsListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        accounts = Account.objects.select_related("branch__bank").filter(user=self.request.user)
        serializer = AccountsListSerializer(accounts, many=True)
        context = {"data": serializer.data, "count": accounts.count()}

        return Response(context, status=HTTP_200_OK)


class AccountsListGenericAPIView(ListAPIView):
    serializer_class = AccountsListSerializer

    def get_queryset(self):
        return Account.objects.select_related("branch__bank").filter(user=self.request.user)


class AccountsViewSet(ReadOnlyModelViewSet):
    serializer_class = AccountsListSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Account.objects.select_related("branch__bank").filter(user=self.request.user)
        return Account.objects.none()
