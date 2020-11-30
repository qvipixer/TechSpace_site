# Generated by Django 3.1.2 on 2020-11-30 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20201201_0002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='description_full',
        ),
        migrations.RemoveField(
            model_name='project',
            name='description_short',
        ),
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.TextField(default=123, verbose_name='Описание проекта'),
            preserve_default=False,
        ),
    ]