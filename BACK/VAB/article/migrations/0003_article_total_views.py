# Generated by Django 3.0.4 on 2020-04-10 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20200410_1804'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='total_views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]