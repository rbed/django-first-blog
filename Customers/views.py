from django.shortcuts import render, render_to_response, HttpResponseRedirect, get_object_or_404
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView
from .models import Customer, Task
from .forms import TaskForm, CustomerForm, CustomerFormNew
from django.utils import timezone

#class CustomersView(ListView):
#    template_name = 'customers/customers_list.html'
#    model = Customer
#    context_object_name = "customer_list"
#    queryset = Customer.objects.all().order_by('domain')


def task_new(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.pub_date = timezone.now()
            task.save()
            pk = task.pk
            return render_to_response('customers/task/{}/edit'.format(pk))
        else:
            form = TaskForm()
            return render(request, 'customers/task_new.html', {'form': form})
    else:
        form = TaskForm()
        return render_to_response('customers/task_new.html', {'form':form})


def customer_new(request):
    if request.method == "POST":
        form = CustomerFormNew(request.POST)
        if form.is_valid():
            print('ok')
            customer = form.save(commit=False)
            customer.start_date = timezone.now()
            customer.end_date = timezone.now()
            customer.save()
            pk = customer.pk
            return redirect('/customers/{}'.format(pk))
        else:
            print('chuj')
            return render_to_response('customers/customer_detail.html', {'a': form})
    else:
        form = CustomerFormNew()
        return render(request, 'customers/customer_new.html', {'form' : form})


def customer_edit(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.save()
            pk = customer.pk
            return redirect('/customers/{}/edit'.format(pk))
    else:
        form = CustomerForm(instance=customer)
        return render(request, 'customers/customer_edit.html', {'form' : form})


def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            pk = task.pk
            return redirect('/customers/task/{}'.format(pk))
    else:
        form = TaskForm(instance=task)
        return render(request, 'customers/task_edit.html', {'form':form})


def customers_list(request):
    klienci = Customer.objects.all()
    return render_to_response('customers/customers_list.html', context={
        'klienci' : klienci,
    })


def customers_detail(request, pk):
    klient = Customer.objects.get(pk=pk)
    zadania = Task.objects.filter(for_whom=klient)
    return render_to_response('customers/customer_detail.html', context={
        'pk': pk,
        'klient': klient,
        'zadania': zadania,
    })


def task_list(request):
    taski = Task.objects.all()
    return render_to_response('customers/task_list.html', context={
        'taski':taski,
    })


def task_detail(request, pk):
    task = Task.objects.get(pk=pk)
    return render_to_response('customers/task_detail.html', context={'task': task})


class CustomersDetailView(DetailView):
    model = Customer
    template_name = 'customers/customer_detail.html'


class TaskView(ListView):
    model = Task
    template_name = 'customers/task_list.html'
    context_object_name = 'task_list1'
    queryset = Task.objects.all()


class TaskDetailView(DetailView):
    model = Task
    template_name = 'customers/task_detail.html'


class TaskCustomerListView(DetailView):
    template_name = 'customers/task_customers_detail.html'
    model = Customer
    context_object_name = "customer"


def dupa(request):
    id_klienta = request.GET.get('id_klienta', 'brak_id')
    klient = Customer.objects.get(pk=id_klienta)
    jakis_task = Task.objects.get(pk=1)
    return render_to_response('customers/dupa.html', context={
        'klient': klient,
        'task': jakis_task,
        'id_klienta': id_klienta
    })



# Czyli w naszym przypadku customer/customers_list.html. W szablonie tym list obiektów typu Customer będzie
# dostępna w zmiennej object_list. Jeżeli "object_list" nam się nie podoba to można podać nazwę zrozumiałą
# dla człowieka za pomocą atrybutu context_object_name. Możemy także ograniczyć zbiór obiektów listowanych
# przez widok (domyślnie wszystkie) podając dla atrybutu queryset własne zapytanie-QuerySet dla modelu.
#http://www.python.rk.edu.pl/w/p/przeglad-nowych-generic-views-django-opartych-o-klasy/


#In [2]: from Customers.models import *
#In [3]: c = Customer.objects.get(pk=1)
#In [4]: c.task_set.all()
#Out[4]: <QuerySet [<Task: Task object>, <Task: Task object>, <Task: Task object>, <Task: Task object>]>
#In [5]: c.task_set
#Out[5]: <django.db.models.fields.related_descriptors.create_reverse_many_to_one_manager.<locals>.RelatedManager at 0x7f7edef344e0>
#In [6]: c.task_set.all()
#Out[6]: <QuerySet [<Task: Task object>, <Task: Task object>, <Task: Task object>, <Task: Task object>]>



#In [1]: def funkcja(x):
#   ...:     print(x)
#   ...:
#   ...:
#In [2]: funkcja(3)
#3
#In [3]: dupa = funkcja
#In [4]: dupa("string")
#string


#In [1]: s = {'a':1}
#In [3]: s['a']
#Out[3]: 1
#In [4]: s['aki']
#---------------------------------------------------------------------------
#KeyError                                  Traceback (most recent call last)
#<ipython-input-4-5ae0616d3e93> in <module>()
#----> 1 s['aki']
#KeyError: 'aki'
#In [5]: s.get('a', 'dupa')
#Out[5]: 1
#In [6]: s.get('sdloa', 'dupa')
#Out[6]: 'dupa'
#In [7]:




#radnar@radnarG:~/virtualenv/Poll/Pool$ curl http://127.0.0.1:8000/customers/dupa/?id_klienta=kurwa -v
#*   Trying 127.0.0.1...
#* Connected to 127.0.0.1 (127.0.0.1) port 8000 (#0)
#> GET /customers/dupa/?id_klienta=kurwa HTTP/1.1
#> Host: 127.0.0.1:8000
#> User-Agent: curl/7.47.0
#> Accept: */*
#>
#* HTTP 1.0, assume close after body
#< HTTP/1.0 200 OK
#< Date: Sun, 29 Oct 2017 13:51:44 GMT
#< Server: WSGIServer/0.2 CPython/3.5.2
#< X-Frame-Options: SAMEORIGIN
#< Content-Length: 182
#< Content-Type: text/html; charset=utf-8
#<
#<!DOCTYPE html>
#<html lang="en">
#<head>
#    <meta charset="UTF-8">
#    <title>dupa</title>
#</head>
#<body>
#<h1>kurwa</h1>
#kontekst:
#a: pekado.pl<br />
#b: zrobic costam
#</body>
#* Closing connection 0
