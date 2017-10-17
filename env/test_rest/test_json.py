import json

data = {'vim_type': 'openstack', 'auth_url': 'http://10.20.0.10:5000/v3', 'username': 'demo', 'password': '111111'}

jsonStr = json.dumps(data)
print jsonStr


text = json.loads(jsonStr)
print text.get('username')

