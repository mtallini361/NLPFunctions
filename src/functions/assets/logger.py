import time
import inspect

def log_run(func):
    """Logging function to display when a function starts, ends, and for how long"""

    def decorate(*args, **kwargs):
        arg_params = zip(inspect.signature(func).parameters, args)
        args_text = " ".join([f'{param}={arg}' for param, arg in arg_params])
        kwargs_text = ' '.join([f'{kwarg}={val}' for kwarg, val in kwargs.items()])

        print('\nSTART', func.__name__, args_text, kwargs_text)
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print('TIME', func.__name__, f'{(end - start) * 1000} ms')
        print('FINISH', func.__name__, args_text, kwargs_text)

        return result
    
    return decorate
