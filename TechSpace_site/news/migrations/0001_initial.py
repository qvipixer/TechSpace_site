# Generated by Django 3.1.2 on 2020-11-29 23:55

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='не определено', max_length=128, verbose_name='Заголовок')),
                ('create', models.DateField(default=datetime.date.today, verbose_name='Дата добавления')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')),
                ('description_short', models.TextField(verbose_name='Короткое описание')),
                ('description_full', models.TextField(verbose_name='Полное описание')),
                ('author', models.CharField(default='не определено', max_length=64, verbose_name='Автор')),
                ('image',
                 models.ImageField(blank=True, default='null.jpg', upload_to='article/%Y/%m/%d', verbose_name='Эскиз')),
                ('slug', models.SlugField(max_length=200, verbose_name='URL')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article',
                                               to='home.category')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article',
                                                  to='home.subcategory')),
                ('tags', models.ManyToManyField(blank=True, related_name='article', to='home.Tags')),
            ],
            options={
                'verbose_name': 'Статью',
                'verbose_name_plural': 'Статьи',
            },
        ),
    ]
