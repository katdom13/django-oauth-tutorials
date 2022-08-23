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

print(code_verifier)
print(code_challenge)


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
