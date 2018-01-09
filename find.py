import os
from tkinter import *

master = Tk()
img = PhotoImage(file='uaa_logo.png')
lbl = Label(master, image=img)
lbl.place(x=10, y=150)
master.title("Buscador de archivos")
master.geometry("520x300+30+30")
Label(master, text="Ingrese el archivo a buscar").grid(row=0,column=2)
Label(master, text="Archivo").grid(row=1)
Label(master, text="Directorio").grid(row=2)
Label(master, text="Localidad de memoria").grid(row=3)

e1 = Entry(master)
e2 = Label(text=' ')
e3 = Label(text=' ')
e4 = Label(text=' ')


e1.grid(row=1, column=2)
e2.grid(row=2, column=2)
e3.grid(row=3, column=2)
e4.grid(row=4, column=2)


def abrirArchivo():
    file = e1.get()
    for r, d, f in os.walk(r'c:'):
        for files in f:
            if files == file:
                tmp = os.path.join(r, files)
    try:
        os.startfile(tmp)
    except Exception as e:
        print(e)



def finder():
   file = e1.get()
   for r, d, f in os.walk(r"C:\\Users\\DELL I7567\\Desktop\\"):
      for files in f:
         if files == file:
            e2.config(text=os.path.join(r, files))
            e3.config(text = os.walk(file))

try:
   Button(master, text='Abrir', command=abrirArchivo).grid(row=5, column=1, sticky=W, pady=3)
   Button(master, text='Buscar', command=finder).grid(row=5, column=3, sticky=W, pady=3)
except Exception as e:
   print (e)
mainloop( )