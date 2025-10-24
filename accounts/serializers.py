from rest_framework import serializers

from accounts.models import Account


class AccountsListSerializer(serializers.ModelSerializer):
    bank_name = serializers.CharField(source="branch.bank.name", read_only=True)

    
    class Meta:
        model = Account
        fields = ["id", "account_number", "balance", "bank_name"]


class AccountsCreateSerializer(serializers.ModelSerializer):


    class Meta:
        model = Account
        fields = "__all__"


class AccountBalanceUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Account
        fields = ["balance"]
    
    def validate_balance(self, value):
        if value < 0:
            raise serializers.ValidationError("Balance cannot be negative.")
        return value
