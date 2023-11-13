from flask import render_template, request
import dao
from SaleApp.App import app, login
from SaleApp.App.Admin import admin

@app.route('/')
def index():
    kw = request.args.get('kw')
    return render_template(
        'index.html',
        categories = dao.load_categories(),
        products=dao.load_products(kw)
    )
@app.route('/admin/login', methods=['post'])
def admin_login():
    request.form.get('username')
    request.form.get('password')
@login.user_loader
def get_user(user_id):
    return dao.get_user_by_id(user_id)

if __name__ == "__main__":
    app.run(debug=False)