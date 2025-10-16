from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.http import JsonResponse
from django.views import View

from banks.models import Bank


class BankListView(LoginRequiredMixin, View):

    login_url = '/login/'

    def get(self, request):
        banks = Bank.objects.annotate(
            branch_count=Count('branches')
        )
        data = [
            {
                "name": bank.name,
                "is_islamic": bank.is_islamic,
                "branch_count": bank.branch_count,
            }
            for bank in banks
        ]
        return JsonResponse({'data': data})
