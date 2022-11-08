from rest_framework import serializers
from .models import Category, Transaction


class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'category',)


class TransactionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('id',
                  'summa_transaction',
                  'date_transaction',
                  'time_transaction',
                  'category_transaction',
                  'organization',
                  'description',
                  )
