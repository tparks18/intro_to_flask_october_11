from app import app
from flask import render_template

@app.route('/')
def index():
    name = 'Tatyana'
    title = 'Coding Temple Flask'
    return render_template('index.html', name_of_user=name, title=title)

@app.route('/products')
def products():
    title = 'Products'
    products = ['apple', 'banana', 'peach', 'orange']
    return render_template('products.html', title=title, products=products)