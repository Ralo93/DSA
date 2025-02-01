import functools
import time

array = [1, 2, 3, 4, 5, 10000, 5, 35, 35, 5, 1000000]


def time_function(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs): # *are any kind of arguments, kwargs are any kind of keyword arguments like age=25, city='Berlin'

        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()

        print(f"Execution time: {end_time-start_time:.8f} seconds")

        return result
    return wrapper


@time_function
def get_max(arr):

    result = [x**2 for x in arr]
    return result

result = get_max(array)
print(result)



