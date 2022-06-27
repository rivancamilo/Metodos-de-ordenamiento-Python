from tkinter import *


tiempo = [0.12,0.789,1.45,45.012,32.14]


##***************************************************************************************
##***************************************************************************************
##***************************************************************************************
##***************************************************************************************
##***************************************************************************************
##***************************************************************************************
##***************************************************************************************
##***************************************************************************************
##              contenido Inicio
##***************************************************************************************
root = Tk()
root.state(newstate = "zoomed")
root.resizable(0, 0)
root.config(background="lightblue")
root.title("Algoritmos de Ordenamiento")

f1_root = Frame(root, width=600, height=500, background="lightblue")
f1_root.pack(fill="both", expand=True, padx=20, pady=20)

##----------------------------------  contenedor encabexzado    -------------------------
f2_root = Frame(root,width=600, height=160,background="lightblue")
f2_root.place(in_=f1_root, anchor="c", relx=.5, rely=.25)
label_root = Label(f2_root, text="Seleccione un Metodo de Ordenamiento")
label_root.place(anchor="center",relx=.5 ,rely=.5)
label_root.config(bg="lightblue",fg="black",font=("Arial,52"))

##***************************************************************************************
##              contenedor botones
##***************************************************************************************
f3_root = Frame(root,width=600, height=280, background="lightblue")
f3_root.place(in_=f1_root, anchor="c", relx=.5, rely=.58)
##***************************************************************************************
##              Botones
##***************************************************************************************
btn1_root = Button(f3_root,text="Metodo Burbuja 1",height = 2, width = 20,
              font=("Arial,18"))
btn1_root.place(anchor="center",relx=.5 ,rely=.1)

btn2_root = Button(f3_root,text="Metodo Burbuja 1",height = 2, width = 20,
              font=("Arial,18"))
btn2_root.place(anchor="center",relx=.5 ,rely=.29)

btn3_root = Button(f3_root,text="Metodo Burbuja 1",height = 2, width = 20,
              font=("Arial,18"))
btn3_root.place(anchor="center",relx=.5 ,rely=.48)

btn4_root = Button(f3_root,text="Metodo Burbuja 1",height = 2, width = 20,
              font=("Arial,18"))
btn4_root.place(anchor="center",relx=.5 ,rely=.67)



root.mainloop()