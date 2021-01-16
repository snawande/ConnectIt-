# Generated by Django 3.1.4 on 2021-01-16 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default='YYYY-MM-DD')),
                ('student_name', models.CharField(max_length=100)),
                ('uni_name', models.CharField(max_length=100)),
                ('program_name', models.CharField(max_length=100)),
                ('term', models.CharField(max_length=100)),
                ('faculty_name', models.CharField(max_length=100)),
                ('short_biography', models.CharField(max_length=500)),
                ('interests_and_hobbies', models.CharField(max_length=250)),
                ('image', models.ImageField(blank=True, upload_to='blog/images')),
            ],
        ),
    ]
