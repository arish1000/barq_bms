from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ReadOnlyModelViewSet

from accounts.models import Account
from accounts.serializers import AccountsListSerializer, AccountsCreateSerializer


class AccountsListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        accounts = Account.objects.select_related("branch__bank")
        serializer = AccountsListSerializer(accounts, many=True)
        context = {"data": serializer.data, "count": accounts.count()}

        return Response(context, status=HTTP_200_OK)


class AccountsListGenericAPIView(ListAPIView):
    serializer_class = AccountsListSerializer

    def get_queryset(self):
        return Account.objects.select_related("branch__bank")


class AccountsViewSet(ReadOnlyModelViewSet):
    serializer_class = AccountsListSerializer

    def get_queryset(self):
        return Account.objects.select_related("branch__bank")


class AccountsCreateListGenericAPIView(ListCreateAPIView):
    def get_serializer_class(self):
        if self.request.method == "POST":
            return AccountsCreateSerializer
        return AccountsListSerializer

    def get_queryset(self):
        return Account.objects.select_related("branch__bank")


class AccountsRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    def get_serializer_class(self):
        if self.request.method == "GET":
            return AccountsListSerializer
        return AccountsCreateSerializer

    def get_queryset(self):
        return Account.objects.select_related("branch__bank")
