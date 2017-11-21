from django.db import models
from django.utils import timezone


class Agreement(models.Model):
    title = models.CharField(max_length=100)
    ile_kat = models.IntegerField(default=0)
    ile_wiz = models.IntegerField(default=0)
    ile_prec = models.IntegerField(default=0)
    ile_spons = models.IntegerField(default=0)
    ile_sidewide = models.IntegerField(default=0)
    ile_satelit = models.IntegerField(default=0)
    extra = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title



class Customer(models.Model):
    domain = models.CharField(max_length=200)
    start_date = models.DateTimeField('agreement start date')
    end_date = models.DateTimeField('agreement completion end 6 mts')
    agreement = models.ForeignKey(Agreement, null=True, blank=True)

    def __str__(self):
        return self.domain



#class Status(models.Model):
#    status_field = models.CharField(max_length=50)
#    def __str__(self):
#        return self.status_field

STATUS_CHOICES = (
    ('Do zrobienia', 'Do zrobienia'),
    ('W trakcie - u klienta', 'W trakcie - u klienta'),
    ('W trakcie - Gebuko', 'W trakcie - Gebuko'),
    ('Zrobione', 'Zrobione'),
)

class Task(models.Model):
    task_text = models.TextField()
    pub_date = models.DateTimeField('start')
    end_date = models.DateTimeField('completion', blank=True, null=True)
    status_change_date = models.DateTimeField('stat_change', auto_now=True, blank=True, null=True)
    prior = models.BooleanField(default=False)
    for_whom = models.ForeignKey(Customer)
#    task_status = models.ForeignKey(Status)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='d')

#usuwamy def str poniewaz wiecej opcji ustawienia tego mamy w admin.py
#    def __str__(self):
#        return (self.task_text)








class Note(models.Model):
    note_text = models.CharField(max_length=500)



