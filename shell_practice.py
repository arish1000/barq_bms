from datetime import date

from banks.models import Bank, BankBranch
from users.models import User
from accounts.models import BankAccount


# Create
bank = Bank.objects.create(
    name="Meezan Bank",
    swift_code="MEZNPKKA",
    is_islamic=True,
    established_date=date(1997, 1, 1)
)

bank = Bank.objects.create(
    name="MCB",
    swift_code="MEZNPKHH",
    is_islamic=True,
    established_date=date(1997, 1, 1)
)

bank = Bank.objects.create(
    name="Alflah",
    swift_code="MEZNPKYY",
    is_islamic=True,
    established_date=date(1991, 1, 1)
)



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

# get all the fields
banks = Bank.objects.values()

# get the name column only
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





















