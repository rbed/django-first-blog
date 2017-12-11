from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Category
from django.utils import timezone
from .forms import ArtForm

# Create your views here.

#widok listy art
#widok art

def article_list(request):
    article = Article.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')
    category = Category.objects.all()
    return render(request, 'blog/post_list.html', {'article': article, "category": category})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    category = Category.objects.all()
    return render(request, 'blog/art_detail.html', {'art': article, "category": category})

def article_new(request):
    if request.method == "POST":
        form = ArtForm(request.POST)
        if form.is_valid():
            art = form.save(commit=False)
            art.author = request.user
            art.pub_date = timezone.now()
            art.save()
            return redirect('blog:art-detail', pk=art.pk)
    else:
        form = ArtForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def category_list(request, pk):
    category = Category.objects.all()
    article = Article.objects.filter(category=pk)
    return render(request, 'blog/category_list.html', {'article': article, "category": category})
