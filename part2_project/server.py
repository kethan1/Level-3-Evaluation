import socket
import random
import threading
import time
import datetime

class Server:
    def __init__(self, port=5050):
        self.users = []
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind(('', port))
        self.s.listen()
        self.log_file = open("dsmeg.txt", "w")

    def return_time_formatted(self):
        return datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S")

    def random_numbers_list(self, quantity):
        return ' '.join([str(random.randint(0, 9)) for _ in range(quantity)])

    def new_user(self, conn, addr):
        threading.Thread(target=self.listen_for_messages, args=(conn, addr), daemon=True).start()
        self.users.append([conn, addr])

    def listen_for_messages(self, conn, addr):
        recieved = conn.recv(1024).decode()
        print(self.return_time_formatted(), f"Recieved: {recieved}", file=self.log_file)
        if recieved == "GET /random_numbers HTTP/1.1":
            conn.send(f"HTTP/1.1 200 OK | {self.random_numbers_list(10)}".encode())
            print(self.return_time_formatted(), "Sent: HTTP/1.1 200 OK", file=self.log_file)
        print(self.return_time_formatted(), "thread ended", file=self.log_file)
        print(self.return_time_formatted(), f"{addr} disconnected\n", file=self.log_file)

    def listen_for_users(self):
        while True:
            conn, addr = self.s.accept()
            print(self.return_time_formatted(), f"{addr} connected", file=self.log_file)
            print(self.return_time_formatted(), "HTTP/1.1 100 Continue", file=self.log_file)
            print(self.return_time_formatted(), "thread started", file=self.log_file)
            self.new_user(conn, addr)

    def start_listen_for_users(self):
        threading.Thread(target=self.listen_for_users, daemon=True).start()

    def close(self):
        for user in self.users:
            user[0].close()
        self.log_file.close()

server1 = Server()
server1.start_listen_for_users()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    pass

server1.close()
