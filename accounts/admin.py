from django.contrib import admin
from accounts.models import BankAccount

# Register your models here.

@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'branch', 'account_number', 'account_type', 'balance', 'is_active')
    list_filter = ('is_active', 'account_type')
    search_fields = ('user__username', 'user__email')

