

# Importation des modules
from pyfunct import *
from tkinter import *
import tkinter.ttk as ttk

# index

TKINTER = 'tkinter'
TTK = 'ttk'
GAUCHE = 'gauche'
DROITE = 'droite'

######################################################
# ___________      ____________     |              /                                        #
#               |                                       |                        |            /                                          #
#               |                                       |                        |          /                                            #
#               |                                       |                        |        /                                              #
#               |                                       |                        |      /                                                #
#               |                                       |                        |    /                                                  #
#               |                                       |                        |  /                                                    #
#               |                                       |                        |/                                                      #
#               |                                       |                        |\                                                      #
#               |                                       |                        |  \                                                    #
#               |                                       |                        |    \                                                  #
#               |                                       |                        |      \                                                #
#               |                                       |                        |        \                                              #
#               |                                       |                        |          \                                            #
#               |                                       |                        |            \                                          #
#               |                                       |                        |              \                                        #
######################################################


# Classe de l'entrée avec commande
class Entryttk(ttk.Entry, ttk.Button, ttk.Label, ttk.Checkbutton, ttk.Radiobutton, ttk.Frame):

    def __init__(self, master=None, **kw):
        self.frame = ttk.Frame(master)
        ttk.Entry.__init__(self, self.frame, kw)
        self.num = 1
        self.grid(row=1, column=1, padx=0, pady=0, sticky=EW)
        self.pal = []

    def _grid(self, **kw):
        self.frame.grid(kw)

    def _pack(self, **kw):
        self.frame.pack(kw)

    def _place(self, **kw):
        self.frame.place(kw)

    def _destroy(self):
        self.frame.destroy()

    def _forget(self):
        self.frame.forget()

    def _grid_forget(self):
        self.frame.grid_forget()

    def _pack_forget(self):
        self.frame.pack_forget()

    def _place_forget(self):
        self.frame.place_forget()

    def delwidget(self, widget):
        a = self.pal.index(widget)
        del(self.pal[a])
        widget.destroy()
        a = int(self.num) - 1
        self.num = 1
        if len(self.pal) > 0:
            for ww in self.pal:
                ww.grid(row=1, column=self.num + 1, padx=0, pady=0, sticky=EW)
                self.num += 1
    
    def add_button(self, type_=TTK, **kw):
        if type_ == TKINTER:
            b = Button(self.frame)
        else:
            b = ttk.Button(self.frame)
        b.configure(kw)
        b['width'] = 2
        self.pal.append(b)
        if self.num <= 20:
            b.grid(row=1, column=self.num + 1, rowspan=2, padx=0, pady=0, sticky=EW)
            self.num += 1
        return b

    def add_label(self, type_=TTK, **kw):
        if type_ == TKINTER:
            b = Label(self.frame)
        else:
            b = ttk.Label(self.frame)
        b.configure(kw)
        b['width'] = 2
        self.pal.append(b)
        if self.num <= 20:
            b.grid(row=1, column=self.num + 1, rowspan=2, padx=0, pady=0, sticky=EW)
            self.num += 1
        return b

    def add_checkbutton(self, type_=TTK, **kw):
        if type_ == TKINTER:
            b = Checkbutton(self.frame)
        else:
            b = ttk.Checkbutton(self.frame)
        b.configure(kw)
        b['width'] = 2
        self.pal.append(b)
        if self.num <= 20:
            b.grid(row=1, column=self.num + 1, rowspan=2, padx=0, pady=0, sticky=EW)
            self.num += 1
        return b

    def add_entry(self, type_=TTK, **kw):
        if type_ == TKINTER:
            b = Entry(self.frame)
        else:
            b = ttk.Entry(self.frame)
        b.configure(kw)
        b['width'] = 2
        self.pal.append(b)
        if self.num <= 20:
            b.grid(row=1, column=self.num + 1, rowspan=2, padx=0, pady=0, sticky=EW)
            self.num += 1
        return b

    def add_radiobutton(self, type_=TTK, **kw):
        if type_ == TKINTER:
            b = Radiobutton(self.frame)
        else:
            b = ttk.Radiobutton(self.frame)
        b.configure(kw)
        b['width'] = 2
        self.pal.append(b)
        if self.num <= 20:
            b.grid(row=1, column=self.num + 1, rowspan=2, padx=0, pady=0, sticky=EW)
            self.num += 1
        return b

    def scrolled(self, type_=TTK, **kw):
        if type_ == TKINTER:
            b = Scrollbar(self.frame)
        else:
            b = ttk.Scrollbar(self.frame)
        try:
            b.config(kw)
            b.config(orient=HORIZONTAL)
        finally:
            b.configure(kw)
            b.configure(orient=HORIZONTAL)
        try:
            b['width'] = 10
        except:
            pass
        self['xscrollcommand'] = b.set
        self.bar = b
        b.grid(row=2, column=1, sticky=EW)


