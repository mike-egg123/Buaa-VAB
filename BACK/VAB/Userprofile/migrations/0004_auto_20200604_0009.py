# Generated by Django 3.0.4 on 2020-06-03 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Userprofile', '0003_auto_20200329_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='headshot',
            field=models.ImageField(null=True, upload_to='headshot/'),
        ),
    ]
