from django.contrib import admin

from apps.courses.models import Course, Chapter, Section, CourseResource


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ['name']}),
        ('Course Information', {
            'fields': ['description', 'level', 'stu_num', 'duration',
                       'fav_num', 'category']
        })
    )
    list_display = ['name', 'description', 'level', 'stu_num', 'duration',
                    'fav_num', 'category']
    list_filter = ['name', 'level']
    search_fields = ['name', 'level']


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ['name', 'duration', 'course']
    list_filter = ['name', 'course__name']
    search_fields = ['name', 'course__name']


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['name', 'duration', 'chapter']
    list_filter = ['name', 'chapter__name']
    search_fields = ['name', 'chapter__name']


@admin.register(CourseResource)
class CourceResourceAdmin(admin.ModelAdmin):
    list_display = ['name', 'course']
    list_filter = ['name', 'course__name']
    search_fields = ['name', 'course__name']
