# Decorators

## Simple Wrapper Function
Create a simple example for showcasing how they work

```python
def time_function(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs): # *are any kind of arguments, kwargs are any kind of keyword arguments like age=25, city='Berlin'

        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()

        print(f"Execution time: {end_time-start_time:.8f} seconds")

        return result
    return wrapper
```

Useful python decorators for ML and data science. Lets dive in!
  
So first we have a timing wrapper function for monitoring function performance and trying to find any bottlenecks. Really handy I think.

```python
import functools
import time
import logging
import os
from typing import Any, Callable
import numpy as np

def timing_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        
        # Configure logging if not already configured
        logging.basicConfig(level=logging.INFO, format='%(message)s')
        
        logging.info(f"Function: {func.__name__}")
        print(f"Execution time: {end_time - start_time:.4f} seconds")
        
        return result
    return wrapper
    
@timing_decorator 
def compute_square(n): 
    return [x2 for x in range(n)] 
    
Use: compute_square(100000) # 
```


Next Claude provided me with a great retry mechanism with an exponential backoff factor. 
Great for any network transmission tasks like API calls, up or downloads or message queue interactions or microservice communications.


```python
def retry_with_backoff(max_retries=3, backoff_factor=2, exceptions=(Exception,)):
    """Retry decorator with exponential backoff for resilient function execution"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            x = 0
            while x < max_retries:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    time.sleep(backoff_factor ** x)
                    x += 1
            raise Exception(f"Function {func.__name__} failed after {max_retries} attempts")
        return wrapper
    return decorator
```

Logging predictions is always a good way to sanity check your model or to find anomalies which you should look into! Standard practice while developing any model.

```python
def log_model_predictions(log_dir='./model_logs'):
    """Decorator to log model prediction details"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            os.makedirs(log_dir, exist_ok=True)
            logging.basicConfig(filename=os.path.join(log_dir, 'predictions.log'), level=logging.INFO)
            
            start_time = time.time()
            result = func(*args, **kwargs)
            
            logging.info(f"Function: {func.__name__}")
            logging.info(f"Execution Time: {time.time() - start_time:.4f} seconds")
            logging.info(f"Input Shape: {[arg.shape if hasattr(arg, 'shape') else type(arg) for arg in args]}")
            logging.info(f"Output Shape: {result.shape if hasattr(result, 'shape') else type(result)}")
            
            return result
        return wrapper
    return decorator
```

This decorator function will help you validate input shapes, i think this can come very handy especially in deep learning where you need to think though your tensor dimensions anyway.
In particular, this can save you from some silent failing processes where tensor operations do work but not in an expected way.

```python
def validate_input_shape(expected_dims=None):
    """Validate input tensor dimensions before processing"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if expected_dims:
                input_tensor = args[0]  # Assumes first argument is the input tensor
                if len(input_tensor.shape) != expected_dims:
                    raise ValueError(f"Expected {expected_dims} dimensions, got {len(input_tensor.shape)}")
            return func(*args, **kwargs)
        return wrapper
    return decorator
```

Great function to check your memory profile for a single function call. Should not be used together with the timing function, as the execution time shoots up quite a lot.

```python
def memory_profile(func: Callable[..., Any]) -> Callable[..., Any]:
    """Memory profiling decorator using memory_profiler"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        from memory_profiler import memory_usage
        mem_usage = memory_usage((func, args, kwargs), max_iterations=1)
        print(f"Memory Usage for {func.__name__}: {max(mem_usage)} MiB")
        return func(*args, **kwargs)
    return wrapper
```


```python
# Example Usage
@timing_decorator
@retry_with_backoff(max_retries=3)
@log_model_predictions(log_dir='./ml_logs')
@validate_input_shape(expected_dims=2)
@memory_profile
def process_data(data):
    """Sample function simulating data processing"""
    return np.mean(data, axis=0)


# Demonstrative usage
def main():
    sample_data = np.random.rand(100, 10)
    processed_result = process_data(sample_data)
    
    #complex_result = process_data(100000)

if __name__ == "__main__":
    
    main()
