from django.db import models

# Create your models here.


class Bank(models.Model):
    name = models.CharField(max_length=100)
    swift_code = models.CharField(max_length=11)
    is_islamic = models.BooleanField(default=False)
    established_date = models.DateField()

    def __str__(self):
        return self.name


class BankBranch(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name='branches')
    name = models.CharField(max_length=100)
    branch_code = models.CharField(max_length=5)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name



