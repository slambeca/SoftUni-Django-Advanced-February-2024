# get_response is a func
import time

from django.utils.deprecation import MiddlewareMixin


class MeasureExecutionTimeMiddleware(MiddlewareMixin):
    # Before
    def process_request(self, request):
        self.start_time = time.time()

    # After
    def process_response(self, request, response):
        self.end_time = time.time()
        self.duration = self.start_time - self.end_time
        print(f"{self.duration} seconds")
        return response


def measure_time(get_response):
    def middleware(request, *args, **kwargs):
        # Before the request
        start_time = time.time()

        result = get_response(request, *args, **kwargs)

        # After the request
        end_time = time.time()
        print(f"Executed in {end_time - start_time} seconds")

        return result

    return middleware