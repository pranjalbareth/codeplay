# Generated by Django 3.0.7 on 2020-09-22 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_remove_blog_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='time',
        ),
        migrations.AddField(
            model_name='application',
            name='position',
            field=models.CharField(default='NOT SPECIFIED', max_length=20),
        ),
    ]
