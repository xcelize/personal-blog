from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Article, Comment
from .forms import CommentForm


def index(request):
    # Je veux recuperer mes 5 derniers post
    try:
        four_last_articles = Article.objects.all().reverse()[5]
    except:
        four_last_articles = Article.objects.all()
    return render(request, 'blog/index.html', {
                  'five_articles': four_last_articles
                })


@login_required
def article(request, slug_article):
    article = Article.objects.get(slug=slug_article)
    return render(request, 'blog/article.html', {
        'article': article
    })

@login_required
def post_comment(request):
    if request.method == 'POST':
        form = CommentForm(request)
        if form.is_valid():
            content = request.POST.get('comment', False)
            Comment.create(content=content, user=request.user.id)
            return redirect('/blog/')



