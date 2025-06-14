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
@app.route('/')
def index():
    return render_template('index.html', product = products)

app.run(debug=True)