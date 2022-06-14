from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from ckeditor.fields import RichTextField
from utils.__init__ import create_new_ref_number


class Supplier(models.Model):
    company_name = models.CharField(max_length=50, null=False)
    supplier_first_name = models.CharField(max_length=50, null=False)
    supplier_last_name = models.CharField(max_length=50, null=False)
    contact_title = models.CharField(max_length=50)
    contact = models.IntegerField(null=False,
                                    validators=[
                                        MinValueValidator(0000000000),
                                        MaxValueValidator(9999999999)
                                    ]
                                    )
    email = models.CharField(max_length=50, null = False)
    address_1 = models.CharField(max_length=100)
    address_2 = models.CharField(max_length=100)
    city = models.CharField(max_length=50, null = False)
    state = models.CharField(max_length=50, null = False)
    Pincode = models.IntegerField(null=False,
                                validators=[
                                    MinValueValidator(000000),
                                    MaxValueValidator(999999)
                                ]
                                )
    country = models.CharField(max_length=50, default='India')
    site_url = models.CharField(max_length=100, null=True)
    gst_in = models.CharField(max_length=100, null=False)
    pan = models.CharField(max_length=100, null=False)
    thumbnail = models.ImageField(
                                default='avatar.jpg', upload_to="supplier_image")
    is_active = models.BooleanField(default=True)
    notes = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.company_name


class Category(models.Model):
    cateegory_name = models.CharField(max_length=50, null=False)
    thumbnail = models.ImageField(default='avatar.jpg',upload_to="Category_image")
    
    class Meta:
        verbose_name_plural = 'Category'

    def __str__(self):
        return self.cateegory_name


class Brand(models.Model):
    brand_name = models.CharField(max_length=50, null=False)
    thumbnail = models.ImageField(default='avatar.jpg', upload_to="Brands_images")
    
    class Meta:
        verbose_name_plural = 'Brand'

    def __str__(self):
        return self.brand_name


class Collection(models.Model):
    collection_name = models.CharField(max_length=50, null=False)
    thumbnails = models.ImageField(default='avatar.jpg', upload_to="Collections_image")
    
    class Meta:
        verbose_name_plural = 'collection'

    def __str__(self):
        return self.collection_name


class Tag(models.Model):
    tag_name = models.CharField(max_length=75, null=True)

    def __str__(self):
        return self.tag_name


class Type(models.Model):
    type_name = models.CharField(max_length=75, null=True)
    thumbnail = models.ImageField(default='avatar.jpg', upload_to="type_image")

    def __str__(self):
        return self.type_name


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    supplier = models.ForeignKey(
        Supplier, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=50, null=False)
    meta_title = models.CharField(max_length=100, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    collection = models.ForeignKey(
        Collection, on_delete=models.SET_NULL, null=True)
    # slug = models.SlugField(max_length=100, null=True, blank=True)
    description = RichTextField(config_name='portal_config')
    price = models.FloatField(null=False, blank=True)
    discount_percent = models.FloatField(null=False, blank=True)
    discount_amount = models.FloatField(null=False, blank=True)
    summary = models.TextField(blank=True)
    quantity = models.SmallIntegerField(null=False)
    type = models.ForeignKey(Type,  on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag)
    sku = models.CharField(
        max_length=10,
        blank=True,
        editable=False,
        unique=True,
        default=create_new_ref_number(10)
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Product'

    def __str__(self):
        return self.title


class Base_relation_table(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    collection = models.ForeignKey(Collection, on_delete=models.DO_NOTHING)


class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    image = models.ImageField(default='avatar.jpg', upload_to="product_image")


class VoucherCode(models.Model):
    coupon_code = models.CharField(
        max_length=8,
        blank=True,
        editable=True,
        unique=True,
        default=create_new_ref_number(8)
    )
    discount_amount = models.FloatField(null=False, blank=True)
    discount_perc = models.FloatField(null=False, blank=True)
    is_active = models.BooleanField(default=True)
    validity = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Voucher'

    def __str__(self):
        return self.coupon_code


class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    parent = models.BigIntegerField(null=False)
    title = models.CharField(max_length=100, null=False)
    rating = models.SmallIntegerField(null=False)
    published = models.SmallIntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(auto_now=True)
    review = models.TextField(blank=True)