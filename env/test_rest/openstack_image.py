from keystoneauth1.identity import v3
from keystoneauth1 import session
from novaclient import client as novaclient



auth = v3.Password(auth_url="http://10.20.0.10:5000/v3", username="demo", password="111111", project_name="demo",user_domain_id="default", project_domain_id="default")

sess = session.Session(auth=auth)
nova = novaclient.Client('2', session=sess)
data = nova.images.list()
image = data[0]
print(image.name + ' ' + image.id)
