# Generated by Django 3.0.7 on 2020-09-21 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_short_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='tag',
            field=models.CharField(default='General', max_length=30),
        ),
    ]
