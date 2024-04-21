from django.shortcuts import render

# Create your views here.

from .models import Goods
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

def product(request):
    
    q = ""
    sp = ""
    ep = ""
    
    if 'q' in request.GET:
        q = request.GET['q']
        sp = request.GET['startp']
        ep = request.GET['endp']
        
        if len(q) > 0 and len(sp) == 0 and len(ep) == 0:
            data = Goods.objects.filter(name__icontains=q).order_by('-price')
        elif len(q) == 0 and len(sp) > 0 and len(ep) > 0:
            data = Goods.objects.filter(price__gte=sp, price__lte=ep).order_by('price')
    else:
    
        data = Goods.objects.all().order_by('-id')
    
    # 分頁
    paginator = Paginator(data, 36)
    page = request.GET.get('page')
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
        
    return render(request, 'product.html', locals())