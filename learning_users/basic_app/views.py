from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from django.shortcuts import render
from basic_app.forms import UserForm, UserProfileInfoForm
from basic_app.models import UserProfileInfo


# Create your views here.
def index(request):
    return render(request, 'basic_app/index.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('<h1>User is NOT active!</h1>')
        else:
            print('Username: {} with password: {} is not valid'.format(username, password))
            return HttpResponse('<h1>Invalid Account</h1>')
    else:
        return render(request, 'basic_app/login.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def special_view(request):
    return render(request, 'basic_app/special_view.html')


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            # Save user information
            user = user_form.save()
            user.set_password(user.password)  # Hash the password
            user.save()

            # Get profile information
            profile = profile_form.save(commit=False)  # Don't commit to database, Yet
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()

            #
            registered = True
        else:
            print('ERROR {}, {}'.format(user_form.errors, profile_form.errors))
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    data_dict = {
        'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered,
    }
    return render(request, 'basic_app/registration.html', context=data_dict)
