# Generated by Django 4.2.5 on 2023-10-07 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olx', '0009_alter_olx_fuel_type_alter_olx_gear'),
    ]

    operations = [
        migrations.AlterField(
            model_name='olx',
            name='fuel_type',
            field=models.CharField(choices=[('petrol', 'Petrol'), ('cng', 'CNG'), ('desel', 'Desel')], default='petrol', max_length=200),
        ),
    ]
