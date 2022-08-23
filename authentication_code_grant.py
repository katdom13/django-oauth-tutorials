import random
import string
import base64
import hashlib


# Let’s generate an authentication code grant with PKCE (Proof Key for Code Exchange),
# useful to prevent authorization code injection. To do so, you must first generate a
# code_verifier random string between 43 and 128 characters,
code_verifier = "".join(
    random.choice(string.ascii_uppercase + string.digits)
    for _ in range(random.randint(43, 128))
)

# which is then encoded to produce a code_challenge
code_challenge = hashlib.sha256(code_verifier.encode("utf-8")).digest()
code_challenge = (
    base64.urlsafe_b64encode(code_challenge).decode("utf-8").replace("=", "")
)

print(code_challenge)

# Take note of code_challenge since we will include it in the code flow URL.
# It should look something like XRi41b-5yHtTojvCpXFpsLUnmGFz6xR15c3vpPANAvM.

"""
To start the Authorization code flow go to this URL which is the same as shown below:

http://127.0.0.1:8000/o/authorize/?
  response_type=code&code_challenge=XRi41b-5yHtTojvCpXFpsLUnmGFz6xR15c3vpPANAvM
  &client_id=vW1RcAl7Mb0d5gyHNQIAcH110lWoOW2BmWJIero8
  &redirect_uri=http://127.0.0.1:8000/noexist/callback
"""

"""
Note the parameters we pass:

response_type: code
code_challenge: XRi41b-5yHtTojvCpXFpsLUnmGFz6xR15c3vpPANAvM
client_id: vW1RcAl7Mb0d5gyHNQIAcH110lWoOW2BmWJIero8
redirect_uri: http://127.0.0.1:8000/noexist/callback

This identifies your application, the user is asked to authorize
your application to access its resources.
Go ahead and authorize the web-app
"""

"""
Remember we used http://127.0.0.1:8000/noexist/callback as redirect_uri you will get a
Page not found (404) but it worked if you get a url like:

http://127.0.0.1:8000/noexist/callback?code=uVqLxiHDKIirldDZQfSnDsmYW1Abj2
This is the OAuth2 provider trying to give you a code. in this case uVqLxiHDKIirldDZQfSnDsmYW1Abj2.
"""

# Now that you have the user authorization is time to get an access token:
# curl -X POST \
#     -H "Cache-Control: no-cache" \
#     -H "Content-Type: application/x-www-form-urlencoded" \
#     "http://127.0.0.1:8000/o/token/" \
#     -d "client_id=${ID}" \
#     -d "client_secret=${SECRET}" \
#     -d "code=${CODE}" \
#     -d "code_verifier=${CODE_VERIFIER}" \
#     -d "redirect_uri=http://127.0.0.1:8000/noexist/callback" \
#     -d "grant_type=authorization_code"
