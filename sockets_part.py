"""
Sockets
1.	List out all socket terminologies.
2.	Give an example of a basic server template
3.	Give an example of a basic client template
4.	Give an example of a one-way socket communication
5.	Give an example of a turn-based socket communication
6.	Give an example of a two-way threaded communication
"""

"""
IP Address - IP Address refers to a computer, that is public ip address (accessible on any wifi, 
router settings may or may not support this), and local ip address (on local wifi), this format:
XXX.XXX.X.XX

Port - One Stream of Communication of IP, there can be tons of ports per IP, allows system to 
communicate to more than one stream of data over 1 IP

Socket - Packets of data communicated over an IP:PORT

HTTP - hypertext transfer protocol, basis of communication on web, implements GET, POST, DELETE
and more

HTTPS - Encrypted version of HTTP

DNS - Domain name system, provides a human-friendly naming internet resources.

Server - Waits for client to connect by binding the address the client can use to connect

Client - Connects to server using server's address (IP:Port)

Stream Sockets (TCP) - Data delivery is guaranteed and it will arrive in the same order it was sent, 
An error is outputed if data unable to be sent or is not recieved. These use TCP. 

Datagram Sockets (UDP) - Data delivery is not guaranteed and it might not to arrive in the
same order it was sent. Unlike stream sockets, an open connection is not needed, as you build
the packet with the destination information. These use UDP. These sockets are faster than
stream sockets. 
"""

# 2. 

# import socket
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# s.bind(('', 2234))

# s.listen(2)

# conn, addr = s.accept()

# conn.send("hi".encode())
# print(conn.recv(1024).decode())

# conn.close()

# 3. 

# import socket

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# s.connect(("192.168.0.29", 2234))

# print(s.recv(1024).decode())
# s.send("Hi".encode())

# s.close()

# 4. 

# server

# import socket
# import time
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# s.bind(('', 2234))

# s.listen(2)

# conn, addr = s.accept()

# while True:
#     to_send = input("Enter text, q to quit: ")
#     conn.send(to_send.encode())
#     if to_send == "q":
#         break

# conn.close()

# client 

# import socket

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# s.connect(("192.168.0.29", 2234))

# while True:
#     to_send = s.recv(1024).decode()
#     if to_send == "q":
#         break
#     print(to_send)

# s.close()

# 5.

# server

# import socket
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# s.bind(('', 2234))

# s.listen(2)

# conn, addr = s.accept()

# while True:
#     to_send = input("Enter text, q to quit: ")
#     conn.send(to_send.encode())
#     if to_send == "q":
#         break
#     recieved = conn.recv(1024).decode()
#     if recieved == "q":
#         break
#     print(recieved)

# conn.close()

# client

# import socket

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# s.connect(("192.168.0.29", 2234))

# while True:
#     recieved = s.recv(1024).decode()
#     if recieved == "q":
#         break
#     print(recieved)
#     to_send = input("Enter text, q to quit: ")
#     s.send(to_send.encode())
#     if to_send == "q":
#         break

# s.close()

# 6.

# server

import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('', 2234))

s.listen(2)

conn, addr = s.accept()

print("Connected")

to_continue = True

def get_messages():
    while True:
        recieved = conn.recv(1024).decode()
        if recieved == "q":
            to_continue = False
        print("Client:", recieved)

t = threading.Thread(target=get_messages)

t.start()

while to_continue:
    to_send = input("")
    conn.send(to_send.encode())
    if to_send == "q":
        break

conn.close()

# client

# import socket
# import threading

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# s.connect(("192.168.0.29", 2234))

# print("Connected")

# to_continue = True

# def get_messages():
#     while True:
#         recieved = s.recv(1024).decode()
#         if recieved == "q":
#             to_continue = False
#         print("Server:", recieved)

# t = threading.Thread(target=get_messages)

# t.start()

# while to_continue:
#     to_send = input("")
#     s.send(to_send.encode())
#     if to_send == "q":
#         break

# s.close()
