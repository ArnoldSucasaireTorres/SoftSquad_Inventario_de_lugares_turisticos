# Generated by Django 3.1.11 on 2021-07-30 21:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('destinos', '0003_auto_20210730_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destino',
            name='usuarios',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
