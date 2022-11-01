# Generated by Django 3.2.16 on 2022-11-01 09:07

from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.embeds.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0024_index_image_file_hash'),
        ('wagtailcore', '0077_alter_revision_user'),
        ('base', '0003_standardpage_search_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='standardpage',
            options={'verbose_name': 'Standard page', 'verbose_name_plural': 'Standard pages'},
        ),
        migrations.AddField(
            model_name='homepage',
            name='body',
            field=wagtail.fields.StreamField([('heading_block', wagtail.blocks.StructBlock([('heading_text', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('size', wagtail.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4')], required=False))])), ('paragraph_block', wagtail.blocks.RichTextBlock(icon='fa-paragraph', template='blocks/paragraph_block.html')), ('image_block', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.blocks.CharBlock(required=False)), ('attribution', wagtail.blocks.CharBlock(required=False))])), ('block_quote', wagtail.blocks.StructBlock([('text', wagtail.blocks.TextBlock()), ('attribute_name', wagtail.blocks.CharBlock(blank=True, label='e.g. Mary Berry', required=False))])), ('code', wagtail.blocks.StructBlock([('language', wagtail.blocks.ChoiceBlock(choices=[('bash', 'Bash/Shell'), ('css', 'CSS'), ('diff', 'diff'), ('html', 'HTML'), ('javascript', 'Javascript'), ('json', 'JSON'), ('python', 'Python'), ('scss', 'SCSS'), ('yaml', 'YAML')], help_text='Coding language', identifier='language', label='Language')), ('code', wagtail.blocks.TextBlock(identifier='code', label='Code'))], label='Code')), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/watch?v=SGJFWirQ3ks', icon='fa-s15', template='blocks/embed_block.html'))], blank=True, use_json_field=True, verbose_name='Home content block'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='featured_section_1',
            field=models.ForeignKey(blank=True, help_text='First featured section for the homepage. Will display up to three child items.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Featured section 1'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='featured_section_1_title',
            field=models.CharField(blank=True, help_text='Title to display above the promo copy', max_length=255),
        ),
        migrations.AddField(
            model_name='homepage',
            name='featured_section_2',
            field=models.ForeignKey(blank=True, help_text='Second featured section for the homepage. Will display up to three child items.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Featured section 2'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='featured_section_2_title',
            field=models.CharField(blank=True, help_text='Title to display above the promo copy', max_length=255),
        ),
        migrations.AddField(
            model_name='homepage',
            name='featured_section_3',
            field=models.ForeignKey(blank=True, help_text='Third featured section for the homepage. Will display up to six child items.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Featured section 3'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='featured_section_3_title',
            field=models.CharField(blank=True, help_text='Title to display above the promo copy', max_length=255),
        ),
        migrations.AddField(
            model_name='homepage',
            name='hero_cta',
            field=models.CharField(default=True, help_text='Text to display on Call to Action', max_length=255, verbose_name='Hero CTA'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homepage',
            name='hero_cta_link',
            field=models.ForeignKey(blank=True, help_text='Choose a page to link to for the Call to Action', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Hero CTA link'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='hero_text',
            field=models.CharField(default=True, help_text='Write an introduction for the bakery', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homepage',
            name='image',
            field=models.ForeignKey(blank=True, help_text='Homepage image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='promo_image',
            field=models.ForeignKey(blank=True, help_text='Promo image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='promo_text',
            field=wagtail.fields.RichTextField(blank=True, help_text='Write some promotional copy', max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='promo_title',
            field=models.CharField(blank=True, help_text='Title to display above the promo copy', max_length=255),
        ),
    ]
