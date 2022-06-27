from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Progressbar
from turtle import bgcolor, width
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import random
from timeit import default_timer
import time
from metodos import burbuja,merge_sort,insertion_sort

##***************************************************************************************
##             DECLARACION DE VARIABLES GLOBALES
##***************************************************************************************
datos = []
d1 = []
d2 = []
d3 = []
cantidad = []
tiempo = []
t1 = []
t2 = []
t3 = []
global labeltxt
##***************************************************************************************
##            FUNCION PARA GENERAR UNA LISTA DE NÚMEROS RAMDON SIN REPETICIÓN 
##***************************************************************************************
def llenarArray(num_max):
    #declaramos lista vacia
    lista = []
    for i in range(num_max): 
        num = random.randint(1,(num_max*100))
        ##generamos un numero que no este en la lista
        while num in lista:
            num = random.randint(1,(num_max*100))
        lista.append(num)
        #print(random.randint(1, 10))
    #print('impresion lista   '+str(lista))
    return lista
##***************************************************************************************
##            FUNCIÓN PARA SALIR CUANDO ESTAMOS EN UNA GRÁFICA INDIVIDUAL
##***************************************************************************************
def quitGraficaIndi():
    try:
        root.destroy()
        Otraventana.destroy()
    except:
        print('cerrando programa')
##***************************************************************************************
##            FUNCIÓN PARA SALIR CUANDO ESTAMOS EN LA GRAFICA DE COMPARACIÓN
##***************************************************************************************
def quitGraficaCompare():
    try:
        root.destroy()
        Terceraventana.destroy()
    except:
        print('cerrando programa')
##***************************************************************************************
##            FUNCIÓN PARA LIMPIAR LAS LISTAS DE LA GRÁFICA DE COMPARACIÓN
##***************************************************************************************
def clsArrayCompare():
    for indice in range(len(cantidad)-1,-1,-1):
        cantidad.pop(indice)
        t1.pop(indice)
        t2.pop(indice)
        t3.pop(indice)
        
##***************************************************************************************
##            FUNCIÓN PARA LIMPIAR LAS LISTAS DE LA GRÁFICA INDIVIDUAL
##***************************************************************************************
def clsArrayIndi():
    for indice in range(len(cantidad)-1,-1,-1):
        cantidad.pop(indice)
        tiempo.pop(indice)
##***************************************************************************************
##            FUNCIÓN PARA GENERAR LA GRÁFICA INDIVIDUAL
##***************************************************************************************   
def mainGraficaIndi():
    Otraventana.state(newstate = "withdraw")
    root.state(newstate = "zoomed")
    ##reseteamos los datos ingresados previamente
    cantidadLabel.place_forget()
    optionMetodo.set(None)
    numDatos.delete(0, END)
    numIteracion.config(state=NORMAL)
    numIteracion.delete(0, END)
    numIteracion.config(state=DISABLED)
    clsArrayIndi()
##***************************************************************************************
##            FUNCIÓN PARA GENERAR LA GRÁFICA DE COMPARACIÓN
##***************************************************************************************
def mainGraficaCompare():
    Terceraventana.state(newstate = "withdraw")
    root.state(newstate = "zoomed")
    ##reseteamos los datos ingresados previamente
    cantidadLabel.place_forget()
    optionMetodo.set(None)
    numDatos.delete(0, END)
    numIteracion.config(state=NORMAL)
    numIteracion.delete(0, END)
    numIteracion.config(state=DISABLED)
    clsArrayCompare()
##***************************************************************************************
##     FUNCION PARA REGRESAR A LA VENTANA INICIAL DESDE LA GRÁFICA DE COMPARACIÓN
##***************************************************************************************
def windowGraficaCompare():
    root.state(newstate = "withdraw")
    Terceraventana.state(newstate = "zoomed")
##***************************************************************************************
##     FUNCION PARA REGRESAR A LA VENTANA INICIAL DESDE LA GRÁFICA INDIVIDUAL
##***************************************************************************************
def windowGrafica():
    root.state(newstate = "withdraw")
    Otraventana.state(newstate = "zoomed") #state(newstate = "withdraw")root.deiconify, zoomed()
