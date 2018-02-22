# python-dns-project-yousongzhang

Fake-DNS-Server
===============

Fake DNS Server: Resolve domain names and reponse with a static IP. 

this fake DNS server respone DNS request with a static IP which is set by user.
 



Running
=======

The server can be started with the dns_serer.py script. For example::

python dns_serer.py <static IP> 

(add sudo for binding reserve port 53)

python dns_serer.py 192.168.1.23   (default DNS respone ip is 192.168.1.1)
