# Generated by Django 4.2.5 on 2024-02-08 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory_models', '0009_alter_cylinder_tanks_volume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cylinder',
            name='tanks_volume',
            field=models.IntegerField(default=0),
        ),
    ]
