from django.db import models

from apps.users.models import BaseModel


class Course(BaseModel):
    LEVEL_CHOICE = [
        ('L', 'LOW'),
        ('M', 'MIDDLE'),
        ('H', 'HIGH')
    ]

    teacher = models.ForeignKey('organizations.teacher',
                                on_delete=models.CASCADE)
    #org = models.ForeignKey('organizations.org', on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name='course name')
    description = models.CharField(max_length=255,
                                   verbose_name='course description')
    level = models.CharField(choices=LEVEL_CHOICE, max_length=1,
                             verbose_name='course level')
    stu_num = models.PositiveIntegerField(
        default=0,
        verbose_name='number of students of the course')
    duration = models.PositiveIntegerField(default=0,
                                           verbose_name='Course duration')
    fav_num = models.PositiveIntegerField(
        default=0,
        verbose_name='number of favorite of the course')
    view_num = models.PositiveIntegerField(
        default=0,
        verbose_name='number of views of the course')
    category = models.CharField(max_length=50, null=True, blank=True,
                                verbose_name='course category')
    course_note = models.CharField(max_length=255, null=True, blank=True,
                                   verbose_name='course note')
    teacher_comment = models.CharField(max_length=255, null=True, blank=True,
                                       verbose_name='teacher comment')
    detail = models.TextField(verbose_name='Course detail')
    cover_img = models.ImageField(upload_to="courses/%Y/%m",
                                  default="default.jpeg",
                                  max_length=100,
                                  verbose_name='cover of the course')
    tag = models.CharField(max_length=50, null=True, blank=True,
                           verbose_name='course tag')

    class Meta:
        verbose_name = 'course'
        verbose_name_plural = 'courses'

    def __str__(self):
        return self.name


class Chapter(BaseModel):
    course = models.ForeignKey('Course', on_delete=models.CASCADE,
                               verbose_name='course')
    name = models.CharField(max_length=30, verbose_name='chapter name')
    duration = models.PositiveIntegerField(default=0,
                                           verbose_name='chapter duration')

    class Meta:
        verbose_name = 'chapter'
        verbose_name_plural = 'chapters'

    def __str__(self):
        return self.name


class Section(BaseModel):
    chapter = models.ForeignKey('Chapter', on_delete=models.CASCADE,
                                verbose_name='chapter')
    name = models.CharField(max_length=30, verbose_name='section name')
    duration = models.PositiveIntegerField(default=0,
                                           verbose_name='section duration')
    url = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'section'
        verbose_name_plural = 'sections'

    def __str__(self):
        return self.name


class CourseResource(BaseModel):
    course = models.ForeignKey('Course', on_delete=models.CASCADE,
                               verbose_name='course')
    name = models.CharField(max_length=30, verbose_name='Resource name')
    file = models.FileField(upload_to='courses/resources/%Y/%m',
                            verbose_name='resource file')

    class Meta:
        verbose_name = 'course resource'
        verbose_name_plural = 'course resources'

    def __str__(self):
        return self.name
