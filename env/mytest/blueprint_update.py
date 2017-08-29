import requests
from requests.auth import HTTPBasicAuth

#url = 'http://192.168.104.30/v1/resource/grant'
# query grant
url = 'http://10.20.0.20/v1/resource/grant'

# query all blueprint
url = 'http://10.20.0.20:80/api/v3/blueprints?id=myos'
# query one by id
#url = 'http://10.20.0.20:80/api/v3/blueprints/myos'
headers = {'Tenant': 'default_tenant', 'Content-Type':'application/json'}
querystring = {'_include': 'id,description'}

#resp = requests.get(
#    url, auth=HTTPBasicAuth('admin', 'admin'), headers=headers,
#    params=querystring,
#)


url = 'http://10.20.0.20:80/api/v3/blueprints/proxy/update?active=true&vendor=h3c'
resp = requests.put(
    url, auth=HTTPBasicAuth('admin', 'admin'), headers=headers,
    #data={'active':'true'},    
) 

print(resp.status_code)
print(resp.text)