# Classe de la radiobutton avec commande
class Radiobuttonttk(ttk.Entry, ttk.Button, ttk.Label, ttk.Checkbutton, ttk.Radiobutton, ttk.Frame):

    def __init__(self, master=None, **kw):
        self.frame = ttk.Frame(master)
        ttk.Radiobutton.__init__(self, self.frame)
        self.configure(kw)
        self.num = 1
        self.grid(row=1, column=1, padx=0, pady=0, sticky=EW)
        self.pal = []

    def _grid(self, **kw):
        self.frame.grid(kw)

    def _pack(self, **kw):
        self.frame.pack(kw)

    def _place(self, **kw):
        self.frame.place(kw)

    def _destroy(self):
        self.frame.destroy()

    def _forget(self):
        self.frame.forget()

    def _grid_forget(self):
        self.frame.grid_forget()

    def _pack_forget(self):
        self.frame.pack_forget()

    def _place_forget(self):
        self.frame.place_forget()

    def delwidget(self, widget):
        a = self.pal.index(widget)
        del(self.pal[a])
        widget.destroy()
        a = int(self.num) - 1
        self.num = 1
        if len(self.pal) > 0:
            for ww in self.pal:
                ww.grid(row=1, column=self.num + 1, padx=0, pady=0, sticky=EW)
                self.num += 1
    
    def add_button(self, type_=TTK, **kw):
        if type_ == TKINTER:
            b = Button(self.frame)
        else:
            b = ttk.Button(self.frame)
        b.configure(kw)
        b['width'] = 2
        self.pal.append(b)
        if self.num <= 20:
            b.grid(row=1, column=self.num + 1, rowspan=2, padx=0, pady=0, sticky=EW)
            self.num += 1
        return b

    def add_label(self, type_=TTK, **kw):
        if type_ == TKINTER:
            b = Label(self.frame)
        else:
            b = ttk.Label(self.frame)
        b.configure(kw)
        b['width'] = 2
        self.pal.append(b)
        if self.num <= 20:
            b.grid(row=1, column=self.num + 1, rowspan=2, padx=0, pady=0, sticky=EW)
            self.num += 1
        return b

    def add_checkbutton(self, type_=TTK, **kw):
        if type_ == TKINTER:
            b = Checkbutton(self.frame)
        else:
            b = ttk.Checkbutton(self.frame)
        b.configure(kw)
        b['width'] = 2
        self.pal.append(b)
        if self.num <= 20:
            b.grid(row=1, column=self.num + 1, rowspan=2, padx=0, pady=0, sticky=EW)
            self.num += 1
        return b

    def add_entry(self, type_=TTK, **kw):
        if type_ == TKINTER:
            b = Entry(self.frame)
        else:
            b = ttk.Entry(self.frame)
        b.configure(kw)
        b['width'] = 2
        self.pal.append(b)
        if self.num <= 20:
            b.grid(row=1, column=self.num + 1, rowspan=2, padx=0, pady=0, sticky=EW)
            self.num += 1
        return b

    def add_radiobutton(self, type_=TTK, **kw):
        if type_ == TKINTER:
            b = Radiobutton(self.frame)
        else:
            b = ttk.Radiobutton(self.frame)
        b.configure(kw)
        b['width'] = 2
        self.pal.append(b)
        if self.num <= 20:
            b.grid(row=1, column=self.num + 1, rowspan=2, padx=0, pady=0, sticky=EW)
            self.num += 1
        return b


# Classe du checkbutton avec commande
class Checkbuttonttk(ttk.Entry, ttk.Button, ttk.Label, ttk.Checkbutton, ttk.Radiobutton, ttk.Frame):

    def __init__(self, master=None, **kw):
        self.frame = ttk.Frame(master)
        ttk.Checkbutton.__init__(self, self.frame)
        self.configure(kw)
        self.num = 1
        self.grid(row=1, column=1, padx=0, pady=0, sticky=EW)
        self.pal = []

    def _grid(self, **kw):
        self.frame.grid(kw)

    def _pack(self, **kw):
        self.frame.pack(kw)

    def _place(self, **kw):
        self.frame.place(kw)

    def _destroy(self):
        self.frame.destroy()

    def _forget(self):
        self.frame.forget()

    def _grid_forget(self):
        self.frame.grid_forget()

    def _pack_forget(self):
        self.frame.pack_forget()

    def _place_forget(self):
        self.frame.place_forget()

    def delwidget(self, widget):
        a = self.pal.index(widget)
        del(self.pal[a])
        widget.destroy()
        a = int(self.num) - 1
        self.num = 1
        if len(self.pal) > 0:
            for ww in self.pal:
                ww.grid(row=1, column=self.num + 1, padx=0, pady=0, sticky=EW)
                self.num += 1
    
    def add_button(self, type_=TTK, **kw):
        if type_ == TKINTER:
            b = Button(self.frame)
        else:
            b = ttk.Button(self.frame)
        b.configure(kw)
        b['width'] = 2
        self.pal.append(b)
        if self.num <= 20:
            b.grid(row=1, column=self.num + 1, rowspan=2, padx=0, pady=0, sticky=EW)
            self.num += 1
        return b

    def add_label(self, type_=TTK, **kw):
        if type_ == TKINTER:
            b = Label(self.frame)
        else:
            b = ttk.Label(self.frame)
        b.configure(kw)
        b['width'] = 2
        self.pal.append(b)
        if self.num <= 20:
            b.grid(row=1, column=self.num + 1, rowspan=2, padx=0, pady=0, sticky=EW)
            self.num += 1
        return b

    def add_checkbutton(self, type_=TTK, **kw):
        if type_ == TKINTER:
            b = Checkbutton(self.frame)
        else:
            b = ttk.Checkbutton(self.frame)
        b.configure(kw)
        b['width'] = 2
        self.pal.append(b)
        if self.num <= 20:
            b.grid(row=1, column=self.num + 1, rowspan=2, padx=0, pady=0, sticky=EW)
            self.num += 1
        return b

    def add_entry(self, type_=TTK, **kw):
        if type_ == TKINTER:
            b = Entry(self.frame)
        else:
            b = ttk.Entry(self.frame)
        b.configure(kw)
        b['width'] = 2
        self.pal.append(b)
        if self.num <= 20:
            b.grid(row=1, column=self.num + 1, rowspan=2, padx=0, pady=0, sticky=EW)
            self.num += 1
        return b

    def add_radiobutton(self, type_=TTK, **kw):
        if type_ == TKINTER:
            b = Radiobutton(self.frame)
        else:
            b = ttk.Radiobutton(self.frame)
        b.configure(kw)
        b['width'] = 2
        self.pal.append(b)
        if self.num <= 20:
            b.grid(row=1, column=self.num + 1, rowspan=2, padx=0, pady=0, sticky=EW)
            self.num += 1
        return b


