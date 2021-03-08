import time
import grpc
from locust import User, between
from locust import task, events

from tensorflow_serving.apis import prediction_service_pb2_grpc
import cnn_test_data


class GrpcClient(object):
    """override self.client"""
    def __init__(self):
        self.host_port = 'localhost:8500'
        self.channel = grpc.insecure_channel(self.host_port)
        self.stub = prediction_service_pb2_grpc.PredictionServiceStub(self.channel)

    def connect(self, grpc_request):
        start_time = time.time()
        result = None
        try:
            result = self.stub.Predict(grpc_request, 0.5)
            # print("@@@tf_grpc ", result)
            total_time = int((time.time() - start_time) * 1000)
            # if res.errCode != 0:
            #     raise Exception("errCode=", res.errCode)
            events.request_success.fire(
                request_type='grpc',
                name='grpc-success',
                response_time=total_time,
                response_length=0
            )
        except Exception as e:
            total_time = int((time.time() - start_time) * 1000)
            events.request_failure.fire(
                request_type='grpc',
                name='grpc-fail',
                response_time=total_time,
                exception=e
            )
        return result


class GrpcUser(User):

    # abstract = True
    def __init__(self, *args, **kwargs):
        super(GrpcUser, self).__init__(*args, **kwargs)
        self.client = GrpcClient()

    # host_port = 'localhost:8500'
    wait_time = between(0.5, 0.5)


    @task(1)
    def predict(self):
        grpc_request = cnn_test_data.get_grpc_request()
        # print(grpc_request)
        self.client.connect(grpc_request)


if __name__ == "__main__":
    # host = 'http://localhost:8500'
    # cmd = 'locust -f tfs_grpc_client.py'
    # os.system(cmd)
    # print(cnn_test_data.get_grpc_request())
    print()