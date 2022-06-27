from tkinter import *
import tkinter as tk
from tkinter import font
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure


#root.iconbitmap("")
##root.resizable(False,False);



def salir():
    #graficaindi.state(newstate = "deiconify")
    root.state(newstate = "zoomed") #state(newstate = "withdraw")root.deiconify, zoomed()
    graficaindi.state(newstate = "withdraw")
    print("salir..")
      
root = Tk()
root.title("Algoritmos de Ordenamiento")
root.state(newstate = "zoomed")
root.config(background="lightblue")
root.resizable(0,0)


graficaindi = Toplevel()
graficaindi.state(newstate = "withdraw") ##BORRAMOS LA VENTANA DE GRAFICA
graficaindi.config(background="lightblue")
graficaindi.resizable(0,0)
##***************************************************************************************
##***************************************************************************************
##***************************************************************************************
##***************************************************************************************
##***************************************************************************************
##***************************************************************************************
##***************************************************************************************
##***************************************************************************************
##              contenido GRAFICA
##***************************************************************************************
def grafica_indi():
    graficaindi.state(newstate = "zoomed")
    root.state(newstate = "withdraw")
    
    f1 = Frame(graficaindi,width=800, height=500,background="blue")
    f1.pack(fill="both",padx=15, pady=15,side="left",expand=True)
    f5 = Frame(f1, width=800, height=500, background="green")
    f5.place(in_=f1, anchor="c", relx=.5, rely=.4)

    f6 = Frame(f1, width=700, height=80, background="green")
    f6.place(in_=f1, anchor="c", relx=.5, rely=.78)
    ##*********************************************************************************
    ##    impresion de la grafica
    ##*********************************************************************************
    """ figure = plt.Figure(figsize=(7,7), dpi=100)
    ax = figure.add_subplot(111)
    ax.plot(tiempo, datos)
    ax.set_xlabel('Tiempo (x)', size = 14),ax.set_ylabel('Cantidad de datos ', size = 14)
    ax.set_title(titulo, 
            fontdict={'family': 'serif', 
                        'color' : 'darkblue',
                        'weight': 'bold',
                        'size': 18})
    line = FigureCanvasTkAgg(figure, f5)
    line.draw()
    line.get_tk_widget().pack()
    #-----------------------AÑADIR BARRA DE HERRAMIENTAS--------------------------
    toolbar = NavigationToolbar2Tk(line, f6)# barra de iconos
    toolbar.update()
    line.get_tk_widget().pack(side="top", fill="both") """


    f2 = Frame(graficaindi, width=800, height=500, background="green")
    f2.pack(fill="both", padx=2, pady=15,side="right",expand=True)
    """ btn2 = Button(f2,text="Metodo Burbuja 1",height = 2, width = 20,font=("Arial,18"),command=salir)
    btn2.place(anchor="center",relx=.5 ,rely=.89)
    
    ##*********************************************************************************
    ##    Frame para el listbox
    ##*********************************************************************************
    f3 = Frame(f2, width=350, height=300, background="green")
    f3.place(in_=f2, anchor="c", relx=.5, rely=.25)
    scrollbar = Scrollbar(f3)
    scrollbar.pack( side = "right", fill = Y )
    mylist = Listbox(f3, yscrollcommand = scrollbar.set ,width=40,font=("Arial,52") )
    ##imprimimos los items en el lisbox 
    for indice,itme in enumerate(datosx):
        mylist.insert(END, "Eje X ={} \t --- \t Eje Y ={}".format(datosx[indice],datosy[indice]))
        #mylist.insert(END, "This is line number " + str(line))
    mylist.pack( side = "left", fill = "both" )
    scrollbar.config( command = mylist.yview ) """





f1 = Frame(root, width=600, height=500, background="lightblue")
f1.pack(fill="both", expand=True, padx=20, pady=20)
##***************************************************************************************
##              contenedor encabexzado
##***************************************************************************************
f2 = Frame(root,width=600, height=160,background="lightblue")
f2.place(in_=f1, anchor="c", relx=.5, rely=.25)
label = Label(f2, text="Seleccione un Metodo de Ordenamiento")
label.place(anchor="center",relx=.5 ,rely=.5)
label.config(bg="lightblue",fg="black",font=("Arial,52"))

##***************************************************************************************
##              contenedor botones
##***************************************************************************************
f3 = Frame(root,width=600, height=280, background="red")
f3.place(in_=f1, anchor="c", relx=.5, rely=.58)
##***************************************************************************************
##              Botones
##***************************************************************************************
btn1 = Button(f3,text="Metodo Burbuja 1",height = 2, width = 20,font=("Arial,18"),command=grafica_indi())
btn1.place(anchor="center",relx=.5 ,rely=.1)

btn2 = Button(f3,text="Metodo Burbuja 1",height = 2, width = 20,font=("Arial,18"))
btn2.place(anchor="center",relx=.5 ,rely=.29)

btn3 = Button(f3,text="Metodo Burbuja 1",height = 2, width = 20,font=("Arial,18"))
btn3.place(anchor="center",relx=.5 ,rely=.48)

btn4 = Button(f3,text="Metodo Burbuja 1",height = 2, width = 20,font=("Arial,18"))
btn4.place(anchor="center",relx=.5 ,rely=.67)

graficaindi.mainloop()
root.mainloop() 