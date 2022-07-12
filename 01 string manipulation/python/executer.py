import time

class Executer:
    def __init__(self, tests, function) -> None:
        self.tests = tests
        self.function = function

    def run(self):
        for test in self.tests:
            start = time.process_time_ns()
            result = self.function(test)
            end = time.process_time_ns()
            print(f"Input: {test}\nOutput: {result}\nTime: {(end - start)}ns\n")
        