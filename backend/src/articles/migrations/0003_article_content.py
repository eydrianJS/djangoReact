# Generated by Django 2.1.5 on 2019-01-17 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20190117_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content',
            field=models.TextField(default='SOME STRING'),
        ),
    ]
