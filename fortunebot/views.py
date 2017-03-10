from django.http import HttpResponse
from django.views.decorators.csrf import requires_csrf_token
# Create your views here.

from . import webhooks

def index(request):
    return HttpResponse("INDEX")

@requires_csrf_token
def webhook(request):
    return webhooks.handle(request)
