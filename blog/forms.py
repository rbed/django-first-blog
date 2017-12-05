from django import forms
from .models import Article

class ArtForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'text', 'meta_title', 'meta_desc', 'category', 'subcategory')

