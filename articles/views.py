from django.shortcuts import render

# Import Article from models in current directory
from .models import Article

# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by('date')
    # sending articles data to the template
    return render(request,'articles/article_list.html', {'articles': articles})
    # go to articles templates folder