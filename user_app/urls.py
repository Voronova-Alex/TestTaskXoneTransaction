from django.urls import path

from .views import APIProfile

urlpatterns = [
    path('', APIProfile.as_view())
    ]