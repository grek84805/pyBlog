# Generated by Django 3.2.16 on 2022-11-01 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_auto_20221101_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pyblogsitespecificsettings',
            name='site_name',
            field=models.CharField(blank=True, max_length=254, null=True, verbose_name='First name'),
        ),
    ]