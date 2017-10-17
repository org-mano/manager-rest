import requests
import json
from requests.auth import HTTPBasicAuth
import demjson

# query all blueprint
url = 'http://10.20.0.20:80/api/v3/vnf_imgs'
# query one by id
#url = 'http://10.20.0.20:80/api/v3/blueprints/myos'
headers = {'Tenant': 'default_tenant', 'Content-Type':'application/json'}
querystring = {'_include': 'id,param,status,type'}

resp = requests.get(
    url, auth=HTTPBasicAuth('admin', 'admin'), headers=headers,
    #params=querystring,
)


#url = 'http://10.20.0.20:80/api/v3/vims/test_vim'
#resp = requests.put(
#    url, auth=HTTPBasicAuth('admin', 'admin'), headers=headers,
#    data={"type": "openstack", "param": "{'p1':'v1','p2':'v2'}"},    
#) 

print(resp.status_code)
print(resp.text)

jsonObj = json.loads(resp.text)
paramStr = jsonObj.get('param')
print paramStr

#paramObj = json.loads(paramStr)
#print paramObj.get('auth_url')

#obj = demjson.decode(paramStr)
#print obj.get('auth_url')
