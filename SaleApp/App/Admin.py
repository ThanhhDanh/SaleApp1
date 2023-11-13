from SaleApp.App import app, db
from flask_admin import Admin, BaseView, expose
from SaleApp.App.models import Categories, Products
from flask_admin.contrib.sqla import ModelView

admin = Admin(app=app, name='Quản lý bán hảng', template_mode='bootstrap4')


class CategoriesView(ModelView):
    column_list = ['id','name','products']
    can_export = True
    column_searchable_list = ['name']


class ProductsView(ModelView):
    column_list = ['id','name','price']
    can_export = True
    column_searchable_list = ['name']
    column_filters = ['price','name']
    column_editable_list = ['name','price']
    details_modal = True
    edit_modal = True

class StateView(BaseView):
    @expose("/")
    def __index__(self):
        return self.render('admin/state.html')

admin.add_view(CategoriesView(Categories, db.session))
admin.add_view(ProductsView(Products, db.session))
admin.add_view(StateView(name='Thống Kê Báo Cáo'))