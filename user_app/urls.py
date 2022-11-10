from django.urls import path

from .views import APIProfile

urlpatterns = [
    path('user/', APIProfile.as_view())
    ]