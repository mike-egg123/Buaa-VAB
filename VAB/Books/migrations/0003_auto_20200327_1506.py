# Generated by Django 3.0.4 on 2020-03-27 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0002_book_book_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='Book_img',
            field=models.ImageField(upload_to=''),
        ),
    ]