# Generated by Django 4.2.5 on 2024-02-08 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory_models', '0006_alter_cylinder_volume_of_tanks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cylinder',
            name='volume_of_tanks',
        ),
    ]
