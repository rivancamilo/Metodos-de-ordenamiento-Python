import tkinter as tk
from tkinter import Button, messagebox


def menu():
    try:
        ent1_value = int(ent1.get())
    except ValueError:
        messagebox.showwarning("Error", "Escribir solo números enteros.")
    else:
        if ent1_value == 1:
            vsismorresistente()
        elif ent1_value == 2:
            vperf_suelos()
        elif ent1_value == 3:
            #vz_sismica()
            print('Hola')
        else:
            messagebox.showwarning("Error", "Escribir la opción correcta")

def salir():
    vprincipal.destroy()
def principal():
    v_sism_rres.destroy()
    v_suelos.destroy()
    vprincipal.state('zoomed') 

def vsismorresistente():
    vprincipal.withdraw()
    v_sism_rres.title("ZONAS SISMORRESISTENTE")
    v_sism_rres.state('zoomed')
    v_sism_rres.configure(background = "light sky blue")
    btn2 = Button(v_sism_rres,text="Metodo Burbuja 1",height = 2, width = 20,font=("Arial,18"),command=principal())
    btn2.place(anchor="center",relx=.5 ,rely=.89)

def vperf_suelos():
    vprincipal.withdraw()
    v_suelos.title("PERFILES DE SUELOS")
    v_suelos.state('zoomed')
    v_suelos.configure(background = "light sky blue")

#Configuración de la ventana
vprincipal = tk.Tk()
vprincipal.title("SISMICIDAD")
vprincipal.state('zoomed')
vprincipal.configure(background="light sky blue")

#ETIQUETAS:
#Menu Principal:
v_sism_rres = tk.Toplevel(vprincipal)
v_suelos = tk.Toplevel(vprincipal)

#ENTRADAS:
#Menu Principal:
ent1 = tk.Entry(vprincipal)
ent1.pack(pady = 1, ipady = 5)

#BOTONES:
#Boton para abrir opciones:
botonmenu = tk.Button(vprincipal, text = "Aceptar", fg = "black", command = menu)
botonmenu.pack(padx = 5, pady = 5)

botonsalir = tk.Button(vprincipal, text = "Salir", fg = "black", command = salir)
botonsalir.pack(padx = 5, pady = 5)

vprincipal.mainloop()