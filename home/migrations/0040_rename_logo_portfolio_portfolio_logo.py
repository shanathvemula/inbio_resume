# Generated by Django 5.0.1 on 2024-02-05 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0039_portfolio_delete_portfolios'),
    ]

    operations = [
        migrations.RenameField(
            model_name='portfolio',
            old_name='logo',
            new_name='portfolio_logo',
        ),
    ]
