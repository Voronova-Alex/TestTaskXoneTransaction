from django.core.mail import send_mail
from datetime import date, timedelta
from django.contrib.auth.models import User
from user_transactions.models import Transaction, Category
from django.conf import settings


def list_user_mail():
    list_email = User.objects.all().values_list('id', 'email')
    return list_email


def user_info(user, email):
    category_user = Category.objects.filter(user_id=user)
    transaction_sum = sum(Transaction.objects.filter(user_id=user).values_list('summa_transaction', flat=True))
    transaction_statistics_user = []
    for i in category_user:
        transaction_user = Transaction.objects.filter(user_id=user, category_transaction=i,
                                                      date_transaction=date.today() - timedelta(days=1)).values_list(
            'summa_transaction', flat=True)
        if transaction_user:
            transaction_statistics_user.append(f'- {i}: {sum(transaction_user)}\n')
    if not transaction_statistics_user:
        transaction_statistics_user.append('Транзакций не было')

    return [[email], user, transaction_sum, ''.join(transaction_statistics_user)]


def send(user_info):
    print(user_info)
    send_mail('Инфо',
              f'Доброе утро, {user_info[1]}!\nТекущий баланс: {user_info[2]}.\nВчерашнии транзакции:\n{user_info[3]}',
              settings.EMAIL_HOST_USER, user_info[0])
