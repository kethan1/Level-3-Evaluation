import socket
import random
import threading
import time

class Server:
    def __init__(self, port=5050):
        self.users = []
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind(('', port))
        self.s.listen()

    def random_numbers_list(self, quantity):
        return ' '.join([random.randint(0, 9) for _ in range(quantity)])

    def new_user(self, conn, addr):
        threading.Thread(target=self.listen_for_messages, args=(conn, addr), daemon=True).start()
        self.users.append([conn, addr])

    def listen_for_messages(self, conn, addr):
        while True:
            print(1232, conn, addr)
            recieved = self.s.recv(1024).decode()
            if recieved == "GET /random_numbers HTTP/1.1":
                self.s.send("HTTP/1.1 200 OK".encode())
                self.s.send(self.random_numbers_list().encode())
            print("recieved:", recieved)
            # addr, recieved = self.s.recvfrom(1024).decode()
            # if recieved == "GET /random_numbers HTTP/1.1":
            #     self.s.sendto("HTTP/1.1 200 OK".encode(), addr)
            #     self.s.sendto(self.random_numbers_list().encode(), addr)
            # print("recieved:", recieved)

    def listen_for_users(self):
        while True:
            print(1)
            conn, addr = self.s.accept()
            print(2)
            self.new_user(conn, addr)

print(1)
server1 = Server()
print(2)
threading.Thread(target=server1.listen_for_users, daemon=True).start()
print(3)

while True:
    if server1.users == []:
        time.sleep(180)
        if server1.users == []:
            break
