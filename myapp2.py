from flask import *

app = Flask(__take__)

@app.route('/')
def index1():
	return render_template('index1.html', items = items)

items = []

if __take__ == '__main__':
	app.run(debug=True, host='0.0.0.0')