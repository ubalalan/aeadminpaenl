# Generated by Django 3.1.3 on 2021-01-10 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commissions', '0015_auto_20210111_0113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commission',
            name='dollar',
            field=models.DecimalField(decimal_places=2, max_digits=3, verbose_name='Kur Fiyatı'),
        ),
    ]
