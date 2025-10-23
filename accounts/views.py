from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ReadOnlyModelViewSet

from accounts.models import Account
from accounts.serializers import AccountsListSerializer


@method_decorator(login_required(login_url="/users/login/"), name="dispatch")
class AccountsListView(View):
    def get(self, request, *args, **kwargs):
            accounts = Account.objects.select_related("branch__bank").filter(user=request.user)
            data = [ {
                "account_number": acc.account_number,
                "balance": acc.balance,
                "bank": acc.branch.bank.name,
            } for acc in accounts]
            
            return JsonResponse({"data": data})

class AccountsListAPIView(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        accounts = Account.objects.select_related("branch__bank").filter(user=request.user)
        serializer = AccountsListSerializer(accounts, many=True)

        return Response({
            "data": serializer.data,
            "count": accounts.count()
        }, status=status.HTTP_200_OK)

class AccountsListGenericAPIView(ListAPIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = AccountsListSerializer

    def get_queryset(self):

        return Account.objects.select_related("branch__bank").filter(user=self.request.user)

class AccountsViewSet(ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = AccountsListSerializer

    def get_queryset(self):

        return Account.objects.select_related("branch__bank").filter(user=self.request.user)


