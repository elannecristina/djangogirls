from django.conf.urls import include,url
from django.contrib import admin
from .views import index,post_list,post_list2,post_list0,post_list00,amanda

urlpatterns = [
    url(r'^$',index,name='index'),
    url(r'^post/$', post_list0, name='post_list0'),
    #url(r'^post/\d+$', post_list, name='post_list'),
    url(r'^post/(?P<id1>\d+)$', post_list00, name='post_list00'),


]
