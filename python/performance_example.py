
from functools import wraps
import time

def timeit_seconds(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} [s]')
        return result
    return timeit_wrapper

def timeit_milliseconds(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter_ns()
        result = func(*args, **kwargs)
        end_time = time.perf_counter_ns()
        total_time = (end_time - start_time) / 1000000
        print(f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} [ms]')
        return result
    return timeit_wrapper

def timeit_microseconds(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter_ns()
        result = func(*args, **kwargs)
        end_time = time.perf_counter_ns()
        total_time = (end_time - start_time) / 1000
        print(f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} [us]')
        return result
    return timeit_wrapper

def timeit_nanoseconds(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter_ns()
        result = func(*args, **kwargs)
        end_time = time.perf_counter_ns()
        total_time = end_time - start_time
        print(f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} [ns]')
        return result
    return timeit_wrapper

@timeit_seconds
def calculate_sum(num):
    """
    Simple function that accumulates the numbers from 0 to the square of num
    """
    total_sum = sum((x for x in range(0, num**2)))
    return total_sum

if __name__ == '__main__':
    calculate_sum(10)
    calculate_sum(100)
    calculate_sum(1000)
    calculate_sum(5000)
    calculate_sum(10000)
