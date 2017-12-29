from django import forms
from .models import Topic

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': 'waht is on your mind'}
        ),
        max_length=40000,
        help_text='tekst wyjasniajacy jak wpisac zeby nie spieprzyc'
    )

    class Meta:
        model = Topic
        fields = ['subject', 'message']