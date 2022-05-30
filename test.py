from email.mime import base
import jwt
from datetime import datetime,timedelta
secret_key = "secretkeyflask2k22"
import base64

encoded_jwt = jwt.encode({"user_id": "23"}, secret_key, algorithm="HS256")
aaa = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiNTM0In0.xAHwgcUvLE1z60UzgNLDyTgtC4V-4yaHei0mf-_B-7k"
decoded_jwt = jwt.decode(aaa,secret_key,algorithms=['HS256'])
print(decoded_jwt)

import bcrypt

hash_pasw = bcrypt.hashpw("asd123".encode("utf-8"),bcrypt.gensalt())
"b'$2b$12$eQvsx75jxb3pu4Duy1cUQOfRBgmRY5jd/fvlfmZNd6Zbh1gkkOkFu'"
print(hash_pasw.decode("utf-8"))
print(bcrypt.checkpw("asd123".encode("utf-8"),hashed_password = hash_pasw))
