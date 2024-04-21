from django.shortcuts import render

# Create your views here.
from .models import Travel
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def tours(request):
    
    platform = ''
    if 'platform' in request.GET:
        
        platform = request.GET['platform']
        if (platform == "全部"):
            alltours = Travel.objects.all().order_by('createDate')
        elif (len(platform) > 0):
            alltours = Travel.objects.filter(area__icontains=platform).order_by('-createDate')
        
        else:
            alltours = Travel.objects.all().order_by('createDate')
            
    else:
        alltours = Travel.objects.all().order_by('createDate')
    
    region = ''
    if 'region' in request.GET:
        
        region = request.GET['region']
        if (region == "全區"):
            alltours = Travel.objects.all().order_by('createDate')
            
        elif (len(region) > 0):
            alltours = Travel.objects.filter(area__icontains=region).order_by('-createDate')
        
        else:
            alltours = Travel.objects.all().order_by('-createDate')
    else:
        alltours = Travel.objects.all().order_by('-id') 
        
    tour = ''
    if "tour" in request.GET:
        
        t = request.GET['tour']
        
        if (len(t) > 0):
            alltours = Travel.objects.filter(area__icontains=t).order_by('-price')
        else:
            alltours = Travel.objects.all().order_by('-id') 
    else:
        alltours = Travel.objects.all().order_by('id') 
    # 表示所有的資料all()由大到小排序order_by('-id')
    # order_by 排序 id 是欄位名稱
    # order_by('id') 依 id 做遞增
    # order_by('-id') 依 id 做遞減
        
    paginator = Paginator(alltours,9)
    page = request.GET.get('page')
    try:
        alltours = paginator.page(page)
    
    except PageNotAnInteger:
        alltours = paginator.page(1)
        
    except EmptyPage:
        alltours = paginator.page(paginator.num_pages)

    return render(request,'tour.html',locals())
    # locals() 將函式 tour 中的變數整個帶過去給 tour.html