from flask import Flask, request
from gevent.pywsgi import WSGIServer
import tensorflow as tf
import keras
import numpy as np


app = Flask(__name__)
app.config['DEBUG'] = False

tf.compat.v1.disable_eager_execution()


sess = tf.compat.v1.Session()
tf.compat.v1.keras.backend.set_session(sess)
MNIST_MODEL = keras.models.load_model('../model/1')


@app.route('/')
def index():
    return 'Index Page'


@app.route('/hello')
def hello():
    return 'Hello, World'


@app.route('/mnist-1', methods=['POST'])
def mnist():
    # print("@@@", request)
    # print("@@@", request.data.decode('utf-8'))
    model_input = request.json["image"]
    with sess.as_default():
        with sess.graph.as_default():
            model_output = sess.run(tf.convert_to_tensor(MNIST_MODEL.predict(model_input), dtype=tf.float32))
    return dict({'model_output': model_output.tolist()})


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=8502)
    # app.run()
    WSGIServer(('127.0.0.1', 8502), app).serve_forever()

