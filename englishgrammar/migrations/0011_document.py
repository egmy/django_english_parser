# Generated by Django 4.0.3 on 2022-04-23 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('englishgrammar', '0010_language'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docfile', models.FileField(upload_to='documents/%Y/%m/%d')),
            ],
        ),
    ]
