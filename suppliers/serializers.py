from rest_framework.serializers import ModelSerializer

from suppliers.models import Supplier


class SupplierSerializer(ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'
        read_only_fields = ['debt']
