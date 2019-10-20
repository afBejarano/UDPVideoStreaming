import tkinter as tk
import os
import sys


r = ''
def show_entry_fields():
    r = e1.get()
    os.system("python client.py --port {}".format(r))
    sys.exit()

master = tk.Tk()
master.title('Streaming UDP - Cliente')
tk.Label(master, text="Especifique el canal al cual desea conectarse").grid(row=0)
tk.Label(master, text="Controles:").grid(row=1)
tk.Label(master, text="- Click izquierdo en pantalla reproduccion => Play/Pause").grid(row=2)
tk.Label(master, text="- Click derecho en pantalla reproduccion => Salir").grid(row=3)
e1 = tk.Entry(master)
e1.insert(10, "65123")
e1.grid(row=0, column=1)

tk.Button(master,text='Reproducir', command=show_entry_fields).grid(row=0,column=2, sticky=tk.W, pady=4)


master.mainloop()