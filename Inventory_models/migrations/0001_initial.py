# Generated by Django 4.2.5 on 2024-01-29 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recieved_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag1', models.IntegerField()),
                ('tag2', models.IntegerField()),
                ('tag3', models.IntegerField()),
                ('tag4', models.IntegerField()),
                ('tag5', models.IntegerField()),
                ('tag6', models.IntegerField()),
                ('tag7', models.IntegerField()),
                ('tag8', models.IntegerField()),
            ],
        ),
    ]
