# Generated by Django 5.0.1 on 2024-02-03 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_homepage_favicon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='favicon',
        ),
    ]
