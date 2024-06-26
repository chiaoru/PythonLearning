from django.db import models

# Create your models here.

class myNews(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    photo_url = models.CharField(max_length=200)
    c_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'news' # 資料庫中的資料表名稱，所以跟applications同名沒關係