from .models import Category, Transaction
from .serializers import CategoryCreateSerializer, TransactionCreateSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class ApiCategoryList(generics.ListAPIView):
    serializer_class = CategoryCreateSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        user = self.request.user
        return Category.objects.filter(user=user)

class ApiTransactionList(generics.ListAPIView):
    serializer_class = TransactionCreateSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['date_transaction', 'time_transaction', 'summa_transaction']

    def get_queryset(self):
        user = self.request.user
        return Transaction.objects.filter(user=user)