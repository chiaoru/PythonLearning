from django.db import models

# Create your models here.

# 如要在 django 中要上傳圖片的話，需要安裝pillow
# pip install pillow

from django.utils import timezone

class Photo(models.Model):
    image = models.ImageField(upload_to='images/', blank=False, null=False)
    upload_date=models.DateField(default=timezone.now)