from django.db import models
from django.contrib.auth.models import AbstractUser


class BaseModel(models.Model):
    is_deleted = models.BooleanField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True


class UserProfile(AbstractUser, BaseModel):
    GENDER_CHOICE = [
        ('M', 'MALE'),
        ('F', 'FEMALE')
    ]

    birthday = models.DateField(null=True, blank=True)
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICE,
        null=True,
        blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    mobile = models.CharField(max_length=11)
    avatar = models.ImageField(upload_to="avatar/%Y/%m",
                               default="default.jpeg")

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.username
