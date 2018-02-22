# python-dns-project-yousongzhang

Fake-DNS-Server
===============

Fake DNS Server: Resolve domain names and reponse with a fake IP. 

mode 1: 
DNS server respone all DNS request with a static IP which is set by user(default : 192.168.1.1).
for exmaple:
python dns_server.py  192.168.1.23 

mode 1: 
DNS server respone specail domain DNS request with a static IP and respone other DNS request with normal IP which query for 8.8.8.8.

for example:
python dns_server.py  192.168.1.23 www.163.com


 



Running
=======

The server can be started with the dns_serer.py script. 

Mode 1:
For example::

python dns_serer.py <static IP> 

(add sudo for binding reserve port 53)

python dns_serer.py 192.168.1.23   (default DNS respone ip is 192.168.1.1)

Mode 2:
for example :  
sudo python dns_server.py  192.168.1.23 www.163.com  
pyminifakeDNS:: dom.query. 60 IN A 192.168.1.23  

Respuesta: ib.adnxs.com. -> 172.217.6.46  
Respuesta: mail.google.com. -> 216.58.194.174  
Respuesta: www.googleapis.com. -> 216.58.194.174  
Respuesta: www.163.com. -> 192.168.1.23     ****  only this domain fake ****  
Respuesta: lax1-ib.adnxs.com. -> 216.58.194.174  




