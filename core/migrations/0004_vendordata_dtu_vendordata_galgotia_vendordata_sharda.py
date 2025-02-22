# Generated by Django 5.1.2 on 2024-11-25 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_vendordata_bennett'),
    ]

    operations = [
        migrations.CreateModel(
            name='VendorData_Dtu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254)),
                ('shop_name', models.CharField(max_length=100)),
                ('info', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='VendorData_Galgotia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254)),
                ('shop_name', models.CharField(max_length=100)),
                ('info', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='VendorData_sharda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254)),
                ('shop_name', models.CharField(max_length=100)),
                ('info', models.TextField()),
            ],
        ),
    ]
