from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from django.utils import timezone
from .forms import ArtForm

# Create your views here.

#widok listy art
#widok art

def article_list(request):
    article = Article.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')
    return render(request, 'blog/post_list.html', {'article': article})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'blog/art_detail.html', {'art': article})

def article_new(request):
    if request.method == "POST":
        form = ArtForm(request.POST)
        if form.is_valid():
            art = form.save(commit=False)
            art.author = request.user
            art.pub_date = timezone.now()
            art.save()
            return redirect('art-detail', pk=art.pk)
    else:
        form = ArtForm()
    return render(request, 'blog/post_edit.html', {'form': form})
