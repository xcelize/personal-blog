# Generated by Django 2.2.3 on 2019-07-05 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_article_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='short_description',
            field=models.CharField(default=str, max_length=254),
            preserve_default=False,
        ),
    ]
