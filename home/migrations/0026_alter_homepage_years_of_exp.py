# Generated by Django 5.0.1 on 2024-02-04 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_homepage_years_of_exp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='years_of_exp',
            field=models.IntegerField(default=0),
        ),
    ]
