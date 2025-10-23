from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

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
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        banks = Bank.objects.annotate(
            branch_count=Count("branches")
        )
        serializer = BankListSerializer(banks, many=True)

        return Response({
            "data": serializer.data,
            "count": banks.count()
        }, status=status.HTTP_200_OK)


class BankListGenericView(ListAPIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = BankListSerializer
    
    def get_queryset(self):

        return Bank.objects.annotate(
            branch_count=Count("branches")
        )


class BankViewSet(ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = BankListSerializer
    
    def get_queryset(self):

        return Bank.objects.annotate(
            branch_count=Count("branches")
        )
