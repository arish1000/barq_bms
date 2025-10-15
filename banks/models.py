from django.db import models


class Bank(models.Model):
    name = models.CharField(max_length=100)
    swift_code = models.CharField(max_length=11)
    is_islamic = models.BooleanField(default=False)
    established_date = models.DateField()

    class Meta:
        ordering = ["established_date"]
        verbose_name = "Bank"
        verbose_name_plural = "Banks"
        db_table = "bank"

    def __str__(self):
        return self.name


class BankBranch(models.Model):
    name = models.CharField(max_length=100)
    branch_code = models.CharField(max_length=5)
    address = models.CharField(max_length=100)

    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name='branches')

    class Meta:
        ordering = ["name"]
        verbose_name = "Branch Branch"
        verbose_name_plural = "Branch Branches"
        db_table = "branch"


    def __str__(self):
        return self.name



