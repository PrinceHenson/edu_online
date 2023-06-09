# Generated by Django 4.0.6 on 2023-04-14 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='description',
            field=models.CharField(max_length=255, verbose_name='city description'),
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=30, verbose_name='city name'),
        ),
        migrations.AlterField(
            model_name='org',
            name='address',
            field=models.CharField(max_length=100, verbose_name='organization address'),
        ),
        migrations.AlterField(
            model_name='org',
            name='category',
            field=models.IntegerField(choices=[(1, 'INDIVIDUAL'), (2, 'COLLEGES AND UNIVERSITIES'), (3, 'TRAINING ORGANIZATIONS')], verbose_name='organization category'),
        ),
        migrations.AlterField(
            model_name='org',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizations.city', verbose_name='organization in which city'),
        ),
        migrations.AlterField(
            model_name='org',
            name='course_num',
            field=models.PositiveIntegerField(default=0, verbose_name='number of courses in this organization'),
        ),
        migrations.AlterField(
            model_name='org',
            name='fav_num',
            field=models.PositiveIntegerField(default=0, verbose_name='number of favorite of the course'),
        ),
        migrations.AlterField(
            model_name='org',
            name='image',
            field=models.ImageField(upload_to='head_image/%Y/%m', verbose_name='organization head image'),
        ),
        migrations.AlterField(
            model_name='org',
            name='stu_num',
            field=models.PositiveIntegerField(default=0, verbose_name='number of students in this organization'),
        ),
        migrations.AlterField(
            model_name='org',
            name='tag',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='organization tag'),
        ),
        migrations.AlterField(
            model_name='org',
            name='view_num',
            field=models.PositiveIntegerField(default=0, verbose_name='number of views of the course'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='company',
            field=models.CharField(max_length=30, verbose_name='the company that teacher works in'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='fav_num',
            field=models.PositiveIntegerField(default=0, verbose_name='number of favorite of the course'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='image',
            field=models.ImageField(upload_to='head_image/%Y/%m', verbose_name='teacher head image'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='org',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizations.org', verbose_name='organization'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='teach_feature',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='teaching features of the teacher'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='view_num',
            field=models.PositiveIntegerField(default=0, verbose_name='number of views of the course'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='working_age',
            field=models.PositiveIntegerField(),
        ),
    ]
