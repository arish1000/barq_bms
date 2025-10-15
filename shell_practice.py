from datetime import date
from django.db.models import Count

from banks.models import Bank, BankBranch
from users.models import User
from accounts.models import BankAccount


# Create banks
banks = [
    {"name": "ABC Bank", "swift_code": "ABC12345678", "is_islamic": False, "established_date": date(1990, 5, 12)},
    {"name": "XYZ Islamic Bank", "swift_code": "XYZ87654321", "is_islamic": True, "established_date": date(2000, 3, 20)},
    {"name": "National Bank", "swift_code": "NAT11223344", "is_islamic": False, "established_date": date(1985, 7, 15)},
]
for bank in banks:
    Bank.objects.create(**bank)

# Create Branches
banks = Bank.objects.all()
for bank in banks:
    branches_data = [
        {"name": f"{bank.name} Main Branch", "branch_code": "001", "address": "Main Street 1"},
        {"name": f"{bank.name} City Branch", "branch_code": "002", "address": "City Center 5"},
        {"name": f"{bank.name} Suburb Branch", "branch_code": "003", "address": "Suburb Road 10"},
    ]
    for branch_data in branches_data:
        BankBranch.objects.create(bank=bank, **branch_data)

# Filter
islamic_banks = Bank.objects.filter(is_islamic=True)
non_islamic_banks = Bank.objects.filter(is_islamic=False)
and_query = Bank.objects.filter(is_islamic=True, name="Meezan Bank")

# Filter Islamic banks with active accounts
banks = Bank.objects.filter(is_islamic=True, branches__branch_accounts__is_active=True)

# Get
bank = Bank.objects.get(name="Meezan Bank")
bank = Bank.objects.get(pk=1)

# Values
banks = Bank.objects.values()
banks = Bank.objects.values('name')

# Select_related
branches = BankBranch.objects.select_related('bank')
accounts = BankAccount.objects.select_related('user')
accounts = BankAccount.objects.select_related('branch')
accounts = BankAccount.objects.select_related('user', 'branch')

# Prefetch_related
banks = Bank.objects.prefetch_related('branches')
banks = Bank.objects.prefetch_related('branches', 'branches__branch_accounts')
users = User.objects.prefetch_related('user_accounts')

# Annotate
banks = Bank.objects.annotate(
    total_accounts=Count('branches__branch_accounts')
)
