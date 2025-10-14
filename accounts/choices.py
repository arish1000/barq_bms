from django.db import models


class AccountType(models.TextChoices):
    CURRENT = 'CURRENT', 'Current'
    SAVING = 'SAVING', 'Saving'