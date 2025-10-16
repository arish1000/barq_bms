from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import Account
from accounts.serializers import AccountsListSerializer


class AccountsListView(APIView):

    def get(self, request):
        accounts = Account.objects.select_related('branch__bank').all()
        serializer = AccountsListSerializer(accounts, many=True)
        return Response(serializer.data)

