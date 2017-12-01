from django.shortcuts import render
from .models import Article
from django.utils import timezone


# Create your views here.

#widok listy art
#widok art

def article_list(request):
    article = Article.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')
    return render(request, 'blog/post_list.html', {'article': article})

