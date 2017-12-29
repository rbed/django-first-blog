from django.conf.urls import include, url
from django.contrib import admin
from .views import article_list, article_detail, article_new, category_list, user_new, user_detail


app_name = 'blog'
urlpatterns = [
    url(r'^$', article_list, name='post-list'),
    url(r'^(?P<pk>[0-9]+)/$', article_detail, name='art-detail'),
    url(r'^new/$', article_new, name='art-new'),
    url(r'^category/(?P<pk>[0-9]+)$', category_list, name='category-list'),
    url(r'^user/$', user_new, name='user-new'),
    url(r'^user/(?P<pk>[0-9]+)$', user_detail, name='user-detail'),
]