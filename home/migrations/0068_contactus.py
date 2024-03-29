# Generated by Django 5.0.1 on 2024-02-07 12:03

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0067_homepage_contact_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('your_name', models.CharField(max_length=250)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=2500)),
                ('message', models.TextField()),
            ],
            options={
                'db_table': 'ContactUs',
            },
        ),
    ]
