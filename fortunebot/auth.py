from . import config
import requests
import base64
import json
import sys


# Authenticate with the application id and application secret
def authenticateApp():
    # Build API for requesting access token of application
    auth_api = '%s/oauth/token' % config.WATSON_WORK_SERVICES

    # Pull in app id and app secret
    credentials = b'%s:%s' % (config.APP_ID, config.APP_SECRET)
    # credentials = credentials.encode(encoding='ASCII')

    # Construct "client_credentials" request for token
    payload = {"grant_type": "client_credentials"}
    headers = {"Authorization": "Basic %s" % base64.b64encode(credentials)}

    # POST to /oauth/token to obtain access token
    authResponse = requests.post(auth_api, data=payload, headers=headers)
    print("===================")
    print(authResponse.text)
    print(authResponse.GET)
    print(authResponse.content_type)
    print(authResponse.content_params)
    print(json.loads(authResponse.body.decode("utf-8")))
    print("===================")

    sys.stderr.flush()
    body = json.loads(authResponse.body.decode("utf-8"))
    return body['access_token']
