# Generated by Django 4.1.1 on 2022-09-21 21:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('completed', models.BooleanField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Yarn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=50)),
                ('color_code', models.CharField(max_length=7)),
                ('amount_owned', models.IntegerField()),
                ('size', models.IntegerField()),
                ('material', models.CharField(max_length=50)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='YarnsForProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_needed', models.IntegerField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyKnitting.project')),
                ('yarn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyKnitting.yarn')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.FileField(upload_to='project_photos')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyKnitting.project')),
            ],
        ),
        migrations.CreateModel(
            name='Pattern',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pattern', models.FileField(upload_to='project_pattern')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyKnitting.project')),
            ],
        ),
        migrations.CreateModel(
            name='NeedlesForProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_needed', models.IntegerField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyKnitting.project')),
                ('yarn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyKnitting.yarn')),
            ],
        ),
        migrations.CreateModel(
            name='Needle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('size', models.IntegerField()),
                ('length', models.IntegerField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