##***************************************************************************************
##             FUNCIÓN PARA HABILITAR EL ENTRY DEL NÚMERO DE ITERACIONES
##***************************************************************************************
def validCheck():
    numIteracion.config(state=NORMAL)
    btn4Data_win.config(state=NORMAL)
##***************************************************************************************
##          FUNCIÓN PARA REALIZAR UNA PAUSA EN LA EJECUCIÓN DE SCRIPT
##***************************************************************************************   
def step():
    base = int(numDatos.get())
    if (base > 0 & base<100):    
        for i in range(4):
            f4Data_win.update_idletasks()
            pb['value'] += 25
            time.sleep(1)
    elif (base > 100 & base<999):    
        for i in range(5):
            f4Data_win.update_idletasks()
            pb['value'] += 20
            time.sleep(1)
    elif (base > 999 & base<9999):    
        for i in range(10):
            f4Data_win.update_idletasks()
            pb['value'] += 10
            time.sleep(1)
    elif (base > 9999 & base<99999):    
        for i in range(20):
            f4Data_win.update_idletasks()
            pb['value'] += 5
            time.sleep(1)
##***************************************************************************************
##     FUNCIÓN PARA GENERAR LA GRÁFICA DE COMPARACIÓN
##***************************************************************************************        
def grafica_compara():
    if(optionMetodo.get()==1):
        titulo="Ordenamiento por Inserción"
    elif (optionMetodo.get()==2):
        titulo="Ordenamiento por Mezcla"
    elif (optionMetodo.get()==3):
        titulo="Ordenamiento de Burbuja"
    else:
        titulo="Comparación de Métodos"
        
    if(str(len(t1))==numIteracion.get() and str(len(t2))==numIteracion.get() and str(len(t3))==numIteracion.get()):
        windowGraficaCompare()
    ##*********************************************************************************
    ##    contenedor de la grafica
    ##*********************************************************************************
    f1 = Frame(Terceraventana,width=450, height=500,background="lightblue")
    f1.pack(fill="both",padx=15, pady=15,side="left",expand=True)
    
    f5 = Frame(f1, width=450, height=500, background="lightblue")
    f5.place(in_=f1, anchor="c", relx=.5, rely=.4)

    f6 = Frame(f1, width=700, height=80, background="lightblue")
    f6.place(in_=f1, anchor="c", relx=.5, rely=.72)
    ##*********************************************************************************
    ##    impresion de la grafica
    ##*********************************************************************************
    figure = plt.Figure(figsize=(8.3,5), dpi=73)
    ax = figure.add_subplot(111)
    ax.plot(cantidad,t1,marker='*',label="Inserción")
    ax.plot(cantidad,t2,marker='+',label="Mezcla")
    ax.plot(cantidad,t3,marker='*',label="Burbuja")
    ax.set_xlabel('Cantidad de datos', size = 14),ax.set_ylabel('Tiempo', size = 14)
    ax.set_title(titulo, 
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


    f2 = Frame(Terceraventana, width=400, height=500, background="lightblue")
    f2.pack(fill="both", padx=2, pady=15,side="right",expand=True)
    ##*********************************************************************************
    ##    Frame para el metodo 1
    ##*********************************************************************************
    frameMetodo1 = Frame(f2, width=300, height=60, background="lightblue")
    frameMetodo1.place(in_=f2, anchor="c", relx=.35, rely=.19)
    labelMetodo1 = Label(f2, text="Ordenamiento por Inserción",font=('Arial',16),bg="lightblue")
    labelMetodo1.place( relx=.1, rely=.05)
    scrollbar1 = Scrollbar(frameMetodo1)
    scrollbar1.pack( side = "right", fill = Y )
    listMetodo1 = Listbox(frameMetodo1, yscrollcommand = scrollbar1.set ,width=30,height=6, font=('Arial',12))
    ##*********************************************************************************
    ##    Frame para el metodo 2
    ##*********************************************************************************
    frameMetodo2 = Frame(f2, width=300, height=60, background="lightblue")
    frameMetodo2.place(in_=f2, anchor="c", relx=.35, rely=.43)
    labelMetodo2 = Label(f2, text="Ordenamiento por Mezcla",font=('Arial',16),bg="lightblue")
    labelMetodo2.place( relx=.1, rely=.29)
    scrollbar2 = Scrollbar(frameMetodo2)
    scrollbar2.pack( side = "right", fill = Y )
    listMetodo2 = Listbox(frameMetodo2, yscrollcommand = scrollbar2.set ,width=30,height=6, font=('Arial',12))
    ##*********************************************************************************
    ##    Frame para el metodo 3
    ##*********************************************************************************
    frameMetodo3 = Frame(f2, width=300, height=100, background="lightblue")
    frameMetodo3.place(in_=f2, anchor="c", relx=.35, rely=.67)
    labelMetodo3 = Label(f2, text="Ordenamiento de Burbuja",font=('Arial',16),bg="lightblue")
    labelMetodo3.place( relx=.1, rely=.53)
    scrollbar3 = Scrollbar(frameMetodo3)
    scrollbar3.pack( side = "right", fill = Y )
    listMetodo3 = Listbox(frameMetodo3, yscrollcommand = scrollbar3.set ,width=30,height=6,font=('Arial',12))

    ##*********************************************************************************
    ##    Frame footer
    ##*********************************************************************************
    frameFooter = Frame(f2, width=500, height=80, background="lightblue")
    frameFooter.place( anchor="s", relx=.5, rely=.93)
    btnExit = Button(frameFooter,text="Salir",height = 1, width = 15,font=('Arial',12),command=quitGraficaCompare)
    btnExit.place(anchor="se",relx=.97 ,rely=.7)
    btnMain = Button(frameFooter,text="Inicio",height = 1, width = 15,font=('Arial',12),command=mainGraficaCompare)
    btnMain.place(anchor="sw",relx=.05 ,rely=.7)
    #btn1.pack(side="right")

    ##imprimimos los items en el lisbox 
    for indice,itme in enumerate(cantidad):
        listMetodo1.insert(END, "Eje X ={} --- Eje Y ={}".format(cantidad[indice],t1[indice]))
        listMetodo2.insert(END, "Eje X ={} --- Eje Y ={}".format(cantidad[indice],t2[indice]))
        listMetodo3.insert(END, "Eje X ={} --- Eje Y ={}".format(cantidad[indice],t3[indice]))
        
    listMetodo1.pack( side = "left", fill = "both" )
    scrollbar1.config( command = listMetodo1.yview )
     #metodo 2
    listMetodo2.pack( side = "left", fill = "both" )
    scrollbar2.config( command = listMetodo2.yview )
    #metodo 3
    listMetodo3.pack( side = "left", fill = "both" )
    scrollbar3.config( command = listMetodo3.yview )
##***************************************************************************************
##     FUNCIÓN PARA GENERAR LA GRÁFICA INDIVIDUAL
##***************************************************************************************
def grafica_indi():
    
    if(optionMetodo.get()==1):
        titulo="Ordenamiento por Inserción"
        labeltxt="Inserción"
    elif (optionMetodo.get()==2):
        titulo="Ordenamiento por Mezcla"
        labeltxt="Mezcla"
    elif (optionMetodo.get()==3):
        titulo="Ordenamiento de Burbuja"
    else:
        titulo="Comparación de Métodos"
        labeltxt="Burbuja"
        
    if(str(len(tiempo))==numIteracion.get()):
        windowGrafica()
    ##*********************************************************************************
    ##    contenedor de la grafica
    ##*********************************************************************************
    f1 = Frame(Otraventana,width=450, height=500,background="lightblue")
    f1.pack(fill="both",padx=15, pady=15,side="left",expand=True)
    
    f5 = Frame(f1, width=450, height=500, background="lightblue")
    f5.place(in_=f1, anchor="c", relx=.5, rely=.4)

    f6 = Frame(f1, width=700, height=80, background="lightblue")
    f6.place(in_=f1, anchor="c", relx=.5, rely=.72)
    ##*********************************************************************************
    ##    impresion de la grafica
    ##*********************************************************************************
    figure = plt.Figure(figsize=(8.3,5), dpi=73)
    ax = figure.add_subplot(111)
    ax.plot(cantidad,tiempo,marker='*',label=labeltxt)
    ax.set_xlabel('Cantidad de datos', size = 14),ax.set_ylabel('Tiempo', size = 14)
    ax.set_title(titulo, 
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


    f2 = Frame(Otraventana, width=400, height=500, background="lightblue")
    f2.pack(fill="both", padx=2, pady=15,side="right",expand=True)
    ##*********************************************************************************
    ##    Frame para el listbox
    ##*********************************************************************************
    f3 = Frame(f2, width=300, height=80, background="lightblue")
    f3.place(in_=f2, anchor="c", relx=.5, rely=.25)
    scrollbar = Scrollbar(f3)
    scrollbar.pack( side = "right", fill = Y )
    mylist = Listbox(f3, yscrollcommand = scrollbar.set ,width=40,font=("Arial,52") )
    ##imprimimos los items en el lisbox 
    for indice,itme in enumerate(cantidad):
        mylist.insert(END, "Eje X ={} \t --- Eje Y ={}".format(cantidad[indice],tiempo[indice]))
      #mylist.insert(END, "This is line number " + str(line))
    mylist.pack( side = "left", fill = "both" )
    scrollbar.config( command = mylist.yview )
    
    ##*********************************************************************************
    ##    Frame footer
    ##*********************************************************************************
    frameFooter = Frame(f2, width=500, height=80, background="lightblue")
    frameFooter.place( anchor="s", relx=.5, rely=.94)
    btnExit = Button(frameFooter,text="Salir",height = 1, width = 13,font=('Arial',12),command=quitGraficaIndi)
    btnExit.place(anchor="se",relx=.97 ,rely=.7)
    btnMain = Button(frameFooter,text="Inicio",height = 1, width = 13,font=('Arial',12),command=mainGraficaIndi)
    btnMain.place(anchor="sw",relx=.05 ,rely=.7)
##***************************************************************************************
##     FUNCION PARA HABILITAR LA CANTIDAD Y DESACTIVAR EL NÚMERO DE ITERACIONES
##***************************************************************************************   
def validIteracion():
    if(len(numIteracion.get())>0):
        numDatos.config(state=NORMAL)
        btn5Data_win.config(state=NORMAL)
        numIteracion.config(state=DISABLED)
        btn4Data_win.config(state=DISABLED)
##***************************************************************************************
##     FUNCIÓN PARA CARGAR LAS LISTAS Y VALIDAR LA CANTIDAD DE DATOS A GENERAR
##***************************************************************************************          
def addCantidad():
    if(len(numDatos.get())>0):
        cantidad.append(int(numDatos.get()))
        if(optionMetodo.get()==1):
            pb.place(in_=f4Data_win, relx=.0, rely=.92,width=800)
            numDatos.config(state=DISABLED)
            btn5Data_win.config(state=DISABLED)
            inicio = default_timer()
            datos = llenarArray(int(numDatos.get()))
            insertion_sort(datos)
            fin = default_timer()
            tiempo.append(round(fin-inicio,4))
            step()
            
        elif(optionMetodo.get()==2):
            pb.place(in_=f4Data_win, relx=.0, rely=.92,width=800)
            numDatos.config(state=DISABLED)
            btn5Data_win.config(state=DISABLED)
            inicio = default_timer()
            datos = llenarArray(int(numDatos.get()))
            merge_sort(datos)
            fin = default_timer()
            tiempo.append(round(fin-inicio,4))
            step()
        elif(optionMetodo.get()==3):
            pb.place(in_=f4Data_win, relx=.0, rely=.92,width=800)
            numDatos.config(state=DISABLED)
            btn5Data_win.config(state=DISABLED)
            inicio = default_timer()
            datos = llenarArray(int(numDatos.get()))
            burbuja(datos)
            fin = default_timer()
            tiempo.append(round(fin-inicio,4))
            step()
        else:
            # ************* metodo 1
            pb.place(in_=f4Data_win, relx=.0, rely=.92,width=800)
            numDatos.config(state=DISABLED)
            btn5Data_win.config(state=DISABLED)
            inicio = default_timer()
            d1 = llenarArray(int(numDatos.get()))
            insertion_sort(d1)
            fin = default_timer()
            t1.append(round(fin-inicio,4))
            step()
            # ************* metodo 2
            pb.config(value=1)
            pb.place(in_=f4Data_win, relx=.0, rely=.92,width=800)
            inicio = default_timer()
            d2 = llenarArray(int(numDatos.get()))
            merge_sort(d2)
            fin = default_timer()
            t2.append(round(fin-inicio,4))
            step()
            # ************* metodo 3
            pb.config(value=1)
            pb.place(in_=f4Data_win, relx=.0, rely=.92,width=800)
            inicio = default_timer()
            d3 = llenarArray(int(numDatos.get()))
            burbuja(d3)
            fin = default_timer()
            t3.append(round(fin-inicio,4))
            step()
            
            
        time.sleep(2.5)
        numDatos.config(state=NORMAL)
        btn5Data_win.config(state=NORMAL) 
        #print(tiempo)   
        #print(cantidad)
        pb.config(value=1)
        pb.place_forget()
        cantidadLabel.place(anchor="sw",relx=.5 ,rely=.95)
        cantidadLabel.configure(text=len(cantidad))
        numDatos.delete(0, END)
        
        #print(numIteracion.get())
    if(len(cantidad)==int(numIteracion.get())):
        numDatos.config(state=DISABLED)
        btn5Data_win.config(state=DISABLED)
        if(optionMetodo.get()!=4):
            f5Data_win.place(in_=f1Data_win, anchor="c", relx=.5, rely=.90)
            btn7Data_win.place(anchor="c",relx=.5 ,rely=.5)
            btn7Data_win.config(command=grafica_indi)
        else:
            f5Data_win.place(in_=f1Data_win, anchor="c", relx=.5, rely=.90)
            btn7Data_win.place(anchor="c",relx=.5 ,rely=.5)
            btn7Data_win.config(command=grafica_compara)
 
##***************************************************************************************
##***************************************************************************************
##***************************************************************************************
##***************************************************************************************
##***************************************************************************************
##***************************************************************************************
##***************************************************************************************
##***************************************************************************************
##           SCRIPT PARA GENERAR EL GRAFICO DEL INGRESO DE DATOS 
##***************************************************************************************
root = Tk()
optionMetodo = IntVar()
root.state(newstate = "zoomed")
root.resizable(0, 0)
root.config(background="lightblue")
root.title("Algoritmos de Ordenamiento")

f1Data_win = Frame(root, width=600, height=500, background="lightblue")
f1Data_win.pack(fill="both", expand=True, padx=20, pady=20)
f2Data_win = Frame(f1Data_win,width=600, height=70,background="lightblue")
f2Data_win.place(in_=f1Data_win, anchor="c", relx=.5, rely=.02)
label = Label(f2Data_win, text="Métodos de Ordenamiento")
label.place(anchor="center",relx=.5 ,rely=.5)
label.config(bg="lightblue",fg="black",font=('Arial', 30))
f3Data_win = Frame(f1Data_win,width=600, height=280, background="lightblue")
f3Data_win.place(in_=f1Data_win, anchor="c", relx=.5, rely=.64)

f4Data_win = Frame(f1Data_win,width=600, height=280, background="lightblue")
f4Data_win.place(in_=f1Data_win, anchor="c", relx=.5, rely=.27)

Label(f4Data_win,text="Seleccione un método de Ordenamiento",font=('Arial', 13),bg="lightblue").place(in_=f4Data_win,relx=.10, rely=.05)
Radiobutton(f4Data_win,text="Ordenamiento por Inserción",variable=optionMetodo,
            value=1,font=('Arial', 12),bg="lightblue",state=NORMAL,command=validCheck).place(in_=f4Data_win, relx=.2, rely=.2,)
Radiobutton(f4Data_win,text="Ordenamiento por Mezcla",variable=optionMetodo,
            value=2,font=('Arial', 12),bg="lightblue",state=NORMAL,command=validCheck).place(in_=f4Data_win, relx=.2, rely=.34)
Radiobutton(f4Data_win,text="Ordenamiento de Burbuja",variable=optionMetodo,
            value=3,font=('Arial', 12),bg="lightblue",state=NORMAL,command=validCheck).place(in_=f4Data_win, relx=.2, rely=.48)
Radiobutton(f4Data_win,text="Comparación de Métodos",variable=optionMetodo,
            value=4,font=('Arial', 12),bg="lightblue",state=NORMAL,command=validCheck).place(in_=f4Data_win, relx=.2, rely=.62)
pb = Progressbar(f4Data_win,orient = HORIZONTAL,length = 100,mode = 'determinate',value=1)
numIteracionLabel = Label(f3Data_win,text="Ingrese un entero para realizar las iteraciones")
numIteracionLabel.place(in_=f3Data_win,anchor="sw", relx=.12, rely=.20)
numIteracionLabel.config(bg="lightblue",fg="black",font=("Arial,32"))
numIteracion = Entry(f3Data_win,font=('Arial', 15),state=DISABLED)
numIteracion.place(in_=f3Data_win,anchor="sw", relx=.12, rely=.35,width=380, height=33)
btn4Data_win = Button(f3Data_win,text="ADD",height = 1, width = 5,font=("Arial,18"),command=validIteracion,state=DISABLED)
btn4Data_win.place(anchor="sw",relx=.78 ,rely=.35)
numDatosLabel = Label(f3Data_win,text="Ingrese un entero para la cantidad de datos a generar")
numDatosLabel.place(in_=f3Data_win,anchor="sw", relx=.12, rely=.45)
numDatosLabel.config(bg="lightblue",fg="black",font=("Arial,32"))
#campo de texto
numDatos = Entry(f3Data_win,font=('Arial', 15),state='disabled')
numDatos.place(in_=f3Data_win,anchor="sw", relx=.12, rely=.60,width=380, height=33)
btn5Data_win = Button(f3Data_win,text="ADD",height = 1, width = 5,font=("Arial,18"),state="disabled",command=addCantidad)
btn5Data_win.place(anchor="sw",relx=.78 ,rely=.60)
cantidadLabel = Label(f3Data_win,bg="lightblue")
cantidadLabel.config(font=('Arial', 44))
cantidadLabel.place(anchor="sw",relx=.5 ,rely=.95)

##***************************************************************************************
##***************************************************************************************
##***************************************************************************************
##***************************************************************************************
##***************************************************************************************
##***************************************************************************************
##***************************************************************************************
##***************************************************************************************
##       SCRIPT PARA GENERAR EL GRAFICO DE LA GRAFICA INDIVIDUAL
##***************************************************************************************
Otraventana = Toplevel()
Otraventana.state(newstate = "withdraw")
Otraventana.title("Algoritmos de Ordenamiento")
Otraventana.config(background="lightblue")
    
##***************************************************************************************
##***************************************************************************************
##***************************************************************************************
##***************************************************************************************
##***************************************************************************************
##***************************************************************************************
##***************************************************************************************
##***************************************************************************************
##        SCRIPT PARA GENERAR EL GRAFICO DE LA GRAFICA DE COMPARACIÓN
##***************************************************************************************        
Terceraventana = Toplevel()
Terceraventana.state(newstate = "withdraw")
Terceraventana.title("Algoritmos de Ordenamiento")
Terceraventana.config(background="lightblue")

f5Data_win = Frame(f1Data_win,width=600, height=80, background="lightblue")
btn7Data_win = Button(f5Data_win,text="Graficar", width = 13,font=('Arial',18))

##***************************************************************************************
##***************************************************************************************
##***************************************************************************************
##***************************************************************************************
##***************************************************************************************
##***************************************************************************************
##***************************************************************************************
##***************************************************************************************
##        SCRIPT PARA MOSTRAR LA VENTANA GRAFICA TKINTER
##***************************************************************************************
Otraventana.mainloop()
Terceraventana.mainloop()
root.mainloop()