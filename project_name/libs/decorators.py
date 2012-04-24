from functools import wraps

sleep_functions = {}
try:
    import eventlet
except ImportError:
    pass
else:
    sleep_functions['eventlet'] = eventlet.greenlet.sleep
try:
    import gevent
except ImportError:
    pass
else:
    sleep_functions['gevent'] = gevent.sleep

def delayed_view(interval=0.5, coroutine=None):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            if coroutine is None:
                return func.delay(*args, **kwargs).get(interval=interval)
            sleep_function = sleep_functions.get(coroutine)
            if not sleep_function:
                raise ValueError("Unsupported coroutine %s" % coroutine)
            result = func.delay(*args, **kwargs)
            while not result.ready():
                sleep_function(interval)
            return result.get()
        return inner
    return wrapper