# Classe du label avec commande
class Labelttk(ttk.Entry, ttk.Button, ttk.Label, ttk.Checkbutton, ttk.Radiobutton, ttk.Frame):

    def __init__(self, master=None, **kw):
        self.frame = ttk.Frame(master)
        ttk.Label.__init__(self, self.frame)
        self.configure(kw)
        self.num = 1
        self.grid(row=1, column=1, padx=0, pady=0, sticky=EW)
        self.pal = []

    def _grid(self, **kw):
        self.frame.grid(kw)

    def _pack(self, **kw):
        self.frame.pack(kw)

    def _place(self, **kw):
        self.frame.place(kw)

    def _destroy(self):
        self.frame.destroy()

    def _forget(self):
        self.frame.forget()

    def _grid_forget(self):
        self.frame.grid_forget()

    def _pack_forget(self):
        self.frame.pack_forget()

    def _place_forget(self):
        self.frame.place_forget()

    def delwidget(self, widget):
        a = self.pal.index(widget)
        del(self.pal[a])
        widget.destroy()
        a = int(self.num) - 1
        self.num = 1
        if len(self.pal) > 0:
            for ww in self.pal:
                ww.grid(row=1, column=self.num + 1, padx=0, pady=0, sticky=EW)
                self.num += 1
    
    def add_button(self, type_=TTK, **kw):
        if type_ == TKINTER:
            b = Button(self.frame)
        else:
            b = ttk.Button(self.frame)
        b.configure(kw)
        b['width'] = 2
        self.pal.append(b)
        if self.num <= 20:
            b.grid(row=1, column=self.num + 1, rowspan=2, padx=0, pady=0, sticky=EW)
            self.num += 1
        return b

    def add_label(self, type_=TTK, **kw):
        if type_ == TKINTER:
            b = Label(self.frame)
        else:
            b = ttk.Label(self.frame)
        b.configure(kw)
        b['width'] = 2
        self.pal.append(b)
        if self.num <= 20:
            b.grid(row=1, column=self.num + 1, rowspan=2, padx=0, pady=0, sticky=EW)
            self.num += 1
        return b

    def add_checkbutton(self, type_=TTK, **kw):
        if type_ == TKINTER:
            b = Checkbutton(self.frame)
        else:
            b = ttk.Checkbutton(self.frame)
        b.configure(kw)
        b['width'] = 2
        self.pal.append(b)
        if self.num <= 20:
            b.grid(row=1, column=self.num + 1, rowspan=2, padx=0, pady=0, sticky=EW)
            self.num += 1
        return b

    def add_entry(self, type_=TTK, **kw):
        if type_ == TKINTER:
            b = Entry(self.frame)
        else:
            b = ttk.Entry(self.frame)
        b.configure(kw)
        b['width'] = 2
        self.pal.append(b)
        if self.num <= 20:
            b.grid(row=1, column=self.num + 1, rowspan=2, padx=0, pady=0, sticky=EW)
            self.num += 1
        return b

    def add_radiobutton(self, type_=TTK, **kw):
        if type_ == TKINTER:
            b = Radiobutton(self.frame)
        else:
            b = ttk.Radiobutton(self.frame)
        b.configure(kw)
        b['width'] = 2
        self.pal.append(b)
        if self.num <= 20:
            b.grid(row=1, column=self.num + 1, rowspan=2, padx=0, pady=0, sticky=EW)
            self.num += 1
        return b


