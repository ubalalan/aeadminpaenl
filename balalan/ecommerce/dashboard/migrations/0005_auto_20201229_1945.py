# Generated by Django 3.1.3 on 2020-12-29 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20201229_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='decription',
            field=models.CharField(max_length=200, null=True, verbose_name='Ürün Yorumları'),
        ),
        migrations.AddField(
            model_name='track',
            name='discount_price',
            field=models.IntegerField(blank=True, null=True, verbose_name='İndirim Fiyatı'),
        ),
        migrations.AddField(
            model_name='track',
            name='images',
            field=models.CharField(max_length=200, null=True, verbose_name='Resim Link'),
        ),
        migrations.AddField(
            model_name='track',
            name='link',
            field=models.CharField(max_length=200, null=True, verbose_name='Link '),
        ),
    ]
