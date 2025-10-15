from django.contrib import admin
from banks.models import Bank, BankBranch


@admin.register(Bank)
class AdminBank(admin.ModelAdmin):
    list_display = ("name", "is_islamic")
    list_filter = ("is_islamic",)
    search_fields = ("name",)


@admin.register(BankBranch)
class AdminBankBranch(admin.ModelAdmin):
    list_display = ("bank", "name")
    list_filter = ("bank",)
    search_fields = ("bank__name", "name",)


