# Generated by Django 5.0.3 on 2024-04-17 09:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0005_remove_placepost_address_remove_placepost_name_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='placepost',
            name='recommended',
            field=models.ManyToManyField(blank=True, related_name='recommended_placepost', to=settings.AUTH_USER_MODEL),
        ),
    ]
