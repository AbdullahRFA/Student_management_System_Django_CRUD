# Generated by Django 5.1.6 on 2025-02-27 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('roll', models.CharField(max_length=5)),
                ('dept', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=300)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=30)),
            ],
        ),
    ]
