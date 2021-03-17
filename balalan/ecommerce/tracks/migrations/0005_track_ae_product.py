# Generated by Django 3.1.3 on 2021-01-08 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20210108_2139'),
        ('tracks', '0004_auto_20210107_0050'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='ae_product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.product', verbose_name='Ürün Bilgisi -AE'),
        ),
    ]
