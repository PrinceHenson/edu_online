from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import View


class LoginView(View):

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print('-----')
        if user:
            # login success
            print('------login success')
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        return render(request, 'login.html',
                      context={'msg': 'username or password is wrong.'})
