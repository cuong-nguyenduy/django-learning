from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView

from accounts import forms
from accounts import models

import logging


logging.basicConfig(level=logging.DEBUG)


# Create your views here.
class SignUpView(CreateView):
    # form_class = forms.UserSignUpForm
    model = models.User
    fields = ('username', 'email', 'password',)
    success_url = reverse_lazy('login')
    # print(str(success_url))
    template_name = 'accounts/signup.html'
