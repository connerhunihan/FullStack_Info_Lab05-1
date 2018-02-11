""" All Flask Application creates an application instance. The web server passes requests it receives
    from clients to this created_object, using a protocol call WSGI here, we are importing Flask library """
from flask import Flask
from flask import make_response #this is for returning response objects to request
from flask import redirect #redirect to webpages
from flask import render_template
from flask.ext.bootstrap import Bootstrap

""" Creating a flask application instance the name argument is_passed to
    flask application constructor. its used to determine the root path """
app = Flask(__name__)
bootstrap = Bootstrap(app)

""" Application instance needs to know what code to run when an URL gets requested
    The association between a URL nd function that handles it_is called a route
    app.route, the most convenient way to define a route @ flask """
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

""" To demonsrtrate routing"""
@app.route('/hello2')
def hello2():
    return '<h1>Hello World 2!</h1>'

""" To demonsrtrate redirect"""
@app.route('/hello3')
def hello3():
    return redirect('https://www.google.com')

""" To demonsrtrate how to set cookies using flask """
@app.route('/response_object')
def returnResponse():
    response = make_response('<h1>I give you cookies</h1>')
    response.set_cookie('Oreo', 'Yummy')
    return response

""" To demonsrtrate how to use variables in routing """
# @app.route('/user/<name>')
# def user(name):
#     return '<h1>Hello, %s!</h1>' % name

""" below code is for jinja template: demonstrate render_template"""
@app.route('/jinja')
def jinja():
    return render_template('index.html')

""" LAB """
@app.route('/netflix')
def netflix():
    return render_template('netflix.html')

""" Demonstrate how template can be imported """
@app.route('/import_example')
def import_example():
    return render_template('import_example.html')

""" Demonstrate how template can be extended """
@app.route('/extend')
def extend():
    return render_template('extend.html')

""" Demonstrate templates can use dictionary, list, objects """
@app.route('/user/<name>')
def user(name):
    mydict = {"key" : "value"}
    mylist = ['a', 'b', 'c', 'd']
    class myObj:
        def somemethod(self):
            return("This is a message inside the class.")
    myobj = myObj()
    return render_template('user.html', name=name, mydict=mydict, mylist=mylist, myobj=myobj)

""" Demonstrate templates can we can import bootstrap templates """
@app.route('/bootstrap_user/<name>')
def bootstrap_user(name):
    mydict = {"key" : "value"}
    mylist = ['a', 'b', 'c', 'd']
    class myObj:
        def somemethod(self):
            return("This is a message inside the class.")
    myobj = myObj()
    return render_template('bootstrap_user.html', name=name, mydict=mydict, mylist=mylist, myobj=myobj)

# Server Setup - This launches Flask integrated development web server
if __name__ == '__main__': # ensure only launched when name matches. If its imported by other script then it wont launch
    app.run(debug=True) # enable debug mode
