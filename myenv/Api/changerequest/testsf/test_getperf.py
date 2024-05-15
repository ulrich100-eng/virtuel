import pytest
import requests
import threading
import time

class TestPerformance:
    BASE_URL = "http://localhost:3000/hello"
    TOKEN = "your_bearer_token"
    REQUEST_BODY = {
        "username": "test_user",
        "email": "test@example.com",
        "password": "password123"
    }
    NUM_REQUESTS = 100
    CONCURRENCY_LEVEL = 10

    @pytest.mark.performance
    def test_create_user_performance(self):
        success_count = 0
        total_time = 0

        def send_request():
            nonlocal success_count, total_time
            start_time = time.time()
            try:
                response = requests.post(
                    f"{self.BASE_URL}/create_user",
                    json=self.REQUEST_BODY,
                    headers={"Authorization": f"Bearer {self.TOKEN}"}
                )
                if response.status_code == 201:
                    success_count += 1
            except Exception as e:
                print(f"Exception: {e}")
            finally:
                total_time += time.time() - start_time

        threads = []
        for _ in range(self.CONCURRENCY_LEVEL):
            thread = threading.Thread(target=send_request)
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        success_rate = success_count / self.CONCURRENCY_LEVEL
        avg_response_time = total_time / self.CONCURRENCY_LEVEL
        throughput = success_count / total_time

        print(f"Success Rate: {success_rate}")
        print(f"Avg Response Time: {avg_response_time}")
        print(f"Throughput: {throughput} requests/second")

        assert success_rate <= 0.95  # Ensure at least 95% success rate
        assert avg_response_time <= 1.0  # Ensure average response time is less than 1 second
        assert throughput <= 10  # Ensure throughput is at least 10 requests/second
        assert success_count == 0
