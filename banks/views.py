from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View

from banks.models import Bank


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