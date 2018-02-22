#!/usr/bin/env python
#title           :dns_server.py
#description     :DNS server which responses specal/all DNS query with a fake IP
#author          :yousong zhang
#date            :20180220
#version         :1.0
#usage           :python dns_server.py <IP> <domain>  (add sudo for binding port 53)
#python_version  :2.7.12
#==============================================================================


import socket,sys,dns.resolver

class DNSQuery:
  def __init__(self, data):
    self.data=data
    self.dominio=''

    tipo = (ord(data[2]) >> 3) & 15   # Opcode bits
    if tipo == 0:                     # Standard query
      ini=12
      lon=ord(data[ini])
      while lon != 0:
        self.dominio+=data[ini+1:ini+lon+1]+'.'
        ini+=lon+1
        lon=ord(data[ini])

  def respuesta(self, ip):
    packet=''
    if self.dominio:
      packet+=self.data[:2] + "\x81\x80"
      packet+=self.data[4:6] + self.data[4:6] + '\x00\x00\x00\x00'   # Questions and Answers Counts
      packet+=self.data[12:]                                         # Original Domain Name Question
      packet+='\xc0\x0c'                                             # Pointer to domain name
      packet+='\x00\x01\x00\x01\x00\x00\x00\x3c\x00\x04'             # Response type, ttl and resource data length -> 4 bytes
      packet+=str.join('',map(lambda x: chr(int(x)), ip.split('.'))) # 4bytes of IP
    return packet

if __name__ == '__main__':
  ip='192.168.1.1'
  if sys.argv[1] is not None:   
	ip=sys.argv[1]
  print 'pyminifakeDNS:: dom.query. 60 IN A %s' % ip
  
  udps = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  udps.bind(('',53))
  
  try:
    while 1:
      data, addr = udps.recvfrom(1024)
      p=DNSQuery(data)
      tmp_ip = ip
      if len(sys.argv) == 3:     # special domain
	if sys.argv[2] in p.dominio :
	      #	print "one this domain (" + sys.argv[2] + ") use fake IP"
		tmp_ip = ip
	else:
		#print "return normal IP"
                my_resolver = dns.resolver.Resolver()
		# 8.8.8.8 is Google's public DNS server
		my_resolver.nameservers = ['8.8.8.8']

		tmp_ip = my_resolver.query('google.com')[0].address
		
		#print "only domain (" +sys.argv[2]+ ") return fake IP"
      else:     
		#print "all domain use fake IP"
		tmp_ip = ip
      udps.sendto(p.respuesta(tmp_ip), addr)
      print 'Respuesta: %s -> %s' % (p.dominio, tmp_ip)
  except KeyboardInterrupt:
    print 'Finalizando'
    udps.close()
