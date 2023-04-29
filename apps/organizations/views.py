import logging

from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render
from django.views import View

from apps.courses.models import Course
from apps.operations.models import UserFavorite
from apps.organizations.models import City, Org, Teacher

logger = logging.getLogger(__name__)


class OrgIndexView(View):
    ORG_CATEGORY = {category[1]: category[0] for category in Org.CATEGORY}

    def _validate(self, request):
        category = request.GET.get('category')
        if category and category not in self.ORG_CATEGORY:
            return 'error'
        city = request.GET.get('city')
        if city and (not city.isdigit or int(city) <= 0):
            return 'error'
        sort = request.GET.get('sort')
        if sort and sort not in ['students', 'courses']:
            return 'error'

    def get(self, request):
        logger.warning('[warning]in org index page...')
        logger.info('[info]in org index page...')
        self._validate(request)
        category = request.GET.get('category', '')
        all_orgs = Org.objects.all()
        hot_orgs = all_orgs.order_by('-fav_num')[:3]

        if category:
            all_orgs = all_orgs.filter(category=self.ORG_CATEGORY[category])
        city = request.GET.get('city', '')
        if city and int(city) > 0:
            all_orgs = all_orgs.filter(city=city)

        sort = request.GET.get('sort', '')
        if sort == 'students':
            all_orgs = all_orgs.order_by('-stu_num')
        elif sort == 'courses':
            all_orgs = all_orgs.order_by('-course_num')

        paginator = Paginator(all_orgs, 10)
        page_num = request.GET.get('page')
        page_orgs = paginator.get_page(page_num)

        org_num = all_orgs.count()
        all_cities = City.objects.all()
        return render(request, 'org_list.html',
                      context={'all_orgs': page_orgs,
                               'org_num': org_num,
                               'all_cities': all_cities,
                               'org_category': category,
                               'city_id': city,
                               'sort': sort,
                               'hot_orgs': hot_orgs})


def be_favorite(user_id, fav_id, fav_type):
    return UserFavorite.objects.filter(user=user_id,
                                       fav_id=fav_id,
                                       fav_type=fav_type)


def org_courses(org_id):
    # step 1: SELECT id from organizations_teacher WHERE org_id = org_id
    # step 2: SELECT * FROM courses_course WHERE teacher_id in (step 1 result)
    teachers = Teacher.objects.filter(org_id=org_id).values_list('id',
                                                                 flat=True)
    return Course.objects.filter(teacher_id__in=list(teachers))


class OrgDescView(View):
    page_title = 'desc'

    def get(self, request, org_id):
        org = get_object_or_404(Org, pk=org_id)
        favorite_record = be_favorite(request.user, org_id, 3)
        favorite = True if favorite_record else False
        return render(request, 'org_detail_desc.html',
                      context={'org': org, 'page_title': self.page_title,
                               'favorite': favorite})


class OrgDetailView(View):
    page_title = 'detail'

    def get(self, request, org_id):
        org = get_object_or_404(Org, pk=org_id)
        courses = org_courses(org_id)[:3]
        teachers = org.teachers()[:3]

        favorite_record = be_favorite(request.user, org_id, 3)
        favorite = True if favorite_record else False
        return render(request, 'org_detail_homepage.html',
                      context={'org': org, 'all_courses': courses,
                               'all_teachers': teachers,
                               'favorite': favorite,
                               'page_title': self.page_title})


class OrgTeacherView(View):
    page_title = 'teacher'

    def get(self, request, org_id):
        org = get_object_or_404(Org, pk=org_id)
        teachers = org.teachers()
        course_num = org_courses(org_id).count()

        favorite_record = be_favorite(request.user, org_id, 3)
        favorite = True if favorite_record else False
        return render(request, 'org_detail_teachers.html',
                      context={'org': org, 'teachers': teachers,
                               'course_num': course_num,
                               'favorite': favorite,
                               'page_title': self.page_title})


class OrgCourseView(View):
    page_title = 'course'

    def get(self, request, org_id):
        org = get_object_or_404(Org, pk=org_id)
        courses = org_courses(org_id)

        paginator = Paginator(courses, 3)
        page_num = request.GET.get('page')
        page_courses = paginator.get_page(page_num)

        favorite_record = be_favorite(request.user, org_id, 3)
        favorite = True if favorite_record else False
        return render(request, 'org_detail_courses.html',
                      context={'org': org, 'courses': page_courses,
                               'favorite': favorite,
                               'page_title': self.page_title})
