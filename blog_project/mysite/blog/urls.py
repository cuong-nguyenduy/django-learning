from django.conf.urls import url
from blog import views

urlpatters = [
    url(r'^$', views.PostListView.as_view(), name='post_list'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^post/(?P<pk>\d+)/$', views.PostDetailView.as_view(), name='post_detail'),
    url(r'^post/create/$', views.PostCreateView.as_view(), name='post_create'),
    url(r'^post/(?P<pk>\d+)/update/$', views.PostUpdateView.as_view(), name='post_update'),
    url(r'^post/(?P<pk>\d+)/delete/$', views.PostDeleteView.as_view(), name='post_delete'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.publish_post, name='publish_post'),
    url(r'^post/drafts/$', views.PostDraftListView.as_view(), name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/comments/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.approve_comment, name='approve_comment'),
    url(r'^comment/(?P<pk>\d+)/delete/$', views.remove_comment, name='remove_comment'),
]
