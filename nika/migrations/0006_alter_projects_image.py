# Generated by Django 5.0.6 on 2024-08-18 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nika', '0005_projects_github_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='image',
            field=models.ImageField(upload_to='nikas/'),
        ),
    ]
