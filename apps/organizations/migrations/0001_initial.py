# Generated by Django 4.0.6 on 2023-04-12 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.PositiveSmallIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=30, verbose_name='City name')),
                ('description', models.CharField(max_length=255, verbose_name='City description')),
            ],
            options={
                'verbose_name': 'city',
                'verbose_name_plural': 'cities',
            },
        ),
        migrations.CreateModel(
            name='Org',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.PositiveSmallIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('tag', models.CharField(blank=True, max_length=30, null=True, verbose_name='Organization tag')),
                ('category', models.IntegerField(verbose_name='Organization category')),
                ('address', models.CharField(max_length=100, verbose_name='Organization address')),
                ('view_num', models.IntegerField(default=0, verbose_name='Number of views of the course')),
                ('fav_num', models.IntegerField(default=0, verbose_name='Number of favorite of the course')),
                ('image', models.ImageField(upload_to='head_image/%Y/%m', verbose_name='Organization head image')),
                ('course_num', models.IntegerField(default=0, verbose_name='Number of courses in this organization')),
                ('stu_num', models.IntegerField(default=0, verbose_name='Number of students in this organization')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizations.city', verbose_name='Organization in which city')),
            ],
            options={
                'verbose_name': 'organization',
                'verbose_name_plural': 'organizations',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.PositiveSmallIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('working_age', models.IntegerField()),
                ('job_title', models.CharField(max_length=30)),
                ('company', models.CharField(max_length=30, verbose_name='The company that teacher works in')),
                ('teach_feature', models.CharField(blank=True, max_length=50, null=True, verbose_name='Teaching features of the teacher')),
                ('view_num', models.IntegerField(default=0, verbose_name='Number of views of the course')),
                ('fav_num', models.IntegerField(default=0, verbose_name='Number of favorite of the course')),
                ('image', models.ImageField(upload_to='head_image/%Y/%m', verbose_name='Organization head image')),
                ('org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizations.org', verbose_name='Organization')),
            ],
            options={
                'verbose_name': 'teacher',
                'verbose_name_plural': 'teachers',
            },
        ),
    ]
