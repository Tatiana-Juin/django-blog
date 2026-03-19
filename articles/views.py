from django.shortcuts import render, get_object_or_404
from .models import Article

# Create your views here.
def home_page(request):
    articles = Article.objects.all()
    return render(request,"index.html",{"mes_articles": articles})

def un_article(request,article_id):
    # articles = Article.objects.all()
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'un_article.html', {'article': article})