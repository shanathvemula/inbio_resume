# Generated by Django 5.0.1 on 2024-02-04 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_whatido'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='years_of_exp',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
    ]