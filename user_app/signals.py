from django.dispatch import receiver
from djoser.signals import user_registered
from django.db.models.signals import post_save, post_delete
from .models import Profile
from user_transactions.models import Transaction, Category


@receiver(user_registered)
def create_profile(user, request, **kwargs):
    Profile.objects.create(user=user)


@receiver(post_save, sender=Transaction)
@receiver(post_delete, sender=Transaction)
def update_profile(sender, instance, created=None, **kwargs):
    user = instance.user
    profile = Profile.objects.get(user=user)
    category_user = Category.objects.filter(user=user)
    transaction_sum = sum(Transaction.objects.filter(user=user).values_list('summa_transaction', flat=True))
    transaction_statistics_user = []
    for i in category_user:
        transaction_user = Transaction.objects.filter(user=user, category_transaction=i).values_list(
            'summa_transaction', flat=True)
        transaction_statistics_user.append(f'{i} - {sum(transaction_user)}\n')
    profile.current_balance = transaction_sum
    profile.transaction_statistics = ''.join(transaction_statistics_user)
    profile.save()
