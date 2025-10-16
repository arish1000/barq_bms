from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from accounts.models import Account


class AccountsListView(LoginRequiredMixin, View):

    login_url = '/login/'

    def get(self, request):

            accounts = Account.objects.select_related('branch__bank').filter(user=request.user)
            data = [ {
                'account_number': acc.account_number,
                'balance': acc.balance,
                'bank': acc.branch.bank.name,
            } for acc in accounts]
            return JsonResponse({'data': data})
