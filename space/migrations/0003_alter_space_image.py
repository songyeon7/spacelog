# Generated by Django 4.2.7 on 2023-11-19 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('space', '0002_space_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='space',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
