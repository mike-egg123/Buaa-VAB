# Generated by Django 3.0.4 on 2020-06-08 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0002_auto_20200608_1026'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlecommentreport',
            name='state',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bookcommentreport',
            name='state',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='videocommentreport',
            name='state',
            field=models.IntegerField(default=0),
        ),
    ]
