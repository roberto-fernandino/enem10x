from django.http import HttpResponseForbidden

from functools import wraps


def user_has_tag(tag):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if getattr(request.user, tag, None):
                return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator