# A simple port scanner

'''
' A port scanner simply scans the ports and determines if they are open
' and if/what is running on it.
'
' The idea of a port scanner is to run through a list of ports, testing to
' see if they are open. We can do this because the steps for using sockets
' for sending data is first you make the connection, then you try to off-load
' the request. Re-visiting our ship metaphor, the dock has no idea
' what contents are in the ship. Thus, if the port is open, the ship can at
' least dock before anyone knows whether or not what the ship is carrying is
' supposed to be there.
'
' With our port scanner, we just attempt to dock at various ports,
' and do nothing else. If we're permitted to dock / connect to open ports,
' then we know at least the port is open. This is a form of "reconnaissance"
' for hackers and penetration testers. 
'''

import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = "pythonprogramming.net"

def pscan(port):
    try:
        s.connect((server, port))
        return True
    except:
        return False

for x in range(1,26):
    if pscan(x):
        print("Port", x, "is open!!!!!!!")
    else:
        print("Port", x, "is closed")
