# Generated by Django 4.1.1 on 2022-09-21 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MyKnitting', '0002_delete_needlesforproject'),
    ]

    operations = [
        migrations.CreateModel(
            name='NeedlesForProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('needle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyKnitting.needle')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyKnitting.project')),
            ],
        ),
    ]
