# Generated by Django 3.2.16 on 2022-11-01 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_pyblogsitespecificsettings_youtube'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pyblogsitespecificsettings',
            name='youtube',
            field=models.URLField(default='url'),
        ),
    ]
