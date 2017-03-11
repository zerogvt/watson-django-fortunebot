import requests
import sys
from . import config

from . import auth

def createMessage(spaceId, text, title, color = config.MESSAGE_COLOR):
    message = {
        "type": "appMessage",
        "version": 1.0,
        "annotations": [
                {
                "type": "generic",
                "text": text,
                "color": color,
                "title": title,
                "version": "1.0"
                }
                        ]
               }

    return message

# Leverage the default title and color values to send a simple message to Watson Work Services
def sendSimpleMessage(spaceId, text):
    print("In fortunebot:message:sendSimpleMessage", file=sys.stderr)
    sys.stderr.flush()
    title = config.MESSAGE_TITLE
    msg = createMessage(spaceId, text, title)
    sendMessage(spaceId, msg)

# Call Send Message API to send message to Watson Work Services
def sendMessage(spaceId, message):
    print("In fortunebot:message:sendMessage", file=sys.stderr)
    sys.stderr.flush()
    api = '%s/v1/spaces/%s/messages' % (config.WATSON_WORK_SERVICES, spaceId)
    accessToken = auth.authenticateApp()
    headers = {'Authorization': 'Bearer %s' % accessToken}
    res = requests.post(api, json=message, headers=headers)
    return res


def echo(request):
    body = request.json
