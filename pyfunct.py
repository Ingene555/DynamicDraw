
import tkinter as tk
import os
from tkinter.colorchooser import askcolor
import pickle as pkl
from datetime import datetime
import ctypes

#Variables
NO='no'
NC='nc'
NE='ne'
SO='so'
SC='sc'
SE='se'
CO='co'
CE='ce'
CERCLE='cercle'
CARRE='carre'
POLYGONE='polygone'
ARC='arc'
LIGNE='ligne'
TEXTE='texte'
FENETRE='fenetre'
LISTE='liste'
ELEMENT='element'
DEVANT='first'
DERRIER='last'
TOUT='both'
PLUS='plus'
BARRE='barre'
AUCUN='aucun'
TEXTE='texte'
VAR='var'
VIDE='\t\t\t\t\t'
SELECTION='selection'
FOCUS='focus'

#Classe du get
class Get(object):
    def __init__(self, master):
        self.master=master

    def x(self):
        return self.master.winfo_width()

    def y(self):
        return self.master.winfo_height()

    def width(self):
        return eval(str(self.master['width']))

    def height(self):
        return eval(str(self.master['height']))

#Classe du flash
class Flash(object):
    def __init__(self, master, coul='grey', bg=None, temps=1.5, fg=None):
        self.master=master
        self.coul=coul
        self.temps=int(temps*1000)
        if bg:
            self.cb=bg
        else:
            self.cb=master['background']
        if fg:
            self.fg=[master['fg'], fg]
        else:
            self.fg=None
        self.p=[self.coul, self.cb]
        self.a=1
        self.b=0
        self.c=int(100)

        self.flash()

    def flash(self):
        self.a+=1
        self.master['background']=self.p[self.a%2]
        if self.fg:
            self.master['fg']=self.fg[self.a%2]
        self.b+=self.c
        if self.b<=self.temps:
            self.master.after(self.c, self.flash)
        else:
            self.master['background']=self.cb
            if self.fg:
                self.master['fg']=self.fg[0]

#Classe de l'active
class ActiveLeave(object):
    def __init__(self, widget, bg = 'blue', fg = 'dark grey', bordure = 0):
        self.wdt = widget
        self.bg_ = widget.cget('background')
        self.bg = bg
        self.fg_ = widget.cget('foreground')
        self.fg = fg
        self.bd_=widget.cget('bd')
        self.bd = bordure
        self.con_ = widget.cget('highlightcolor')
        Assign(self.wdt, self.leave, ['Leave'])
        Assign(self.wdt, self.enter, ['Enter'])

    def leave(self, event = None):
        self.wdt.config(bg = self.bg_, fg = self.fg_, bd = self.bd_, highlightcolor = self.con_)

    def enter(self, event = None):
        self.wdt.config(bg = self.bg, fg = self.fg, bd = self.bd, highlightcolor = self.con_)

#Classe du temps
class Temps():
    def __init__(self):
        self.temps_ = datetime.today()
        self.annee=self.temps_.year
        self.month=self.temps_.month
        self.j=self.temps_.day
        self.h=self.temps_.hour
        self.m=self.temps_.minute
        self.s=self.temps_.second
        self.ms=self.temps_.microsecond
    def temps(self):
        temps=('{}.{}.{} {}:{} {}'.format(self.jour(),self.mois(),self.an(),self.heure(),self.minute(),self.seconde()))
        return temps
    def an(self):
        return self.annee
    def mois(self, n=True):
        dictio={1:'January', 2:'Febuary', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'August', 9:'September',
                10:'October', 11:'November', 12:'December'}
        if n is False:
            return dictio[eval(str(self.month))]
        elif n is True:
            return self.month
    def jour(self, n=True):
        liste=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        if n is False:
            return liste[self.temps_.weekday()]
        elif n is True:
            return self.j
    def heure(self):
        return self.h
    def minute(self):
        return self.m
    def seconde(self):
        return self.s
    def micros(self):
        return self.ms

#Classe de lecture
class Lire(object):
    def __init__(self,fichier=None):
        f=open(fichier,'rb')
        self.t=''
        while True:
            try:
                self.t+=str(pkl.load(f))
            except:
                f.close()
                break
        self.assigne()
    def assigne(self):
        return self.t

class Ecrire(object):
    def __init__(self,fichier=None,info=None):
        f=open(fichier,'wb')
        pkl.dump(info,f)
        f.close()

#Classe menu contextul
class Popup(tk.Menu):
    def __init__(self,master,bind=['Button-3'], *cnf, **kwargs):
        tk.Menu.__init__(self,master, *cnf, **kwargs)
        Assign(master,self.popup,bind)
    def popup(self, event):
        try:
            self.tk_popup(event.x_root, event.y_root, 0)
        finally:
            self.grab_release()
        self.eventX=event.x
        self.eventY=event.y

