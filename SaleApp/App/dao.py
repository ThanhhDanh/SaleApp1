from SaleApp.App.models import Categories, Products

def load_categories():
   return  Categories.query.all()

def load_products(kw=None):
    product = Products.query
    if kw:
        product = product.filter(Products.name.contains(kw))
    return product
