from cProfile import label
from tkinter import *
root = Tk()
root.title("Algoritmos de Ordenamiento")
#root.iconbitmap("")
##root.resizable(False,False);

# Hijo de root, no ocurre nada
frame = Frame(root)  
# Empaqueta el frame en la raíz
frame.pack()      

menubar = Menu(root)
root.config(menu=menubar)  # Lo asignamos a la base


filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Archivo", menu=filemenu)
filemenu.add_command(label="Nuevo")
filemenu.add_command(label="Abrir")
filemenu.add_command(label="Guardar")
filemenu.add_command(label="Cerrar")
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)

def hola():
    print('Hola mundo')



Button(frame,text='Metodo Burbuja',command=hola).pack()



# Color de fondo, background
frame.config(bg="lightblue")     

# Podemos establecer un tamaño,
# la raíz se adapta al frame que contiene
frame.config(width=650,height=550) 

root.mainloop() 