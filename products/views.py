from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from products.models import Product
from products.serializers import ProductSerializer
from users.permissions import IsOwner


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_create(self, serializer):
        """Создание продукта и автоматическое добавление владельца к продукту."""

        product = serializer.save()
        product.owner = self.request.user
        product.save()
