from django.db import models

from config import settings

NULLABLE = {"blank": True, "null": True}


class Product(models.Model):
    """Модель продукта."""

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        **NULLABLE,
        verbose_name="Владелец продукта",
        help_text="Укажите владельца продукта"
    )

    name = models.CharField(max_length=255, verbose_name='Название продукта', help_text='Введите название продукта')
    model = models.CharField(max_length=255, verbose_name='Модель продукта', help_text='Введите модель продукта')
    release_date = models.DateField(verbose_name='Дата выхода продукта на рынок')

    def __str__(self):
        return f'{self.name} - {self.model}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
