# Generated by Django 4.0.6 on 2023-02-20 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_shorts_source_alter_shorts_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likepost',
            name='story',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.darkjokes'),
        ),
        migrations.AlterField(
            model_name='memes',
            name='image',
            field=models.ImageField(default='memes/download.jpg', upload_to='media/memes'),
        ),
        migrations.AlterField(
            model_name='shorts',
            name='video',
            field=models.FileField(default='shorts/download.mp4', upload_to='media/shorts'),
        ),
        migrations.AlterField(
            model_name='stories',
            name='image',
            field=models.ImageField(default='memes/download.jpg', upload_to='media/memes'),
        ),
    ]