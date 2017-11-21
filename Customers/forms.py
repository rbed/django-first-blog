#https://tutorial.djangogirls.org/pl/django_forms/
from django import forms
from .models import Task, Customer, Agreement
from django.forms.extras.widgets import SelectDateWidget
from django.utils import timezone


class TaskForm(forms.ModelForm):
    end_date = forms.DateField(widget=forms.SelectDateWidget(), initial=timezone.now)
    class Meta:
        model = Task
        fields = ('for_whom', 'task_text', 'end_date', 'prior', 'status')
#        widget = {'end_date': SelectDateWidget}


class CustomerFormNew(forms.ModelForm):
    start_date = forms.DateField(widget=forms.SelectDateWidget(), initial=timezone.now)
    class Meta:
        model = Customer
        fields = ('domain', 'agreement')
#        widgets ={'start_date': SelectDateWidget}

class CustomerForm(forms.ModelForm):
    start_date = forms.DateField(widget=forms.SelectDateWidget(), initial=timezone.now)

    class Meta:
        model = Customer
        fields = ('domain', 'agreement', 'start_date')
        widgets ={'start_date': SelectDateWidget}


#class CustomerForm(forms.ModelForm):
#    domain = forms.CharField(max_length=100)
#    agreement = forms.ModelChoiceField(queryset=Agreement.objects.all())
#    start_date = forms.DateField(widget=SelectDateWidget