# Generated by Django 4.2.10 on 2024-03-20 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0002_rename_post_tweet_alter_tweet_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='tweet',
            table='tweets',
        ),
    ]