#Classe de selection
class Select(object):
    def __init__(self,master, x, y, width=5, height=5, object=None, kind='selection'):
        self.master=master
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.obj=object
        self.kind=kind
        self.selector=None
        self.listSelector=[]
    
    def setSelector(self):
        if self.selector:
            self.master.delete(self.selector)
            self.selector=None
        if len(self.listSelector)>0:
            for ww in self.listSelector:
                self.master.delete(ww)
                self.listSelector=[]
        x=self.x;y=self.y
        w=self.width/2;h=self.height/2
        if self.kind==SELECTION:
            self.selector=self.master.create_polygon(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                                                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                     fill='white', outline=COLORS['--dark-blue'])
        elif self.kind==FOCUS:
            self.listSelector.append(self.master.create_oval(0, 0, 0, 0, outline=COLORS['--dark-orange']))
            self.listSelector.append(self.master.create_oval(0, 0, 0, 0, outline=COLORS['--light-color']))
            self.listSelector.append(self.master.create_oval(0, 0, 0, 0, outline=COLORS['--dark-orange']))
    
    def setCoords(self, x=None, y=None):
        a=x-self.x if x else 0
        b=y-self.y if y else 0
        if self.kind==SELECTION:
            self.master.move(self.selector, a, b)
            self.master.lift(self.selector)
        elif self.kind==FOCUS:
            for ww in self.listSelector:
                self.master.move(ww, a, b)
                self.master.lift(ww)
        self.x+=a
        self.y+=b
    
    def setSize(self, width=None, height=None):
        w=width/2 if width else self.width/2
        h=height/2 if height else self.height/2
        x=self.x
        y=self.y
        if self.kind==SELECTION:
            self.master.coords(self.selector, x-w, y-h-5, x+w+5, y-h-5, x+w+5, y+h+5, x-w-5, y+h+5, x-w-5, y-h, 
                                                     x-w-3, y-h, x-w-3, y+h+3, x+w+3, y+h+3, x+w+3, y-h-3, x-w, y-h-3)
        elif self.kind==FOCUS:
            self.master.coords(self.listSelector[0], x-w-4, y-h-4, x+w+4, y+h+4)
            self.master.coords(self.listSelector[1], x-w-3, y-h-3, x+w+3, y+h+3)
            self.master.coords(self.listSelector[2], x-w-2, y-h-2, x+w+2, y+h+2)
            self.master.lift(self.listSelector[0])
            self.master.lift(self.listSelector[1])
            self.master.lift(self.listSelector[2])

    def setStat(self, stat='normal'):
        if self.kind==SELECTION:
            self.master.itemconfig(self.selector, stat=stat)
        elif self.kind==FOCUS:
            for ww in self.listSelector:
                self.master.itemconfig(ww, stat=stat)
    
    def destroy(self):
        if self.kind==SELECTION:
            self.master.delete(self.selector)
        elif self.kind==FOCUS:
            for ww in self.listSelector:
                self.master.delete(ww)
    
    


#Classe de message
class Message(object):
    def __init__(self,label,type_=(TEXTE,None),message='☺',temps=3.5,fond='SystemButtonFace',
                coul='black',messagefinal=''):
        self.label=label
        self.type0=type_[0]
        self.type1=type_[1]
        self.msg1=message
        self.temps=temps
        self.fond=fond
        self.coul=coul
        self.msg2=messagefinal
        self.fondi=label['bg']
        self.couli=label['fg']
    def affiche(self):
        if self.type0==TEXTE:
            self.label['text']=self.msg1
        else:self.type1.set(self.msg1)
        self.label.config(bg=self.fond, fg=self.coul)
        self.label.after(int(self.temps*1000), self.initial)
    def initial(self):
        if self.type0==TEXTE:
            self.label['text']=self.msg2
        else:self.type1.set(self.msg2)
        self.label.config(bg=self.fondi, fg=self.couli)



#Classe de bind
class Assign(object):
    def __init__(self,mil,definit,touche=[]):
        self.m=mil
        self.d=definit
        self.t=touche
        for ww in self.t:
            self.m.bind('<{}>'.format(ww),self.d)
    def modifie(self,mil=None,definit=None,touche=[]):
        if mil!=None:
            self.m=mil
        if definit!=None:
            self.d=definit
        if touche!=[]:
            self.t=touche
        for ww in self.t:
            self.m.bind('<{}>'.format(ww),self.d)

class Unsassign(object):
    def __init__(self,mil, touche=[], definit=None):
        self.m=mil
        self.d=definit
        self.t=touche
        for ww in self.t:
            self.m.unbind(f'<{ww}>')
    def modifie(self,mil=None,definit=None,touche=[]):
        if mil!=None:
            self.m=mil
        if definit!=None:
            self.d=definit
        if touche!=[]:
            self.t=touche
        for ww in self.t:
            self.m.unbind('<{}>'.format(ww))

#Classe des COULEURS
class Couleur(object):
    def __init__(self, color='black'):
        self.coul=askcolor('black')[1]
    def assigne(self):
        return self.coul

