# Generated by Django 4.0.6 on 2023-04-29 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_course_org'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='is_deleted',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='course',
            name='is_deleted',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='courseresource',
            name='is_deleted',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='section',
            name='is_deleted',
            field=models.BooleanField(default=0),
        ),
    ]
