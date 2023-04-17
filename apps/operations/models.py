from django.db import models

from django.contrib.auth import get_user_model

from apps.users.models import BaseModel


USER_PROFILE_MODEL = get_user_model()


class CourseComment(BaseModel):
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE)
    user = models.ForeignKey(USER_PROFILE_MODEL, on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'course comment'
        verbose_name_plural = 'course comments'

    def __str__(self):
        return '{course}_{user}'.format(course=self.course, user=self.user)


class UserFavorite(BaseModel):
    FAVORITE_TYPE = [
        (1, 'COURSE'),
        (2, 'TEACHER'),
        (3, 'ORGANIZATION')
    ]

    user = models.ForeignKey(USER_PROFILE_MODEL, on_delete=models.CASCADE)
    fav_id = models.PositiveIntegerField()
    fav_type = models.CharField(choices=FAVORITE_TYPE, max_length=12)

    class Meta:
        verbose_name = 'user favorite'
        verbose_name_plural = 'user favorites'

    def __str__(self):
        return '{user}_{fav_type}_{fav_id}'.format(user=self.user,
                                                   fav_type=self.fav_type,
                                                   fav_id=self.fav_id)


class UserMessage(BaseModel):
    user = models.ForeignKey(USER_PROFILE_MODEL, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'user message'
        verbose_name_plural = 'user messages'

    def __str__(self):
        return self.message


class UserCourse(BaseModel):
    user = models.ForeignKey(USER_PROFILE_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'user course'
        verbose_name_plural = 'user courses'

    def __str__(self):
        return self.course
