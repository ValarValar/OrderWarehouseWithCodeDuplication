# Generated by Django 4.2 on 2023-04-22 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_name', models.CharField(max_length=30, verbose_name='Название заказа')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('status', models.IntegerField(choices=[(1, 'New'), (2, 'In Process'), (3, 'Stored'), (4, 'Complete')], default=1)),
            ],
        ),
    ]
