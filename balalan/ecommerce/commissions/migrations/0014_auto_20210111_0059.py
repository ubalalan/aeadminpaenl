# Generated by Django 3.1.3 on 2021-01-10 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commissions', '0013_auto_20210110_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commission',
            name='dollar',
            field=models.DecimalField(decimal_places=2, max_digits=3, verbose_name='Kur Fiyatı'),
        ),
    ]
