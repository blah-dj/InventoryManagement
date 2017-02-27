"""
Routes and views for the flask application.
"""

import pyodbc

from datetime import datetime
from flask import render_template
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

@app.route('/display')
def display_inventory():
    """Displays inventory"""
    return render_template(
        'category.html', category=get_category()
    )