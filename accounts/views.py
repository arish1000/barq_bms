from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from accounts.models import Account
from accounts.serializers import AccountsListSerializer, AccountsCreateSerializer, AccountBalanceUpdateSerializer


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


class AccountsCreateListGenericAPIView(ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return AccountsCreateSerializer
        return AccountsListSerializer

    def get_queryset(self):
        return Account.objects.select_related("branch__bank").filter(user=self.request.user)


class AccountsRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_serializer_class(self):
        if self.request.method == "GET":
            return AccountsListSerializer
        return AccountsCreateSerializer

    def get_queryset(self):
        return Account.objects.select_related("branch__bank").filter(user=self.request.user)


class AccountBalanceUpdateAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def patch(self, request, pk):
        try:
            account = Account.objects.get(pk=pk, user=request.user)
        except Account.DoesNotExist:
            return Response(
                {"error": "Account not found or you don't have permission to access it."}, 
                status=404
            )
        
        serializer = AccountBalanceUpdateSerializer(account, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Balance updated successfully",
                "account_id": account.id,
                "new_balance": account.balance
            }, status=HTTP_200_OK)
        
        return Response(serializer.errors, status=400)
