from django.contrib import admin
from .models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = ("owner", "platform", "username", "password")
admin.site.register(Account, AccountAdmin)