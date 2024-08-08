from django.urls import path

from store.views import CatgoryListView, ProductListView, ProductListByCategoryView, RequestView, OrderView, \
    ProductDetailView, UrlVideoView

urlpatterns = [
    path('category', CatgoryListView.as_view(), name='category'),
    path('category/<slug:slug>', ProductListByCategoryView.as_view(), name='category_products'),
    path('product', ProductListView.as_view(), name='product'),
    path('product/<slug:slug>', ProductDetailView.as_view(), name='product_detail'),  # Yangi yo'l
    path('request', RequestView.as_view(), name='request'),
    path('order', OrderView.as_view(), name='order'),
    path('urlVideo', UrlVideoView.as_view(), name='urlVideo'),

]
