# Generated by Django 4.0.6 on 2023-04-29 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0004_alter_userfavorite_fav_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursecomment',
            name='is_deleted',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='usercourse',
            name='is_deleted',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='userfavorite',
            name='is_deleted',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='usermessage',
            name='is_deleted',
            field=models.BooleanField(default=0),
        ),
    ]