from django.conf.urls import url
from . import views


app_name = 'groups'
urlpatterns = [
    url(r'^$', views.ListGroupView.as_view(), name='group_all'),
    url(r'^new/$', views.CreateGroupView.as_view(), name='create'),
    url(r'^posts/in/(?P<slug>[-\w]+)/$', views.SingleGroupView.as_view(), name='group_single'),
    url(r'^join/(?P<slug>[-\w]+)/$', views.JoinGroupView.as_view(), name='group_join'),
    url(r'^leave/(?P<slug>[-\w]+)/$', views.LeaveGroupView.as_view(), name='group_leave'),
]
