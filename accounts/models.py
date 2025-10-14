from django.db import models

from .choices import AccountType
from banks.models import BankBranch
from users.models import User


class BankAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_accounts')
    branch = models.ForeignKey(BankBranch, on_delete=models.CASCADE, related_name='branch_accounts')
    account_number = models.CharField(max_length=11)
    account_type = models.CharField(choices=AccountType.choices, default='CURRENT')
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.account_number



