# Generated by Django 5.0.1 on 2024-02-05 08:15

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0040_rename_logo_portfolio_portfolio_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='likes',
        ),
        migrations.AddField(
            model_name='portfolio',
            name='description2',
            field=wagtail.fields.RichTextField(blank=True),
        ),
    ]
