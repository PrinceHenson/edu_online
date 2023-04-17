from django.contrib import admin

from apps.organizations.models import City, Org, Teacher


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    list_filter = ['name']
    search_fields = ['name']


@admin.register(Org)
class OrgAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'category', 'fav_num', 'course_num',
                    'stu_num', 'city']
    list_filter = ['name', 'category', 'city__name']
    search_fields = ['name', 'category', 'city__name']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    #fields = (('name', 'working_age'), 'job_title', 'company', 'fav_num',
    #          'org')
    list_display = ['name', 'working_age', 'job_title', 'company', 'fav_num',
                    'org']
    list_filter = ['name', 'org__name']
    search_fields = ['name', 'org__name']
