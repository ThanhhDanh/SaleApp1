from flask import Flask, render_template, request
import dao
app = Flask(__name__)
@app.route('/')
def index():
    request.args.get('kw')
    return render_template(
        'index.html',
        categories = dao.load_categories(),
        products=dao.load_products()
    )

if __name__ == "__main__":
    app.run(debug=True)