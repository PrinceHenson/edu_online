from django.views.generic import DetailView, ListView

from apps.courses.models import Course, CourseTag
from apps.operations.models import UserFavorite


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
        tags = CourseTag.objects.filter(course=course_id).values_list('tag')
        related_courses = []
        for tag_id in tags:
            courses = CourseTag.objects.filter(
                tag=tag_id[0]).exclude(
                course=course_id).select_related('course')
            related_courses += courses
        return [i.course for i in list(set(related_courses))]

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
