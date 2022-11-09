from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    current_balance = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Текущий баланс', default='0.00')
    transaction_statistics = models.TextField(verbose_name='Статистика', default='Нет данных')

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'