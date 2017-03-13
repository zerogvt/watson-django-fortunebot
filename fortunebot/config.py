import os

# Server port
PORT = os.getenv('PORT', 8080)

# Watson Work Services API
WATSON_WORK_SERVICES = 'https://api.watsonwork.ibm.com'

# Applicaion ID
APP_ID = os.getenv('APP_ID')

# Application secret
APP_SECRET = os.getenv('APP_SECRET')

# Webhook secret
WEBHOOK_SECRET = os.getenv('WEBHOOK_SECRET')

# Webhook trigger word
WEBHOOK_TRIGGER = '@oscar'

# Send message color
MESSAGE_COLOR = '#6699ff'

# Send message title
MESSAGE_TITLE = 'Echo test'

MYDEBUG = True
