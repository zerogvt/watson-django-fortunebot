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
    creds_str = "%s:%s" % (config.APP_ID, config.APP_SECRET)
    credentials = base64.b64encode(creds_str.encode("ASCII"))
    print(credentials)

    # Construct "client_credentials" request for token
    payload = {"grant_type": "client_credentials"}
    headers = {"Authorization": "Basic %s" % credentials.decode('ASCII')}
    
    # POST to /oauth/token to obtain access token
    authResponse = requests.post(auth_api, data=payload, headers=headers)
    print("===================>>")
    print("#%s#" % payload)
    print(headers)
    body = json.loads(authResponse.text)
    print("Reply: %s" % body)
    print("===================<<")
    sys.stderr.flush()
    return body['access_token']
