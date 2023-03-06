# Generated by Django 4.1.5 on 2023-02-25 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_app', '0002_add_products_alter_add_category_category_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ADD_Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.CharField(max_length=20)),
                ('recipe_ingredients', models.TextField()),
                ('recipe_instructions', models.TextField()),
                ('recipe_image', models.ImageField(upload_to='sample')),
            ],
        ),
    ]
