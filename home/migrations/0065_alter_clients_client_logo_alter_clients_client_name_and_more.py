# Generated by Django 5.0.1 on 2024-02-07 04:28

import django.db.models.deletion
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0064_alter_clients_client_url_alter_clients_language'),
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='client_logo',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailimages.image'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='clients',
            name='client_name',
            field=wagtail.fields.RichTextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='clients',
            name='client_url',
            field=wagtail.fields.RichTextField(default=''),
            preserve_default=False,
        ),
    ]
