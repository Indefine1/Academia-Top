from flask import Flask, render_template_string,render_template

app = Flask(__name__)

products = [{
    'product_name':'Телевизор',
    'price': 10000},
    {'product_name': 'Компьютер',
    'price': 100000},
    {'product_name':'Холодильник',
    'price': 20000}
    ]
purchase = [{
    'product_name':'Стиральная машина','price': 12000},
    {'product_name':"Электрическая плита",'price': 15000},
    {'product_name':'Стиральный порошок','price': 450}]

@app.route('/')
def index():
    return render_template('index.html', product = products)

@app.route('/products')
def purchase_product():
    return render_template('products.html', purchase_product = purchase)

@app.route('/products/0')
def view_product():
    return render_template('0.html', purchase_product = purchase)

app.run(debug=True)