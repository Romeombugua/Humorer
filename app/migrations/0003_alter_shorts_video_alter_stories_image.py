# Generated by Django 4.2.1 on 2023-08-24 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_memes_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shorts',
            name='video',
            field=models.FileField(default='shorts/download.mp4', upload_to='shorts'),
        ),
        migrations.AlterField(
            model_name='stories',
            name='image',
            field=models.ImageField(default='memes/download.jpg', upload_to='memes'),
        ),
    ]
