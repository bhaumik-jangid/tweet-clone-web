# Generated by Django 5.0.6 on 2024-07-06 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0014_rename_firstname_tweetuserdata_first_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tweetuserdata',
            old_name='coverImage',
            new_name='cover_Image',
        ),
        migrations.RenameField(
            model_name='tweetuserdata',
            old_name='lastName',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='tweetuserdata',
            old_name='profileImage',
            new_name='profile_Image',
        ),
    ]
