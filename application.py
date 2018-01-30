from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

a = ['12', 'ab', 'cdef']

@app.route('/<name>')
def index(name):
    return render_template('user.html', name=a[1:])


@app.route('/')
def cctv():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
