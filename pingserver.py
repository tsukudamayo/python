# coding: utf-8

import socket
import time

host = '127.0.0.1'
port = 2999
bufsize = 512

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((host, port))
while(True):
    data, addr = sock.recvfrom(bufsize)
    sock.sendto("%.6f" % time.time(), addr)
