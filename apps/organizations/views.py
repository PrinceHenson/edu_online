import logging

from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View

from apps.organizations.models import City, Org

logger = logging.getLogger(__name__)


class OrgView(View):
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
