# Generated by Django 4.1 on 2022-12-31 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0003_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='categorys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
