from SaleApp.App import app, db
from flask_admin import Admin
from SaleApp.App.models import Categories, Products
from flask_admin.contrib.sqla import ModelView

admin = Admin(app=app, name='Quản lý bán hảng', template_mode='bootstrap4')


class CategoriesView(ModelView):
    column_list = ['id','name','products']
    can_export = True
    column_searchable_list = ['name']


class ProductsView(ModelView):
    column_list = ['id','name','product_id']
    can_export = True
    column_searchable_list = ['name']
    column_filters = ['price','name']
    column_editable_list = ['name','price']
    details_modal = True
    edit_modal = True

admin.add_view(CategoriesView(Categories, db.session))
admin.add_view(ProductsView(Products, db.session))