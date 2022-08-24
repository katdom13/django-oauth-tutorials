# The Client Credential flow is simpler than the Authorization Code flow.


import base64
import os
from pathlib import Path

import environ

BASE_DIR = Path(__file__).resolve().parent

env = environ.Env()
environ.Env.read_env((os.path.join(BASE_DIR, ".env")))

client_id = os.environ.get("SERVICE_WORKER_CLIENT_ID")
client_secret = os.environ.get("SERVICE_WORKER_CLIENT_SECRET")


# We need to encode client_id and client_secret as
# HTTP base authentication encoded in base64
credential = f"{client_id}:{client_secret}"
credential = base64.b64encode(credential.encode("utf-8"))
print(credential)


"""
To start the Client Credential flow you call /token/ endpoint directly:

curl -X POST \
    -H "Authorization: Basic ${CREDENTIAL}" \
    -H "Cache-Control: no-cache" \
    -H "Content-Type: application/x-www-form-urlencoded" \
    "http://127.0.0.1:8000/o/token/" \
    -d "grant_type=client_credentials"
"""
