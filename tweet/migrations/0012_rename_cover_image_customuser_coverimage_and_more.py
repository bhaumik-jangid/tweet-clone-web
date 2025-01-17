# Generated by Django 5.0.6 on 2024-07-06 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0011_alter_customuser_instagram'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='cover_Image',
            new_name='coverImage',
        ),
        migrations.RenameField(
            model_name='customuser',
            old_name='profile_Image',
            new_name='profileImage',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='instagram',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
