# Generated by Django 4.2.5 on 2023-10-07 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olx', '0012_alter_olx_fuel_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='olx',
            name='gear',
            field=models.CharField(choices=[('manual', 'Manual'), ('automatic', 'Automatic')], default='manual', max_length=500),
        ),
    ]
