from django.db.models import Count
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response

from banks.models import Bank
from banks.serializers import BankListSerializer


class BankListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        banks = Bank.objects.annotate(
            branch_count=Count("branches")
        )
        serializer = BankListSerializer(banks, many=True)
        context = {"data": serializer.data, "count": banks.count()}

        return Response(context, status=HTTP_200_OK)


class BankListGenericAPIView(ListAPIView):
    serializer_class = BankListSerializer

    def get_queryset(self):
        return Bank.objects.annotate(
            branch_count=Count("branches")
        )


class BankViewSet(ReadOnlyModelViewSet):
    serializer_class = BankListSerializer

    def get_queryset(self):
        return Bank.objects.annotate(
            branch_count=Count("branches")
        )
