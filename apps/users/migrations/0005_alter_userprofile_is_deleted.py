# Generated by Django 4.0.6 on 2023-04-29 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_userprofile_head_img_userprofile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='is_deleted',
            field=models.BooleanField(default=0),
        ),
    ]