# Classe du radiobutton avec commande
class Buttonttk(ttk.Entry, ttk.Button, ttk.Label, ttk.Checkbutton, ttk.Radiobutton, ttk.Frame):

    def __init__(self, master=None, **kw):
        self.frame = ttk.Frame(master)
        ttk.Button.__init__(self, self.frame)
        self.configure(kw)
        self.num = 1
        self.grid(row=1, column=1, padx=0, pady=0, sticky=EW)
        self.pal = []

    def _grid(self, **kw):
        self.frame.grid(kw)

    def _pack(self, **kw):
        self.frame.pack(kw)

    def _place(self, **kw):
        self.frame.place(kw)

    def _destroy(self):
        self.frame.destroy()

    def _forget(self):
        self.frame.forget()

    def _grid_forget(self):
        self.frame.grid_forget()

    def _pack_forget(self):
        self.frame.pack_forget()

    def _place_forget(self):
        self.frame.place_forget()

    def delwidget(self, widget):
        a = self.pal.index(widget)
        del(self.pal[a])
        widget.destroy()
        a = int(self.num) - 1
        self.num = 1
        if len(self.pal) > 0:
            for ww in self.pal:
                ww.grid(row=1, column=self.num + 1, padx=0, pady=0, sticky=EW)
                self.num += 1
    
    def add_button(self, type_=TTK, **kw):
        if type_ == TKINTER:
            b = Button(self.frame)
        else:
            b = ttk.Button(self.frame)
        b.configure(kw)
        b['width'] = 2
        self.pal.append(b)
        if self.num <= 20:
            b.grid(row=1, column=self.num + 1, rowspan=2, padx=0, pady=0, sticky=EW)
            self.num += 1
        return b

    def add_label(self, type_=TTK, **kw):
        if type_ == TKINTER:
            b = Label(self.frame)
        else:
            b = ttk.Label(self.frame)
        b.configure(kw)
        b['width'] = 2
        self.pal.append(b)
        if self.num <= 20:
            b.grid(row=1, column=self.num + 1, rowspan=2, padx=0, pady=0, sticky=EW)
            self.num += 1
        return b

    def add_checkbutton(self, type_=TTK, **kw):
        if type_ == TKINTER:
            b = Checkbutton(self.frame)
        else:
            b = ttk.Checkbutton(self.frame)
        b.configure(kw)
        b['width'] = 2
        self.pal.append(b)
        if self.num <= 20:
            b.grid(row=1, column=self.num + 1, rowspan=2, padx=0, pady=0, sticky=EW)
            self.num += 1
        return b

    def add_entry(self, type_=TTK, **kw):
        if type_ == TKINTER:
            b = Entry(self.frame)
        else:
            b = ttk.Entry(self.frame)
        b.configure(kw)
        b['width'] = 2
        self.pal.append(b)
        if self.num <= 20:
            b.grid(row=1, column=self.num + 1, rowspan=2, padx=0, pady=0, sticky=EW)
            self.num += 1
        return b

    def add_radiobutton(self, type_=TTK, **kw):
        if type_ == TKINTER:
            b = Radiobutton(self.frame)
        else:
            b = ttk.Radiobutton(self.frame)
        b.configure(kw)
        b['width'] = 2
        self.pal.append(b)
        if self.num <= 20:
            b.grid(row=1, column=self.num + 1, rowspan=2, padx=0, pady=0, sticky=EW)
            self.num += 1
        return b

######################################################
#                                       ____________     |              /                                          #
#                                                       |                        |            /                                            #
#                                                       |                        |          /                                              #
#                                                       |                        |        /                                                #
#                                                       |                        |      /                                                  #
#                                                       |                        |    /                                                    #
#                                                       |                        |  /                                                      #
#                                                       |                        |/                                                        #
#                                                       |                        |\                                                        #
#                                                       |                        |  \                                                      #
#                                                       |                        |    \                                                    #
#                                                       |                        |      \                                                  #
#                                                       |                        |        \                                                #
#                                                       |                        |          \                                              #
#                                                       |                        |            \                                            #
#                                                       |                        |              \                                          #
######################################################


# Classe de l'entrée
class Entrytk(Entry, Button, Label, Checkbutton, Radiobutton, Frame):

    def __init__(self, master=None, **kw):
        self.frame = Frame(master)
        Entry.__init__(self, self.frame)
        self.config(kw)
        self.num = 1
        self.grid(row=1, column=1, padx=0, pady=0, sticky=EW)
        self.pal = []

    def _grid(self, **kw):
        self.frame.grid(kw)

    def _pack(self, **kw):
        self.frame.pack(kw)

    def _place(self, **kw):
        self.frame.place(kw)

    def _destroy(self):
        self.frame.destroy()

    def _forget(self):
        self.frame.forget()

    def _grid_forget(self):
        self.frame.grid_forget()

    def _pack_forget(self):
        self.frame.pack_forget()

    def _place_forget(self):
        self.frame.place_forget()

    def delwidget(self, widget):
        a = self.pal.index(widget)
        del(self.pal[a])
        widget.destroy()
        a = int(self.num) - 1
        self.num = 1
        if len(self.pal) > 0:
            for ww in self.pal:
                ww.grid(row=1, column=self.num + 1, padx=0, pady=0, sticky=EW)
                self.num += 1

    def add_button(self, type_=TKINTER, **kw):
        if type_ == TTK:
            b = ttk.Button(self.frame)
        else:
            b = Button(self.frame)
        b.configure(kw)
        b['width'] = 2
        self.pal.append(b)
        if self.num <= 20:
            b.grid(row=1, column=self.num + 1, rowspan=2, padx=0, pady=0, sticky=EW)
            self.num += 1
        return b

    def add_label(self, type_=TKINTER, **kw):
        if type_ == TTK:
            b = ttk.Label(self.frame)
        else:
            b = Label(self.frame)
        b.configure(kw)
        b['width'] = 2
        self.pal.append(b)
        if self.num <= 20:
            b.grid(row=1, column=self.num + 1, rowspan=2, padx=0, pady=0, sticky=EW)
            self.num += 1
        return b

    def add_checkbutton(self, type_=TKINTER, **kw):
        if type_ == TTK:
            b = ttk.Checkbutton(self.frame)
        else:
            b = Checkbutton(self.frame)
        b.configure(kw)
        b['width'] = 2
        self.pal.append(b)
        if self.num <= 20:
            b.grid(row=1, column=self.num + 1, rowspan=2, padx=0, pady=0, sticky=EW)
            self.num += 1
        return b

    def add_entry(self, type_=TKINTER, **kw):
        if type_ == TTK:
            b = ttk.Entry(self.frame)
        else:
            b = Entry(self.frame)
        b.configure(kw)
        b['width'] = 2
        self.pal.append(b)
        if self.num <= 20:
            b.grid(row=1, column=self.num + 1, rowspan=2, padx=0, pady=0, sticky=EW)
            self.num += 1
        return b

    def add_radiobutton(self, type_=TKINTER, **kw):
        if type_ == TTK:
            b = ttk.Radiobutton(self.frame)
        else:
            b = Radiobutton(self.frame)
        b.configure(kw)
        b['width'] = 2
        self.pal.append(b)
        if self.num <= 20:
            b.grid(row=1, column=self.num + 1, rowspan=2, padx=0, pady=0, sticky=EW)
            self.num += 1
        return b

    def scrolled(self, type_=TKINTER, **kw):
        if type_ == TTK:
            b = ttk.Scrollbar(self.frame)
        else:
            b = Scrollbar(self.frame)
        try:
            b.config(kw)
            b.config(orient=HORIZONTAL)
        finally:
            b.configure(kw)
            b.configure(orient=HORIZONTAL)
        try:
            b['width'] = 10
        except:
            pass
        self['xscrollcommand'] = b.set
        self.bar = b
        b.grid(row=2, column=1, sticky=EW)


