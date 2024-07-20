from django.contrib import admin
from suppliers.models import Supplier


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    """Отображение модели Supplier в админ-панели Django."""

    list_display = ('name', 'email', 'country', 'city', 'level', 'supplier', 'debt', 'created_at')
    list_filter = ('city',)
    search_fields = ('name', 'city',)
    actions = ['cleanup_debt']

    def cleanup_debt(self, request, queryset):
        """Очистка задолженности перед поставщиком у выбранных объектов."""

        queryset.update(debt=0.00)

    cleanup_debt.short_description = 'Очистить задолженность'
