# Generated by Django 3.2.16 on 2022-11-03 00:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_coursesindexpage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogindexpage',
            options={'verbose_name': 'Category Blog Page', 'verbose_name_plural': 'Categories Blog Pages'},
        ),
    ]