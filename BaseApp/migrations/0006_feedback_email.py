# Generated by Django 5.1.4 on 2024-12-26 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BaseApp', '0005_feedback_image_alter_feedback_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='Email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
