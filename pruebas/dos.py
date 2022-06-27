from tkinter import *
from tkinter import font
import os

from numpy import size

ancho_ventana = 800
alto_ventana = 550
root = Tk()
root.title("Algoritmos de Ordenamiento")
x_ventana = root.winfo_screenwidth() // 2 - ancho_ventana // 2
y_ventana = root.winfo_screenheight() // 2 - alto_ventana // 2
posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
root.geometry(posicion)
root.config(background="red")

#root.resizable(0,0)

datos = []
ruta = os.path.abspath(os.getcwd())


f1 = Frame(root, width=600, height=500, background="blue")
f1.pack(fill="both", expand=True, padx=20, pady=20)

f2 = Frame(root,width=600, height=70,background="orange")
f2.place(in_=f1, anchor="c", relx=.5, rely=.15)
label = Label(f2, text="Metodo de Ordenamiento Burbuja")
label.place(anchor="center",relx=.5 ,rely=.5)
label.config(bg="lightblue",fg="black",font=("Arial,52"))

f3 = Frame(root,width=600, height=280, background="green")
f3.place(in_=f1, anchor="c", relx=.5, rely=.50)

def validIteracion():
    if(len(numIteracion.get())>0):
        numDatos.config(state=NORMAL)
        btn5.config(state=NORMAL)
        numIteracion.config(state=DISABLED)
        btn4.config(state=DISABLED)
        
def addCantidad():
    if(len(numDatos.get())>0):
        datos.append(int(numDatos.get()))
        cantidadLabel.configure(text=len(datos))
        numDatos.delete(0, END)
        #print(numIteracion.get())
    if(len(datos)==int(numIteracion.get())):
        numDatos.config(state=DISABLED)
        btn5.config(state=DISABLED)
        btn3.config(state=NORMAL)

def grafica():
    print(datos)

numIteracionLabel = Label(f3,text="Ingrese un entero para realizar las iteraciones")
numIteracionLabel.place(in_=f3,anchor="sw", relx=.12, rely=.20)
numIteracionLabel.config(bg="lightblue",fg="black",font=("Arial,32"))
numIteracion = Entry(f3,font=("Arial,32"))
numIteracion.place(in_=f3,anchor="sw", relx=.12, rely=.35,width=380, height=33)
btn4 = Button(f3,text="ADD",height = 1, width = 5,font=("Arial,18"),command=validIteracion)
btn4.place(anchor="sw",relx=.78 ,rely=.35)


numDatosLabel = Label(f3,text="Ingrese un entero para la cantidad de datos a generar")
numDatosLabel.place(in_=f3,anchor="sw", relx=.12, rely=.45)
numDatosLabel.config(bg="lightblue",fg="black",font=("Arial,32"))
#campo de texto
numDatos = Entry(f3,font=("Arial,32"),state='disabled')
numDatos.place(in_=f3,anchor="sw", relx=.12, rely=.60,width=380, height=33)
btn5 = Button(f3,text="ADD",height = 1, width = 5,font=("Arial,18"),state="disabled",command=addCantidad)
btn5.place(anchor="sw",relx=.78 ,rely=.60)


cantidadLabel = Label(f3,font=("Arial,789"),width=3,height=3)
cantidadLabel.place(anchor="sw",relx=.10 ,rely=.85)
btn3 = Button(f3,text="Generar",height = 2, width = 20,font=("Arial,18"),state="disabled",command=grafica)
btn3.place(anchor="center",relx=.8 ,rely=.85)



root.mainloop() 