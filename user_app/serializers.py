from rest_framework import serializers

from .models import Profile


class ProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'current_balance', 'transaction_statistics',)
