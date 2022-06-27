from tkinter import *
from tkinter.ttk import Progressbar
import time



        

ws = Tk()
ws.title('PythonGuides')
ws.geometry('200x150')
ws.config(bg='#345')


pb = Progressbar(ws,orient = HORIZONTAL,length = 100,mode = 'determinate')
pb.place(x=40, y=20)

txt = Label(ws,text = '0%',bg = '#345',fg = '#fff')
txt.place(x=150 ,y=20 )

Button(ws,text='Start',command=step).place(x=40, y=50)

ws.mainloop()