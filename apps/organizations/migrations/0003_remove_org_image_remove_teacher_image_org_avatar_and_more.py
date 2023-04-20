# Generated by Django 4.0.6 on 2023-04-19 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0002_alter_city_description_alter_city_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='org',
            name='image',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='image',
        ),
        migrations.AddField(
            model_name='org',
            name='avatar',
            field=models.ImageField(default='default.jpeg', upload_to='org/%Y/%m'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='avatar',
            field=models.ImageField(default='default.jpeg', upload_to='org/teacher/%Y/%m'),
        ),
    ]