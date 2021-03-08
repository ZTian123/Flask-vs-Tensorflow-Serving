import numpy as np
from tensorflow import keras
import tensorflow as tf
import random as rand
from tensorflow_serving.apis import predict_pb2
import json

(_, _), (x_test, y_test) = keras.datasets.mnist.load_data()
x_test = x_test.astype("float32") / 255
x_test = np.expand_dims(x_test, -1)
test_range = [10, 19]



def get_grpc_request():
    idx = rand.randint(test_range[0], test_range[1])
    IMAGE_EXAMPLE = (np.array([x_test[idx]])).tolist()
    # IMAGE_EXAMPLE = (np.array([x_test[0]])).tolist()
    grpc_request = predict_pb2.PredictRequest()
    grpc_request.model_spec.name = 'tf_mnist'
    grpc_request.model_spec.signature_name = 'serving_default'
    grpc_request.inputs['input_1'].CopyFrom(tf.make_tensor_proto(IMAGE_EXAMPLE, shape=[1, 28, 28, 1]))
    return grpc_request


def get_tfs_rest_request():
    idx = rand.randint(test_range[0], test_range[1])
    IMAGE_EXAMPLE = (np.array([x_test[idx]])).tolist()
    # IMAGE_EXAMPLE = (np.array([x_test[0]])).tolist()
    return json.dumps({"signature_name": "serving_default", "instances": IMAGE_EXAMPLE})


def get_flask_request():
    idx = rand.randint(test_range[0], test_range[1])
    IMAGE_EXAMPLE = (np.array([[x_test[idx]]])).tolist()
    # IMAGE_EXAMPLE = (np.array([x_test[0]])).tolist()
    return json.dumps({"image": IMAGE_EXAMPLE})
    # return IMAGE_EXAMPLE


if __name__ == '__main__':
    model = keras.models.load_model('model/2')
    print(model.predict(np.array([x_test[0]])))

