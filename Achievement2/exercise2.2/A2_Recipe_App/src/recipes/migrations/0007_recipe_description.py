# Generated by Django 4.2.6 on 2023-10-27 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_alter_recipe_ingredients'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='description',
            field=models.CharField(default='', max_length=500),
        ),
    ]