from django.conf.urls import url
from . import views


app_name = 'posts'

urlpatterns = [
    url(r'^$', views.PostListView.as_view(), name='post_all'),
    url(r'^new/$', views.CreatePostView.as_view(), name='post_create'),
    url(r'^by/(?P<username>[-\w]+)/$', views.UserPostView.as_view(), name='for_user'),
    url(r'^by/(?P<username>[-\w]+)/(?P<pk>\d+)/$', views.PostDetailView.as_view(), name='single'),
    url(r'^delete/(?P<pk>\d+)/$', views.DeletePostView.as_view(), name='post_delete'),
]
