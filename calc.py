from tkinter import *

def press(num):
    equation.set(equation.get()+str(num)) 

def equalpress(): 
    try:
        equation.set(str(eval(equation.get())) ) 
 
    except: 
        equation.set(" error ") 

def clear(): 
    equation.set("") 
 
 
if __name__ == "__main__":
    gui = Tk() 
    gui.title("Simple Calculator") 
    gui.configure(bg="light grey")
    gui.geometry("270x150") 
    equation = StringVar() 
    Label(gui, textvariable=equation).grid(columnspan=4)
    Button(gui, text=' 1 ', command=lambda: press(1), height=1, width=7) .grid(row=2, column=0) 
    Button(gui, text=' 2 ',command=lambda: press(2), height=1, width=7).grid(row=2, column=1) 
    Button(gui, text=' 3 ', command=lambda: press(3), height=1, width=7) .grid(row=2, column=2) 
    Button(gui, text=' 4 ', command=lambda: press(4), height=1, width=7) .grid(row=3, column=0) 
    Button(gui, text=' 5 ', command=lambda: press(5), height=1, width=7) .grid(row=3, column=1) 
    Button(gui, text=' 6 ', command=lambda: press(6), height=1, width=7) .grid(row=3, column=2) 
    Button(gui, text=' 7 ', command=lambda: press(7), height=1, width=7) .grid(row=4, column=0)  
    Button(gui, text=' 8 ', command=lambda: press(8), height=1, width=7).grid(row=4, column=1) 
    Button(gui, text=' 9 ', command=lambda: press(9), height=1, width=7).grid(row=4, column=2) 
    Button(gui, text=' 0 ', command=lambda: press(0), height=1, width=7).grid(row=5, column=0) 
    Button(gui, text=' + ', command=lambda: press("+"), height=1, width=7).grid(row=2, column=3) 
    Button(gui, text=' - ', command=lambda: press("-"), height=1, width=7).grid(row=3, column=3) 
    Button(gui, text=' * ', command=lambda: press("*"), height=1, width=7).grid(row=4, column=3) 
    Button(gui, text=' / ', command=lambda: press("/"), height=1, width=7).grid(row=5, column=3) 
    Button(gui, text=' = ', command=lambda: equalpress(), height=1, width=7).grid(row=5, column=2) 
    Button(gui, text='Clear', command=lambda: clear(), height=1, width=7) .grid(row=5, column='1') 
    Button(gui, text='.', command=lambda: press('.'), height=1, width=7).grid(row=6, column=0) 

    gui.mainloop() 