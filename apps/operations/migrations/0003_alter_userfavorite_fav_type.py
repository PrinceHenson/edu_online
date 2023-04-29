# Generated by Django 4.0.6 on 2023-04-25 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0002_alter_userfavorite_options_alter_usermessage_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfavorite',
            name='fav_type',
            field=models.PositiveIntegerField(choices=[(1, 'COURSE'), (2, 'TEACHER'), (3, 'ORGANIZATION')], max_length=12),
        ),
    ]
