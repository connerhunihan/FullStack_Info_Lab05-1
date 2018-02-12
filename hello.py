from flask import Flask
from flask import render_template

""" Creating a flask application instance the name argument is_passed to
    flask application constructor. its used to determine the root path """
app = Flask(__name__)

""" Application instance needs to know what code to run when an URL gets requested
    The association between a URL nd function that handles it_is called a route
    app.route, the most convenient way to define a route @ flask """
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

""" LAB """
@app.route('/netflix')
def netflix():
    return render_template('netflix.html')

# Server Setup - This launches Flask integrated development web server
if __name__ == '__main__': # ensure only launched when name matches. If its imported by other script then it wont launch
    app.run(debug=True) # enable debug mode
