from django.db import models
from users.models import BaseModel

class Bank(BaseModel):
    name = models.CharField(max_length=100)
    swift_code = models.CharField(max_length=11)
    is_islamic = models.BooleanField(default=False)
    established_date = models.DateField()


    class Meta:
        verbose_name = "Bank"
        verbose_name_plural = "Banks"
        db_table = "bank"

    def __str__(self):
        return self.name


class BankBranch(BaseModel):
    name = models.CharField(max_length=100)
    branch_code = models.CharField(max_length=5)
    address = models.CharField(max_length=100)

    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name="bank_branches")

    class Meta:
        verbose_name = "Branch"
        verbose_name_plural = "Branches"
        db_table = "branch"


    def __str__(self):
        return self.name



