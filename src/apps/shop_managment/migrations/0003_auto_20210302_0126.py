# Generated by Django 3.1 on 2021-03-02 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_managment', '0002_auto_20210302_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
