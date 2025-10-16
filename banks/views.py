from django.db.models import Count
from rest_framework.response import Response
from rest_framework.views import APIView

from banks.models import Bank
from banks.serializers import BankListSerializer


class BankListView(APIView):

    def get(self, request):
        banks = Bank.objects.annotate(
            branch_count=Count('branches')
        )
        serializer = BankListSerializer(banks, many=True)
        return Response(serializer.data)


