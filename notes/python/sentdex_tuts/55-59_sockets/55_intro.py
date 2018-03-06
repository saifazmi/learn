# Socket programming intro

'''
' Socket programming in python can be challenging as there are plenty
' of documentations on how to do socket programming in python, but not much
' when it comes to *learning* socket programming using python.
'
' Another issues is that most of the sample code for socket programming is in
' python2 and this is an issue because of the difference between strings and
' byte strings
'''

'''
' Sockets are used in networking. The idea of a socket is to aid in
' the communication between two entities. When you view a website, you are
' opening a port and connecting to that website via sockets. In case of a
' web server this is port number 80 (or 8080)
'
' A natural point of confusion here is the difference between sockets and ports
' You can think of a port much like a shipping port, where boats dock at
' the port and unload goods. Then, you can think of the ship itself as
' the socket. The ocean is the internet. Much like shipping ports,
' a socket (our ship in this metaphor), is bound by a specific port.
' Docking at a different port is not allowed, for ships or sockets!
'''

'''
' General port numbers and services:
' 8080 : http
' 20/21: ftp
' 22   : ssh
'
' Lower number ports are very specific and used by specific apps, but higher
' number ports are more general purpose and used for various purposes,
' inlcuding testing and running web services, etc.
'''

import socket


# create a socket
s = socket.socket(socket.AF_INET, # connection type IPv4, AF_INET6 for IPv6
                  socket.SOCK_STREAM) # TCP connection, can be UDP
print(s) # socket descriptor
                  
server = "saifazmi.com" # can also be an IP addr
port = 80

# fetch server IP
server_ip = socket.gethostbyname(server)
print(server_ip)

# Create a HTTP GET request
request = "GET / HTTP/1.1\nHOST: "+server+"\n\n"

# connect, takes only one argument
s.connect((server, port))

# send request
'''
' here is the main diff between py3 vs py2
' we want to send strings, but we are actually using byte strings, so encode
'''
s.send(request.encode())

# Get reults, takes buffer size
result = s.recv(1024)
# print(result) # the received request data starts with b'' i.e. byte string

# Buffering data
while (len(result) > 0): # while there is still something to come from result
    print(result)
    result = s.recv(1024)
