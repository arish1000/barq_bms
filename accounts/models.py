from django.db import models

from accounts.choices import AccountType
from users.models import BaseModel


class Account(BaseModel):
    account_number = models.CharField(max_length=11)
    account_type = models.CharField(choices=AccountType.choices, default=AccountType.CURRENT)
    balance = models.PositiveIntegerField(max_length=11)

    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="user_accounts")
    branch = models.ForeignKey("banks.Branch", on_delete=models.CASCADE, related_name="bank_accounts")


    class Meta:
        verbose_name = "Bank Account"
        verbose_name_plural = "Bank Accounts"
        db_table = "bank_accounts"

    def __str__(self):
        return f"{self.account_number}-{self.user.username}"
