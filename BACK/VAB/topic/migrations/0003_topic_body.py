# Generated by Django 3.0.4 on 2020-06-13 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0002_topic_topicimg'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='body',
            field=models.TextField(blank=True, max_length=1000),
        ),
    ]