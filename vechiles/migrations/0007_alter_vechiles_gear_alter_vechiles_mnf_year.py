# Generated by Django 4.2.5 on 2023-10-10 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vechiles', '0006_alter_vechiles_gear_alter_vechiles_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vechiles',
            name='gear',
            field=models.CharField(choices=[('manual', 'Manual'), ('automatic', 'Automatic'), ('no_gear', 'No Gear')], default='manual', max_length=500),
        ),
        migrations.AlterField(
            model_name='vechiles',
            name='mnf_year',
            field=models.DateTimeField(),
        ),
    ]
