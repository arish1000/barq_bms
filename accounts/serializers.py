from rest_framework import serializers

from accounts.models import Account


class AccountsListSerializer(serializers.ModelSerializer):
    bank_name = serializers.CharField(source='branch.bank.name', read_only=True)
    
    class Meta:
        model = Account
        fields = ['account_number', 'balance', 'bank_name']
