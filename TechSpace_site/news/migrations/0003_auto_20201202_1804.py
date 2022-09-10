# Generated by Django 3.1.2 on 2020-12-02 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('home', '0001_initial'),
        ('news', '0002_auto_20201201_0034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='article',
                                    to='home.category'),
        ),
        migrations.AlterField(
            model_name='article',
            name='subcategory',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='article',
                                    to='home.subcategory'),
        ),
    ]
