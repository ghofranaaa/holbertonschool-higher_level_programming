from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    products = []
    error = None

    if source == 'json':
        products = read_json_data('products.json')
    elif source == 'csv':
        products = read_csv_data('products.csv')
    elif source == 'sql':
        products = read_sql_data()
    else:
        error = "Wrong source"

    if product_id is not None:
        products = [p for p in products if p['id'] == product_id]
        if not products and not error:
            error = "Product not found"

    return render_template('product_display.html', products=products, error=error)

def read_json_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def read_csv_data(file_path):
    products = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['price'] = float(row['price'])
            row['id'] = int(row['id'])
            products.append(row)
    return products

def read_sql_data():
    products = []
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()
        for row in rows:
            products.append({
                'id': row[0],
                'name': row[1],
                'category': row[2],
                'price': row[3]
            })
        conn.close()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    return products

if __name__ == '__main__':
    app.run(debug=True, port=5000)