def rendre_bien(texte):
    txt=''
    for ww in texte.strip():
        if ww==' ':
            ww='_'
        txt+=ww
    txt=str(((txt.lower()).strip()).title())
    return txt

#Classe de police
class Police(object):
    def __init__(self,font='Calibri'):
        self.font=rendre_bien(font)
        if not self.font in POLICE:
            print('Erreur de police','La police %s n\'est pas dans notre repertoire' %self.font)
    def assigne(self):
        return self.font

#Curseur system
class Cursor(object):
    def __init__(self, cursor = "C:\\Windows\\Cursors\\arrow_r.cur"):
        chemin_image_curseur = cursor
        user32 = ctypes.windll.user32
        user32.LoadCursorFromFileW.restype = ctypes.c_void_p
        curseur = user32.LoadCursorFromFileW(chemin_image_curseur)
        self.cur = curseur
        user32.SetSystemCursor(curseur, 32512)

    def setdefault(self):
        chemin_image_curseur = "C:\\Windows\\Cursors\\arrow_r.cur"
        user32 = ctypes.windll.user32
        user32.LoadCursorFromFileW.restype = ctypes.c_void_p
        curseur = user32.LoadCursorFromFileW(chemin_image_curseur)
        self.cur = curseur
        user32.SetSystemCursor(curseur, 32512)

    def setcursor(self, cursor = "C:\\Windows\\Cursors\\arrow_r.cur"):
        chemin_image_curseur = cursor
        user32 = ctypes.windll.user32
        user32.LoadCursorFromFileW.restype = ctypes.c_void_p
        curseur = user32.LoadCursorFromFileW(chemin_image_curseur)
        self.cur = curseur
        user32.SetSystemCursor(curseur, 32512)




#Couleurs
COLORS = {
    "--dark-color": "#212529",
    "--light-color": "#fff",
    "--light-light-color": "#ebf1f1",
    "--dark-orange": "#ff5436",
    "--light-orange": "#ff8975",
    "--dark-turquoise": "#50e3c2",
    "--light-turquoise": "#59ebcb",
    "--dark-color-1": "#2c3f50",
    "--light-color-1": "#34495e",
    "--dark-cyan": "#00abcf",
    "--light-cyan": "#07b7dc",
    "--dark-orange-1": "#a45a37",
    "--light-orange-1": "#f2b597",
    "--dark-olive": "#0a3b47",
    "--light-olive": "#1a5c6c",
    "--dark-pale-green": "#a1abb0",
    "--light-pale-green": "#b0b791",
    "--dark-light-blue": "#7da4e3",
    "--light-light-blue": "#98bbf5",
    "--dark-blue": "#008fff",
    "--light-blue": "#45adff",
    "--dark-green": "#a4c013",
    "--light-green": "#bddb0b",
    "--dark-purple": "#6200ee",
    "--light-purple": "#bb86fc",
    "--dark-yellow": "#e7a930",
    "--light-yellow": "#e6bc43",
    "--dark-light-color": "#bec3c7",
    "--dark-pink": "#df65a0",
    "--light-pink": "#e77baf",
    "--dark-move": "#2520de",
    "--light-move": "#6c68ff",
    "--dark-green-1": "#27903c",
    "--light-green-1": "#36b64f",
    "--dark-orange-2": "#ff8d2c",
    "--light-orange-2": "#fea255",
    "--dark-olive-1": "#046262",
    "--light-olive-1": "#1f8384",
    "--dark-pink-1": "#e054b8",
    "--light-pink-1": "#ff74d9",
    "--dark-red": "#e23d4d",
    "--light-red": "#ec6170"
}


#Curseurs
CURSEURS=['X_cursor','arrow','based_arrow_down','based_arrow_up','boat','bogosity',
          'bottom_left_corner','bottom_right_corner','bottom_side','bottom_tee','box_spiral',
          'center_ptr','circle','clock','coffee_mug','cross','cross_reverse','crosshair','diamond_cross',
          'dot','dotbox','double_arrow','draft_large','draft_small','draped_box','exchange','fleur','gobbler',
          'gumby','hand1','hand2','heart','icon','iron_cross','left_ptr','left_side','left_tee','leftbutton','ll_angle',
          'lr_angle','man','middlebutton','mouse','pencil','pirate','plus','question_arrow','right_ptr','right_side',
          'right_tee','rightbutton','rtl_logo','sailboat','sb_down_arrow','sb_h_double_arrow','sb_left_arrow',
          'sb_right_arrow','sb_up_arrow','sb_v_double_arrow','shuttle','sizing','spider','spraycan','star','target',
          'tcross','top_left_arrow','top_left_corner','top_right_corner','top_side','top_tee','trek','ul_angle',
          'umbrella','ur_angle','watch','xterm']

POLICE = [f for f in os.listdir('C:\\Windows\\Fonts') if f.lower().endswith(('.ttf', '.otf'))]
