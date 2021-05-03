import socket
from sqlite3_class import SQLite3_Class 
from tkinter import *
import datetime
import os

"homework, output numbers to database (with timestamp)"

class Client:
    def __init__(self, ip="127.0.0.1", port=5050, window_title="Server-Client Communication"):
        self.ip = ip
        self.port = port
        self.root = Tk()
        if window_title is not None:
            self.root.title(window_title)
        os.remove("numbers_database.db")
        self.database = SQLite3_Class("numbers_database.db")
        self.database.custom_execute_command("CREATE TABLE IF NOT EXISTS numbers_table (numbers TEXT, date TEXT)", output=False)

    def return_time_formatted(self):
        return datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S")

    def get_random_numbers(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.ip, self.port))
        self.s.send("GET /random_numbers HTTP/1.1".encode())
        http_code, random_numbers = self.s.recv(1024).decode().split(" | ")
        random_numbers = list(map(int, random_numbers.split()))    
        self.random_numbers = random_numbers
        self.s.close()
        return self.random_numbers

    def sort(self, list):
        copyList = list.copy()
        if len(list) != 1:
            middle = len(copyList)//2
            left = copyList[:middle]
            right = copyList[middle:]

            mergeSortLeft = self.sort(left)
            mergeSortRight = self.sort(right)

            current, currentLeft, currentRight = 0, 0, 0

            while currentLeft < len(mergeSortLeft) and currentRight < len(mergeSortRight):
                if mergeSortLeft[currentLeft] < mergeSortRight[currentRight]:
                    copyList[current] = mergeSortLeft[currentLeft]
                    currentLeft+=1
                else:
                    copyList[current] = mergeSortRight[currentRight]
                    currentRight+=1
                current+=1

            while currentLeft < len(mergeSortLeft):
                copyList[current] = mergeSortLeft[currentLeft]
                currentLeft+=1
                current+=1

            while currentRight < len(mergeSortRight):
                copyList[current] = mergeSortRight[currentRight]
                currentRight+=1
                current+=1

        return copyList

    def UI_setup(self):
        self.display_random_numbers()
        new_numbers = Button(self.root, text="New Numbers", command=self.display_random_numbers)
        sort_button = Button(self.root, text="Sort Numbers", command=self.display_sorted_numbers)
        new_numbers.grid(row=1, column=3)
        sort_button.grid(row=1, column=6)

    def display_random_numbers(self):
        self.get_random_numbers()
        self.database.insert("numbers_table", (' '.join(str(element) for element in self.random_numbers), self.return_time_formatted()))
        for index, random_number in enumerate(self.random_numbers):
            label = Label(self.root, text=random_number, font=["Arial", 12])
            label.grid(row=0, column=index, padx=20)
            

    def display_sorted_numbers(self):
        sorted_numbers = self.sort(self.random_numbers)
        self.database.update_specific("numbers_table", {"numbers": ' '.join(str(element) for element in sorted_numbers)}, f"numbers='{' '.join(str(element) for element in self.random_numbers)}'")
        self.random_numbers = sorted_numbers
        for index, random_number in enumerate(self.random_numbers):
            label = Label(self.root, text=random_number, font=["Arial", 12])
            label.grid(row=0, column=index, padx=20)

    def UI_listen(self):
        self.root.mainloop()

    def close(self):
        self.database.commit()
        self.database.close()

client1 = Client(ip=input("Enter IP: "))

client1.UI_setup()
client1.UI_listen()

client1.close()
