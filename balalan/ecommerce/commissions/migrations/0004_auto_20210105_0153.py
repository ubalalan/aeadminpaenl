# Generated by Django 3.1.3 on 2021-01-04 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commissions', '0003_auto_20210105_0139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commission',
            name='ae_commission',
        ),
        migrations.AddField(
            model_name='commission',
            name='ae_commission_rate',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=7, verbose_name='Platform Komisyon Oranı'),
            preserve_default=False,
        ),
    ]
