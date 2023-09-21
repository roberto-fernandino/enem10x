from django.http import HttpResponseForbidden
from time import time 
from functools import wraps


def user_has_tag(tag):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if getattr(request.user, tag, None):
                return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator


def time_check(func):
    def wrapper(*args, **kwargs):
        print(f"Running {func.__name__}")
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time() - t1
        print(f"Took: {t2:.2f}s")
        return result
    return wrapper
    