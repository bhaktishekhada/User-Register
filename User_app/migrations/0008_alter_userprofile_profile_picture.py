# Generated by Django 5.0.7 on 2024-08-07 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User_app', '0007_alter_userprofile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(null=True, upload_to='profile_picture/'),
        ),
    ]
