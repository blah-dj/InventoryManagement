"""
Routes and views for the flask application.
"""

import pyodbc

from datetime import datetime
from flask import render_template, request
from InventoryManagement import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'action.html'
    )

@app.route('/display_inventory')
def display_category():
    """Displays inventory"""
    return render_template(
        'category.html', category=get_category()
    )

@app.route('/update_inventory')
def update_category():
    """Displays inventory"""
    return render_template(
        'update_category.html', category=get_category()
    )

def get_category():
    server = 'home-stuff.database.windows.net'
    database = 'TheVadersInventoryManagement'
    username = 'thevaders'
    password = 'Zomb!e1421'
    driver= '{ODBC Driver 13 for SQL Server}'
    cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
    record = cursor.execute("select * from categories")
    categories = record.fetchall()   
    return categories

@app.route('/display/', methods=['POST', 'GET'])
def display_inventory():
    """Displays inventory"""
    if request.method == 'POST':
        category = str(request.form['getinventoryfor'])
    if request.method == 'GET':
        category = str(request.args.get('getinventoryfor'))
        '''
        category = str(request.query_string)
        import pdb;pdb.set_trace()
        (Pdb) category
        'getinventoryfor=Kitchen'
        (Pdb) type(category)
        <type 'str'>
        (Pdb) category.split('=')
        ['getinventoryfor', 'Kitchen']
        (Pdb) category.split('=')[1]
        'Kitchen'
        (Pdb)
        '''
    return render_template(
        'category_state.html', category=getinventorystatus(category)
    )

@app.route('/update/', methods=['POST', 'GET'])
def update_inventory():
    """Displays inventory"""
    if request.method == 'POST':
        category = str(request.form['getinventoryfor'])
    if request.method == 'GET':
        category = str(request.args.get('getinventoryfor'))
        '''
        category = str(request.query_string)
        import pdb;pdb.set_trace()
        (Pdb) category
        'getinventoryfor=Kitchen'
        (Pdb) type(category)
        <type 'str'>
        (Pdb) category.split('=')
        ['getinventoryfor', 'Kitchen']
        (Pdb) category.split('=')[1]
        'Kitchen'
        (Pdb)
        '''
    return render_template(
        'inventory_state.html', category=getinventorystatus(category)
    )

def getinventorystatus(category):
    server = 'home-stuff.database.windows.net'
    database = 'TheVadersInventoryManagement'
    username = 'thevaders'
    password = 'Zomb!e1421'
    driver= '{ODBC Driver 13 for SQL Server}'
    cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
    record = cursor.execute("select items.name, items.quantity, categories.category from items INNER JOIN categories ON categories.id=items.category and categories.category='%s'" % category)
    categories = record.fetchall()
    return categories

@app.route('/add_item/')
def update_item():
    """Displays inventory"""
    item_list = str(request.args.get('item'))
    item = item_list.split('_')[0].replace("+", " ")
    if len(item_list.split('_')) == 3:
        category = item_list.split('_')[1].replace("+", " ")
        quantity = int(item_list.split('_')[2].replace("+", " "))
        return render_template('update_existing_item.html', item=item,
                               category=category, quantity=quantity)
    if item == "Add New Item":
        return render_template('add_new_item.html')

def update_database(category, item, quantity):
    server = 'home-stuff.database.windows.net'
    database = 'TheVadersInventoryManagement'
    username = 'thevaders'
    password = 'Zomb!e1421'
    driver= '{ODBC Driver 13 for SQL Server}'
    cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
    record = cursor.execute("select items.name, items.quantity, categories.category from items INNER JOIN categories ON categories.id=items.category and categories.category='%s'" % category)
    categories = record.fetchall()
    return categories