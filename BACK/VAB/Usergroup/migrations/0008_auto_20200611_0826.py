# Generated by Django 3.0.4 on 2020-06-11 00:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_article_likes'),
        ('Usergroup', '0007_auto_20200611_0816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usergroup',
            name='top_article',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='article.Article'),
        ),
    ]
