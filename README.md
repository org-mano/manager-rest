# manager-rest
本仓库项目为manager rest, 覆盖原manager路径"/opt/manager/"下对应文件, 如:
```
cp -rf env/* /opt/manager/env/
```
### nginx
a. 修改配置文件/etc/nginx/conf.d/rest-location.cloudify，增加API路由
```
location ~ ^/v1/resource/grant {
    proxy_pass         http://cloudify-rest;
    proxy_redirect     off;

    proxy_set_header   Host             $host;
    proxy_set_header   X-Real-IP        $remote_addr;
    proxy_set_header   X-Server-Port    $server_port;
    proxy_set_header   X-Forwarded-For  $proxy_add_x_forwarded_for;
}
location ~ ^/v1/vnfs/lifecyclechangesnotification {
    proxy_pass         http://cloudify-rest;
    proxy_redirect     off;

    proxy_set_header   Host             $host;
    proxy_set_header   X-Real-IP        $remote_addr;
    proxy_set_header   X-Server-Port    $server_port;
    proxy_set_header   X-Forwarded-For  $proxy_add_x_forwarded_for;
}
location ~ ^/v1/vnfs/eventnotification {
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
### 系统环境
a. log文件
```
touch /var/log/rest_api.log
chmod 777 /var/log/rest_api.log
```
### 调试命令
1、PUT "/v1/resource/grant"
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
}' "http://10.128.3.31/v1/resource/grant"
```
2、POST "/v1/vnfs/lifecyclechangesnotification"
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
}' "http://10.128.3.31/v1/vnfs/lifecyclechangesnotification"
```
3、POST "/v1/vnfs/eventnotification"
```
curl -X POST -H "Content-Type: application/json" -H "tenant: default_tenant" -u admin:admin -d '
{
    "nfvoid": "1",
    "vnfmid": "876543211",
    "vnfinstanceid": "2",
    "eventtype": "2",
    "eventdescription": "This is an important event",
    "jobid": "1"
}' "http://10.128.3.31/v1/vnfs/eventnotification"
```
