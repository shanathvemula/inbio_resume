# Generated by Django 5.0.1 on 2024-02-07 04:23

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0062_alter_clients_client_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='client_name',
            field=wagtail.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='language',
            field=wagtail.fields.RichTextField(blank=True, null=True),
        ),
    ]
