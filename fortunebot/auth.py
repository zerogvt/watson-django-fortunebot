from . import config
import requests
import base64
import json
import sys
import datetime


access_token = None
renew_at = None

# Authenticate with the application id and application secret
def authenticateApp():
    global access_token
    global renew_at
    if access_token is not None  and renew_at is not None:
        now = datetime.datetime.now()
        if now < renew_at:
            return access_token
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
    body = json.loads(authResponse.text)
    if config.MYDEBUG:
        print("===================>>")
        print("Sent auth payload: #%s#" % payload)
        print(" with headers: %s" % headers)
        print("Got reply text: %s" % body)
        print("===================<<")
        sys.stderr.flush()

    if body['access_token']:
        access_token = body['access_token']
        secs_to_live = body['expires_in']
        renew_at = datetime.datetime.now() +\
                   datetime.timedelta(seconds=secs_to_live)
    return access_token

