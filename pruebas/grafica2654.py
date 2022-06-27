from tkinter import *
from tkinter import font
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
root = Tk()
root.title("Algoritmos de Ordenamiento")
root.state('zoomed')
root.config(background="lightblue")
#root.resizable(0,0)


#root.iconbitmap("")
##root.resizable(False,False);

tiempo = [0.12,0.789,1.45,45.012,32.14]
datos = [50,80,250,3546,1893]


f1 = Frame(root, width=600, height=500, background="red")
f1.pack(fill="both", expand=True, padx=10, pady=10)





f2 = Frame(f1,width=800, height=260,background="blue")
f2.pack(fill="both",padx=2, pady=2,side="left")
#------------------------------CREAR GRAFICA---------------------------------
fig = Figure(figsize=(5, 5), dpi=100)
fig.add_subplot(111).plot(tiempo,datos )
canvas = FigureCanvasTkAgg(fig, master=f2)  # CREAR AREA DE DIBUJO DE TKINTER.
canvas.draw()
canvas.get_tk_widget().pack(side="top", fill="both")
#-----------------------AÑADIR BARRA DE HERRAMIENTAS--------------------------
toolbar = NavigationToolbar2Tk(canvas, f2)# barra de iconos
toolbar.update()
canvas.get_tk_widget().pack(side="top", fill="both")

# Crear una barra de deslizamiento con orientación vertical.
scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = Y )
listbox1=Listbox(f2, selectmode="MULTIPLE", yscrollcommand=scrollbar.set )
#listbox1=Listbox(f2, selectmode="MULTIPLE")
listbox1.pack()
scrollbar.config( command = listbox1.yview )

listbox1.insert(0,"papa")
listbox1.insert(1,"manzana")
listbox1.insert(2,"pera")
listbox1.insert(3,"sandia")
listbox1.insert(4,"naranja")
listbox1.insert(5,"melon")
listbox1.insert(6,"manzana")
listbox1.insert(7,"pera")
listbox1.insert(8,"sandia")
listbox1.insert(9,"naranja")
listbox1.insert(10,"melon")
listbox1.insert(11,"manzana")
listbox1.insert(12,"pera")
listbox1.insert(13,"sandia")
listbox1.insert(14,"naranja")
listbox1.insert(15,"melon")
listbox1.insert(16,"manzana")
listbox1.insert(17,"pera")
listbox1.insert(18,"sandia")
listbox1.insert(19,"naranja")



f3 = Frame(f1, height=260, background="green")
f3.pack(fill="both",padx=2, pady=2,expand=True)



f4 = Frame(f1, height=260, background="orange")
f4.pack(fill="both", expand=True, padx=2, pady=2)


root.mainloop() 