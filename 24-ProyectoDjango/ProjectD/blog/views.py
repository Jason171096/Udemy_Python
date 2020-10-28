from django.shortcuts import render
from blog.models import Category, Article
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def articles(request):

    #Sacar los articulos
    articles = Article.objects.all()
    paginator = Paginator(articles, 2)

    #recoger un numero de pagina
    page = request.GET.get('page')
    page_articles = paginator.get_page(page)


    return render(request, 'articles.html', {
        'title': 'Articulos',
        'articles': page_articles
    })

@login_required(login_url='login')
def category(request, category_id):

    category = Category.objects.get(id=category_id)

    return render(request, 'category.html', {
        'category': category
    })

@login_required(login_url='login')
def article(request, article_id):

    article = Article.objects.get(id=article_id)

    return render(request, 'article.html', {
        'article': article
    })
