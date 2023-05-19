from django.urls import path

from apps.operations import views


urlpatterns = [
    path('fav/', views.FavoriteView.as_view(), name='fav'),
]
