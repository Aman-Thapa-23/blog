# Generated by Django 3.1.7 on 2021-04-01 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookblog', '0004_auto_20210401_1221'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]