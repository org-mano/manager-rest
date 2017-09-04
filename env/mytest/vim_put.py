import requests
from requests.auth import HTTPBasicAuth


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


url = 'http://10.20.0.20:80/api/v3/vims/test_vim4'
resp = requests.put(
    url, auth=HTTPBasicAuth('admin', 'admin'), headers=headers,
    json={"type": "openstack", "inputs": "{'username':'demo','password':'111111','auth_url':'http://10.20.0.10:5000/v3','project_name':'demo','user_domain_id':'default','project_domain_id':'default'}"},    
    #json={'type': 'openstack'}
) 

print(resp.status_code)
print(resp.text)


