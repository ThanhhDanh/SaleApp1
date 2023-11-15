from App.models import Categories, Products, User
import hashlib
from App import app

def load_categories():
   return  Categories.query.all()

def load_products(kw=None, cate_id = None, page =None):
    product = Products.query
    if kw:
        product = product.filter(Products.name.contains(kw))

    if cate_id:
        product = product.filter(Products.product_id.__eq__(cate_id))

    if page:
        page = int(page)
        page_size = app.config['PAGE_SIZE']
        start = (page - 1)*page_size

        return product.slice(start, start + page_size)

    return product.all()


def get_user_by_id(user_id):
    return User.query.get(user_id)

def auth_user(username, password):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    return  User.query.filter(User.username.__eq__(username.strip()),
                              User.password.__eq__(password)).first()