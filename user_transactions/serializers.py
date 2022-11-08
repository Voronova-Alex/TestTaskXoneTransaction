from rest_framework import serializers
from .models import Category, Transaction


class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('category',)


class TransactionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('summa_transaction',
                  'date_time_transaction',
                  'category_transaction',
                  'organization',
                  'description',
                  )
