# Binding and Listening with Sockets

import socket
import sys

host = ""
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((host, port))
except socket.error as e:
    print(str(e))

'''
' This starts listening on the port specified earlier and also defines the
' size of the listening queue, i.e. number of connection accepted at a time
'''

s.listen(5)

conn, addr = s.accept()
print(conn)
print(addr)

print("connected to: " + addr[0] + ":" + str(addr[1]))
