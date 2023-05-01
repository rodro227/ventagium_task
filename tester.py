import time
import memory_profiler

class CodeTester:
    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.start_mem = None
        self.end_mem = None

    def start(self):
        self.start_time = time.perf_counter()
        self.start_mem = memory_profiler.memory_usage()[0]

    def end(self):
        self.end_time = time.perf_counter()
        self.end_mem = memory_profiler.memory_usage()[0]

        print(f"Time elapsed: {self.end_time - self.start_time:.6f} seconds")
        print(f"Memory used: {self.end_mem - self.start_mem:.6f} MiB")
