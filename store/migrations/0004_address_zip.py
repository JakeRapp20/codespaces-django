# Generated by Django 4.2.2 on 2023-06-23 03:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0003_add_slug_to_product"),
    ]

    operations = [
        migrations.AddField(
            model_name="address",
            name="zip",
            field=models.CharField(default="84401", max_length=6),
            preserve_default=False,
        ),
    ]
