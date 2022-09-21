# Generated by Django 4.1.1 on 2022-09-21 21:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MyKnitting', '0003_needlesforproject'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Needle',
            new_name='Needles',
        ),
        migrations.RenameField(
            model_name='needlesforproject',
            old_name='needle',
            new_name='needles',
        ),
        migrations.AddField(
            model_name='project',
            name='public',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
