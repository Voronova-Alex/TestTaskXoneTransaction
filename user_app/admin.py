from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'current_balance', 'transaction_statistics',)
