from django.db import models
from django.utils import timezone

NULLABLE = {"blank": True, "null": True}


class Supplier(models.Model):
    """Модель поставщика торговой сети электроники."""

    LEVEL_CHOICES = [
        (0, 'Завод'),
        (1, 'Розничная сеть'),
        (2, 'Индивидуальный предприниматель'),
    ]

    name = models.CharField(max_length=100, verbose_name='Название')
    email = models.EmailField(unique=True, verbose_name='Email')
    country = models.CharField(max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=100, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица')
    house = models.CharField(max_length=100, verbose_name='Номер дома')
    level = models.IntegerField(choices=LEVEL_CHOICES, verbose_name='Уровень иерархии')
    supplier = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        **NULLABLE,
        verbose_name='Поставщик',
        related_name='suppliers'
    )
    debt = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
        verbose_name='Задолженность перед поставщиком'
    )
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Время создания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Звено сети'
        verbose_name_plural = 'Звенья сети'
