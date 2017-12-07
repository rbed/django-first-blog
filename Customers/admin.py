from django.contrib import admin
from Customers.models import Customer, Task, Agreement

class AgreementInLine(admin.TabularInline):
    model = Agreement
    extra = 1

class AgreementAdmin(admin.ModelAdmin):
    model = Agreement
    list_display = ('title', 'ile_kat', 'ile_wiz', 'ile_prec', 'ile_spons', 'ile_sidewide', 'ile_satelit', 'extra')

class CustomerAdmin(admin.ModelAdmin):
    model = Customer
    #fieldsets to dodatkwe utawienie pol formualrza edycji dnaeog egzamplarza klienta
#    fieldsets = [
#        (None, {'fields': ['domain']}),
#        ('Date information', {'fields': ['start_date'], 'classes': ['collapse']}),
#    ]
    #list_display odpowiada za wyswietlanie listy klientow oraz jej kolumn
    list_display = ('domain', 'start_date', 'agreement', 'end_date')

    #fields odpowiada za wyswietlenie pol wewnatrz danego egzamplarza klienta



class TaskAdmin(admin.ModelAdmin):
    model = Task
    list_display = ('task_text', 'for_whom', 'pub_date', 'status')
    fields = ('for_whom', ('task_text', 'status'), ('pub_date', 'status_change_date', 'end_date'))
    list_filter = ['for_whom__domain']

    #   zeby status okreslony w modelach był mozliwy do wywolania z panelu listy taskow w adminie, piszemy funkcje ktore go wywolaja
    # wiecej tu https://docs.djangoproject.com/pl/1.11/ref/contrib/admin/actions/
    def change_stat_uklienta(self, request, queryset):
        rows_updated = queryset.update(status='k')
        if rows_updated ==1:
            message_bit = "1 task was"
        else:
            message_bit = "%s tasks were" %rows_updated
        self.message_user(request, "%s successfully marked as u klienta." %message_bit)
    change_stat_uklienta.short_description = "zmien status na u klienta"
    actions = [change_stat_uklienta]



admin.site.register(Customer, CustomerAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Agreement, AgreementAdmin)

# Register your models here.
