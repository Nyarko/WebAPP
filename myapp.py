from flask import *
import json
#Flask, render_template, request, redirect, Response, json
import os
 
#app initializer
app = Flask(__name__)

#This calls or loads the html file
@app.route('/')
def index():
	return render_template('index.html', items=items)
items = []

#this is for the lists
@app.route('/add_todo')
def add_todo():
	item = request.args.get("item")
	date = request.args.get("date")
	itda = 'Item: ' + item  + '; Due: ' + date + '\n'
	items.append(itda)
	# this would return a new page with the listings:	", ".join(items)
	return redirect("http://localhost:5000/", code=302)

#for json get files
@app.route('/get_todos')
def get_todos():
	resp = Response(json.dumps(items))
	resp.headers['Content-Type'] = 'application/json'
	return resp

#this is to fill in the to
#@app.route('/<name>')
#def foo(name):
#    return render_template('index.html', to=name)

#in case i add /whereis, this will load
@app.route('/whereis')
def words():
	word = "this is me work please"
	return word

#will load this if /whereami is added to link
@app.route('/whereami')
def whereami():
    return 'Ghana!'
 
#handles app properties (something like that)
if __name__ == '__main__':
	port = os.environ.get('PORT', 5000)
app.run(debug=True, host='0.0.0.0', port=port)