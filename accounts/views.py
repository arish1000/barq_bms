from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator

from accounts.models import Account

@method_decorator(login_required(login_url="/login/"), name="dispatch")
class AccountsListView(View):
    def get(self, request, *args, **kwargs):
            accounts = Account.objects.select_related("branch__bank").filter(user=request.user)
            data = [ {
                "account_number": acc.account_number,
                "balance": acc.balance,
                "bank": acc.branch.bank.name,
            } for acc in accounts]
            
            return JsonResponse({"data": data})
