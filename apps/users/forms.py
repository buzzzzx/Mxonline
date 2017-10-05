# -*- coding: utf-8 -*-
__author__ = 'buzz'
__date__ = '2017/10/5 下午12:02'

from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)
