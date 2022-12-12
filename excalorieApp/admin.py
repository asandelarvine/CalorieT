from django.contrib import admin
from .models import *

# Register your models here.

class foodAdmin(admin.ModelAdmin):
    class Meta:
        model=Fooditem
    list_display=['name']
    list_filter=['name']
    
class BmiAdmin(admin.ModelAdmin):
    list_display = ('user', 'weight', 'height', 'bmi', 'date')

admin.site.register(Profile)
admin.site.register(UserFooditem)
admin.site.register(Category)
admin.site.register(Fooditem,foodAdmin)
admin.site.register(Bmi, BmiAdmin)
