import numpy as np
import tensorflow as tf
from tensorflow_serving.apis import predict_pb2
import json
import data_prerprocessing

x_test = data_prerprocessing.get_data(64, 64)
# test_range = [0, 9]


def get_grpc_request():
    # idx = rand.randint(test_range[0], test_range[1])
    # IMAGE_EXAMPLE = (np.array([x_test[idx]])).tolist()
    IMAGE_EXAMPLE = (np.array(x_test, dtype=np.float_)).tolist()
    grpc_request = predict_pb2.PredictRequest()
    grpc_request.model_spec.name = 'tf_cnn'

    grpc_request.model_spec.signature_name = 'serving_default'
    grpc_request.inputs['conv2d_input'].CopyFrom(tf.make_tensor_proto(IMAGE_EXAMPLE, shape=[1, 64, 64, 1]))
    return grpc_request


def get_tfs_rest_request():
    # idx = rand.randint(test_range[0], test_range[1])
    # IMAGE_EXAMPLE = (np.array([x_test[idx]])).tolist()
    IMAGE_EXAMPLE = (np.array(x_test)).tolist()
    return json.dumps({"signature_name": "serving_default", "instances": IMAGE_EXAMPLE})


def get_flask_request():
    # idx = rand.randint(test_range[0], test_range[1])
    # IMAGE_EXAMPLE = (np.array([[x_test[idx]]])).tolist()
    IMAGE_EXAMPLE = (np.array([x_test])).tolist()
    # print(IMAGE_EXAMPLE)
    # x = IMAGE_EXAMPLE
    # while len(x) > 0:
    #     print(len(x))
    #     x = x[0]
    return json.dumps({"image": IMAGE_EXAMPLE})
    # return IMAGE_EXAMPLE


if __name__ == '__main__':
    get_flask_request()
    # model = keras.models.load_model('../model/2')
    # print(model.predict(np.array([x_test[0]])))

