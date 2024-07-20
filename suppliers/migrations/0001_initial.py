# Generated by Django 4.2.2 on 2024-07-20 15:56

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('country', models.CharField(max_length=100, verbose_name='Страна')),
                ('city', models.CharField(max_length=100, verbose_name='Город')),
                ('street', models.CharField(max_length=100, verbose_name='Улица')),
                ('house', models.CharField(max_length=100, verbose_name='Номер дома')),
                ('level', models.IntegerField(choices=[(0, 'Завод'), (1, 'Розничная сеть'), (2, 'Индивидуальный предприниматель')], verbose_name='Уровень иерархии')),
                ('debt', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Задолженность перед поставщиком')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Время создания')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='suppliers', to='suppliers.supplier', verbose_name='Поставщик')),
            ],
            options={
                'verbose_name': 'Звено сети',
                'verbose_name_plural': 'Звенья сети',
            },
        ),
    ]
