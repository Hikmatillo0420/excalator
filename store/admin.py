from django.contrib import admin
from django.utils.html import format_html

from store.models import Category, Product, Request, Order, ProductImage



class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0
    fields = ['image', 'display_image']
    readonly_fields = ['display_image']

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 100px; height:auto;" />', obj.image.url)
        return "No Image"

    display_image.short_description = 'Current Image'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # exclude = 'slug',
    list_display = ['id', 'title', 'description', 'category_image']
    prepopulated_fields = {'slug': ('title',)}

    def category_image(self, obj: Category):
        return format_html(f'<img style="border-radius: 5px;" width="50px" height="50px" src="{obj.image.url}"/>')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    exclude = 'slug',
    list_display = ['id', 'title', 'quantity', 'daily_price', 'hourly_price', 'description']


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'phone', 'description']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'address', 'description', 'product', 'type', 'price', 'quantity']
