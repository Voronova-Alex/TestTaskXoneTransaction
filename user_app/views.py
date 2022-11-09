from .models import Profile
from .serializers import ProfileCreateSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class APIProfile(generics.ListAPIView):
    serializer_class = ProfileCreateSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        user = self.request.user
        return Profile.objects.filter(user=user)

