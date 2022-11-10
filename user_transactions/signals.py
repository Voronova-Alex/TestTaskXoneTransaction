from django.dispatch import receiver
from djoser.signals import user_registered

from .models import Category

DEFAULT_CATEGORY = ["Забота о себе",
                    "Зарплата",
                    "Здоровье и фитнес",
                    "Кафе и рестораны",
                    "Машина",
                    "Образование",
                    "Отдых и развлечения",
                    "Платежи, комиссии",
                    "Покупки: одежда, техника",
                    "Продукты",
                    "Проезд"
                    ]

@receiver(user_registered)
def create_user_default_category(user, request, **kwargs):
    for i in DEFAULT_CATEGORY:
        Category.objects.create(user=user, category=i)
