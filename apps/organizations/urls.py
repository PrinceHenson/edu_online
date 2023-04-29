from django.urls import path

from apps.organizations import views


urlpatterns = [
    path('', views.OrgIndexView.as_view(), name='list'),
    path('<int:org_id>/', views.OrgDescView.as_view(), name='desc'),
    path('<int:org_id>/teachers/', views.OrgTeacherView.as_view(),
         name='teachers'),
    path('<int:org_id>/courses/', views.OrgCourseView.as_view(),
         name='courses'),
    # path('<int:org_id>/desc/', views.OrgDescView.as_view(),
    #      name='desc'),
]
