from flask import render_template,request
from app import app

# Return the main page http://127.0.0.1:5000/ or when /index is present (http://127.0.0.1:5000/index)
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    return render_template('index.html', title='Home', user=user)

# Expecting a parameter username (http://127.0.0.1:5000/profile/derek)
# the parameter name needs to be the same with variable
@app.route('/profile/<username>')
def profile(username):
    return '<h2>Hey there %s<h2>' %username

# Casting parameter to integer
@app.route('/id/<int:post_id>')
def id(post_id):
    return '<h2>Your id number is:  %s<h2>' %post_id

# import request module
@app.route('/type')
def type_request():
    return 'Method Used: %s' %request.method

# Set default = none if no input detected
@app.route('/state/<state>')
def state(state=None):
    return render_template('state.html',name=state)


# point to the country.html files in the templates folder
# need to import render_template from flask
# pass the variable name to the template
@app.route('/countries/<country>')
def country(country):
    return render_template('country.html',name=country)

@app.route('/food/')
def food():
    food = ["Cheese", "Tuna", "Pork"]
    return render_template('food.html',food=food)