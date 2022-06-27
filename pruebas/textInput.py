from cProfile import label
from tkinter import *
root = Tk()
root.title("Algoritmos de Ordenamiento")


titulo = Label(root,text="Metodo de Ordenamiento ")
titulo.grid(row=2,column=3,padx=55,pady=25)
titulo.config(bg="lightblue",fg="black",font=("Arial,32"))


numDatosLabel = Label(root,text="Nemero de datos")
numDatosLabel.grid(row=3,column=3,sticky="e",padx=5,pady=5)
numDatosLabel.config(bg="lightblue",fg="black",font=("Arial,32"))

numDatos = Entry(root)
numDatos.grid(row=3,column=4,padx=20)


numIteracionLabel = Label(root,text="numero de la iteracion")
numIteracionLabel.grid(row=4,column=3,sticky="e",padx=5,pady=5)
numIteracionLabel.config(bg="lightblue",fg="black",font=("Arial,32"))

numIteracion = Entry(root)
numIteracion.grid(row=4,column=4,padx=20)

# Color de fondo, background
root.config(bg="lightblue")     
root.config(width=650,height=550) 
root.mainloop() 