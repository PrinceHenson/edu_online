from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import View

from apps.users.forms import LoginForm


class LoginView(View):

    def get(self, request):
        login_data = LoginForm()
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('index'))
        return render(request, 'login.html',
                      context={'login_data': login_data})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if not login_form.is_valid():
            return render(request, 'login.html',
                          context={'login_form': login_form})
        username = login_form.cleaned_data['username']
        password = login_form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if not user:
            # authenticate failed
            return render(request, 'login.html',
                          context={'login_form': login_form,
                                   'msg': 'username or password is wrong.'})

        login(request, user)
        return HttpResponseRedirect(reverse('index'))


class LogoutView(View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse("login"))