# Classe du label1
class Labeltk(Entry, Button, Label, Checkbutton, Radiobutton, Frame):

    def __init__(self, master=None, **kw):
        self.frame = Frame(master)
        Label.__init__(self, self.frame)
        self.config(kw)
        self.num = 1
        self.grid(row=1, column=1, padx=0, pady=0, sticky=EW)
        self.pal = []

    def _grid(self, **kw):
        self.frame.grid(kw)

    def _pack(self, **kw):
        self.frame.pack(kw)

    def _place(self, **kw):
        self.frame.place(kw)

    def _destroy(self):
        self.frame.destroy()

    def _forget(self):
        self.frame.forget()

    def _grid_forget(self):
        self.frame.grid_forget()

    def _pack_forget(self):
        self.frame.pack_forget()

    def _place_forget(self):
        self.frame.place_forget()

    def delwidget(self, widget):
        a = self.pal.index(widget)
        del(self.pal[a])
        widget.destroy()
        a = int(self.num) - 1
        self.num = 1
        if len(self.pal) > 0:
            for ww in self.pal:
                ww.grid(row=1, column=self.num + 1, padx=0, pady=0, sticky=EW)
                self.num += 1

    def add_button(self, type_=TKINTER, **kw):
        if type_ == TTK:
            b = ttk.Button(self.frame)
        else:
            b = Button(self.frame)
        b.configure(kw)
        b['width'] = 2
        self.pal.append(b)
        if self.num <= 20:
            b.grid(row=1, column=self.num + 1, rowspan=2, padx=0, pady=0, sticky=EW)
            self.num += 1
        return b

    def add_label(self, type_=TKINTER, **kw):
        if type_ == TTK:
            b = ttk.Label(self.frame)
        else:
            b = Label(self.frame)
        b.configure(kw)
        b['width'] = 2
        self.pal.append(b)
        if self.num <= 20:
            b.grid(row=1, column=self.num + 1, rowspan=2, padx=0, pady=0, sticky=EW)
            self.num += 1
        return b

    def add_checkbutton(self, type_=TKINTER, **kw):
        if type_ == TTK:
            b = ttk.Checkbutton(self.frame)
        else:
            b = Checkbutton(self.frame)
        b.configure(kw)
        b['width'] = 2
        self.pal.append(b)
        if self.num <= 20:
            b.grid(row=1, column=self.num + 1, rowspan=2, padx=0, pady=0, sticky=EW)
            self.num += 1
        return b

    def add_entry(self, type_=TKINTER, **kw):
        if type_ == TTK:
            b = ttk.Entry(self.frame)
        else:
            b = Entry(self.frame)
        b.configure(kw)
        b['width'] = 2
        self.pal.append(b)
        if self.num <= 20:
            b.grid(row=1, column=self.num + 1, rowspan=2, padx=0, pady=0, sticky=EW)
            self.num += 1
        return b

    def add_radiobutton(self, type_=TKINTER, **kw):
        if type_ == TTK:
            b = ttk.Radiobutton(self.frame)
        else:
            b = Radiobutton(self.frame)
        b.configure(kw)
        b['width'] = 2
        self.pal.append(b)
        if self.num <= 20:
            b.grid(row=1, column=self.num + 1, rowspan=2, padx=0, pady=0, sticky=EW)
            self.num += 1
        return b


