from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from product.models import Product

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=50, null=False)
    state = models.CharField(max_length=50, null=False)
    pin_code = models.IntegerField(null=False, 
        validators=[
            MinValueValidator(0000),
            MaxValueValidator(9999)
            ]   
    )
    country = models.CharField(max_length=50, null=False)
    address_line1 = models.CharField(max_length=100, null=False)
    address_line2 = models.CharField(max_length=100, null=False)

    class Meta:
        verbose_name_plural = 'Address'

class BillingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    b_city = models.CharField(max_length=50, null=False)
    b_state = models.CharField(max_length=50, null=False)
    b_pin_code = models.IntegerField(null=False, 
        validators=[
            MinValueValidator(0000),
            MaxValueValidator(9999)
            ]
    )
    b_country = models.CharField(max_length=50, null=False)
    b_address_line1 = models.CharField(max_length=100, null=False)
    b_address_line2 = models.CharField(max_length=100, null=False)

    class Meta:
        verbose_name_plural = 'BillingAddress'

class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    s_city = models.CharField(max_length=50, null=False)
    s_state = models.CharField(max_length=50, null=False)
    s_pin_code = models.IntegerField(null=False, 
        validators=[
            MinValueValidator(0000),
            MaxValueValidator(9999)
            ]
    )
    s_country = models.CharField(max_length=50, null=False)
    s_address_line1 = models.CharField(max_length=100, null=False)
    s_address_line2 = models.CharField(max_length=100, null=False)

    class Meta:
        verbose_name_plural = 'ShippingAddress'

class Credit_Card(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    creditcard_type = models.CharField(max_length=25, null=False)
    creditcard_exp_month = models.IntegerField(null=False,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(12)
    ]
    )
    creditcard_exp_year = models.IntegerField(
        validators=[
            MinValueValidator(0000),
            MaxValueValidator(9999)
    ]
    )

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=50,null=False)

class Shipper(models.Model):    
    company_name = models.CharField(max_length=50,  null=False)
    contact = models.IntegerField(
        validators=[
            MinValueValidator(0000),
            MaxValueValidator(9999)
    ])

class Whishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)


#------------------------Shopping cart models–----------------------

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.SmallIntegerField(blank=True)
    subtotal = models.FloatField()
    item_discount = models.FloatField()
    tax = models.FloatField()
    shipping_charge = models.FloatField()
    total = models.FloatField()
    discount = models.FloatField()
    coupon_code = models.ForeignKey(VoucherCode, on_delete=models.CASCADE)
    grand_total = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=False)
    updated_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.BigIntegerField(null=False)
    order = models.BigIntegerField(null=False)
    sku = models.CharField(max_length=100, null=False)
    price = models.FloatField(null=False, blank=True)
    discount = models.FloatField(null=False, blank=True)
    quantity = models.SmallIntegerField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    context = models.TextField(blank=True)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=False)

class Cart_item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart     = models.ForeignKey(Cart, on_delete=models.CASCADE)
    price = models.IntegerField(null=False)
    discount = models.FloatField(null=False)
    quantity = models.SmallIntegerField(null=False)
    active = models.SmallIntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=False)
    updated_at = models.DateTimeField(auto_now_add=False)
    content = models.TextField(blank=True)

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    code = models.CharField(max_length=100, null=False)
    type = models.SmallIntegerField(blank=True)
    mode = models.SmallIntegerField(blank=True)
    status = models.SmallIntegerField(blank=True)
    created_at = models.DateTimeField(auto_now_add=False)
    updated_at = models.DateTimeField(auto_now_add=True)
    context = models.TextField(blank=True)

# class Transactions(models.Model):
#     txn_id = models.CharField(max_length=50, null=False)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
#     order = models.ForeignKey(Orders, on_delete=models.CASCADE)
#     amount = models.FloatField(null=False, blank=True)
#     other_charges = models.FloatField(null=False, blank=True)
#     tax = models.FloatField(null=False, blank=True)
#     response = models.CharField(max_length=250, null=False)
#     response = models.CharField(max_length=15, null=False)
#     created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
#     updated_at = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return self.txn_id