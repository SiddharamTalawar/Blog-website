# Generated by Django 4.1 on 2023-01-02 07:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0006_post_post_image_alter_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
