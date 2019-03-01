from tkinter import Tk, Label, Button, Entry, OptionMenu, END, W, E, Checkbutton, IntVar, StringVar, Scrollbar, Text
from random import *


class coe_generator:
    def __init__(self, master):
        self.master = master
        master.title("Piccola Katy COE generator - by gmammarella")

        self.filename = "coefile"
        self.filecore = ""
        self.initstring = "memory_initialization_radix=16;\nmemory_initialization_vector=\n"

        #labels:
        Label(master, text="Nome file:").grid(row=0, column=0, sticky=W)
        Label(master, text="numero parole:").grid(row=1, column=0, sticky=W)
        Label(master, text="numero bit parola:").grid(row=2, column=0, sticky=E)

        #entry
        self.namefileentry = Entry(master, width=15)
        self.namefileentry.insert(END, self.filename)
        self.namefileentry.grid(row=0, column=1)
        Label(master, text=".coe").grid(row=0, column=2, sticky=W)


        self.nword = Entry(master, width=15)
        self.nword.insert(END, "")
        self.nword.grid(row=1, column=1)

        self.nbit = Entry(master, width=15)
        self.nbit.insert(END, "")
        self.nbit.grid(row=2, column=1)


        Button(master, text="Quit", command=master.quit, width=10).grid(row=3, column=1, columnspan=3, pady=4)
        Button(master, text="Generate", command=lambda:self.generate(), width=10).grid(row=3, column=0, pady=4)

    def generate(self):
        self.nomefile = str(self.namefileentry.get() + ".coe")
        self.coefile = open(self.nomefile, "w+")

        self.coefile.write(self.initstring)
        self.fillfile()
        self.coefile.write(self.filecore)

        self.coefile.close()

    def fillfile(self):
        nw = int(self.nword.get())
        nb = int(self.nbit.get())


        for x in range(0, nw):
            for y in range(0, nb):
                self.filecore += format(randint(0,16), '01x')
            self.filecore += ",\n"

        self.filecore = self.filecore[:-2]
        self.filecore += ";"

root = Tk()
my_gui = coe_generator(root)
root.mainloop()