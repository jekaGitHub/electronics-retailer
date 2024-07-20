from django.contrib.auth.models import AbstractUser
from django.db import models


from suppliers.models import NULLABLE


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name="Email")

    phone = models.CharField(
        max_length=35,
        verbose_name="Номер телефона",
        help_text="Укажите телефон",
        **NULLABLE
    )
    city = models.CharField(
        max_length=35, verbose_name="Город", help_text="Укажите город", **NULLABLE
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
