# Generated by Django 5.1.7 on 2025-03-17 07:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0003_alter_post_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="image",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="blog.category",
            ),
        ),
    ]
