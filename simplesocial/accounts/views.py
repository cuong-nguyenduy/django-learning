from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView

from accounts import forms
from accounts import models

import logging


logging.basicConfig(level=logging.DEBUG)


# Create your views here.
class SignUpView(CreateView):
    form_class = forms.UserSignUpForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

