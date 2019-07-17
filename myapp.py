from flask import Flask, render_template
 
app = Flask(__name__)

@app.route('/foo/<name>')
def foo(name):
	return render_template('index.html', to=name)


@app.route('/<name>')
def index(name):
    return render_template('index.html', to=name)

@app.route('/whereis')
def words():
	word = "this is me work please"
	return word

@app.route('/whereami')
def whereami():
    return 'Ghana!'
 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')