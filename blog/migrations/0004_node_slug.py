# Generated by Django 3.2.16 on 2022-10-28 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True),
        ),
    ]
