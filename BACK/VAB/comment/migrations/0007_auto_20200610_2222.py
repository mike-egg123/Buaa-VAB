# Generated by Django 3.0.4 on 2020-06-10 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0006_articlecomment_canbeseen'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookcomment',
            name='hates',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bookcomment',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
