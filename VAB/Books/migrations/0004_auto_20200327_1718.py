# Generated by Django 3.0.4 on 2020-03-27 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0003_auto_20200327_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='Book_img',
            field=models.ImageField(null=True, upload_to='img'),
        ),
    ]