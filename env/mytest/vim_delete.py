import requests
from requests.auth import HTTPBasicAuth


# query one by id
#url = 'http://10.20.0.20:80/api/v3/blueprints/myos'
headers = {'Tenant': 'default_tenant', 'Content-Type':'application/json'}
querystring = {'_include': 'id,description'}


url = 'http://10.20.0.20:80/api/v3/vims/test_vim4'
resp = requests.delete(
    url, auth=HTTPBasicAuth('admin', 'admin'), headers=headers,
    #json={"type": "openstack", "inputs": "{'username':'demo','password':'111111','auth_url':'http://10.20.0.10:5000/v3','project_name':'demo','user_domain_id':'default','project_domain_id':'default'}"},    
    #json={'type': 'openstack'}
) 

print(resp.status_code)
print(resp.text)


