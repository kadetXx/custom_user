# Generated by Django 3.1.1 on 2020-09-27 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useramount',
            name='user_amount',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=19),
        ),
    ]
