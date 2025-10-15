from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User

@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ("username", "email")
    search_fields = ("username", "email")
