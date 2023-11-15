from App import app, db
from flask_admin import Admin, BaseView, expose
from App.models import Categories, Products, UserRoleEnum
from flask_admin.contrib.sqla import ModelView
from flask_login import  logout_user, current_user
from flask import redirect

admin = Admin(app=app, name='Quản lý bán hảng', template_mode='bootstrap4')


# chặn quyền truy cập
# is_authenticated: True là đn còn false là hk
class AuthenticatedAdmin(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == UserRoleEnum.ADMIN


class AuthenticatedUser(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated

class CategoriesView(AuthenticatedAdmin):
    column_list = ['id','name','products']
    can_export = True
    column_searchable_list = ['name']


class ProductsView(AuthenticatedAdmin):
    column_list = ['id','name','price']
    can_export = True
    column_searchable_list = ['name']
    column_filters = ['price','name']
    column_editable_list = ['name','price']
    details_modal = True
    edit_modal = True


class StateView(AuthenticatedUser):
    @expose("/")
    def __index__(self):
        return self.render('admin/state.html')

class LogoutView(AuthenticatedUser):
    @expose("/")
    def index(self):
        logout_user()
        return  redirect('/admin')


admin.add_view(CategoriesView(Categories, db.session))
admin.add_view(ProductsView(Products, db.session))
admin.add_view(StateView(name='Thống Kê Báo Cáo'))
admin.add_view(LogoutView(name='Đăng xuất'))