# Generated by Django 4.0.6 on 2023-03-19 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_darkjokes_like_count_jokes_like_count_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='shorts',
            name='is_cut',
            field=models.BooleanField(default=False),
        ),
    ]
