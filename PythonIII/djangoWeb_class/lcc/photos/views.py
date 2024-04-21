from django.shortcuts import render, redirect

# Create your views here.

from .forms import UploadModelForm
from .models import Photo

def uploadFile(request): # 建立上傳表單物件
    photos = Photo.objects.all()
    form = UploadModelForm()
    if request.method == 'POST':
        form = UploadModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            redirect('/photos')
    context = {
        'photos':photos,
        'form':form
        }
    
    return render(request, 'photos.html', locals())