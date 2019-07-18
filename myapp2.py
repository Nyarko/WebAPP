from flask import *

app = Flask(__name__)

@app.route('/')
def index1():
	return render_template('index1.html', items = items)

items = []

@app.route('/add_todo')
def add_todo():
	item = request.args.get("item")
	items.append(item)
	return redirect("http://localhost:5000/", code=302)

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')