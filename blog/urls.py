from django.urls import path
from django.conf.urls import include,url
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/edit', views.post_edit, name='post_edit'),
    path('post/new/', views.post_new, name='post_new'),
    path(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    path(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    path(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
]
