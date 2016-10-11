import requests
import json
r = requests.get('http://codeforces.com/api/user.rating?handle=archit910')
jobject = json.dumps(r.text)
print jobject