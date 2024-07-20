from django.contrib import admin
from products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "owner",
        "title",
        "model",
        "release_date",
    )
    list_filter = ("owner", "title",)
    search_fields = ("title",)
