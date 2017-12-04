from django.conf.urls import include, url
from django.contrib import admin
from .views import article_list, article_detail


app_name = 'blog'
urlpatterns = [
    url(r'^$', article_list, name='post-list'),
    url(r'^(?P<pk>[0-9]+)/$', article_detail, name='art-detail'),
]