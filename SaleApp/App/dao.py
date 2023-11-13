from SaleApp.App.models import Categories, Products, User

def load_categories():
   return  Categories.query.all()

def load_products(kw=None):
    product = Products.query
    if kw:
        product = product.filter(Products.name.contains(kw))
    return product


def get_user_by_id(user_id):
    return User.query.get(user_id)