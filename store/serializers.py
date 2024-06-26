from rest_framework import serializers

from store.models import Category, Product, ProductImage, Request, Order


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'description', 'image', 'slug')


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('image',)


class ProductSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'category', 'title', 'quantity', 'daily_price', 'hourly_price', 'description', 'slug', 'images')

    def get_images(self, obj):
        return [image.image.url for image in obj.images.all()]


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ('id', 'title', 'phone', 'description')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'name', 'phone', 'address', 'description', 'product', 'type', 'price', 'quantity')
