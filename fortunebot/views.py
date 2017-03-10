from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt 
# Create your views here.

from . import webhooks

def index(request):
    return HttpResponse("INDEX")

@csrf_exempt 
def webhook(request):
    return webhooks.handle(request)
