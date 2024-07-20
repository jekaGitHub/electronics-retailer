from django.contrib import admin
from products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "owner",
        "name",
        "model",
        "release_date",
    )
    list_filter = ("owner", "name",)
    search_fields = ("name",)
