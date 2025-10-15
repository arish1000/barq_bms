from django.db import models

from accounts.choices import AccountType
from banks.models import BankBranch
from users.models import User, BaseModel


class BankAccount(BaseModel):
    account_number = models.CharField(max_length=11)
    account_type = models.CharField(choices=AccountType.choices, default=AccountType.CURRENT)
    balance = models.PositiveIntegerField(max_length=11)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_accounts")
    branch = models.ForeignKey(BankBranch, on_delete=models.CASCADE, related_name="branch_accounts")

    class Meta:
        verbose_name = "Bank Account"
        verbose_name_plural = "Bank Accounts"
        db_table = "bank_accounts"

    def __str__(self):
        return self.account_number



