# coding: utf-8

import socket
import time

host = '127.0.0.1'
host = host.encode('utf-8')
# debug
print(type(host))
print(host)
port = 2999
bufsize = 512

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
stime = "%.6f" % time.time()
sock.sendto(stime, (socket.gethostbyname_ex(host), port))
data, addr = sock.recvform(bufsize)
etime = "%.6f" % time.time()

print("forward : " + str(float(data) - float(stime)))
print("backward : " + str(float(etime) - float(data)))
print("total : " + str(float(etime) - float(stime)))

time.sleep(1)
sock.close()

