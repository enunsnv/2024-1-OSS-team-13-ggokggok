# Generated by Django 4.2.11 on 2024-04-18 07:10

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PlaceInfo",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=200)),
                ("address", models.TextField()),
                ("review", models.IntegerField()),
                ("category", models.CharField(max_length=50)),
            ],
        ),
    ]
