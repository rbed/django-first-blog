from django.conf.urls import url
from .views import TaskCustomerListView, customers_list, customers_detail, dupa, task_list, task_detail, \
    task_new, customer_new, customer_edit, task_edit
from . import forms

app_name = 'Customers'
urlpatterns = [
    url(r'^$', customers_list, name='customers-list'),
    url(r'^(?P<pk>[0-9]+)/$', customers_detail, name='detail1'),

    url(r'^add$', customer_new, name='customer_new'),
    url(r'^(?P<pk>[0-9]+)/edit/$', customer_edit, name='customer_edit'),

    url(r'^task/$', task_list, name='task-list'),
    url(r'^task/(?P<pk>[0-9]+)/$', task_detail, name='task-detail'),

    url(r'^task/(?P<pk>[0-9]+)/edit/$', task_edit, name='task_edit'),
    url(r'^task/new/$', task_new, name='task_new'),

    url(r'^dupa/$', dupa, name='cos'),
    url(r'^task/customer/(?P<pk>[0-9]+)/$', TaskCustomerListView.as_view(), name='task-customer-list')
]




#urlpatterns = [
#    url(r'^$', views.IndexView.as_view(), name='index'),
#    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
#    url(r'^(?P<pk>[0-9]+)/result/$', views.ResultView.as_view(), name='result'),
#    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
#]

