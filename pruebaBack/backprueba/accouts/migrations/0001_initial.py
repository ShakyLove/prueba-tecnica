# Generated by Django 4.2.1 on 2023-06-03 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('value_count', models.DecimalField(decimal_places=2, max_digits=10)),
                ('identification', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('tarjet_number', models.CharField(max_length=16)),
                ('account_number', models.CharField(max_length=20)),
                ('csv_number', models.CharField(max_length=4)),
                ('tarjet_date', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movements', to='accouts.account')),
            ],
        ),
    ]