# Generated by Django 4.0.3 on 2022-04-17 20:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('englishgrammar', '0004_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='sentence',
            new_name='noun',
        ),
    ]
