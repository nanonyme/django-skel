from functools import wraps

sleep_functions = {}
try:
    import eventlet
except ImportError:
    pass
else:
    sleep_functions['eventlet'] = eventlet.sleep
try:
    import gevent
except ImportError:
    pass
else:
    sleep_functions['gevent'] = gevent.sleep

class DelayedView(object):
    def __init__(self, interval=0.5, coroutine=None):
        self.interval = interval
        self.coroutine = coroutine
        
    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if self.coroutine is None:
                return func.delay(*args, **kwargs).get(interval=self.interval)
            sleep_function = sleep_functions.get(self.coroutine)
            if not sleep_function:
                raise ValueError("Unsupported coroutine %s" % self.coroutine)
            result = func.delay(*args, **kwargs)
            while not result.ready():
                sleep_function(self.interval)
            return result.get()
        return wrapper

def delayed_view(*args, **kwargs):
    return DelayedView(*args, **kwargs)


