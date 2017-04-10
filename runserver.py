"""
This script runs the InventoryManagement application using a development server.
"""

from os import environ
from InventoryManagement import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', '')
    try:
        PORT = int(environ.get('SERVER_PORT', '80'))
    except ValueError:
        PORT = 80
    app.debug=True
    app.run(HOST, PORT)

