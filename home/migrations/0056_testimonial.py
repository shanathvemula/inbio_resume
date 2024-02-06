# Generated by Django 5.0.1 on 2024-02-06 20:15

import django.core.validators
import django.db.models.deletion
import modelcluster.fields
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0055_alter_experience_end_date'),
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('subtitle', wagtail.fields.RichTextField()),
                ('title', wagtail.fields.RichTextField()),
                ('designation', wagtail.fields.RichTextField()),
                ('app_name', wagtail.fields.RichTextField()),
                ('app_date', wagtail.fields.RichTextField()),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('description', wagtail.fields.RichTextField()),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='testimonial', to='home.homepage')),
                ('thumbnail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
