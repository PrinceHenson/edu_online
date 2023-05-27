from django.urls import path

from apps.courses import views


urlpatterns = [
    path('', views.CourseIndexView.as_view(), name='list'),
    path('<int:pk>/', views.CourseDetailView.as_view(), name='detail'),
    path('<int:course_id>/learn', views.CourseStudyView.as_view(),
         name='learn'),
]
