# Generated by Django 5.0.1 on 2024-02-04 14:45

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_alter_homepage_years_of_exp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='years_of_exp',
            field=wagtail.fields.RichTextField(default=0),
        ),
    ]
