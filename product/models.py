from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Supplier(models.Model):
    company_name = models.CharField(max_length=50, null=False)
    supplier_first_name = models.CharField(max_length=50, null=False)
    supplier_last_name = models.CharField(max_length=50, null=False)
    contact = models.IntegerField(null=False,
    validators=[
        MinValueValidator(0000000000),
        MaxValueValidator(9999999999)
    ]
    )
    email = models.CharField(max_length=50, null = False)
    city = models.CharField(max_length=50, null = False)
    state = models.CharField(max_length=50, null = False)
    Pincode = models.IntegerField(null=False,
    validators=[
        MinValueValidator(000000),
        MaxValueValidator(999999)
    ]
    )
    country = models.CharField(max_length=50, null=False)
    s_site = models.CharField(max_length=100, null=True)
    payment_methods = models.CharField(max_length=50, null=True)
    goods_type = models.CharField(max_length=50, null=True)
    notes = models.CharField(max_length=100, null=True)
    discount = models.CharField(max_length=50, null=True)

class Category(models.Model):
    cateegory_name = models.CharField(max_length=50, null=False)
    thumbnail = models.ImageField(default='avatar.jpg',upload_to="Category_image")
    
    class Meta:
        verbose_name_plural = 'Category'

class Brand(models.Model):
    brand_name = models.CharField(max_length=50, null=False)
    thumbnail = models.ImageField(default='avatar.jpg', upload_to="Brands_images")
    
    class Meta:
        verbose_name_plural = 'Brand'

class Collection(models.Model):
    collection_name = models.CharField(max_length=50, null=False)
    thumbnails = models.ImageField(default='avatar.jpg', upload_to="Collections_image")
    
    class Meta:
        verbose_name_plural = 'collection'

class Pattern(models.Model):
    option_name = models.CharField(max_length=50, null=False)
    
    class Meta:
        verbose_name_plural = 'Pattern'

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    pattern = models.ForeignKey(Pattern, on_delete=models.SET_NULL, null=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=50, null=False)
    meta_title = models.CharField(max_length=100, null=True)
    slug = models.SlugField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=50, null=False)
    price = models.FloatField(null=True, blank=True)
    discount = models.FloatField(null=True, blank=True) 
    summary = models.TextField(blank=True)
    quantity = models.SmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=False, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=True)
    starts_at = models.DateTimeField(auto_now_add=True)
    ends_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Product'

class Base_relation_table(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    collection = models.ForeignKey(Collection, on_delete=models.DO_NOTHING)

class Option(models.Model):
    option_name = models.CharField(max_length=50, null=False)
    product = models.ManyToManyField(Product)
    
    class Meta:
        verbose_name_plural = "Option"

class OptionValue(models.Model):
    Option = models.ForeignKey(Option, on_delete=models.CASCADE)
    value_name = models.CharField(max_length=50, null=False)
    class Meta:
        verbose_name_plural = "OptionValue"

class Finish(models.Model):
    finish_name = models.CharField(max_length=50, null=False)
    
    class Meta:
        verbose_name_plural = "Finish"

class Color(models.Model):
    color_name = models.CharField(max_length=50, null=False)
    
class Dimension(models.Model):
    dimension_value = models.CharField(max_length=50, null=False)

class ProductVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    finish = models.ForeignKey(Finish , on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    thumbnail = models.CharField(max_length=50, null=False)

    class Meta: 
        verbose_name_plural = 'Product variant'

class Dimensions_has_product_variant(models.Model):
    dimensions = models.ForeignKey(Dimension, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE)

class VariantValue(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    Option = models.ForeignKey(Option, on_delete=models.CASCADE)
    value = models.ForeignKey(OptionValue, on_delete=models.CASCADE)
    dimesions = models.ForeignKey(Dimensions_has_product_variant, on_delete=models.CASCADE)
    variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE)
    price = models.CharField(max_length=50, null=False)
    sku = models.CharField(max_length=50, null=False)


    class Meta:
        verbose_name_plural = 'Variant value'

class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    parent = models.BigIntegerField(null=False)
    title = models.CharField(max_length=100, null=False)
    rating = models.SmallIntegerField(null=False)
    published = models.SmallIntegerField(null=False)
    created_at =  models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(auto_now=True)
    context = models.TextField(blank=True)

class ProductMeta(models.Model):
    product = models.BigIntegerField(null=False)
    key = models.CharField(max_length=50, null=False)
    context = models.TextField(blank=True)

class tag(models.Model):
    title = models.CharField(max_length=75, null=True)
    metatitle = models.CharField(max_length=100, null=True)
    slug = models.CharField(max_length=100, null=True)
    context = models.TextField(blank=True)