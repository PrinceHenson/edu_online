from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from apps.courses.models import Course
from apps.operations.forms import UserFavoriteForm
from apps.operations.models import UserFavorite
from apps.organizations.models import Org, Teacher


class FavoriteView(View):
    def post(self, request):
        if not request.user.is_authenticated:
            return JsonResponse({'status': 'fail', 'msg': 'has not login'})
        user_fav_form = UserFavoriteForm(request.POST)
        if not user_fav_form.is_valid():
            return JsonResponse({
                'status': 'fail',
                'msg': 'params error'
            })

        fav_id = user_fav_form.cleaned_data['fav_id']
        fav_type = user_fav_form.cleaned_data['fav_type']
        favorite_record = UserFavorite.objects.filter(user=request.user,
                                                      fav_id=fav_id,
                                                      fav_type=fav_type)
        if favorite_record:
            favorite_record.delete()
            # todo: 同步修改org/course/teacher表中的fav_num是否有更好的办法
            if fav_type == 1:
                course = Course.objects.get(pk=fav_id)
                course.fav_num -= 1
                course.save()
            elif fav_type == 2:
                teacher = Teacher.objects.get(pk=fav_id)
                teacher.fav_num -= 1
                teacher.save()
            elif fav_type == 3:
                org = Org.objects.get(pk=fav_id)
                org.fav_num -= 1
                org.save()
            return JsonResponse({'status': 'success', 'msg': '取消收藏成功'})
        else:
            user_fav_model = UserFavorite()
            user_fav_model.user = request.user
            user_fav_model.fav_id = fav_id
            user_fav_model.fav_type = fav_type
            user_fav_model.save()
            # todo: 同步修改org/course/teacher表中的fav_num是否有更好的办法
            if fav_type == 1:
                course = Course.objects.get(pk=fav_id)
                course.fav_num += 1
                course.save()
            elif fav_type == 2:
                teacher = Teacher.objects.get(pk=fav_id)
                teacher.fav_num += 1
                teacher.save()
            elif fav_type == 3:
                org = Org.objects.get(pk=fav_id)
                org.fav_num += 1
                org.save()
            return JsonResponse({'status': 'success', 'msg': '收藏成功'})
