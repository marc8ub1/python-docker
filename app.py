from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return '<h1>Hello, world!</h1><p>Welcome to my webpage.</p>'


@app.route('/hello/<name>')
def hello_world(name):
    return render_template('hello_name.html', name=name.title())


if __name__ == "__main__":
    app.run(debug=True)
