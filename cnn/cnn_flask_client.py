from locust import HttpUser, task, between
import cnn_test_data
import os

URL_FLASK_REST = "/cnn"
JSON_HEADER = {"content-type": "application/json"}

DATA_EXAMPLE = cnn_test_data.get_flask_request()
print("start")
print("@@@DATA_EXAMPLE=", DATA_EXAMPLE)


class Demo(HttpUser):
    wait_time = between(0.0, 0.0)

    @task(1)
    def test_post(self):
        json_response = self.client.post(URL_FLASK_REST, data=DATA_EXAMPLE, headers=JSON_HEADER)
        # print("@@@", json.loads(json_response.text))


if __name__ == "__main__":
    # host = 'http://127.0.0.1:8502'
    # cmd = 'locust -f cnn_flask_client.py'
    # os.system(cmd)
    print()
