# Generated by Django 3.1.3 on 2020-12-29 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20201229_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='decription',
            field=models.CharField(max_length=200, null=True, verbose_name='Ürün Yorumları'),
        ),
        migrations.AlterField(
            model_name='track',
            name='images',
            field=models.CharField(max_length=200, null=True, verbose_name='Resim Link'),
        ),
    ]
