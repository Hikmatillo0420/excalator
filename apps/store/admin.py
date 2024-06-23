from _ast import Store

from django.contrib import admin
from django.utils.html import format_html

from apps.store.models import *


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude = 'slug',
    list_display = ['id', 'title', 'description', 'category_image']

    def category_image(self, obj: Category):
        return format_html(f'<img style="border-radius: 5px;" width="50px" height="50px" src="{obj.image.url}"/>')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    exclude = 'slug',
    list_display = ['id', 'title', 'quantity', 'daily_price', 'hourly_price', 'description']


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'phone', 'description']
