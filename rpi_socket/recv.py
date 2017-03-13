#!/usr/bin/env python3
import socket
import os

# 监听2048端口的udp socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('localhost', 2048))
print('Waiting for command')
while True:
    data, address = s.recvfrom(2048)
    cmd = data.decode('utf-8')
    print("Receive command: %s " % cmd)
    # 如果命令多可以采用字典。现简化用两个if
    if cmd == 'touch':
        os.system('touch /tmp/hello')
    if cmd == 'rm':
        os.system('rm /tmp/hello')
s.close()