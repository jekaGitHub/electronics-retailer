from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter

from suppliers.models import Supplier
from suppliers.serializers import SupplierSerializer
from users.permissions import IsOwner


class SupplierViewSet(ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    filter_backends = [SearchFilter]
    search_fields = ['country']

    def get_permissions(self):
        """Права доступа. Создавать звено торговой сети может только авторизованный пользователь.
        Просмотреть список, просмотреть один объект, а также обновить и удалить может только авторизованный владелец."""

        if self.action == 'create':
            self.permission_classes = (IsAuthenticated,)
        elif self.action in ['list', 'update', 'retrieve']:
            self.permission_classes = (IsAuthenticated, IsOwner,)
        elif self.action == 'destroy':
            self.permission_classes = (IsAuthenticated, IsOwner,)
        return super().get_permissions()

    def perform_create(self, serializer):
        """Создание звена торговой сети и автоматическое добавление владельца."""

        serializer.save(owner=self.request.user)
