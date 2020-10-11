# Generated by Django 3.1.2 on 2020-10-11 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apex_api', '0002_auto_20201011_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertransaction',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='usertransaction',
            name='amount_in_btc',
            field=models.DecimalField(decimal_places=10, max_digits=10),
        ),
    ]
