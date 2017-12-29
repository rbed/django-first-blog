from django import forms
from .models import Article, User

class ArtForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'text', 'meta_title', 'meta_desc', 'category', 'subcategory')

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'password')

