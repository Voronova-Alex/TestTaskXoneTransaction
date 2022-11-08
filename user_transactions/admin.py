from django.contrib import admin
from .models import Category, Transaction


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'category',)


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'user',
                    'summa_transaction',
                    'date_transaction',
                    'time_transaction',
                    'category_transaction',
                    'organization',
                    'description',)
