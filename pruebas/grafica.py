""" #IMPORTAMOS LIBRERIAS NECESARIAS.
import tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import numpy as np

#------------------------------CREAR VENTANA---------------------------------
root = tkinter.Tk()
root.wm_title("Grafica insertada en Tkinter")


#------------------------------CREAR GRAFICA---------------------------------
fig = Figure(figsize=(5, 4), dpi=100)
t = np.arange(0, 3, .01)
fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

canvas = FigureCanvasTkAgg(fig, master=root)  # CREAR AREA DE DIBUJO DE TKINTER.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

#-----------------------AÑADIR BARRA DE HERRAMIENTAS--------------------------
toolbar = NavigationToolbar2Tk(canvas, root)# barra de iconos
toolbar.update()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

#-----------------------------BOTÓN "cerrar"----------------------------------
def cerrar():
    root.quit()     
    root.destroy()

button = tkinter.Button(master=root, text="cerrar", command=cerrar)
button.pack(side=tkinter.BOTTOM)

tkinter.mainloop() """

""" import tkinter

from matplotlib.ft2font import VERTICAL

root = tkinter.Tk()

f1 = tkinter.Frame(root, width=600, height=500, background="red")
f1.pack(padx=20, pady=20)

scrollbar = tkinter.Scrollbar(f1)
scrollbar.pack( side = "right", fill = tkinter.Y )
mylist = tkinter.Listbox(f1, yscrollcommand = scrollbar.set ,width=40 )

for line in range(100):
   mylist.insert(tkinter.END, "This is line number " + str(line))
   
mylist.pack( side = "left", fill = "both" )
scrollbar.config( command = mylist.yview )

tkinter.mainloop() """

import tkinter as tk
from tkinter import ttk

import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import pandas as pd


# DataFrame para ejemplo
df = pd.DataFrame({"Foo": (1, 5, 8, 7, 5, 1, 5),
                   "Bar": (4.25, 5, 6, 1.3, 1, 2.6, 3.7)}
                  )

# Creamos una figura y añadimos algunas gráficas en subplots
fig1 = Figure(figsize=(5, 5), dpi=100)
ax1 = fig1.add_subplot(311)
ax2 = fig1.add_subplot(312)
ax3 = fig1.add_subplot(313)
df.plot(ax=ax1)
df.plot.bar(ax=ax2)
df.plot.area(ax=ax3)


# Ventana principal
root = tk.Tk()

# Canvas  y barras de desplazamiento
canvas = tk.Canvas(root, borderwidth=0, background="#ffffff")
hsb = tk.Scrollbar(root, orient="horizontal", command=canvas.xview)                 
vsb = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(xscrollcommand=hsb.set)
canvas.configure(yscrollcommand=vsb.set)
hsb.pack(side="bottom", fill="x")
vsb.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)

# Vamos a usar un ttk.Labelframe para contener FigureCanvasTkAgg
plot_frame = ttk.Labelframe(canvas, text='Plots')
canvas.create_window((4,4), window=plot_frame, anchor="nw", tags="plot_frame")
plot_frame.bind("<Configure>",
                lambda event: canvas.configure(scrollregion=canvas.bbox("all"))
                )

# Creamos una instancia de FigureCanvas que renderizará la figura
canvas1 = FigureCanvasTkAgg(fig1, master=plot_frame)
canvas1.draw()
canvas1.get_tk_widget().grid(row=0, column=0)

root.mainloop()