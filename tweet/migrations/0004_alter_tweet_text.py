# Generated by Django 5.0.6 on 2024-07-03 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0003_alter_tweet_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='text',
            field=models.CharField(max_length=300),
        ),
    ]
