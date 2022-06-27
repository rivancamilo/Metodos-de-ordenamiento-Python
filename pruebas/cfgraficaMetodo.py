from cProfile import label
from tkinter import *
from tkinter import font
from xml.parsers import expat
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
Terceraventana = Tk()
Terceraventana.title("Algoritmos de Ordenamiento")
Terceraventana.state('zoomed')
Terceraventana.config(background="lightblue")
Terceraventana.resizable(0,0)


#Terceraventana.iconbitmap("")
##Terceraventana.resizable(False,False);

t1 = [32.14,0.789,1.45,45.012,0.12]
t2 = [0.36,1.45,32.14,0.789,45.012]
t3 = [45.012,0.12,0.789,1.45,32.14]
cantidad = [50,80,250,3546,1893]

def grafica_indi():
   ##*********************************************************************************
   ##    contenedor de la grafica
   ##*********************************************************************************
   f1 = Frame(Terceraventana,width=800, height=500,background="blue")
   f1.pack(fill="both",padx=15, pady=15,side="left",expand=True)
   f5 = Frame(f1, width=800, height=500, background="green")
   f5.place(in_=f1, anchor="c", relx=.5, rely=.4)

   f6 = Frame(f1, width=700, height=80, background="green")
   f6.place(in_=f1, anchor="c", relx=.5, rely=.78)
   ##*********************************************************************************
   ##    impresion de la grafica
   ##*********************************************************************************
   figure = plt.Figure(figsize=(7,7), dpi=100)
   ax = figure.add_subplot(111)
   ax.plot(t1, cantidad,marker='*',label="Mert Sort")
   ax.plot(t2, cantidad,marker='+',label="Burbuja")
   ax.plot(t3, cantidad,marker='*',label="Mezcla")
   ax.set_xlabel('Tiempo (x)', size = 14),ax.set_ylabel('Cantidad de datos ', size = 14)
   ax.set_title("Metodos de Comparacion", 
            fontdict={'family': 'serif', 
                     'color' : 'darkblue',
                     'weight': 'bold',
                     'size': 18})
   ax.legend()
   line = FigureCanvasTkAgg(figure, f5)
   line.draw()
   line.get_tk_widget().pack()
   #-----------------------AÑADIR BARRA DE HERRAMIENTAS--------------------------
   toolbar = NavigationToolbar2Tk(line, f6)# barra de iconos
   toolbar.update()
   line.get_tk_widget().pack(side="top", fill="both")


   f2 = Frame(Terceraventana, width=800, height=500, background="red")
   f2.pack(fill="both", padx=2, pady=15,side="right",expand=True)
   ##*********************************************************************************
   ##    Frame para el metodo 1
   ##*********************************************************************************
   frameMetodo1 = Frame(f2, width=350, height=300, background="green")
   frameMetodo1.place(in_=f2, anchor="c", relx=.35, rely=.20)
   labelMetodo1 = Label(f2, text="Metodo de Ordenamiento Burbuja",font=('Arial',16))
   labelMetodo1.place( relx=.1, rely=.07)
   scrollbar1 = Scrollbar(frameMetodo1)
   scrollbar1.pack( side = "right", fill = Y )
   listMetodo1 = Listbox(frameMetodo1, yscrollcommand = scrollbar1.set ,width=40,font=("Arial,52"))
   ##*********************************************************************************
   ##    Frame para el metodo 2
   ##*********************************************************************************
   frameMetodo2 = Frame(f2, width=350, height=300, background="green")
   frameMetodo2.place(in_=f2, anchor="c", relx=.35, rely=.45)
   labelMetodo2 = Label(f2, text="Metodo de Ordenamiento Burbuja",font=('Arial',16))
   labelMetodo2.place( relx=.1, rely=.32)
   scrollbar2 = Scrollbar(frameMetodo2)
   scrollbar2.pack( side = "right", fill = Y )
   listMetodo2 = Listbox(frameMetodo2, yscrollcommand = scrollbar2.set ,width=40,font=("Arial,52"))
   ##*********************************************************************************
   ##    Frame para el metodo 3
   ##*********************************************************************************
   frameMetodo3 = Frame(f2, width=350, height=300, background="green")
   frameMetodo3.place(in_=f2, anchor="c", relx=.35, rely=.7)
   labelMetodo3 = Label(f2, text="Metodo de Ordenamiento Burbuja",font=('Arial',16))
   labelMetodo3.place( relx=.1, rely=.57)
   scrollbar3 = Scrollbar(frameMetodo3)
   scrollbar3.pack( side = "right", fill = Y )
   listMetodo3 = Listbox(frameMetodo3, yscrollcommand = scrollbar3.set ,width=40,font=("Arial,52"))
   
   
   ##*********************************************************************************
   ##    Frame footer
   ##*********************************************************************************
   frameFooter = Frame(f2, width=1200, height=80, background="green")
   frameFooter.place( anchor="s", relx=.35, rely=.94)
   btnExit = Button(frameFooter,text="Salir",height = 1, width = 15,font=('Arial',14))
   btnExit.place(anchor="se",relx=.97 ,rely=.7)
   btnMain = Button(frameFooter,text="Inicio",height = 1, width = 15,font=('Arial',14))
   btnMain.place(anchor="sw",relx=.29 ,rely=.7)
   #btn1.pack(side="right")
   
   ##imprimimos los items en el lisbox 
   for indice,itme in enumerate(cantidad):
      listMetodo1.insert(END, "Eje X ={} --- Eje Y ={}".format(t1[indice],cantidad[indice]))
      listMetodo2.insert(END, "Eje X ={} --- Eje Y ={}".format(t1[indice],cantidad[indice]))
      listMetodo3.insert(END, "Eje X ={} --- Eje Y ={}".format(t1[indice],cantidad[indice]))
      
   listMetodo1.pack( side = "left", fill = "both" )
   scrollbar1.config( command = listMetodo1.yview )
   #metodo 2
   listMetodo2.pack( side = "left", fill = "both" )
   scrollbar2.config( command = listMetodo2.yview )
   #metodo 3
   listMetodo3.pack( side = "left", fill = "both" )
   scrollbar3.config( command = listMetodo3.yview )


grafica_indi()

Terceraventana.mainloop() 