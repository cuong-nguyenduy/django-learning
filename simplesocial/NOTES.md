# Authentication
## **Using django.contrib.auth**
There are two ways:
- Use functional views
- Use Class-based Views

### **1. Funtional Views**
```
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^login/$',
        auth_views.login,
        name='login'),
    url(r'^logout/$',
        auth_views.logout,
        name='logout'),
]
```

By default, `auth_view.login` use `registration/login.html` as the template. To change this behaviour, pass the option `template_name` as below:

```
url(r'^login/$', auth_views.login, {'template_name': 'core/login.html'}, name='login'),
```

The code alters the default behaviour and will look for the template at `core/login.html`

### **2. Using Class-based Views**
```
urlpatterns = [
    url(r'^login/$',
        auth_views.LoginView.as_view(template_name='core/login.html'),
        name='login'),
    url(r'^logout/$',
        auth_views.LogoutView.as_view(),
        name='logout'),
]
```