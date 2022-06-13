from product.models import Product, Category

def get_categoryes():
    categoryes = Category.objects.all()
    return categoryes

def get_categoryes_by_name(cat_name):
    category = Category(name=cat_name)
    return category

def get_product_details():
    products = []
    item = {}
    # item['product'] = Pro
    pass