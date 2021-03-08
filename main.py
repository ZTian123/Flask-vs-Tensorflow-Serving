# coding=utf-8
# This is a sample Python script.

from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'


@app.route('/hello')
def hello():
    return 'Hello, World'


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run()

