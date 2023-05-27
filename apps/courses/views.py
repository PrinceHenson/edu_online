import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import connection
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView, View

from apps.courses.models import Course, CourseResource, CourseTag
from apps.operations.models import UserFavorite


logger = logging.getLogger(__name__)


def be_favorite(user_id, fav_id, fav_type):
    return UserFavorite.objects.filter(user=user_id,
                                       fav_id=fav_id,
                                       fav_type=fav_type)


class CourseIndexView(ListView):
    template_name = 'courses/courses_list.html'
    context_object_name = 'all_courses'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CourseIndexView, self).get_context_data()
        sort_type = self.request.GET.get('sort', '')
        context['sort_type'] = sort_type
        return context

    def get_queryset(self):
        sort_type = self.request.GET.get('sort', '')
        if sort_type == 'hot':
            ordering = '-fav_num'
        elif sort_type == 'students':
            ordering = '-stu_num'
        else:
            ordering = '-created_at'
        return Course.objects.order_by(ordering)


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/course_detail.html'

    def _get_related_courses(self):
        course_id = self.object.id
        tags = CourseTag.objects.filter(course=course_id).values('tag')
        tags_list = [tag['tag'] for tag in tags]
        courses = CourseTag.objects.filter(
            tag__in=tags_list).exclude(
            course=course_id).select_related('course')
        results = [i.course for i in list(set(courses))]
        # logger.warning('[+++++++++++]')
        # for query in connection.queries:
        #     logger.warning(query['sql'])
        #     logger.warning('----------')
        # logger.warning('[+++++++++++]')
        return results

    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data()
        if not self.request.user.is_authenticated:
            return context
        course_fav_record = be_favorite(self.request.user, self.object.id, 1)
        course_favorite = True if course_fav_record else False
        org_fav_record = be_favorite(self.request.user,
                                     self.object.teacher.org.id,
                                     3)
        org_favorite = True if org_fav_record else False
        context['course_favorite'] = course_favorite
        context['org_favorite'] = org_favorite
        context['related_courses'] = self._get_related_courses()[0:3]
        return context


class CourseStudyView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'next'

    def get(self, request, course_id):
        course = get_object_or_404(Course, pk=course_id)
        course_recourses = CourseResource.objects.filter(
            course=course_id).values('name', 'file')
        return render(request, 'courses/course_study.html',
                      context={'course': course,
                               'course_recourses': course_recourses})
