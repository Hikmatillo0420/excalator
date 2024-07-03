from modeltranslation.translator import TranslationOptions, register

from store.models import Category, Product


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
