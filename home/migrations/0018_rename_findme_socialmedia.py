# Generated by Django 5.0.1 on 2024-02-03 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_remove_homepage_favicon'),
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FindMe',
            new_name='SocialMedia',
        ),
    ]