# Classe du button1
class Buttontk(Entry, Button, Label, Checkbutton, Radiobutton, Frame):

    def __init__(self, master=None, **kw):
        self.frame = Frame(master)
        Button.__init__(self, self.frame)
        self.config(kw)
        self.num = 1
        self.grid(row=1, column=1, padx=0, pady=0, sticky=EW)
        self.pal = []

    def _grid(self, **kw):
        self.frame.grid(kw)

    def _pack(self, **kw):
        self.frame.pack(kw)

    def _place(self, **kw):
        self.frame.place(kw)

    def _destroy(self):
        self.frame.destroy()

    def _forget(self):
        self.frame.forget()

    def _grid_forget(self):
        self.frame.grid_forget()

    def _pack_forget(self):
        self.frame.pack_forget()

    def _place_forget(self):
        self.frame.place_forget()

    def delwidget(self, widget):
        a = self.pal.index(widget)
        del(self.pal[a])
        widget.destroy()
        a = int(self.num) - 1
        self.num = 1
        if len(self.pal) > 0:
            for ww in self.pal:
                ww.grid(row=1, column=self.num + 1, padx=0, pady=0, sticky=EW)
                self.num += 1

    def add_button(self, type_=TKINTER, **kw):
        if type_ == TTK:
            b = ttk.Button(self.frame)
        else:
            b = Button(self.frame)
        b.configure(kw)
        b['width'] = 2
        self.pal.append(b)
        if self.num <= 20:
            b.grid(row=1, column=self.num + 1, rowspan=2, padx=0, pady=0, sticky=EW)
            self.num += 1
        return b

    def add_label(self, type_=TKINTER, **kw):
        if type_ == TTK:
            b = ttk.Label(self.frame)
        else:
            b = Label(self.frame)
        b.configure(kw)
        b['width'] = 2
        self.pal.append(b)
        if self.num <= 20:
            b.grid(row=1, column=self.num + 1, rowspan=2, padx=0, pady=0, sticky=EW)
            self.num += 1
        return b

    def add_checkbutton(self, type_=TKINTER, **kw):
        if type_ == TTK:
            b = ttk.Checkbutton(self.frame)
        else:
            b = Checkbutton(self.frame)
        b.configure(kw)
        b['width'] = 2
        self.pal.append(b)
        if self.num <= 20:
            b.grid(row=1, column=self.num + 1, rowspan=2, padx=0, pady=0, sticky=EW)
            self.num += 1
        return b

    def add_entry(self, type_=TKINTER, **kw):
        if type_ == TTK:
            b = ttk.Entry(self.frame)
        else:
            b = Entry(self.frame)
        b.configure(kw)
        b['width'] = 2
        self.pal.append(b)
        if self.num <= 20:
            b.grid(row=1, column=self.num + 1, rowspan=2, padx=0, pady=0, sticky=EW)
            self.num += 1
        return b

    def add_radiobutton(self, type_=TKINTER, **kw):
        if type_ == TTK:
            b = ttk.Radiobutton(self.frame)
        else:
            b = Radiobutton(self.frame)
        b.configure(kw)
        b['width'] = 2
        self.pal.append(b)
        if self.num <= 20:
            b.grid(row=1, column=self.num + 1, rowspan=2, padx=0, pady=0, sticky=EW)
            self.num += 1
        return b


# Classe du checkbutton1
class Checkbuttontk(Entry, Button, Label, Checkbutton, Radiobutton, Frame):

    def __init__(self, master=None, **kw):
        self.frame = Frame(master)
        Checkbutton.__init__(self, self.frame)
        self.config(kw)
        self.num = 1
        self.grid(row=1, column=1, padx=0, pady=0, sticky=EW)
        self.pal = []

    def _grid(self, **kw):
        self.frame.grid(kw)

    def _pack(self, **kw):
        self.frame.pack(kw)

    def _place(self, **kw):
        self.frame.place(kw)

    def _destroy(self):
        self.frame.destroy()

    def _forget(self):
        self.frame.forget()

    def _grid_forget(self):
        self.frame.grid_forget()

    def _pack_forget(self):
        self.frame.pack_forget()

    def _place_forget(self):
        self.frame.place_forget()

    def delwidget(self, widget):
        a = self.pal.index(widget)
        del(self.pal[a])
        widget.destroy()
        a = int(self.num) - 1
        self.num = 1
        if len(self.pal) > 0:
            for ww in self.pal:
                ww.grid(row=1, column=self.num + 1, padx=0, pady=0, sticky=EW)
                self.num += 1

    def add_button(self, type_=TKINTER, **kw):
        if type_ == TTK:
            b = ttk.Button(self.frame)
        else:
            b = Button(self.frame)
        b.configure(kw)
        b['width'] = 2
        self.pal.append(b)
        if self.num <= 20:
            b.grid(row=1, column=self.num + 1, rowspan=2, padx=0, pady=0, sticky=EW)
            self.num += 1
        return b

    def add_label(self, type_=TKINTER, **kw):
        if type_ == TTK:
            b = ttk.Label(self.frame)
        else:
            b = Label(self.frame)
        b.configure(kw)
        b['width'] = 2
        self.pal.append(b)
        if self.num <= 20:
            b.grid(row=1, column=self.num + 1, rowspan=2, padx=0, pady=0, sticky=EW)
            self.num += 1
        return b

    def add_checkbutton(self, type_=TKINTER, **kw):
        if type_ == TTK:
            b = ttk.Checkbutton(self.frame)
        else:
            b = Checkbutton(self.frame)
        b.configure(kw)
        b['width'] = 2
        self.pal.append(b)
        if self.num <= 20:
            b.grid(row=1, column=self.num + 1, rowspan=2, padx=0, pady=0, sticky=EW)
            self.num += 1
        return b

    def add_entry(self, type_=TKINTER, **kw):
        if type_ == TTK:
            b = ttk.Entry(self.frame)
        else:
            b = Entry(self.frame)
        b.configure(kw)
        b['width'] = 2
        self.pal.append(b)
        if self.num <= 20:
            b.grid(row=1, column=self.num + 1, rowspan=2, padx=0, pady=0, sticky=EW)
            self.num += 1
        return b

    def add_radiobutton(self, type_=TKINTER, **kw):
        if type_ == TTK:
            b = ttk.Radiobutton(self.frame)
        else:
            b = Radiobutton(self.frame)
        b.configure(kw)
        b['width'] = 2
        self.pal.append(b)
        if self.num <= 20:
            b.grid(row=1, column=self.num + 1, rowspan=2, padx=0, pady=0, sticky=EW)
            self.num += 1
        return b


