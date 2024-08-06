# this is the import for the tkinter module
from tkinter import *


def quit():
    root.quit()



# this line is initialising the root window
root=Tk()




# this line is setting the title of the window
root.title("Hello, world!")

# this line is setting the size of the window
root.geometry("300x400")

# this line is setting the background color of the window
root.configure(bg="blue")

# this line is setting the text of the label
text=StringVar()
text.set("Hello, world!")
w= Label(root, textvariable=text).pack(anchor=N)

# this line is setting the text of the button
button = Button(root, textvariable=text, command=lambda: quit() ).pack()

# this line is setting the text of the entry
entryValue = StringVar()
entry= Entry(root, textvariable=entryValue).pack()

# this line is setting the text of the checkbutton and radiobutton
checkButtonValue = IntVar()
checkButton = Checkbutton(root, text="Check me!", variable=checkButtonValue).pack()

# this line is setting the text of the radiobutton
radioButtonValue = IntVar()
radioButton1 = Radiobutton(root, text="Option 1", variable=radioButtonValue, value=1).pack()
radioButton1 = Radiobutton(root, text="Option 2", variable=radioButtonValue, value=2).pack()

#this line is for setting the image in the window
img = PhotoImage(file="").pack()


root.mainloop()