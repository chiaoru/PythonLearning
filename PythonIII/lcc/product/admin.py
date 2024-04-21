from django.contrib import admin

# Register your models here.
from .models import Goods

class GoodsAdmin(admin.ModelAdmin): # 希望在後台有自訂顯示的方式
    list_display = ('name', 'price', 'c_date') # 在後台顯示的欄位名稱
admin.site.register(Goods, GoodsAdmin)