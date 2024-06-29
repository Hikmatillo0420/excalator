from django.core.exceptions import ValidationError
from django.db.models import Model, DateTimeField, CharField, TextField, ImageField, SlugField, IntegerField, \
    FloatField, \
    PositiveBigIntegerField, ForeignKey, CASCADE
from re import sub as re_sub
from re import match as re_match
from django.db import models

from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class BaseModel(Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if hasattr(self, 'slug') and not self.slug:
            self.slug = self.generate_slug(self.title if getattr(self, 'title', None) else self.name)
        super().save(force_insert, force_update, using, update_fields)

    def generate_slug(self, text):
        s = re_sub(r'[^\w\s-]', '', text).strip().lower()
        s = re_sub(r'\s+', '-', s)
        s = re_sub(r'-+', '-', s)
        existing_slugs = self.__class__.objects.filter(slug__startswith=s).last()
        if existing_slugs:
            number = existing_slugs.slug.split('-')[-1]
            s = f'{s}-{int(number) + 1}' if number.isdigit() else f'{s}-1'
        return s


def validate_phone(value):
    clean_number = re_sub(r'[^\d]', '', value)
    if clean_number.startswith('998'):
        if re_match(r'^998\d{9}$', clean_number):
            return clean_number
    raise ValidationError("Invalid phone number format. Please use '998yyxxxxxxx'.")


class Category(BaseModel):
    title = CharField(max_length=255, verbose_name=_("Name"))
    description = TextField(verbose_name=_('Description'))
    image = ImageField(upload_to='images/category', verbose_name=_('Image'))
    slug = SlugField(max_length=255, verbose_name=_('Slug'), unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        app_label = 'store'


class Product(BaseModel):
    category = ForeignKey('store.Category', on_delete=CASCADE, verbose_name=_('Category'))
    title = CharField(max_length=255, verbose_name=_("Name"))
    quantity = PositiveBigIntegerField(default=1, verbose_name=_('Quantity'))
    # made_in = CharField(max_length=255, null=True, verbose_name=_('made_in'))
    daily_price = FloatField(verbose_name="daily_price", default=0)
    hourly_price = FloatField(verbose_name="hourly_price", default=0)
    description = TextField(verbose_name=_('Description'))
    slug = SlugField(max_length=255, verbose_name=_('Slug'), unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwargs)


class ProductImage(BaseModel):
    product = ForeignKey('store.Product', on_delete=CASCADE, related_name='images', verbose_name='product')
    image = ImageField(upload_to="images/product", verbose_name=_('Image'))

    def __str__(self):
        return str(self.product.title)


class Request(BaseModel):
    title = CharField(max_length=255, verbose_name=_("Name"))
    phone = CharField(_('Phone'), max_length=255, validators=(validate_phone,))
    description = TextField(verbose_name=_('Description'))

    def __str__(self):
        return self.title


class Order(BaseModel):
    class TimeType(models.TextChoices):
        daily_price = 'daily_price', _('daily_price')
        hourly_price = 'hourly_price', _('hourly_price')

    name = CharField(max_length=255, verbose_name=_('Full name'))
    phone = CharField(_('Phone'), max_length=255, validators=(validate_phone,))
    address = CharField(max_length=255, verbose_name=_("Address"),  null=True, blank=True)
    description = TextField(verbose_name=_('Description'), null=True, blank=True)
    product = ForeignKey('store.Product', on_delete=CASCADE, related_name='orders', verbose_name='product')
    type = CharField(max_length=255, verbose_name=_('Type'), choices=TimeType.choices)
    price = FloatField(verbose_name=_('Price'))
    quantity = IntegerField(default=1, verbose_name=_('Quantity'))

    def __str__(self):
        return self.name
