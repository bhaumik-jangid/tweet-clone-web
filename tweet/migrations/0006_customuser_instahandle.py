# Generated by Django 5.0.6 on 2024-07-06 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0005_customuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='instaHandle',
            field=models.CharField(default='/tweet/profile/user.username/', max_length=100),
        ),
    ]
