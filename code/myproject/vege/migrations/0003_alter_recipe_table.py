# Generated by Django 5.0.1 on 2024-01-17 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0002_rename_recipe_description_recipe_receipe_description_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='recipe',
            table='vege_recipe',
        ),
    ]
