import hmac
import json
import hashlib
from django.http import HttpResponse
from . import config
from . import message

def handle(request):
    return HttpResponse("OOINDEX")
    if not request:
        raise Exception('Invalid Request')

    body = request.json

    # Call verification function if request type is verification, else process message
    if str(body['type']) == 'verification':
        print("[INFO] Verification challenge")
        return verification(body)
    elif str(body['type']) == 'message-created':
        print("[INFO] Message")
        return parseMessage(body)


def verification(inp):
    responseBody = {'response': str(inp['challenge'])}
    response = HttpResponse(response=json.dumps(responseBody),
                      content_type='application/json', status=200)
    newhdr = hmac.new(config.WEBHOOK_SECRET, msg=str(json.dumps(responseBody)), 
                      digestmod=hashlib.sha256).hexdigest()
    response.headers['X-Outbound-Token'] = newhdr
    print(response)
    return response

# Process message and send respond back to Watson Work Services for test 
def parseMessage(body):
    spaceId = body['spaceId']
    splitContent = body['content'].split(' ')
    if config.WEBHOOK_TRIGGER in splitContent:
        message.sendSimpleMessage(spaceId, ' '.join(splitContent[1:]))
    return HttpResponse(status=200)
