# Generated by Django 3.0.4 on 2020-06-10 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_article_likes'),
        ('Usergroup', '0004_auto_20200610_2304'),
    ]

    operations = [
        migrations.AddField(
            model_name='usergroup',
            name='top_article',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='article.Article'),
        ),
    ]
