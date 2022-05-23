from gc import collect
import imp
from django.contrib import admin
from .models import Category, Brand, Collection, Color, Dimension, Finish, Option, OptionValue, Pattern, Product, ProductReview, ProductVariant, VariantValue, Supplier, Base_relation_table, tag, ProductMeta, Dimensions_has_product_variant

# Register your models here.
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Collection)
admin.site.register(Product)
admin.site.register(Option)
admin.site.register(OptionValue)
admin.site.register(Pattern)
admin.site.register(Finish)
admin.site.register(Color)
admin.site.register(Dimension)
admin.site.register(ProductVariant)
admin.site.register(VariantValue)
admin.site.register(ProductReview)
admin.site.register(ProductMeta)
admin.site.register(tag)
admin.site.register(Supplier)
admin.site.register(Dimensions_has_product_variant)
admin.site.register(Base_relation_table)