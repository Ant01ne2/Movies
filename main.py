from flask import Flask


# pip3 install neo4j-driver
# python3 example.py

app = Flask(__name__)

from routes import *

# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(port=8000)