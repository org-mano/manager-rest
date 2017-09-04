# manager-rest
本仓库项目为manager rest, 覆盖原manager路径"/opt/manager/"下对应文件, 如:
```
cp -rf env/* /opt/manager/env/
chown -R cfyuser:cfyuser /opt/manager
```
### nginx
a. 修改配置文件/etc/nginx/conf.d/rest-location.cloudify，更新API路由
```
location ~ ^/api/v(1|2|2\.1|3)/(resource|vnfs|blueprints|executions|deployments|nodes|events|search|status|provider|node-instances|version|evaluate|deployment-modifications|tokens|plugins|snapshots|maintenance|deployment-updates|tenants|user-groups|users|cluster|file-server-auth|ldap|secrets) {
    proxy_pass         http://cloudify-rest;
    proxy_redirect     off;

    proxy_set_header   Host             $host;
    proxy_set_header   X-Real-IP        $remote_addr;
    proxy_set_header   X-Server-Port    $server_port;
    proxy_set_header   X-Forwarded-For  $proxy_add_x_forwarded_for;
}
```
b. 重启nginx
```
systemctl restart nginx.service
```
### 调试命令
1、PUT "/api/v3/resource/grant"
```
curl -X PUT -H "Content-Type: application/json" -H "tenant: default_tenant" -u admin:admin -d '
{
    "vnfmid": "13232222",
    "nfvoid": "03212234",
    "vimid": "12345678",
    "exvimidlist": ["exvimid1","exvimid2","exvimid3"],
    "tenant": "tenant1",
    "vnfistanceid": "1234",
    "operationright": "0",
    "vmlist":[
        {
            "vmflavor": "SMP",
            "vmnumber": "3"
        },
        {
            "vmflavor": "CMP",
            "vmnumber": "3"
        }
    ]
}' "http://10.128.3.31/api/v3/resource/grant"
```
2、POST "/api/v3/vnfs/lifecyclechangesnotification"
```
curl -X POST -H "Content-Type: application/json" -H "tenant: default_tenant" -u admin:admin -d '
{
    "nfvoid": "1",
    "vnfmid": "876543211",
    "vimid": "6543211",
    "timestamp": "1234567890",
    "vnfinstanceid": "1",
    "eventtype": "0",
    "vmlist": [
        {
            "vmflavor":"SMP",
            "vmnumber":"2",
            "vmidlist": [
                {
                    "vmname":"vm11",
                    "vmid":"11"
                },
                {
                    "vmname":"vm12",
                    "vmid":"12"
                }
            ]
        },
        {
            "vmflavor":"CMP",
            "vmnumber":"2",
            "vmidlist": [
                {
                    "vmname":"vm21",
                    "vmid":"21"
                },
                {
                    "vmname":"vm22",
                    "vmid":"22"
                }
            ]
        }
    ]
}' "http://10.128.3.31/api/v3/vnfs/lifecyclechangesnotification"
```
3、POST "/api/v3/vnfs/eventnotification"
```
curl -X POST -H "Content-Type: application/json" -H "tenant: default_tenant" -u admin:admin -d '
{
    "nfvoid": "1",
    "vnfmid": "876543211",
    "vnfinstanceid": "2",
    "eventtype": "2",
    "eventdescription": "This is an important event",
    "jobid": "1"
}' "http://10.128.3.31/api/v3/vnfs/eventnotification"
```

4、python client test
PUT "/api/v3/blueprints/<$blueprint_id>/update?active=<$active>&vendor=<$vendor>"
```
import requests
from requests.auth import HTTPBasicAuth
headers = {'Tenant': 'default_tenant', 'Content-Type':'application/json'}
url = 'http://10.20.0.20:80/api/v3/blueprints/myos/update?active=true&vendor=zte'
resp = requests.put(url, auth=HTTPBasicAuth('admin', 'admin'), headers=headers)
print(resp.text)
```
or
```
curl -X PUT -H "Content-Type: application/json" -H "tenant: default_tenant" -u admin:admin "http://10.128.3.31/api/v3/blueprints/myos/update?active=true&vendor=zte"
```

5、install new package on CentOS 7
yum install python-devel
/opt/manager/env/bin/pip install demjson
/opt/manager/env/bin/pip install python-glanceclient
/opt/manager/env/bin/pip install python-novaclient
/opt/manager/env/bin/pip install python-keystoneclient
/opt/manager/env/bin/pip install keystoneauth1

