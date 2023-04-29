from django.db import models

from apps.users.models import BaseModel


class City(BaseModel):
    name = models.CharField(max_length=30, verbose_name='city name')
    description = models.CharField(max_length=255,
                                   verbose_name='city description')

    class Meta:
        verbose_name = 'city'
        verbose_name_plural = 'cities'

    def __str__(self):
        return self.name


class Org(BaseModel):
    CATEGORY = [
        (1, 'INDIVIDUAL'),
        (2, 'COLLEGES AND UNIVERSITIES'),
        (3, 'TRAINING ORGANIZATIONS')
    ]

    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255,
                                   null=True, blank=True)
    tag = models.CharField(max_length=30, null=True, blank=True,
                           verbose_name='organization tag')
    category = models.IntegerField(verbose_name='organization category',
                                   choices=CATEGORY)
    address = models.CharField(max_length=100,
                               verbose_name='organization address')
    view_num = models.PositiveIntegerField(
        default=0,
        verbose_name='number of views of the organization')
    fav_num = models.PositiveIntegerField(
        default=0,
        verbose_name='number of favorite of the organization'
    )
    avatar = models.ImageField(upload_to='org/%Y/%m',
                               max_length=100,
                               default='default.jpeg')
    course_num = models.PositiveIntegerField(
        default=0,
        verbose_name='number of courses in this organization')
    stu_num = models.PositiveIntegerField(
        default=0,
        verbose_name='number of students in this organization'
    )
    is_certified = models.BooleanField(default=False,
                                       verbose_name='certified organization')
    is_gold = models.BooleanField(default=False,
                                  verbose_name='gold organization')
    city = models.ForeignKey('City', on_delete=models.CASCADE,
                             verbose_name='organization in which city')

    class Meta:
        verbose_name = 'organization'
        verbose_name_plural = 'organizations'

    def __str__(self):
        return self.name

    def courses(self):
        return self.course_set.all()

    def teachers(self):
        return self.teacher_set.all()


class Teacher(BaseModel):
    org = models.ForeignKey('Org', on_delete=models.CASCADE,
                            verbose_name='organization')
    name = models.CharField(max_length=30)
    age = models.PositiveIntegerField(null=True, blank=True)
    working_age = models.PositiveIntegerField()
    job_title = models.CharField(max_length=30)
    company = models.CharField(
        max_length=30,
        verbose_name='the company that teacher works in')
    teach_feature = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        verbose_name='teaching features of the teacher')
    view_num = models.PositiveIntegerField(
        default=0,
        verbose_name='number of views of the course')
    fav_num = models.PositiveIntegerField(
        default=0,
        verbose_name='number of favorite of the course'
    )
    avatar = models.ImageField(upload_to='org/teacher/%Y/%m',
                               max_length=100,
                               default='default.jpeg')

    class Meta:
        verbose_name = 'teacher'
        verbose_name_plural = 'teachers'

    def __str__(self):
        return self.name

    def courses(self):
        return self.course_set.count()
