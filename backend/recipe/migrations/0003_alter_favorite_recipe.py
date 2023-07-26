# Generated by Django 3.2 on 2023-07-18 18:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("recipe", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="favorite",
            name="recipe",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="favorites",
                to="recipe.recipe",
            ),
        ),
    ]