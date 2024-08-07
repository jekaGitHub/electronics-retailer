# Generated by Django 4.2.2 on 2024-07-20 14:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название продукта', max_length=255, verbose_name='Название продукта')),
                ('model', models.CharField(help_text='Введите модель продукта', max_length=255, verbose_name='Модель продукта')),
                ('release_date', models.DateField(verbose_name='Дата выхода продукта на рынок')),
                ('owner', models.ForeignKey(blank=True, help_text='Укажите владельца продукта', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Владелец продукта')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
    ]
