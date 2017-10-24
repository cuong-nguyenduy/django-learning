from django.conf.urls import url
from basic_app import views


# For TEMPLATE TAGGING
app_name = 'basic_app'

urlpatterns = [
    url(r'^$', views.relative_url_templates, name='relative'),
    url(r'^relative/$', views.relative_url_templates, name='relative'),
    url(r'^other/$', views.other, name='other'),
]
