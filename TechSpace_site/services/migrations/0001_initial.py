# Generated by Django 3.2.7 on 2021-10-04 03:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Services_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'Категорию услуг',
                'verbose_name_plural': 'Категории услуг',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Services_subCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategory', to='services.services_category')),
            ],
            options={
                'verbose_name': 'Подкатегорию услуг',
                'verbose_name_plural': 'Подкатегории услуг',
                'ordering': ('name',),
            },
        ),
    ]
