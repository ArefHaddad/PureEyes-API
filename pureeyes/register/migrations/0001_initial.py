# Generated by Django 5.0.4 on 2024-04-03 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_name', models.CharField(max_length=100)),
                ('animal_name', models.CharField(max_length=100)),
                ('animal_age', models.IntegerField()),
                ('animal_type', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('mobile_number', models.CharField(max_length=20)),
                ('notes', models.TextField()),
            ],
        ),
    ]
