
from tkinter import *

def funcion():
    Otraventana.state(newstate = "zoomed")
    root.state(newstate = "withdraw")

def funcion2():
    Otraventana.state(newstate = "withdraw")
    root.state(newstate = "zoomed") #state(newstate = "withdraw")root.deiconify, zoomed()


root = Tk()
root.state(newstate = "zoomed")
root.resizable(0, 0)
root.title("Ventana 1")

abrirVentana2 = Button(root, text="Abrir ventana 2", bg="green", 
                       font= ("Times New Roman", 12), 
                       fg="yellow", command=funcion)
abrirVentana2.pack()


Otraventana = Toplevel()
Otraventana.state(newstate = "withdraw")
Otraventana.title("Ventana 2")

miEtiqueta = Label(Otraventana, text="Bienvenido a la ventana 2", bg="#252850", font=("Times New Roman", 12), fg="yellow")
miEtiqueta.pack()

abrirVentana1 = Button(Otraventana, text="Abrir ventana principal", bg="green", font= ("Times New Roman", 12), fg="yellow", command=funcion2)
abrirVentana1.pack()


Otraventana.mainloop()
root.mainloop()
