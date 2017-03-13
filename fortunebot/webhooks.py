import hmac
import json
import hashlib
import sys
from django.http import HttpResponse
from . import config
from . import message
from . import fortunebot

def handle(request):
    print("In fortunebot:webhooks:handle", file=sys.stderr)
    sys.stderr.flush()
    if not request:
        raise Exception('Invalid Request')

    body = json.loads(request.body.decode("utf-8"))

    # Call verification function if request type is verification, else process message
    if str(body['type']) == 'verification':
        print("[INFO] Verification challenge")
        return _verification(body)
    elif str(body['type']) == 'message-created':
        print("[INFO] Message")
        return _parseMessage(body)


def _verification(inp):
    print("In fortunebot:webhooks:verification", file=sys.stderr)
    responseBody = {'response': str(inp['challenge'])}
    sys.stderr.flush()
    response = HttpResponse(content = json.dumps(responseBody),
                      content_type='application/json', status=200)
    tmp = hmac.new(config.WEBHOOK_SECRET.encode('UTF-8'),
                   msg=str(json.dumps(responseBody)).encode('UTF-8'),
                   digestmod=hashlib.sha256)
    newhdr = tmp.hexdigest()
    response['X-Outbound-Token'] = newhdr
    return response


# Process message and send respond back to Watson Work Services for test 
def _parseMessage(body):
    print(str(body), file=sys.stderr)
    spaceId = body['spaceId']
    if config.WEBHOOK_TRIGGER in body['content']:
        arg = body['content'].replace(config.WEBHOOK_TRIGGER,"").strip()
        message.sendSimpleMessage(spaceId, fortunebot.getFortuneWIndex(arg))
    return HttpResponse(status=200)
