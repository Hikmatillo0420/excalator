from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView

from store.models import Category, Product, Request, Order, UrlVideo
from store.serializers import CategorySerializer, ProductSerializer, RequestSerializer, OrderSerializer, \
    UrlVideoSerializer


class CatgoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListByCategoryView(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        slug = self.kwargs['slug']
        return Product.objects.filter(category__slug=slug)


class ProductListView(ListAPIView):
    queryset = Product.objects.order_by('-created_at')
    serializer_class = ProductSerializer


class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'


class RequestView(CreateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer


class OrderView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class UrlVideoView(RetrieveAPIView):
    queryset = UrlVideo.objects.all()
    serializer_class = UrlVideoSerializer
