# Generated by Django 4.0.3 on 2022-04-17 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('englishgrammar', '0003_delete_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sentence', models.IntegerField()),
            ],
        ),
    ]
