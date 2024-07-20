from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter

from suppliers.models import Supplier
from suppliers.serializers import SupplierSerializer
from users.permissions import IsOwner


class SupplierViewSet(ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    filter_backends = [SearchFilter]
    search_fields = ['country']

    def perform_create(self, serializer):
        """Создание звена торговой сети и автоматическое добавление владельца."""

        serializer.save(owner=self.request.user)
