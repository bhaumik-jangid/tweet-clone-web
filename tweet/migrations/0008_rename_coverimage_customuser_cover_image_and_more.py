# Generated by Django 5.0.6 on 2024-07-06 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0007_alter_customuser_instahandle'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='coverImage',
            new_name='cover_Image',
        ),
        migrations.RenameField(
            model_name='customuser',
            old_name='profileImage',
            new_name='profile_Image',
        ),
    ]
