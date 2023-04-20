from django.urls import path

from apps.organizations.views import OrgView


urlpatterns = [
    path('', OrgView.as_view(), name='org_list'),
]
