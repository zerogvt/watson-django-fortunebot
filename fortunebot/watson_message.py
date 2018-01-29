import requests
import sys
from . import config
from . import auth


# Leverage the default title and color values to send a simple message to Watson Work Services
def sendSimpleMessage(spaceId, text):
    if config.MYDEBUG:
        print("In fortunebot:message:sendSimpleMessage", file=sys.stderr)
        sys.stderr.flush()
    title = config.MESSAGE_TITLE
    msg = _createMessage(spaceId, text, title)
    return _sendMessage(spaceId, msg)


def _createMessage(spaceId, text, title, color = config.MESSAGE_COLOR):
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


# Call Send Message API to send message to Watson Work Services
def _sendMessage(spaceId, message):
    if config.MYDEBUG:
        print("In fortunebot:message:sendMessage", file=sys.stderr)
        sys.stderr.flush()
    api = '%s/v1/spaces/%s/messages' % (config.WATSON_WORK_SERVICES, spaceId)
    accessToken = auth.authenticateApp()
    headers = {'Authorization': 'Bearer %s' % accessToken,
               'Content-Type' : 'application/json;charset=UTF-8'}
    res = requests.post(api, json=message, headers=headers)
    return res

# Call Send Message API to send message to Watson Work Services
def ackMessage(spaceId):
    if config.MYDEBUG:
        print("Msg ack", file=sys.stderr)
        sys.stderr.flush()
    api = '%s/v1/spaces/%s/messages' % (config.WATSON_WORK_SERVICES, spaceId)
    accessToken = auth.authenticateApp()
    headers = {'Authorization': 'Bearer %s' % accessToken,
               'status': '%d' % requests.codes.ok}
    res = requests.post(api, json="", headers=headers)
    return res
