from django import forms

from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    username = forms.CharField(required=True, min_length=2)
    password = forms.CharField(required=True, min_length=6)
    #captcha = CaptchaField()
