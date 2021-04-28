# Tkinter

# 3.	Give an example of a Tkinter template with the following:
# a.	Widgets: buttons, labels, entry box, message box
# b.	Positioning: pack, place, grid
# c.	Callbacks
# d.	Frames
# e.	Entry Box (get and delete data) - use tkinter variable
# f.	Canvas

from tkinter import *
from tkinter import messagebox

# Create Window
root = Tk()

# Create 3 frames, one for each positioning system
grid_positioning_system = Frame(width=300, height=100)
pack_positioning_system = Frame(width=300, height=100)
place_positioning_system = Frame(width=300, height=100)

# Set Title of Window
root.title("Tkinter Window")

label_show = StringVar()
label_show.set("default")

label_show2 = StringVar()
label_show2.set("default")

label_show3 = StringVar()
label_show3.set("default")

def set_label_show(which, which_text_var):
    if which.get() == "":
        messagebox.showwarning("showwarning", "Please Do Not Leave Entry Box Blank")
    else:
        which_text_var.set(which.get())
        which.delete(0, END)

# Widgets
label = Label(grid_positioning_system, textvariable=label_show, font=["Arial", 12])
entry = Entry(grid_positioning_system)
button = Button(grid_positioning_system, text="Change Label Text", command=lambda: set_label_show(entry, label_show))
# canvas = Canvas(grid_positioning_system)

label.grid(row=0, column=0)
entry.grid(row=0, column=1)
button.grid(row=1, column=0)
# canvas.grid(row=2, column=0)

label2 = Label(pack_positioning_system, textvariable=label_show2, font=["Arial", 12])
entry2 = Entry(pack_positioning_system)
button2 = Button(pack_positioning_system, text="Change Label Text", command=lambda: set_label_show(entry2, label_show2))
# canvas = Canvas(grid_positioning_system)

label2.pack()
entry2.pack()
button2.pack()

label3 = Label(place_positioning_system, textvariable=label_show3, font=["Arial", 12])
entry3 = Entry(place_positioning_system)
button3 = Button(place_positioning_system, text="Change Label Text", command=lambda: set_label_show(entry3, label_show3))
# canvas = Canvas(grid_positioning_system)

label3.place(x=35, y=7)
entry3.place(x=90, y=13)
button3.place(x=70, y=35)

grid_positioning_system.grid(row=0, column=0)
pack_positioning_system.grid(row=0, column=1)
place_positioning_system.grid(row=0, column=2)

canvas = Canvas(root, width=100, height=100, bg="green")

# pprint(dir(canvas), indent=4)

# Rectangle Oval Line

canvas.create_rectangle((10, 30), (40, 50))
canvas.create_line((10, 20), (90, 20))
canvas.create_oval((50, 50), (70, 70))
canvas.create_text((70, 70), text="h")

canvas.grid(row=1, column=0)

# This function updates the window, and runs until it is closed
root.mainloop()
