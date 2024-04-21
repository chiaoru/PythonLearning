from django.shortcuts import render

# Create your views here.
from .models import myNews

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def news(request):
    data = myNews.objects.all()
    
    # 分頁用
    paginator = Paginator(data, 15)
    page = request.GET.get('page')
    
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    
    
    
    return render(request, 'news.html', locals())

