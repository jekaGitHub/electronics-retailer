from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from products.models import Product
from products.serializers import ProductSerializer
from users.permissions import IsOwner


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        """Права доступа. Создавать продукт может только авторизованный пользователь.
        Просмотреть список, просмотреть один объект, а также обновить и удалить может только авторизованный владелец."""

        if self.action == 'create':
            self.permission_classes = (IsAuthenticated,)
        elif self.action in ['list', 'update', 'retrieve']:
            self.permission_classes = (IsAuthenticated, IsOwner,)
        elif self.action == 'destroy':
            self.permission_classes = (IsAuthenticated, IsOwner,)
        return super().get_permissions()

    def perform_create(self, serializer):
        """Создание продукта и автоматическое добавление владельца к продукту."""

        product = serializer.save()
        product.owner = self.request.user
        product.save()
