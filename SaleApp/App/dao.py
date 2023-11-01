from SaleApp.App.models import Categories, Products

def load_categories():
   return  Categories.query.all()

def load_products(kw=None):
    products = Products.query
    if kw:
        products = products.filter(Products.name.contains(kw))
    return products