# Classe du radiobutton1
class Radiobuttontk(Entry, Button, Label, Checkbutton, Radiobutton, Frame):

    def __init__(self, master=None, **kw):
        self.frame = Frame(master)
        Radiobutton.__init__(self, self.frame)
        self.config(kw)
        self.num = 1
        self.grid(row=1, column=1, padx=0, pady=0, sticky=EW)
        self.pal = []

    def _grid(self, **kw):
        self.frame.grid(kw)

    def _pack(self, **kw):
        self.frame.pack(kw)

    def _place(self, **kw):
        self.frame.place(kw)

    def _destroy(self):
        self.frame.destroy()

    def _forget(self):
        self.frame.forget()

    def _grid_forget(self):
        self.frame.grid_forget()

    def _pack_forget(self):
        self.frame.pack_forget()

    def _place_forget(self):
        self.frame.place_forget()

    def delwidget(self, widget):
        a = self.pal.index(widget)
        del(self.pal[a])
        widget.destroy()
        a = int(self.num) - 1
        self.num = 1
        if len(self.pal) > 0:
            for ww in self.pal:
                ww.grid(row=1, column=self.num + 1, padx=0, pady=0, sticky=EW)
                self.num += 1

    def add_button(self, type_=TKINTER, **kw):
        if type_ == TTK:
            b = ttk.Button(self.frame)
        else:
            b = Button(self.frame)
        b.configure(kw)
        b['width'] = 2
        self.pal.append(b)
        if self.num <= 20:
            b.grid(row=1, column=self.num + 1, rowspan=2, padx=0, pady=0, sticky=EW)
            self.num += 1
        return b

    def add_label(self, type_=TKINTER, **kw):
        if type_ == TTK:
            b = ttk.Label(self.frame)
        else:
            b = Label(self.frame)
        b.configure(kw)
        b['width'] = 2
        self.pal.append(b)
        if self.num <= 20:
            b.grid(row=1, column=self.num + 1, rowspan=2, padx=0, pady=0, sticky=EW)
            self.num += 1
        return b

    def add_checkbutton(self, type_=TKINTER, **kw):
        if type_ == TTK:
            b = ttk.Checkbutton(self.frame)
        else:
            b = Checkbutton(self.frame)
        b.configure(kw)
        b['width'] = 2
        self.pal.append(b)
        if self.num <= 20:
            b.grid(row=1, column=self.num + 1, rowspan=2, padx=0, pady=0, sticky=EW)
            self.num += 1
        return b

    def add_entry(self, type_=TKINTER, **kw):
        if type_ == TTK:
            b = ttk.Entry(self.frame)
        else:
            b = Entry(self.frame)
        b.configure(kw)
        b['width'] = 2
        self.pal.append(b)
        if self.num <= 20:
            b.grid(row=1, column=self.num + 1, rowspan=2, padx=0, pady=0, sticky=EW)
            self.num += 1
        return b

    def add_radiobutton(self, type_=TKINTER, **kw):
        if type_ == TTK:
            b = ttk.Radiobutton(self.frame)
        else:
            b = Radiobutton(self.frame)
        b.configure(kw)
        b['width'] = 2
        self.pal.append(b)
        if self.num <= 20:
            b.grid(row=1, column=self.num + 1, rowspan=2, padx=0, pady=0, sticky=EW)
            self.num += 1
        return b


