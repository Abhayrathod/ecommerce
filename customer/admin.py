from hashlib import new
from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Address)
admin.site.register(BillingAddress)
admin.site.register(ShippingAddress)
admin.site.register(Shipper)
admin.site.register(Credit_Card)
admin.site.register(Payment)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Cart)
admin.site.register(Cart_item)
admin.site.register(Transaction)
admin.site.register(demo)