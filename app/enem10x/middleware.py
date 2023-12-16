import re
from django.conf import settings
import os


class NgrokMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.META.get("HTTP_HOST", "").split(":")[0]
        os.environ.setdefault("NGROK_URL", f"https://{host}")
        if re.match(r"^[a-zA-Z0-9-]+\.ngrok(-free)?\.app$", host):
            if host not in settings.ALLOWED_HOSTS:
                settings.ALLOWED_HOSTS.append(host)
            if f"https://{host}" not in settings.CSRF_TRUSTED_ORIGINS:
                settings.CSRF_TRUSTED_ORIGINS.append(f"https://{host}")
                settings.COOKIE_SECURE = True
                settings.COOKIE_DOMAIN = host
        return self.get_response(request)
