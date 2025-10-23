from rest_framework import serializers

from banks.models import Bank


class BankListSerializer(serializers.ModelSerializer):
    branch_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Bank
        fields = ["id", "name", "is_islamic", "branch_count"]


class BankCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bank
        fields = ['name', 'swift_code', 'is_islamic', 'established_date']