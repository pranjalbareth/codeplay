# Generated by Django 3.0.7 on 2020-09-21 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blog_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='read_time',
            field=models.CharField(default='7 MIN READ', max_length=11),
        ),
    ]