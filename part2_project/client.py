import socket
from tkinter import *

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("127.0.0.1", 5050))

root = Tk()
root.title("Random Numbers")

def random_numbers():
    print(2)
    s.send("GET /random_numbers HTTP/1.1".encode())
    print(3)
    http_code = s.recv(1024).decode()
    print(4)
    random_numbers = s.recv(1024).decode()
    print(5)
    random_numbers = random_numbers.split()
    print(6)
    print(random_numbers)

# while True:
#     to_send = input("Enter text, q to quit: ")
#     s.send(to_send.encode())
#     if to_send == "q":
#         break
#     root.update()
print(1)
random_numbers()
print(7)
s.close()

root.mainloop()
