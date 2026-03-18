from django.shortcuts import render
from .models import Article

# Create your views here.
def home_page(request):
    articles = Article.objects.all()
    return render(request,"index.html",{"mes_articles": articles})