from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
# Create your views here.

from . import webhooks

def index(request):
    return HttpResponse("INDEX")

@ensure_csrf_cookie
def webhook(request):
    return webhooks.handle(request)