# Classe du conteneur
class Conteneur(ttk.Frame, Canvas):

    def __init__(self, master=None, style=TTK, **kw):
        Frame.__init__(self, master)
        self.configure(kw)

        self.can = Canvas(self, width=self['width'], height=self['height'], scrollregion=(0, 0, self['width'], self['height']))

        if style == TTK:
            self.yb = ttk.Scrollbar(self, command=self.can.yview)
            self.xb = ttk.Scrollbar(self, command=self.can.xview, orient=HORIZONTAL)
        elif style == TKINTER:
            self.yb = Scrollbar(self, command=self.can.yview)
            self.xb = Scrollbar(self, command=self.can.xview, orient=HORIZONTAL)
        self.can['xscrollcommand'] = self.xb.set; self.can['yscrollcommand'] = self.yb.set

        self.can.grid(row=1, column=1, sticky=EW)
        self.yb.grid(row=1, column=2, sticky=NS)
        self.xb.grid(row=2, column=1, sticky=EW, pady=15)

        self.y = 0
        self.x = 0
        self.pal_numy = []
        self.pal_numx = []
        self.pal_wdt = []
        self.pal_dw = []
        self.count = 0
        self.countWidget = []

        self.can.bind_all('<MouseWheel>', self.wheel)

    def set_region(self):
        self.a1_ = 0
        self.x, self.y = 0, 0
        self.widget.after(150, self.recuperer)

    def recuperer(self):
        if self.a1_ < len(self.pal_dw):
            self.x += Get(self.pal_dw[self.a1_]).x()
            self.y += Get(self.pal_dw[self.a1_]).y()
            self.a1_ += 1
            self.can['scrollregion'] = (0, 0, self.x, self.y)

    def conf(self, **kw):
        self.config(**kw)
        self.can.config(**kw)

    def add_widget(self, widget):
        self.countWidget = widget
        self.count = 0
        self.addNone1()
    
    def addNone1(self):
        self.add(self.countWidget[0])
        if self.count < len(self.countWidget):
            self.widget.after(500, self.addNone1)
    
    def add(self, widget):
        self.widget = widget
        self.widget.place(x=-1000, y=-1000)
        self.widget.after(150, self.recuper)
        self.count += 1
        del(self.countWidget[0])
        return widget

    def recuper(self):
        x, y = Get(self.widget).x(), Get(self.widget).y()
        self.widget.place_forget()
        self.y += y

        if x > self.x:
            self.x = x

        self.can['scrollregion'] = (0, 0, self.x + 5, self.y + 5)
        self.pal_wdt.append(self.can.create_window(x / 2, self.y - y / 2, window=self.widget))
        self.pal_dw.append(self.widget)
        self.pal_numy.append(y)
        self.pal_numx.append(x)

    def del_widget(self, widget):
        if widget in self.pal_dw:
            a = self.pal_dw.index(widget)
            self.can.delete(self.pal_wdt[a])
            widget.destroy()
            if len(self.pal_wdt) > 0:
                b = list(self.pal_wdt[a:])
                for ww in b:
                    self.can.move(ww, 0, -self.pal_numy[a])
            self.y -= self.pal_numy[a]
            del(self.pal_numy[a])
            del(self.pal_numx[a])
            if len(self.pal_numx) > 0:
                self.x = list(self.pal_numx)
                self.x.sort()
                self.x = self.x[len(self.x) - 1]
            else:
                self.x = 0
            self.can['scrollregion'] = (0, 0, self.x, self.y)

    def remove_widget(self, widget):
        if widget in self.pal_dw:
            a = self.pal_dw.index(widget)
            self.can.delete(self.pal_wdt[a])
            if len(self.pal_wdt) > 0:
                b = list(self.pal_wdt[a:])
                for ww in b:
                    self.can.move(ww, 0, -self.pal_numy[a])
            self.y -= self.pal_numy[a]
            del(self.pal_numy[a])
            del(self.pal_numx[a])
            if len(self.pal_numx) > 0:
                self.x = list(self.pal_numx)
                self.x.sort()
                self.x = self.x[len(self.x) - 1]
            else:
                self.x = 0
            self.can['scrollregion'] = (0, 0, self.x, self.y)
        return widget

    def del_all(self):
        self.can.delete(ALL)
        del(self.pal_wdt[:])
        for ww in self.pal_dw:
            ww.destroy()
        del(self.pal_dw[:])
        del(self.pal_numx[:])
        del(self.pal_numy[:])
        self.x = 0
        self.y = 0
        self.can['scrollregion'] = (0, 0, self.x, self.y)

    def remove_all(self):
        self.can.delete(ALL)
        del(self.pal_wdt[:])
        p = []
        for ww in self.pal_dw:
            p.append(ww)
        del(self.pal_dw[:])
        del(self.pal_numx[:])
        del(self.pal_numy[:])
        self.x = 0
        self.y = 0
        self.can['scrollregion'] = (0, 0, self.x, self.y)
        return p

    def wheel(self, event):
        self.can.yview_scroll(int(-1 * (event.delta / 120)), 'unit')
        self.can.moveto(self.yb.get()[0])


# classe du teste
class Teste(object):

    def __init__(self):
        self.pal1 = list((Entryttk, Labelttk, Buttonttk, Checkbuttonttk, Radiobuttonttk, Entrytk, Labeltk, Buttontk, Checkbuttontk, Radiobuttontk))
        can = Tk()
        can.title('teste des widget')
        self.lab1 = ttk.LabelFrame(can, text='Widgets ttk et tk', labelanchor=N, width=250)
        self.lab1.grid(row=1, column=1, pady=10, padx=2)

        for ww in self.pal1:
            a = ww(self.lab1)
            try:
                a.insert(END, str(a._name))
                a.scrolled(command=a.xview)
            except:
                a['text'] = str(a._name)
            a['width'] = 20
            a.add_button(TTK, text='B1')
            a.add_button(TKINTER, text='B2')
            a.add_label(TTK, text='L1')
            a.add_label(TKINTER, text='L2')
            a.add_checkbutton(TTK, text='C1')
            a.add_checkbutton(TKINTER, text='C2')
            a.add_radiobutton(TTK, text='R1')
            a.add_radiobutton(TKINTER, text='R2')
            a.add_entry(TTK)
            a.pal[len(a.pal) - 1].insert(END, 'E1')
            a.add_entry(TKINTER)
            a.pal[len(a.pal) - 1].insert(END, 'E2')

            a._grid()
        self.lab1.mainloop()


if __name__ == '__main__':
    Teste()
    
