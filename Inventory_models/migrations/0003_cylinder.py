# Generated by Django 4.2.5 on 2024-01-31 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory_models', '0002_line_graph_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cylinder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diameter', models.CharField()),
                ('height', models.CharField()),
            ],
        ),
    ]