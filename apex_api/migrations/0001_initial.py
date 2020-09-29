# Generated by Django 3.1.1 on 2020-09-28 13:50

import apex_api.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('full_name', models.CharField(max_length=50)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'User',
            },
        ),
        migrations.CreateModel(
            name='RecentTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid')], max_length=60)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('merchant', models.CharField(max_length=60)),
                ('transaction_type', models.CharField(choices=[('Deposit', 'Deposit'), ('Withdrawal', 'Withdrawal')], max_length=60)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('currency', models.CharField(choices=[('Ξ ETH', 'Ξ ETH'), ('฿ BTC', '฿ BTC')], max_length=5)),
                ('tokens', models.DecimalField(decimal_places=2, max_digits=9)),
                ('details', models.CharField(choices=[('Deposit to wallet', 'Deposit to wallet'), ('Withdrawal from wallet', 'Withdrawal from wallet')], max_length=100)),
            ],
            options={
                'verbose_name': 'Recent Transactions',
                'verbose_name_plural': 'Recent Transactions',
            },
        ),
        migrations.CreateModel(
            name='UserTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('transaction_type', models.CharField(choices=[('Deposit', 'Deposit'), ('Withdrawal', 'Withdrawal')], max_length=200)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_method', models.CharField(max_length=100)),
                ('status', models.CharField(default='Pending', max_length=100)),
                ('amount_in_btc', models.DecimalField(decimal_places=7, max_digits=10)),
                ('details', models.CharField(choices=[('Deposit to wallet', 'Deposit to wallet'), ('Withdrawal from wallet', 'Withdrawal from wallet')], max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Transactions',
                'verbose_name_plural': 'User Transactions',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='fdhdfs.jpg', upload_to='profile_pics')),
                ('trading_code', models.CharField(blank=True, default=apex_api.models.create_trading_code, max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profile',
            },
        ),
    ]
