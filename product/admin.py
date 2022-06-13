from gc import collect
import imp
from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Collection)
admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(Type)
admin.site.register(ProductImages)
admin.site.register(VoucherCode)
admin.site.register(ProductReview)
admin.site.register(Supplier)
admin.site.register(Base_relation_table)