from django import forms

class MyForm(forms.Form):
    imie = forms.CharField(label='imie', max_length=3)
