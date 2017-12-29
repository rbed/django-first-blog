from django.conf.urls import include, url
from django.contrib import admin
from brazil import views
from accounts import views as account_views


app_name = 'brazil'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^signup/$', account_views.signup, name='signup'),
    url(r'^(?P<pk>\d+)/$', views.board_topics, name='board_topics'),
    url(r'^(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'),

]
