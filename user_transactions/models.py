from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    category = models.CharField(max_length=30, verbose_name='Категория')

    def __str__(self):
        return self.category


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'



class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    summa_transaction = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Сумма транзакции')
    date_transaction = models.DateField(auto_now_add=True, verbose_name='Дата транзакции')
    time_transaction = models.TimeField(auto_now_add=True, verbose_name='Время транзакции')
    category_transaction = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    organization = models.CharField(max_length=30, verbose_name='Организация')
    description = models.TextField(verbose_name='Описание')


    class Meta:
        verbose_name = 'Tранзакция'
        verbose_name_plural = 'Tранзакции'




# Create your models here.
