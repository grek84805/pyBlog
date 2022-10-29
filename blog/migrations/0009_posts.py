# Generated by Django 3.2.16 on 2022-10-28 19:20

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0077_alter_revision_user'),
        ('blog', '0008_alter_node_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('date', models.DateField(verbose_name='Post date')),
                ('body', wagtail.fields.RichTextField(blank=True)),
                ('categories', modelcluster.fields.ParentalManyToManyField(blank=True, to='blog.Node')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]