from django import forms
from django.db import models
from django.conf import settings
# from django.contrib.auth.models import User

# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password']
class Profile(models.Model):
    class Meta:
        verbose_name = u'프로필'
        verbose_name_plural = u'프로필'
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    coin = models.IntegerField(default=0)