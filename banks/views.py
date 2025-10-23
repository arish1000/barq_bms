from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response

from banks.models import Bank
from banks.serializers import BankListSerializer


@method_decorator(login_required(login_url="/users/login/"), name="dispatch")
class BankListView(View):
    def get(self, request, *args, **kwargs):
        banks = Bank.objects.annotate(
            branch_count=Count("branches")
        )
        data = [
            {
                "name": bank.name,
                "is_islamic": bank.is_islamic,
                "branch_count": bank.branch_count,
            }
            for bank in banks
        ]

        return JsonResponse({"data": data})


class BankListApiView(APIView):
    
    def get(self, request, *args, **kwargs):
        banks = Bank.objects.annotate(
            branch_count=Count("branches")
        )
        serializer = BankListSerializer(banks, many=True)
        context = {"data": serializer.data, "count": banks.count()}

        return Response(context, status=HTTP_200_OK)


class BankListGenericView(ListAPIView):
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
