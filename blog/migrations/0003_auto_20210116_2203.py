# Generated by Django 3.1.5 on 2021-01-17 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210116_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='short_biography',
            field=models.TextField(max_length=400),
        ),
    ]
