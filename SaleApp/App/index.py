from flask import render_template, request
import dao
from SaleApp.App import app
from SaleApp.App.Admin import admin

@app.route('/')
def index():
    kw = request.args.get('kw')
    return render_template(
        'index.html',
        categories = dao.load_categories(),
        products=dao.load_products(kw)
    )

if __name__ == "__main__":
    app.run(debug=False)