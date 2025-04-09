import pyfunct as pf
import language as language
from language import getLang, dicoLANG_NAME
import widgets as wd
import object2D
import option2D
import object2W
import option2W
from tkinter import Tk, Toplevel, Frame, Canvas, Button, Menu, Scrollbar, StringVar, IntVar, Label, Entry, Radiobutton, Checkbutton
import tkinter.ttk as ttk
import tkinter.filedialog as fd
import tkinter.messagebox as tkmsg
from tkinter.font import Font
import math
import pickle as pkl
import os 
import capture
import sys
import admin
import webbrowser as wb
from PIL import Image, ImageTk


fen=None
can=None
taskBar, listBar, frRend, frCmd, frOpt=None, None, None, None, None
selector=None
select=None
focus=None
element=None
fromX=fromY=toX=toY=None
backward=list()
forward=list()
history=None
lift=None
globale=None
grid=None
varGrid=None
varButton=None
bBack, bForward, bBg=None, None, None
copy=None
rule=None
opt2D=None
entry=None

background='white'
sizeX=None
sizeY=None
format_='png'
path='local'
colorMode=None
colorValue=False
renderRegion=[getLang('center'), getLang('center'), getLang('all'), getLang('all')]
file=None
exec_func=None
ifRender=False
currentLang=None
ifOpen=False
isOpen=False

def addToList(objectList, item, name=None, command=None):
    def t(a):
        if a[1]:
            a[1]()
        if opt2D:
            index=element.listObj.index(opt2D.obj)
            if element.listEntry[index][0]==item:
                for ww in frOpt.frame.winfo_children():
                    ww.destroy()
        objectList.remove_widget(a[0].frame)
    xcv=item.add_button(bg=item['bg'], fg=pf.COLORS['--dark-red'], relief='flat', highlightthickness=0, 
                      activeforeground=pf.COLORS['--dark-red'], activebackground=item['bg'], bd=0, 
                      command=lambda arg=[item, command]:t(arg), text=chr(57508), cursor='hand2')
    pf.ActiveLeave(xcv, pf.COLORS['--dark-red'], item['bg'])
    objectList.add_widget(item.frame, name=name)
    return [item, item.frame, xcv, name, command]

def writeFile(data, file):
    with open(file, 'wb') as f:
        pkl.dump(data, f)

def readFile(file):
    with open(file, 'rb') as f:
        return pkl.load(f)

def getAngle(a, b, angle, x, y):
    ang = float(-angle) * 2 * math.pi / 360
    rx=x
    ry=y
    fx = a + rx * math.cos(ang) - ry * math.sin(ang)
    fy = b + rx * math.sin(ang) + ry * math.cos(ang)
    return (fx, fy)

def getMirror(listX, listY, a, b, methode='x'):
    if methode == 'x':
        mirroredX = [2*a - x for x in listX]
        return [mirroredX, listY]
    elif methode == 'y':
        mirroredY = [2*b - y for y in listY]
        return [listX, mirroredY]
    elif methode == 'xy':
        mirroredX = [2*a - x for x in listX]
        mirroredY = [2*b - y for y in listY]
        return [mirroredX, mirroredY]
    else:
        return [listX, listY]

def addTriEq(master, x, y):
    c1=getAngle(x, y, 15, 50, 50)
    c2=getAngle(x, y, 145, 50, 50)
    c3=getAngle(x, y, 255, 50, 50)
    return object2D.Polygon(master, [c1[0], c2[0], c3[0]], [c1[1], c2[1], c3[1]])

def addTriRec(master, x, y):
    c1=(x-50, y-50)
    c2=(x-50, y+50)
    c3=(x+50, y+50)
    return object2D.Polygon(master, [c1[0], c2[0], c3[0]], [c1[1], c2[1], c3[1]])

def addSquare(master, x, y):
    c1=(x-50, y-50)
    c2=(x+50, y-50)
    c3=(x+50, y+50)
    c4=(x-50, y+50)
    return object2D.Polygon(master, [c1[0], c2[0], c3[0], c4[0]], [c1[1], c2[1], c3[1], c4[1]])

def addPenta(master, x, y):
    a=24
    c1=getAngle(x, y, 15-a, 50, 50)
    c2=getAngle(x, y, 87-a, 50, 50)
    c3=getAngle(x, y, 159-a, 50, 50)
    c4=getAngle(x, y, 231-a, 50, 50)
    c5=getAngle(x, y, 303-a, 50, 50)
    return object2D.Polygon(master, [c1[0], c2[0], c3[0], c4[0], c5[0]], [c1[1], c2[1], c3[1], c4[1], c5[1]])

def addHexa(master, x, y):
    a=15
    c1=getAngle(x, y, 0-a, 50, 50)
    c2=getAngle(x, y, 60-a, 50, 50)
    c3=getAngle(x, y, 120-a, 50, 50)
    c4=getAngle(x, y, 180-a, 50, 50)
    c5=getAngle(x, y, 240-a, 50, 50)
    c6=getAngle(x, y, 300-a, 50, 50)
    return object2D.Polygon(master, [c1[0], c2[0], c3[0], c4[0], c5[0], c6[0]], [c1[1], c2[1], c3[1], c4[1], c5[1], c6[1]])

def addCircle(master, x, y):
    c1=(x-50, y-50)
    c2=(x+50, y+50)
    return object2D.Oval(master, [c1[0], c2[0]], [c1[1], c2[1]])

def addArc(master, x, y):
    c1=(x-50, y-50)
    c2=(x+50, y+50)
    return object2D.Arc(master, [c1[0], c2[0]], [c1[1], c2[1]])

def addText(master, x, y):
    return object2D.Text(master, [x], [y])

def addWindow(master, x, y):
    return object2D.Window(master, [x], [y], object2W.Button2W(can))

def addImage(master, x, y, image):
    return object2D.Picture(master, [x], [y], image)

class ModifyPoint:
    def __init__(self, master, objet):
        self.master=master
        self.obj=objet
        self.listFocus=list()
        self.x=self.obj.x.copy()
        self.y=self.obj.y.copy()
        for ww in range(len(self.x)):
            self.listFocus.append(pf.Select(self.master, self.x[ww-1], self.y[ww-1], 10, 10, self.obj, pf.FOCUS))
            self.listFocus[-1].setSelector()
            self.listFocus[-1].setSize()
            self.listFocus[-1].setCoords()
        setHistory()
  
    def assign(self):
        pf.Assign(self.master, self.modify, ['Button1-Motion'])
    
    def unassign(self):
        self.master.unbind('<Button1-Motion>')
    
    def modify(self, event):
        global opt2D
        min_distance = float(eval('math.inf'))
        closest_element = None
        click_x, click_y = event.x, event.y
        for i, element in enumerate(self.listFocus):
            elem_x, elem_y = self.x[i], self.y[i]
            distance = math.sqrt((click_x - elem_x) ** 2 + (click_y - elem_y) ** 2)
            if distance < min_distance:
                min_distance = distance
                closest_element = element
        index=self.listFocus.index(closest_element)
        self.x[index]=event.x
        self.y[index]=event.y
        closest_element.setCoords(event.x, event.y)
        for ww in self.listFocus:
            if ww!=closest_element:
                ww.setCoords(self.x[self.listFocus.index(ww)], self.y[self.listFocus.index(ww)])
        self.obj.setCoords(self.x, self.y)

    def destroy(self):
        for ww in self.listFocus:
            ww.destroy()

class ObjectDialog(Toplevel):
    def __init__(self, master, canvas, theme=[pf.COLORS['--dark-color'], pf.COLORS['--light-color'], pf.COLORS['--light-color-1'], pf.COLORS['--dark-color-1']], method='polygon', close='auto', *cnf, **kwargs):
        self.master=master
        self.canvas=canvas
        self.theme=theme
        self.method=method
        self.close=close
        Toplevel.__init__(self,self.master,  *cnf, **kwargs)
        self.wm_attributes('-toolwindow', True)
        self.wm_attributes('-topmost', True)
        self.grab_set()
        self.protocol('WM_DELETE_WINDOW', self.close_modal_window)
        self.title('GeometryTag')
        self['bg']=self.theme[0]
        self.geometry('500x400')
        self.resizable(False, False)
        self.can=Canvas(self, width=400, height=400, bg='white', cursor='tcross')
        self.frame=Canvas(self, width=100, height=400, bg=self['bg'])
        self.can.grid(row=1, column=1)
        self.frame.grid(row=1, column=2, pady=2)
        for ww in range(26):
            self.can.create_line(0, ww*16, 400, ww*16, fill='grey80')
            self.can.create_line(ww*16, 0, ww*16, 400, fill='grey80')
        fr1=Frame(self.frame, width=100, height=15, back=self.theme[0])
        fr1.grid(row=1, column=1)
        fr2=Frame(self.frame, width=100, height=290, bg=self.theme[0])
        fr2.grid(row=2, column=1)
        
        b1=Button(self.frame, text=getLang('insert'), bg=self.theme[0], fg=self.theme[1],
                  bd=0, border=0, relief='flat', highlightthickness=0, cursor='hand2',
                  font=Font(family=pf.POLICE[0], size=12), activebackground=self.theme[3],
                  activeforeground=pf.COLORS['--light-blue'], command=self.insert, state='disabled')
        b2=Button(self.frame, text=getLang('close'), bg=self.theme[0], fg=self.theme[1],
                  bd=0, border=0, relief='flat', highlightthickness=0, cursor='hand2',
                  font=Font(family=pf.POLICE[0], size=12), activebackground=self.theme[3],
                  activeforeground=pf.COLORS['--dark-orange'], command=self.close_modal_window)
        pf.ActiveLeave(b2, self.theme[2], pf.COLORS['--dark-red'])
        pf.ActiveLeave(b1, self.theme[2], pf.COLORS['--dark-blue'])
        b1.grid(row=3, column=1, sticky='ew', pady=3)
        b2.grid(row=4, column=1, sticky='ew', pady=3)
        
        self.bleft=Button(fr1, text='<', bg=self.theme[0], fg=self.theme[1],
                  bd=0, border=0, relief='flat', highlightthickness=0, cursor='hand2',
                  font=Font(family=pf.POLICE[0], size=12), activebackground=self.theme[3],
                  activeforeground=pf.COLORS['--light-green'], command=self.left, width=5, stat='disabled')
        self.bright=Button(fr1, text='>', bg=self.theme[0], fg=self.theme[1],
                  bd=0, border=0, relief='flat', highlightthickness=0, cursor='hand2',
                  font=Font(family=pf.POLICE[0], size=12), activebackground=self.theme[3],
                  activeforeground=pf.COLORS['--light-green'], command=self.right, width=5, stat='disabled')
        pf.ActiveLeave(self.bleft, self.theme[2], pf.COLORS['--light-green'])
        pf.ActiveLeave(self.bright, self.theme[2], pf.COLORS['--dark-green'])
        self.bleft.grid(row=1, column=1, sticky='ew', rowspan=2)
        self.bright.grid(row=1, column=2, sticky='ew', rowspan=2)
        
        self.over, self.active=pf.COLORS['--light-color-1'], pf.COLORS['--dark-color-1']
        self.bg, self.fg=pf.COLORS['--dark-color'], pf.COLORS['--light-color']
        self.pop=pf.Popup(self.can, tearoff=False, bg=self.bg, fg=self.fg, activebackground=self.over,
                           relief='flat', bd=0, border=0)
        self.pop.add_command(label=getLang('erase'), command=self.clean)
        self.binsert=b1
        
        self.listX=[]
        self.listY=[]
        self.listLine=[]
        self.listB=[]
        self.listBx=[]
        self.listBy=[]
        self.listFx=[]
        self.listFy=[]
        self.a=self.canvas.winfo_width()/2
        self.b=self.canvas.winfo_height()/2
        self.line=None
        self.xLine=self.can.create_line(0, 200, 400, 200, fill=pf.COLORS['--dark-blue'])
        self.yLine=self.can.create_line(200, 0, 200, 400, fill=pf.COLORS['--dark-blue'])
        self.obj=None
        
        pf.Assign(self.can, self.createLine, ['Button-1'])
        self.mainloop()
    
    def close_modal_window(self):
        self.grab_release()
        self.destroy()
    
    def insert(self):
        global select, opt2D
        lx=[]
        ly=[]
        for ww in range(len(self.listX)):
            lx.append(self.listX[ww]+self.a-int(self.can['width'])//2)
            ly.append(self.listY[ww]+self.b-int(self.can['height'])//2)
        if self.method=='polygon':
            self.obj=object2D.Polygon(self.canvas, lx, ly)
        elif self.method=='line':
            self.obj=object2D.Line(self.canvas, lx, ly)
        element.addObj(self.obj)
        opt2D=option2D.Option2D(frOpt.frame, self.obj, command=setHistory)
        opt2D.setOption()
        minx=min(self.obj.x)
        maxx=max(self.obj.x)
        miny=min(self.obj.y)
        maxy=max(self.obj.y)
        x, y, wdt, hgt=minx+(maxx-minx)/2, miny+(maxy-miny)/2, maxx-minx, maxy-miny
        select=pf.Select(can, x, y, wdt, hgt, self.obj)
        select.setSelector()
        select.setSize()
        select.setCoords(x, y)
        varButton.set('choosen')
        if self.close=='auto':
            self.close_modal_window()
        return self.obj
        
    def right(self):
        if len(self.listFx)>0:
            x=self.listFx[-1]
            y=self.listFy[-1]
            del(self.listFx[-1])
            del(self.listFy[-1])
            if len(self.listX)==0:
                self.line=self.can.create_line(x,y,x,y)
            self.listX.append(x)
            self.listY.append(y)
            if len(self.listX)>1:
                self.listBx.append(x)
                self.listBy.append(y)
                self.listB.append(self.can.create_line(self.listX[-2], self.listY[-2], self.listBx[-1], self.listBy[-1]))
            self.can.coords(self.xLine, 0, y, 400, y)
            self.can.coords(self.yLine, x, 0, x, 400)
            self.can.lift(self.xLine, self.yLine)
            if self.method=='polygon':
                self.can.coords(self.line, self.listX[0], self.listY[0], x, y)
            self.bleft['stat']='normal'
        else:
            self.bright['stat']='disabled'
        if len(self.listX)>2:self.binsert['stat']='normal'
        else:self.binsert['stat']='disabled'
    
    def left(self):
        if len(self.listB)>0:
            self.can.delete(self.listB[-1])
            del(self.listB[-1])
            self.listFx.append(self.listBx[-1])
            self.listFy.append(self.listBy[-1])
            del(self.listBx[-1])
            del(self.listBy[-1])
            del(self.listX[-1])
            del(self.listY[-1])
            if len(self.listBx)>0:
                self.can.coords(self.line, self.listX[0], self.listY[0], self.listBx[-1], self.listBy[-1])
                self.can.coords(self.xLine, 0, self.listBy[-1], 400, self.listBy[-1])
                self.can.coords(self.yLine, self.listBx[-1], 0, self.listBx[-1], 400)
            else:
                if self.method=='polygon':
                    self.can.coords(self.line, self.listX[0], self.listY[0], self.listX[-1], self.listY[-1])
                self.can.coords(self.xLine, 0, self.listY[-1], 400, self.listY[-1])
                self.can.coords(self.yLine, self.listX[-1], 0, self.listX[-1], 400)
            self.bright['stat']='normal'
        else:
            self.listFx.append(self.listX[0])
            self.listFy.append(self.listY[0])
            del(self.listX[:])
            del(self.listY[:])
            self.can.delete(self.line)
            self.line=None
            self.can.coords(self.xLine, 0, 200, 400, 200)
            self.can.coords(self.yLine, 200, 0, 200, 400)
            self.bleft['stat']='disabled'
        if len(self.listX)>2:self.binsert['stat']='normal'
        else:self.binsert['stat']='disabled'
    
    def clean(self):
        for ww in self.listB:
            self.can.delete(ww)
        self.can.delete(self.line)
        self.line=None
        del(self.listX[:])
        del(self.listY[:])
        del(self.listB[:])
        del(self.listBx[:])
        del(self.listBy[:])
        del(self.listFx[:])
        del(self.listFy[:])
        self.can.coords(self.xLine, 0, 200, 400, 200)
        self.can.coords(self.yLine, 200, 0, 200, 400)
        self.bleft['stat']='disabled'
        self.bright['stat']='disabled'
        if len(self.listX)>2:self.binsert['stat']='normal'
        else:self.binsert['stat']='disabled'
    
    def createLine(self, event):
        x=event.x
        y=event.y
        self.listFx=[]
        self.listFy=[]
        if len(self.listX)==0:
            self.line=self.can.create_line(x,y,x,y)
        self.listX.append(x)
        self.listY.append(y)
        if len(self.listX)>1:
            self.listBx.append(x)
            self.listBy.append(y)
            self.listB.append(self.can.create_line(self.listX[-2], self.listY[-2], self.listBx[-1], self.listBy[-1]))
        self.can.coords(self.xLine, 0, y, 400, y)
        self.can.coords(self.yLine, x, 0, x, 400)
        self.can.lift(self.xLine, self.yLine)
        if self.method=='polygon':
            self.can.coords(self.line, self.listX[0], self.listY[0], x, y)
        self.bright['stat']='disabled'
        self.bleft['stat']='normal'
        if len(self.listX)>=2:self.binsert['stat']='normal'
        else:self.binsert['stat']='disabled'
        
    def get(self):
        return self.obj

class ObjectList(option2D.ScrollableFrame):
    def __init__(self, master, *cnf, **kwargs):
        self.master=master
        option2D.ScrollableFrame.__init__(self, self.master, *cnf, **kwargs)
        self.list=[]
        self.listWidget=[]
        self.listName={}
        self.listRow={}
        self.row=1
    
    def add_widget(self, widget, name=None):
        self.list.append(widget)
        self.listName[widget]=name if name else str(self.row)
        self.listRow[widget]=self.row
        self.list[-1].grid(row=self.listRow[widget], column=1, pady=1, sticky='ew')
        self.row+=1
    
    def remove_widget(self, widget):
        if type(widget)==type(10):
            if widget<len(self.list):
                self.list[widget].grid_forget()
        elif widget in self.listName.values():
            for ww, xx in (self.listName.keys(), self.listName.values()):
                if xx==widget:
                    ww.grid_forget()
                    break
        elif widget in self.list:
            self.list[self.list.index(widget)].grid_forget()
        else:pass
    
    def delete_widget(self, widget):
        if widget=='all':
            for ww in self.list:
                try:
                    ww.destroy()
                except:pass
            self.list=[]
            self.listName={}
            self.listRow={}
            self.listWidget={}
            self.row=1
        if type(widget)==type(10):
            if widget<len(self.list):
                self.list[widget].destroy()
        elif widget in self.listName.values():
            for ww, xx in (self.listName.keys(), self.listName.values()):
                if xx==widget:
                    ww.destroy()
                    break
        elif widget in self.list:
            self.list[self.list.index(widget)].destroy()
        else:pass
    
    def rename_widget(self, widget, name):
        if type(widget)==type(10):
            if widget<len(self.list):
                self.listName[self.list[widget]]=name
        elif widget in self.listName.values():
            for ww, xx in (self.listName.keys(), self.listName.values()):
                if xx==widget:
                    self.listName[ww]=name
                    break
        elif widget in self.list:
            self.listName[self.list[self.list.index(widget)]]=name
        else:pass
    
    def regrid_widget(self, widget):
        if type(widget)==type(10):
            if widget<len(self.list):
                self.list[widget].grid(row=self.listRow[self.list[widget]], column=1, sticky='ew')
        elif widget in self.listName.values():
            for ww, xx in (self.listName.keys(), self.listName.values()):
                if xx==widget:
                    ww.grid(row=self.listRow[ww], column=1, sticky='ew')
                    break
        elif widget in self.list:
            widget.grid(row=self.listRow[widget], column=1, stick='ew')
        else:pass

class MainWindow(Tk):
    def __init__(self, *cnf, **kwargs):
        Tk.__init__(self, *cnf, **kwargs)
        self.title('Dynamic Draw')
        self.screenWidth=self.winfo_screenwidth()
        self.screenHeight=self.winfo_screenheight()
        self.geometry(f'{self.screenWidth-100}x{self.screenHeight-100}+0+0')
        self['bg']=pf.COLORS['--dark-color']
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.style=ttk.Style()
        #self.style.theme_use('alt')
        self.style.configure('Vertical.TNotebook', background=pf.COLORS['--dark-color'], tabposition="wn")
        self.frame=Canvas(self, width=self['width']-250, height=self['height']-120, bg=pf.COLORS['--dark-color'], bd=0, highlightthickness=0)
        self.menu=Menu(self, tearoff=False, bg=pf.COLORS['--dark-color'], fg=pf.COLORS['--light-color'])
        self.taskBar=option2D.ScrollableFrame(self, bg=pf.COLORS['--dark-color'], bd=0, highlightthickness=0, width=self['width']-250, height=self['height']-120)
        self.listBar=ObjectList(self, width=280, height=120, bg=pf.COLORS['--dark-color'], bd=0, highlightthickness=1)
        self.listOption=ttk.Notebook(self, width=250, height=self['height']-150, style='Vertical.TNotebook')
        self.config(menu=self.menu)
        self.taskBar.grid(row=1, column=1, sticky='ew', padx=0, pady=0)
        self.frame.grid(row=2, column=1, sticky='nsew', padx=0, pady=0)
        self.listBar.grid(row=1, column=2, sticky='nsew', padx=0, pady=0)
        self.listOption.grid(row=2, column=2, sticky='nsew', padx=0, pady=0)
        self.taskBar.grid_columnconfigure(1, weight=1)
        self.listOption.grid_rowconfigure(1, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)
        self.frame.grid_rowconfigure(1, weight=1)
        self.listBar.v_scrollbar['width']=11
        self.listBar.can.config(bd=0, highlightthickness=0)
        self.listBar.frame.config(bd=0, highlightthickness=0)
        self.listBar.h_scrollbar['width']=11
        self.taskBar.v_scrollbar['width']=11
        self.taskBar.can.config(bd=0, highlightthickness=0)
        self.taskBar.frame.config(bd=0, highlightthickness=0)
        self.taskBar.h_scrollbar['width']=11
        def on_taskR(event):
            self.taskBar.can.config(width=event.width-15, height=120)
        pf.Assign(self.taskBar, on_taskR, ['Configure'])
        self.can=Canvas(self.frame, width=self['width']-250, height=self['height']-150, bg='white', bd=0, highlightthickness=0,
                        scrollregion=(0, 0, self['width']-120, self['height']-120))
        self.xb=Scrollbar(self.frame, command=self.can.xview, width=11, orient='horizontal')
        self.yb=Scrollbar(self.frame, command=self.can.yview, width=11)
        self.can.grid(row=1, column=1, sticky='nsew')
        self.xb.grid(row=2, column=1, sticky='ew')
        self.yb.grid(row=1, column=2, sticky='ns')
        self.can.grid_columnconfigure(1, weight=1)
        self.can.grid_rowconfigure(1, weight=1)
        self.frm=Frame(self, width=self['width'], height=30, bg=pf.COLORS['--dark-color'], bd=0, highlightthickness=0)
        self.frm.grid(row=3, column=1, columnspan=2, sticky='ew')
        self.frm.grid_columnconfigure(1, weight=1)
        self.labCoords=Label(self.frm, text='X:  Y:\tObject:', bg=pf.COLORS['--dark-color'], fg='white', justify='center', padx=10,
                             font=Font(family=pf.POLICE[0], size=10))
        self.labCoords.grid(row=1, column=1, sticky='w')
        self.labError=Label(self.frm, text='', fg='red', bg=pf.COLORS['--dark-color'], padx=40,
                            font=Font(family='system'))
        self.labError.grid(row=1, column=4, sticky='e')
        self.frameRender=option2D.ScrollableFrame(self.listOption, bg=pf.COLORS['--dark-color'], bd=0, highlightthickness=0, 
                                               width=self.listOption['width'], height=self['height']-150)
        self.frameCommand=option2D.ScrollableFrame(self.listOption, bg=pf.COLORS['--dark-color'], bd=0, highlightthickness=0,
                                                   width=self.listOption['width'], height=self['height']-150)
        self.frameOption=option2D.ScrollableFrame(self.listOption, bg=pf.COLORS['--dark-color'], bd=0, highlightthickness=0,
                                                  width=self.listOption['width'], height=self['height']-150)
        self.frameRender.can.config(width=self.listOption['width']-15, height=self.screenHeight-255)
        self.frameRender.frame.config(bd=0, highlightthickness=0)
        self.frameCommand.can.config(width=self.listOption['width']-15, height=self.screenHeight-255)
        self.frameCommand.frame.config(bd=0, highlightthickness=0)
        self.frameOption.can.config(width=self.listOption['width']-15, height=self.screenHeight-255)
        self.frameOption.frame.config(bd=0, highlightthickness=0)
        self.listOption.add(self.frameRender, text=chr(58102))
        self.listOption.add(self.frameCommand, text=chr(60369))
        self.listOption.add(self.frameOption, text=chr(57684))
        def on_resize(event):
            for ww in (self.frameRender, self.frameCommand, self.frameOption):
                ww['height']=event.height
                ww.can['height']=event.height-20
        pf.Assign(self.listOption, on_resize, ['Configure'])
        self.setNoScroll()
  
    def setNoScroll(self):
        self.taskBar.setNoScroll()
        self.listBar.setNoScroll()
        self.frameCommand.setNoScroll()
        self.frameOption.setNoScroll()
        self.frameRender.setNoScroll()
    
    def getInterface(self):
        return [self.taskBar, self.listBar, self.frameRender, self.frameCommand, self.frameOption]
        
class Selector(object):
    def __init__(self, master, x, y):
        self.master=master
        self.x1=x
        self.y1=y
        self.x2=x 
        self.y2=y
        self.cadre=self.master.create_rectangle(self.x1, self.y1, self.x2, self.y2, outline=pf.COLORS['--dark-blue'], width=1, dash=(1))
    
    def assign(self):
        pf.Assign(self.master, self.motion, ['Button1-Motion']) 
    
    def unassign(self):
        self.master.unbind('<Button1-Motion')
    
    def motion(self, event):
        self.x2=event.x
        self.y2=event.y
        self.master.coords(self.cadre, self.x1, self.y1, self.x2, self.y2)
    
    def destroy(self):
        self.master.delete(self.cadre)
 
class Element:
    def __init__(self, master):
        self.master=master
        self.listObj=list()
        self.listEntry=list()
        self.listLift=list()
        self.dictIndex={'line':0, 'polygon':0, 'oval':0, 'arc':0,
                   'text':0, 'text':0, 'window':0, 'picture':0, 'pen':0}
        self.varEntr=StringVar(value=False)
        
    def addObj(self, object):
        self.listObj.append(object)
        bBack['stat']='normal'
        bForward['stat']='disabled'
        if object.type!='pen':
            self.listObj[-1].setTag(self.listObj[-1].type+str(self.dictIndex[self.listObj[-1].type]))
            self.listObj[-1].setName(self.listObj[-1].tag if object.name=='' else object.name)
            entr=wd.Entrytk(listBar.frame, bg=pf.COLORS['--dark-color'] if len(self.listObj)%2!=0 else pf.COLORS['--dark-color-1'], 
                            fg=pf.COLORS['--light-color'], bd=0, relief='sunken', highlightthickness=1, cursor='arrow',
                            highlightcolor=pf.COLORS['--dark-blue'], insertbackground=pf.COLORS['--light-color'],
                            highlightbackground=pf.COLORS['--dark-color'] if len(self.listObj)%2==0 else pf.COLORS['--dark-color-1'])
            entr.add_radiobutton(variable=self.varEntr, value=self.listObj[-1].tag, bg=entr['bg'], fg=entr['fg'], bd=0, highlightthickness=0,
                                 activebackground=entr['bg'], command=lambda:manualChoosen(object))
            def t(obj):
                unsassign1()
                setArrow()
                varButton.set('arrow')
                l=[]
                for ww in self.listObj:
                    if ww.type!='pen':
                        l.append(ww.getAll())
                    else:
                        l.append(['pen', None])
                history.setHistory(l)
                obj.setStat('hidden')
            def u(event):
                manualChoosen(object)
            pf.Assign(entr, u, ['Button-1'])
            self.addEntry(addToList(listBar, entr, self.listObj[-1].tag, lambda arg=object: t(arg)))
            entr['width']=35
            entr.insert('end', self.listObj[-1].name)
            self.listObj[-1].setStat('hidden')
            self.varEntr.set(self.listObj[-1].tag)
        else:
            self.addEntry(None)
        self.dictIndex[self.listObj[-1].type]+=1 
        self.listLift.append(self.listObj[-1])
        if True:
            l=[]
            for ww in self.listObj:
                if ww.type!='pen':
                    l.append(ww.getAll())
                else:
                    l.append(['pen', None])
            history.setHistory(l)
            if self.listObj[-1].type!='pen':
                self.listObj[-1].setStat('normal')
    
    def addMultipleObj(self, object):
        a=len(object)-1
        for ww in object:
            self.addObj(ww)
            if object.index(ww)!=a:
                del(history.listBack[-1])
        if frOpt.frame.winfo_children():
            for ww in frOpt.frmae.winfo_children():
                ww.destroy()
    
    def addEntry(self, entry):
        self.listEntry.append(entry)
    
    def clear(self):
        for ww in self.listObj:
            ww.destroy()
        for ww in self.listEntry:
            if ww:
                listBar.delete_widget(ww[1])
        del(self.listObj[:])
        del(self.listEntry[:])
        del(self.listLift[:])
        
class GridSpace:
    def __init__(self, master):
        self.master=master
        self.list=list()
        wdt=fen.winfo_screenwidth()
        hgt=fen.winfo_screenheight()
        a=100
        b=wdt if wdt>hgt else hgt
        for ww in range(-a, a, 1):
            self.list.append(self.master.create_line(-a, b/a*ww, wdt, b/a*ww, dash=(1), stat='hidden'))
            self.list.append(self.master.create_line(b/a*ww, -a, b/a*ww,hgt, dash=(1), stat='hidden'))
    
    def view(self):
        for ww in self.list:
            self.master.itemconfig(ww, stat='normal')
        self.lift()
    
    def hide(self):
        for ww in self.list:
            self.master.itemconfig(ww, stat='hidden')
    
    def lift(self):
        for ww in self.list:
            self.master.lift(ww)

class History:
    def __init__(self):
        self.listBack=list()
        self.listWard=list()
    
    def setHistory(self, value):
        if not self.listBack:
            self.listBack.append(value)
            self.listWard=list()
        else:
            if self.listBack[-1]==value:
                pass
            else:
                self.listBack.append(value)
                self.listWard=list()
    
    def setBack(self, value):
        if not self.listBack:
            return None
        else:
            self.listWard.append(value)
            del(self.listBack[-1])
            bForward['stat']='normal'
            return self.listBack
    
    def setWard(self, value):
        if not self.listWard:
            return None
        else:
            self.listBack.append(value)
            del(self.listWard[-1])
            bBack['stat']='normal'
            return self.listBack

    def clear(self):
        del(self.listBack[:])
        del(self.listWard[:])
        bBack['stat']='disabled'
        bForward['stat']='disabled'
    
class Copy:
    def __init__(self):
        self.listCopy=[]
    
    def copy(self, value):
        self.listCopy=list()
        if type(value==type([])):
            for ww in value:
                self.listCopy.append(ww.getAll())
        else:
            self.listCopy.append(value.getAll())
    
    def past(self):
        global select, opt2D
        if self.listCopy:
            setArrow()
            setChoosen()
            if len(self.listCopy)>1:select=list()
            npl=[]
            for ww in self.listCopy:
                if ww[0] in ['line', 'arc', 'polygon', 'oval']:
                    wdt=max(ww[1])-min(ww[1])
                    hgt=max(ww[2])-min(ww[2])
                    obj=object2D.listOfObject[ww[0]](can, ww[1], ww[2])
                elif ww[0]=='text':
                    wdt=len(ww[3])*ww[4]
                    hgt=ww[3].count('\n')*ww[4]
                    obj=object2D.listOfObject[ww[0]](can, ww[1], ww[2])
                elif ww[0]=='picture':
                    wdt=ww[5]
                    hgt=ww[6]
                    obj=object2D.listOfObject[ww[0]](can, ww[1], ww[2], ww[3])
                elif ww[0]=='window':
                    wdt=ww[6]
                    hgt=ww[7]
                    obj=object2D.listOfObject[ww[0]](can, ww[1], ww[2], object2W.Button2W(can))
                obj.setAll(ww)
                opt2D=option2D.Option2D(frOpt.frame, obj, command=setHistory)
                opt2D.setOption()
                if obj.type=='window':
                    obj.option2W=option2W.Option2W(opt2D.fr5, obj.window, command=setHistory)
                    obj.option2W.setOption()
                if len(self.listCopy)>1:
                    select.append(pf.Select(can, obj.pointx, obj.pointy, wdt, hgt, obj))
                    select[-1].setSelector()
                    select[-1].setSize()
                    select[-1].setCoords(obj.pointx, obj.pointy)
                else:
                    select=pf.Select(can, obj.pointx, obj.pointy, wdt, hgt, obj)
                    select.setSelector()
                    select.setSize()
                obj.setStat('hidden')
                npl.append(obj)
            if len(self.listCopy)>1:
                for ww in frOpt.frame.winfo_children():
                    ww.destroy()
                element.addMultipleObj(npl)
            else:
                element.addObj(npl[0])
            return npl
    
    def clear(self):
        self.copy=list()

class LocalEntry:
    def __init__(self):
        self.listEntry=[]
    
    def add(self, entry):
        self.listEntry.append(entry)          

#######################
def unsassign1():
    pf.Unsassign(can, ['Button-1', 'ButtonRelease-1', 'Button1-Motion', 'Button-3', 'Leave', 'FocusOut']) 

def unbindAll(event=None):
    taskBar.setNoScroll()
    listBar.setNoScroll()
    frRend.setNoScroll()
    frCmd.setNoScroll()
    frOpt.setNoScroll()

def setScroll(event):
    unbindAll()
    event.widget.setScroll()

def setNoScroll(event):
    event.widget.setNoScroll()
 
def setSelector(event=None):
    unsassign1()
    global selector
    can['cursor']='crosshair'
    varButton.set('selector')
    for ww in frOpt.frame.winfo_children():
        ww.destroy()
    if selector:
        selector.destroy()
        selector=None
    def t(event):
        global selector, select
        if not selector:
            selector=Selector(can, event.x, event.y)
            selector.assign()
        if select:
            if type(select)==type([]):
                for ww in select:
                    ww.destroy()
            else:
                select.destroy()
            select=None
    def u(event):
        global selector, fromX, fromY, toX, toY
        if selector:
            fromX, fromY, toX, toY=selector.x1, selector.y1, selector.x2, selector.y2
            selector.destroy()
            selector.unassign()
            selector=None
            checkFromTo()
    pf.Assign(can, t, ['Button-1'])
    pf.Assign(can, u, ['ButtonRelease-1', 'Button-3'])

def checkFromTo(event=None):
    global fromX, fromY, toX, toY, select
    if fromX>toX:
        a=fromX
        fromX=toX
        toX=a
    if fromY>toY:
        a=fromY
        fromY=toY
        toY=a
    select=[]
    if element.listObj:
        for ww in element.listObj:
            a=False
            for xx in range(len(ww.x)):
                if fromX<ww.x[xx]<toX and fromY<ww.y[xx]<toX:
                    a=True
                    break
            if a:
                x=min(ww.x)+(max(ww.x)-min(ww.x))/2
                y=min(ww.y)+(max(ww.y)-min(ww.y))/2
                if ww.type in ['line', 'arc', 'polygon', 'oval']:
                    wdt=(max(ww.x)-min(ww.x))
                    hgt=(max(ww.y)-min(ww.y))
                else:
                    wdt=ww.width
                    hgt=ww.height if ww.type!='text' else ww.size
                select.append(pf.Select(can, x, y, wdt, hgt, ww))
                select[-1].setSelector()
                select[-1].setSize()
                select[-1].setCoords(x, y)
                for ww in frOpt.frame.winfo_children():
                    ww.destroy()

def setChoosen(event=None):
    unsassign1()
    varGrid.set(False)
    setGrid()
    global select, focus
    can['cursor']='top_left_arrow'
    varButton.set('choosen')
    if select:
        if type(select)==type([]):
            for ww in select:
                ww.destroy()
            select=None
        else:
            select.destroy()
            select=None
    if focus:
        focus.destroy()
        focus=None
    def t(event):
        global select, focus, opt2D
        if select:
            if type(select)==type([]):
                for ww in select:
                    ww.destroy()
            else:
                select.destroy()
                select=None
        if focus:
            focus.destroy()
            focus=None
        x=event.x
        y=event.y
        close=can.find_closest(x, y)[0]
        wataba=None
        if element.listObj:
            for ww in element.listObj:
                if ww.type!='pen'and close==ww.object:
                    wataba=ww
                    break
        if wataba:
            xx=min(wataba.x)+(max(wataba.x)-min(wataba.x))/2
            yy=min(wataba.y)+(max(wataba.y)-min(wataba.y))/2
            if wataba.type in ['line', 'arc', 'polygon', 'oval']:
                wdt=(max(wataba.x)-min(wataba.x))
                hgt=(max(wataba.y)-min(wataba.y))
            else:
                wdt=wataba.width if wataba.type!='text' else len(wataba.text)*wataba.size
                hgt=wataba.height if wataba.type!='text' else wataba.size*1.5
            select=pf.Select(can, xx, yy, wdt, hgt, wataba)
            select.setSelector()
            select.setSize()
            select.setCoords(xx, yy)
            opt2D=option2D.Option2D(frOpt.frame, wataba)
            opt2D.setOption()
            if wataba.type=='window':
                wataba.option2W=option2W.Option2W(opt2D.fr5, wataba.window)
                wataba.option2W.setOption()
    pf.Assign(can, t, ['Button-1'])

def manualChoosen(object):
    unsassign1()
    global select, focus, opt2D
    can['cursor']='top_left_arrow'
    varButton.set('choosen')
    if select:
        if type(select)==type([]):
            for ww in select:
                ww.destroy()
        else:
            select.destroy()
            select=None
    if focus:
        focus.destroy()
        focus=None
    x=min(object.x)+(max(object.x)-min(object.x))/2
    y=min(object.y)+(max(object.y)-min(object.y))/2
    if object.type in ['line', 'arc', 'polygon', 'oval']:
        wdt=(max(object.x)-min(object.x))
        hgt=(max(object.y)-min(object.y))
    else:
        wdt=object.width if object.type!='text' else len(object.text)*object.size
        hgt=object.height if object.type!='text' else object.size*1.5
    select=pf.Select(can, x, y, wdt, hgt, object)
    select.setSelector()
    select.setSize()
    select.setCoords(x, y)
    opt2D=option2D.Option2D(frOpt.frame, object)
    opt2D.setOption()
    if object.type=='window':
        object.option2W=option2W.Option2W(opt2D.fr5, object.window, command=setHistory).setOption()

def setArrow(event=None):
    global select, focus, opt2D
    varButton.set('arrow')
    opt2D
    if select:
        if type(select)==type([]):
            for ww in select:
                ww.destroy()
            select=None
        else:
            select.destroy()
            select=None
    if focus:
        focus.destroy()
        focus=None
    can['cursor']='arrow'
    unsassign1()

def setPen(event=None):
    unsassign1()
    global select, focus, opt2D
    can['cursor']='dot'
    if select:
        if type(select)==type([]):
            for ww in select:
                ww.destroy()
        else:
            select.destroy()
            select=None
    if focus:
        focus.destroy()
        focus=None
    element.addObj(object2D.Pen(can))
    opt2D=option2D.Option2D(frOpt.frame, element.listObj[-1], command=setHistory)
    opt2D.setOption()
  
def setErase(event=None):
    unsassign1()
    global select, focus
    can['cursor']='iron_cross'
    for ww in frOpt.frame.winfo_children():
        ww.destroy()
    if select:
        if type(select)==type([]):
            for ww in select:
                ww.destroy()
        else:
            select.destroy()
            select=None
    if focus:
        focus.destroy()
        focus=None
    def t(event):
        global select, focus
        if select:
            if type(select)==type([]):
                for ww in select:
                    ww.destroy()
            else:
                select.destroy()
                select=None
        if focus:
            focus.destroy()
            focus=None
        x=event.x
        y=event.y
        close=can.find_closest(x, y)[0]
        wataba=None
        px, py, wdt=None, None, None
        index=None
        if element.listObj:
            for ww in element.listObj:
                none=False
                if ww.type=='pen':
                    for xx in ww.listPen:
                        if close in xx:
                            wataba=close
                            px=ww.x[ww.listPen.index(xx)][xx.index(close)]
                            py=ww.y[ww.listPen.index(xx)][xx.index(close)]
                            wdt=ww.config[ww.listPen.index(xx)][1] if ww.config[ww.listPen.index(xx)][1]>=10 else 10
                            index=[element.listObj.index(ww), ww.listPen.index(xx), xx.index(close)]
                            none=True
                            break
                if none:
                    break
        if wataba:
            if wdt/2>=x-px>=-wdt/2 and wdt/2>=y-py>=-wdt/2:
                can.delete(wataba)
                del(element.listObj[index[0]].listPen[index[1]][index[2]])
                del(element.listObj[index[0]].x[index[1]][index[2]])
                del(element.listObj[index[0]].y[index[1]][index[2]])
                if len(element.listObj[index[0]].listPen[index[1]])==0:
                    del(element.listObj[index[0]].listPen[index[1]])
                    del(element.listObj[index[0]].x[index[1]])
                    del(element.listObj[index[0]].y[index[1]])
                    del(element.listObj[index[0]].config[index[1]])
    pf.Assign(can, t, ['Button1-Motion', 'Double-1'])

def setPolygon():
    setArrow()
    ObjectDialog(fen, can)

def setLine(event=None):
    setArrow()
    ObjectDialog(fen, can, method='line')

def setTriangle1(event=None):
    global select, opt2D
    setArrow()
    setChoosen()
    element.addObj(addTriEq(can, can.winfo_width()/2, can.winfo_height()/2))
    opt2D=option2D.Option2D(frOpt.frame, element.listObj[-1], command=setHistory)
    opt2D.setOption()
    minx, maxx=min(element.listObj[-1].x), max(element.listObj[-1].x)
    miny, maxy=min(element.listObj[-1].y), max(element.listObj[-1].y)
    x, y = minx+(maxx-minx)/2, miny+(maxy-miny)/2
    wdt, hgt=maxx-minx, maxy-miny
    select=pf.Select(can, x, y, wdt, hgt, element.listObj[-1])
    select.setSelector()
    select.setSize()
    select.setCoords(x, y)

def setTriangle2(event=None):
    global select, opt2D
    setArrow()
    setChoosen()
    element.addObj(addTriRec(can, can.winfo_width()/2, can.winfo_height()/2))
    opt2D=option2D.Option2D(frOpt.frame, element.listObj[-1], command=setHistory)
    opt2D.setOption()
    minx, maxx=min(element.listObj[-1].x), max(element.listObj[-1].x)
    miny, maxy=min(element.listObj[-1].y), max(element.listObj[-1].y)
    x, y = minx+(maxx-minx)/2, miny+(maxy-miny)/2
    wdt, hgt=maxx-minx, maxy-miny
    select=pf.Select(can, x, y, wdt, hgt, element.listObj[-1])
    select.setSelector()
    select.setSize()
    select.setCoords(x, y)

def setSquare(event=None):
    global select, opt2D
    setArrow()
    setChoosen()
    element.addObj(addSquare(can, can.winfo_width()/2, can.winfo_height()/2))
    opt2D=option2D.Option2D(frOpt.frame, element.listObj[-1], command=setHistory)
    opt2D.setOption()
    minx, maxx=min(element.listObj[-1].x), max(element.listObj[-1].x)
    miny, maxy=min(element.listObj[-1].y), max(element.listObj[-1].y)
    x, y = minx+(maxx-minx)/2, miny+(maxy-miny)/2
    wdt, hgt=maxx-minx, maxy-miny
    select=pf.Select(can, x, y, wdt, hgt, element.listObj[-1])
    select.setSelector()
    select.setSize()
    select.setCoords(x, y)

def setPenta(event=None):
    global select, opt2D
    setArrow()
    setChoosen()
    element.addObj(addPenta(can, can.winfo_width()/2, can.winfo_height()/2))
    opt2D=option2D.Option2D(frOpt.frame, element.listObj[-1], command=setHistory)
    opt2D.setOption()
    minx, maxx=min(element.listObj[-1].x), max(element.listObj[-1].x)
    miny, maxy=min(element.listObj[-1].y), max(element.listObj[-1].y)
    x, y = minx+(maxx-minx)/2, miny+(maxy-miny)/2
    wdt, hgt=maxx-minx, maxy-miny
    select=pf.Select(can, x, y, wdt, hgt, element.listObj[-1])
    select.setSelector()
    select.setSize()
    select.setCoords(x, y)

def setHexa(event=None):
    global select, opt2D
    setArrow()
    setChoosen()
    element.addObj(addHexa(can, can.winfo_width()/2, can.winfo_height()/2))
    opt2D=option2D.Option2D(frOpt.frame, element.listObj[-1], command=setHistory)
    opt2D.setOption()
    minx, maxx=min(element.listObj[-1].x), max(element.listObj[-1].x)
    miny, maxy=min(element.listObj[-1].y), max(element.listObj[-1].y)
    x, y = minx+(maxx-minx)/2, miny+(maxy-miny)/2
    wdt, hgt=maxx-minx, maxy-miny
    select=pf.Select(can, x, y, wdt, hgt, element.listObj[-1])
    select.setSelector()
    select.setSize()
    select.setCoords(x, y)

def setOval(evnt=None):
    global select, opt2D
    setArrow()
    setChoosen()
    element.addObj(addCircle(can, can.winfo_width()/2, can.winfo_height()/2))
    opt2D=option2D.Option2D(frOpt.frame, element.listObj[-1], command=setHistory)
    opt2D.setOption()
    minx, maxx=min(element.listObj[-1].x), max(element.listObj[-1].x)
    miny, maxy=min(element.listObj[-1].y), max(element.listObj[-1].y)
    x, y = minx+(maxx-minx)/2, miny+(maxy-miny)/2
    wdt, hgt=maxx-minx, maxy-miny
    select=pf.Select(can, x, y, wdt, hgt, element.listObj[-1])
    select.setSelector()
    select.setSize()
    select.setCoords(x, y)

def setArc(event=None):
    global select, opt2D
    setArrow()
    setChoosen()
    element.addObj(addArc(can, can.winfo_width()/2, can.winfo_height()/2))
    opt2D=option2D.Option2D(frOpt.frame, element.listObj[-1], command=setHistory)
    opt2D.setOption()
    minx, maxx=min(element.listObj[-1].x), max(element.listObj[-1].x)
    miny, maxy=min(element.listObj[-1].y), max(element.listObj[-1].y)
    x, y = minx+(maxx-minx)/2, miny+(maxy-miny)/2
    wdt, hgt=maxx-minx, maxy-miny
    select=pf.Select(can, x, y, wdt, hgt, element.listObj[-1])
    select.setSelector()
    select.setSize()
    select.setCoords(x, y)

def setText(event=None):
    global select, opt2D
    setArrow()
    setChoosen()
    element.addObj(addText(can, can.winfo_width()/2, can.winfo_height()/2))
    opt2D=option2D.Option2D(frOpt.frame, element.listObj[-1], command=setHistory)
    opt2D.setOption()
    x, y = element.listObj[-1].x[0], element.listObj[-1].y[0]
    wdt, hgt=len(element.listObj[-1].text)*element.listObj[-1].size, element.listObj[-1].size
    select=pf.Select(can, x, y, wdt, hgt, element.listObj[-1])
    select.setSelector()
    select.setSize()
    select.setCoords(x, y)

def setWindow(event=None):
    global select, opt2D
    setArrow()
    setChoosen()
    element.addObj(addWindow(can, can.winfo_width()/2, can.winfo_height()/2))
    opt2D=option2D.Option2D(frOpt.frame, element.listObj[-1])
    opt2D.setOption()
    element.listObj[-1].option2W=option2W.Option2W(opt2D.fr5, element.listObj[-1].window)
    element.listObj[-1].option2W.setOption()
    x, y = element.listObj[-1].x[0], element.listObj[-1].y[0]
    wdt, hgt=element.listObj[-1].width, element.listObj[-1].height
    select=pf.Select(can, x, y, wdt, hgt, element.listObj[-1])
    select.setSelector()
    select.setSize()
    select.setCoords(x, y)
    
def setImage(event=None):
    global select, opt2D
    setArrow()
    setChoosen()
    a=fd.askopenfilename(title=getLang('select an image'),
                        filetypes=[
                                    ("Images", "*.png *.jpg *.jpeg *.gif *.bmp  *.webp *.webm *.cur"),
                                    ("PNG files", "*.png"),
                                    ("JPEG files", "*.jpg *.jpeg"),
                                    ("GIF files", "*.gif"),
                                    ("BMP files", "*.bmp"),
                                    ("WEBP files", "*.webp"),
                                    ("WEBM files", "*.webm"),
                                    ("CUR files", "*.cur")
                                                            ])
    if a:
        element.addObj(addImage(can, can.winfo_width()/2, can.winfo_height()/2, a))
        opt2D=option2D.Option2D(frOpt.frame, element.listObj[-1], command=setHistory)
        opt2D.setOption()
        x, y = element.listObj[-1].x[0], element.listObj[-1].y[0]
        wdt, hgt=element.listObj[-1].width, element.listObj[-1].height
        select=pf.Select(can, x, y, wdt, hgt, element.listObj[-1])
        select.setSelector()
        select.setSize()
        select.setCoords(x, y)

def setGrid(event=None):
    if varGrid.get():
        grid.view()
    else:
        grid.hide()

def setThemeToButton(button, active=True):
    button['bg']=pf.COLORS['--dark-color']
    button['fg']=pf.COLORS['--light-color']
    try:
        button['activebackground']=pf.COLORS['--dark-color-1']
        button['activeforeground']=pf.COLORS['--light-color']
    except:pass
    button['highlightbackground']=pf.COLORS['--dark-color-1']
    button['highlightcolor']=pf.COLORS['--light-color']
    button['highlightthickness']=0
    button['bd']=0
    button['relief']='sunken'
    if active:
        pf.ActiveLeave(button, pf.COLORS['--light-color-1'], pf.COLORS['--light-color'])
    button['font']=Font(family=pf.POLICE[0], size=12, weight='bold')
    try:
        button['selectcolor']=pf.COLORS['--dark-color-1']
    except:pass

def back(event=None):
    unsassign1()
    setArrow()
    if len(history.listBack)>0:
        l=[]
        for ww in range(len(element.listObj)):
            if element.listObj[ww].type!='pen':
                l.append(element.listObj[ww].getAll())
            else:
                l.append(['pen', None])
        for ww in range(len(history.listBack[-1])):
            if history.listBack[-1][ww][0]!='pen':
                element.listObj[ww].setAll(history.listBack[-1][ww])
                if 'hidden' in history.listBack[-1][ww]:
                    listBar.remove_widget(element.listEntry[ww][1])
                else:
                    listBar.regrid_widget(element.listEntry[ww][1])
        history.setBack(l)
    else:
        bBack['stat']='disabled'

def ward(event=None):
    unsassign1()
    setArrow()
    if len(history.listWard):
        l=[]
        for ww in range(len(element.listObj)):
            if element.listObj[ww].type!='pen':
                l.append(element.listObj[ww].getAll())
            else:
                l.append(['pen', None])
        for ww in range(len(history.listWard[-1])):
            if history.listWard[-1][ww][0]!='pen':
                element.listObj[ww].setAll(history.listWard[-1][ww])
                if 'hidden' in history.listWard[-1][ww]:
                    listBar.remove_widget(element.listEntry[ww][1])
                else:
                    listBar.regrid_widget(element.listEntry[ww][1])
        history.setWard(l)
    else:
        bForward['stat']='disabled'

def setHistory():
    if element.listObj:
        l=[]
        for ww in element.listObj:
            if ww.type!='pen':
                l.append(ww.getAll())
            else:
                l.append(['pen', None])
        history.setHistory(l)
        bForward['stat']='disabled'

def deleteObj(event=None):
    global opt2D
    if select:
        setHistory()
        if type(select)==type([]):
            for ww in select:
                ind=element.listObj.index(ww.obj)
                element.listObj[ind].setStat('hidden')
                listBar.remove_widget(element.listEntry[ind][1])
        else:
            ind=element.listObj.index(select.obj)
            element.listObj[ind].setStat('hidden')
            listBar.remove_widget(element.listEntry[ind][1])
        for ww in frOpt.frame.winfo_children():
            ww.destroy()
        opt2D=None
        unsassign1()
        setArrow()

def duplicateObj(event=None):
    global select, opt2D
    if select:
        if type(select)==type([]):
            l=[]
            for ww in select:
                l.append(ww.obj.getAll())
            u=list()
            for ww in l:
                if ww[0] in ['line', 'arc', 'polygon', 'oval', 'text']:
                    aa=object2D.listOfObject[ww[0]](can, ww[1], ww[2])
                elif ww[0]=='picture':
                    aa=object2D.listOfObject[ww[0]](can, ww[1], ww[2], ww[3])
                elif ww[0]=='window':
                    aa=object2D.listOfObject[ww[0]](can, ww[1], ww[2], object2W.Button2W(can))
                aa.setAll(ww)
                x=aa.pointx
                y=aa.pointy
                x=x-50 if x>can.winfo_width()/2 else x+50
                y=y-50 if y>can.winfo_height()/2 else y+50
                aa.moveTo(x, y)
                aa.setStat('hidden')
                u.append(aa)
            element.addMultipleObj(u)
            unsassign1()
            setArrow()
            setChoosen()
            select=[]
            for ww in u:
                ww.setStat('normal')
                if ww.type in ['line', 'arc', 'polygon', 'oval']:
                    wdt=max(ww.x)-min(ww.x)
                    hgt=max(ww.y)-min(ww.y)
                else:
                    wdt=ww.width if ww.type!='text' else len(ww.text)*ww.size
                    hgt=ww.height if ww.type!='text' else ww.text.count('\n')*ww.size
                select.append(pf.Select(can, ww.pointx, ww.pointy, wdt, hgt, ww))
                select[-1].setSelector()
                select[-1].setSize()
                select[-1].setCoords(ww.pointx, ww.pointy)
        else:
            ww=select.obj.getAll()
            unsassign1()
            setArrow()
            setChoosen()
            if ww[0] in ['line', 'arc', 'polygon', 'oval', 'text']:
                aa=object2D.listOfObject[ww[0]](can, ww[1], ww[2])
            elif ww[0]=='picture':
                aa=object2D.listOfObject[ww[0]](can, ww[1], ww[2], ww[3])
            elif ww[0]=='window':
                aa=object2D.listOfObject[ww[0]](can, ww[1], ww[2], object2W.Button2W(can))
            aa.setAll(ww)
            x=aa.pointx
            y=aa.pointy
            x=x-50 if x>can.winfo_width()/2 else x+50
            y=y-50 if y>can.winfo_height()/2 else y+50
            aa.moveTo(x, y)
            aa.setStat('hidden')
            element.addObj(aa)
            aa.setStat('normal')
            ww=aa
            if ww.type in ['line', 'arc', 'polygon', 'oval']:
                wdt=max(ww.x)-min(ww.x)
                hgt=max(ww.y)-min(ww.y)
            else:
                wdt=ww.width if ww.type!='text' else len(ww.text)*ww.size
                hgt=ww.height if ww.type!='text' else ww.text.count('\n')*ww.size
            opt2D=option2D.Option2D(frOpt.frame, ww)
            opt2D.setOption()
            if ww.type=='window':
                aa.option2W=option2W.Option2W(opt2D.fr5, ww.window, command=setHistory)
                aa.option2W.setOption()
            select=pf.Select(can, ww.pointx, ww.pointy, wdt, hgt, ww)
            select.setSelector()
            select.setSize()
            select.setCoords(ww.pointx, ww.pointy)

def copyObj(event=None):
    if select:
        if type(select)==type(list()):
            l=[]
            for ww in select:
                l.append(ww.obj)
            copy.copy(l.copy())
        else:
            copy.copy([select.obj].copy())

def pastObj(event=None):
    a=copy.past()
    setHistory()
    for ww in a:
        ww.setStat('normal')

def liftObj(event=None):
    if select:
        if type(select)==type(list()):
            for ww in select:
                can.lift(ww.obj.object)
                element.listLift.append(ww.obj)
        else:
            can.lift(select.obj.object)
            element.listLift.append(select.obj)

def setMirrorX(event=None):
    if select:
        if type(select)==type(list()):
            for ww in select:
                obj=ww.obj
                if obj.type in ['line', 'oval', 'polygon', 'arc']:
                    mir=getMirror(obj.x, obj.y, obj.pointx, obj.pointy)
                    obj.setCoords(mir[0], mir[1])
        else:
            obj=select.obj
            if obj.type in ['line', 'oval', 'polygon', 'arc']:
                    lx=[]
                    ly=[]
                    mir=getMirror(obj.x, obj.y, obj.pointx, obj.pointy)
                    obj.setCoords(mir[0], mir[1])
        setHistory()

def setMirrorY(event=None):
    if select:
        if type(select)==type(list()):
            for ww in select:
                obj=ww.obj
                if obj.type in ['line', 'oval', 'polygon', 'arc']:
                    mir=getMirror(obj.x, obj.y, obj.pointx, obj.pointy, 'y')
                    obj.setCoords(mir[0], mir[1])
        else:
            obj=select.obj
            if obj.type in ['line', 'oval', 'polygon', 'arc']:
                    lx=[]
                    ly=[]
                    mir=getMirror(obj.x, obj.y, obj.pointx, obj.pointy, 'y')
                    obj.setCoords(mir[0], mir[1])
        setHistory()

def setMirrorXY(event=None):
    if select:
        if type(select)==type(list()):
            for ww in select:
                obj=ww.obj
                if obj.type in ['line', 'oval', 'polygon', 'arc']:
                    mir=getMirror(obj.x, obj.y, obj.pointx, obj.pointy, 'xy')
                    obj.setCoords(mir[0], mir[1])
        else:
            obj=select.obj
            if obj.type in ['line', 'oval', 'polygon', 'arc']:
                    lx=[]
                    ly=[]
                    mir=getMirror(obj.x, obj.y, obj.pointx, obj.pointy, 'xy')
                    obj.setCoords(mir[0], mir[1])
        setHistory()

def setPoint(event=None):
    global focus
    if select and type(select)!=type([]):
        a=select.obj
        if a.type in ['line', 'oval', 'arc', 'polygon']:
            setArrow()
            can['cursor']='circle'
            varButton.set('verstice')
            focus=ModifyPoint(can, a)
            focus.assign()
            def u(event):
                global focus
                focus.destroy()
                setHistory()
                focus=ModifyPoint(can, a)
                focus.assign()
            pf.Assign(can, u, ['ButtonRelease-1'])
            def t(event):
                global select
                setArrow()
                setChoosen()
                select=pf.Select(can, a.pointx, a.pointy, max(a.x)-min(a.x), max(a.y)-min(a.y), a)
                select.setSelector()
                select.setSize()
                select.setCoords(a.pointx, a.pointy)
                pf.Assign(fen, setPoint, ['Control-Shift-E', 'Control-Shift-e'])
            pf.Assign(fen, t, ['Control-Shift-E', 'Control-Shift-e'])

def setBgColor(button):
    color=button['bg']
    a=pf.Couleur(color).assigne()
    if a:
        can['bg']=a
        button['bg']=a

def setSize(size, event=None):
    global sizeX, sizeY
    try:
        sizeX.set(int(eval(str(size[0]))) if 100<=eval(str(size[0]))<=int(can.winfo_width()) else can.winfo_width())
    except Exception as e:
        print(e)
        sizeX.set(can.winfo_width())
    try:
        sizeY.set(int(eval(str(size[1]))) if 100<eval(str(size[1]))<=int(can.winfo_height()) else can.winfo_height())
    except:
        sizeY.set(can.winfo_height())

def setNew(event=None):
    global opt2D
    setArrow()
    if history:
        history.clear()
    if element:
        element.clear()
    grid.hide()
    opt2D=None
    can['bg']='white'
    sizeX.set(can.winfo_width())
    sizeY.set(can.winfo_height())
    colorMode.set(False)
    bBg['bg']='white'
    try:
        for ww in frOpt.frame.winfo_children():
            ww.destroy()
    except:
        pass
    fen.labCoords['text']='X: Y: \tObject: '
    fen.title('Dynamic Draw')

def checkNew(event=None):
    if len(element.listObj)>0 or len(history.listBack)>0 or len(history.listWard)>0:
        a=tkmsg.askyesno(getLang('new'), getLang('thereisanotherworkinprogressdoyouwanttocreateanotherone'))
        if a:
            setNew()
        else:pass
    else:setNew()

def saveAsFile(event=None):
    global file
    title='untitled.dynd'
    a=1
    while os.path.exists(title):
        title='untitled-%s'%a+'.dynd'
        a+=1
    file_path = fd.asksaveasfilename(
        defaultextension=".dynd",
        filetypes=[("Dynd files", "*.dynd")],
        initialfile=title,
        title=getLang('saveas'))
    if file_path:
        l=[]
        u=[]
        if len(element.listObj)>0:
            for ww in element.listObj:
                l.append(ww.getAll())
                if ww.type=='window':
                    l[-1][3]=ww.window.type
        for ww in element.listLift:
            if ww.type!='pen':
                u.append([ww.type, ww.tag, ww.name])
            else:
                u.append(['pen', None])
        try:
            writeFile([l, u, can['bg'], colorMode.get()], file_path)
            file=file_path
            pf.Message(fen.labError, message='Saved', fond=pf.COLORS['--dark-color'], coul=pf.COLORS['--dark-blue']).affiche()
        except Exception as e:
            pf.Message(fen.labError, message='Failed to save', fond=pf.COLORS['--dark-color'], coul='red').affiche()
            print(e)
    return file_path

def saveFile(event=None):
    global file
    if file:
        l=[]
        u=[]
        if len(element.listObj)>0:
            for ww in element.listObj:
                l.append(ww.getAll())
                if ww.type=='window':
                    l[-1][3]=ww.window.type
        for ww in element.listLift:
            if ww.type!='pen':
                u.append([ww.type, ww.tag, ww.name])
            else:
                u.append(['pen', None])
        try:
            writeFile([l, u, can['bg'], colorMode.get()], file)
            file=file
            pf.Message(fen.labError, message='Saved', fond=pf.COLORS['--dark-color'], coul=pf.COLORS['--dark-blue']).affiche()
        except Exception as e:
            pf.Message(fen.labError, message='Failed to save', fond=pf.COLORS['--dark-color'], coul='red').affiche()
            print(e)
    return file

def setSaveFile(event=None):
    if file:
        if os.path.exists(file):
            a=saveFile()
        else:
            a=saveAsFile()
    else:
        a=saveAsFile()
    return a

def openFile(event=None):
    global file
    if file:
        if file.split('.')[-1]!='dynd':
            file=None
    file_path = fd.askopenfilename(
        defaultextension=".dynd",
        filetypes=[("Dynd files", "*.dynd")], 
        initialfile=file,
        title=getLang('open'))
    if file_path:
        l=readFile(file_path)
        if type(l)!=type([]):
            tkmsg.showerror(getLang('error'), getLang('unabletoreadfile'))
        else:
            try:
                setNew()
                can['bg']=l[2]
                bBg['bg']=l[2]
                colorMode.set(l[3])
                u=[]
                for ww in l[0]:
                    if ww[0] in ['line', 'text', 'oval', 'polygon', 'arc']:
                        u.append(object2D.listOfObject[ww[0]](can, ww[1], ww[2]))
                    elif ww[0]=='window':
                        u.append(object2D.listOfObject[ww[0]](can, ww[1], ww[2], object2W.Button2W(can)))
                    elif ww[0]=='picture':
                        u.append(object2D.listOfObject[ww[0]](can, ww[1], ww[2], ww[3]))
                    elif ww[0]=='pen':
                        u.append(object2D.listOfObject[ww[0]](can))
                    u[-1].setAll(ww)
                element.addMultipleObj(u)
                element.listLift=[]
                for ww in l[1]:
                    if ww[0]!='pen':
                        for xx in element.listObj:
                            if xx.type==ww[0] and xx.name==ww[2]:
                                can.lift(xx.object)
                                element.listLift.append(xx)
                                break
                setArrow()
                file=file_path
                fen.title('Dynamic Draw - file:'+file)
                pf.Message(fen.labError, message='File opened', fond=pf.COLORS['--dark-color'], coul=pf.COLORS['--dark-blue']).affiche()
            except Exception as e:
                tkmsg.showerror(getLang('error'), getLang('unabletoreadfile'))
                pf.Message(fen.labError, message='Failed to open', fond=pf.COLORS['--dark-color'], coul=pf.COLORS['--dark-red']).affiche()
                print(e)

def manualOpenFile(dir):
    try:
        l=readFile(dir)
        if type(l)!=type([]):
            tkmsg.showerror(getLang('error'), getLang('unabletoreadfile'))
        else:
            try:
                setNew()
                can['bg']=l[2]
                bBg['bg']=l[2]
                colorMode.set(l[3])
                u=[]
                for ww in l[0]:
                    if ww[0] in ['line', 'text', 'oval', 'polygon', 'arc']:
                        u.append(object2D.listOfObject[ww[0]](can, ww[1], ww[2]))
                    elif ww[0]=='window':
                        u.append(object2D.listOfObject[ww[0]](can, ww[1], ww[2], object2W.Button2W(can)))
                    elif ww[0]=='picture':
                        u.append(object2D.listOfObject[ww[0]](can, ww[1], ww[2], ww[3]))
                    elif ww[0]=='pen':
                        u.append(object2D.listOfObject[ww[0]](can))
                    u[-1].setAll(ww)
                element.addMultipleObj(u)
                element.listLift=[]
                for ww in l[1]:
                    if ww[0]!='pen':
                        for xx in element.listObj:
                            if xx.type==ww[0] and xx.name==ww[2]:
                                can.lift(xx.object)
                                element.listLift.append(xx)
                                break
                setArrow()
                file=dir
                fen.title('Dynamic Draw - file:'+file)
                pf.Message(fen.labError, message='File opened', fond=pf.COLORS['--dark-color'], coul=pf.COLORS['--dark-blue']).affiche()
            except Exception as e:
                tkmsg.showerror(getLang('error'), getLang('unabletoreadfile'))
                pf.Message(fen.labError, message='Failed to open', fond=pf.COLORS['--dark-color'], coul=pf.COLORS['--dark-red']).affiche()
                print(e)
    except Exception as e:
        tkmsg.showerror(getLang('error'), getLang('unabletoreadfile'))
        print(e)

def exit(event=None):
    if len(element.listObj)>0 or len(history.listBack)>0 or len(history.listWard)>0:
        ask=tkmsg.askyesnocancel(getLang('closing'), getLang('doyouwanttosave'))
        if ask is True:
            a=setSaveFile()
            if a:
                fen.destroy()
        elif ask is False:
            fen.destroy()
        else:pass
    else:
        fen.destroy()
    clearDir('temps')

def setLangue(lang):
    if currentLang!=dicoLANG_NAME[lang]:
        language.setLang(dicoLANG_NAME[lang])
        writeFile(language.lang, 'language.ini')
        ask=tkmsg.askokcancel(getLang('restart'), getLang('the program must restart to apply the change'))
        if ask:
            restartProgram()

def setCapture(event=None):
    global ifRender
    if not ifRender:
        ifRender=True
        fen.geometry('+0+0')
        def after():
            top=Toplevel(fen)
            top.geometry(f'{pf.Get(can).x()}x{pf.Get(can).y()}+0+0')
            top.attributes('-topmost', True)
            top.grab_set()
            top.wm_attributes('-fullscreen', True)
            top['bg']=can['bg']
            render=Canvas(top, width=pf.Get(can).x(), height=pf.Get(can).x(), bg=can['bg'], bd=0, highlightthickness=0, relief='flat')
            render.grid(row=1, column=1, sticky='nsew')
            if len(element.listObj)>0:
                l=[]
                for ww in element.listObj:
                    if ww.type=='pen':
                        a=object2D.listOfObject[ww.type](render)
                    elif ww.type=='window':
                        a=object2D.listOfObject[ww.type](render, ww.x, ww.y, object2W.Button2W(render))
                    elif ww.type=='picture':
                        a=object2D.listOfObject[ww.type](render, ww.x, ww.y, ww.defaultImage)
                    else:
                        a=object2D.listOfObject[ww.type](render, ww.x, ww.y)
                    a.setAll(ww.getAll())
                    l.append(a)
                for ww in element.listLift:
                    for xx in l:
                        if xx.type!='pen':
                            if ww.type==xx.type and ww.name==xx.name:
                                render.lift(xx.object)
                                break
                pf.Unsassign(render, ['Button-1', 'ButtonRelease-1', 'Button1-Motion', 'Button-3', 'Leave']) 
            time=pf.Temps()
            temp=os.path.join('temps', 'temps%s.%s'%(str(time.an())+str(time.mois())+str(time.jour())+str(time.heure())+str(time.minute())+str(time.seconde())+str(time.micros()), 'png'))
            capture.capturer_canvas(top, can, temp)
            if colorValue==True:
                finalTemp=capture.BlackWhite(temp).toIMG(temp)
            else:
                finalTemp=temp
            image=object2D.Picture(render, [int(render.winfo_width()/2)], [int(render.winfo_height())/2], finalTemp)
            image.setImage(width=int(pf.Get(render).x()), height=int(pf.Get(render).y()))
            top.wm_attributes('-fullscreen', False)
            def save(event=None):
                file_path = fd.asksaveasfilename(
                    defaultextension=".png",
                    filetypes=[("PNG files", "*.png"),
                        ("JPEG files", "*.jpg;*.jpeg"),
                        ("GIF files", "*.gif"),
                        ("BMP files", "*.bmp"),
                        ("WEBP files", "*.webp"),
                        ("CUR files", "*.cur")],
                    title=getLang("Sauvegarder l'image sous"))
                if file_path:
                    x=image.width
                    y=image.height
                    try:
                        x=int(eval(str(sizeX.get())))
                        if not 100<=x<=int(pf.Get(render).x()):
                            x=int(pf.Get(render).x())
                    except:
                        pass
                    try:
                        y=int(eval(str(sizeY.get())))
                        if not 100<=y<=int(pf.Get(render).y()):
                            y=int(pf.Get(render).y())
                    except:
                        pass
                    img=object2D.ModSize(finalTemp).setSize(x, y)[1][0]
                    capture.ImgToImg(img).toIMG(file_path)
                    close()
            menu=Menu(top, bg=pf.COLORS['--dark-color'], fg='white')
            top['menu']=menu
            menu.add_command(label=getLang('save'), accelerator='Ctrl+S', command=save)
            #top.resizable(False, False)
            pf.Assign(top, save, ['Control-s', 'Control-S'])
            def close():
                global ifRender
                ifRender=False
                top.grab_release()
                top.destroy()
            top.protocol('WM_DELETE_WINDOW', close)
        fen.after(500, after)

def move(event=None):
        if select:
            if type(select)==type([]):
                pf.Message(fen.labError, message=getLang('cannotmovemorethantwoobjects'), temps=4, fond=fen.labError['bg'], coul='red').affiche()
            else:
                can['cursor']='fleur'
                select.obj.moveTo(event.x, event.y)
                select.setCoords(-1000)

def unmove(event=None):
    global select
    if select:
        if type(select)!=type([]):
            a=select.obj
            object=a
            setSelector()
            setChoosen()
            x=min(object.x)+(max(object.x)-min(object.x))/2
            y=min(object.y)+(max(object.y)-min(object.y))/2
            if object.type in ['line', 'arc', 'polygon', 'oval']:
                wdt=(max(object.x)-min(object.x))
                hgt=(max(object.y)-min(object.y))
            else:
                wdt=object.width if object.type!='text' else len(object.text)*object.size
                hgt=object.height if object.type!='text' else object.size*1.5
            select=pf.Select(can, x, y, wdt, hgt, object)
            select.setSelector()
            select.setSize()
            select.setCoords(x, y)
            opt2D=option2D.Option2D(frOpt.frame, object)
            opt2D.setOption()
            if object.type=='window':
                object.option2W=option2W.Option2W(opt2D.fr5, object.window, command=setHistory).setOption()

def setHelp(event=None):
    import variable as var
    temp='temps\\help.html'
    with open(temp, 'w') as f:
        f.write(var.html)
    wb.open_new_tab(temp)
          
def actualizeData(event=None):
    if opt2D and len(element.listObj)>0:
        if opt2D.obj.type!='pen':
            obj=element.listObj[element.listObj.index(opt2D.obj)]
            x=min(obj.x)+(max(obj.x)-min(obj.x))/2
            y=min(obj.y)+(max(obj.y)-min(obj.y))/2
            opt2D.varX.set(x)
            opt2D.varY.set(y)
            if obj.type in ['window', 'picture']:
                wdt=obj.width
                hgt=obj.height
                opt2D.varWdt.set(wdt)
                opt2D.varHeight.set(hgt)
            if not obj.type in ['pen', 'window', 'arc']:
                ang=obj.angle
                opt2D.varAngle.set(ang)
            opt2D.varName.set(obj.name)

##########

def setTaskBar():
    global varButton, varGrid, bBack, bForward
    fr1=Frame(taskBar, width=15, height=taskBar['height'], bg=pf.COLORS['--dark-color'], bd=0, highlightthickness=0)
    fr2=Frame(fr1, width=15, height=taskBar['height'], bg=pf.COLORS['--dark-color'], bd=0, highlightthickness=0)
    fr3=Frame(fr1, width=15, height=taskBar['height'], bg=pf.COLORS['--dark-color'], bd=0, highlightthickness=0)
    fr4=Frame(fr1, width=15, height=taskBar['height'], bg=pf.COLORS['--dark-color'], bd=0, highlightthickness=0)
    ###################
    bBack=Button(fr1, text=chr(57510), width=0, command=back, state='normal' if history.listBack else 'disabled')
    bForward=Button(fr1, text=chr(57515), width=0, command=ward, state='normal' if history.listWard else 'disabled')
    setThemeToButton(bBack, False)
    setThemeToButton(bForward, False)
    bBack['fg']=pf.COLORS['--light-blue']
    bForward['fg']=pf.COLORS['--light-blue']
    bBack.grid(row=1, column=1, sticky='nsew', pady=5, padx=2)
    bForward.grid(row=1, column=2, sticky='nsew', pady=5, padx=2)
    fr1.grid(row=1, column=1, sticky='w')
    Canvas(fr1, bg=pf.COLORS['--dark-color'], bd=0, highlightthickness=0, height=40, width=20).grid(row=2, column=1, columnspan=2)
    
    ##################################
    varButton=StringVar(value='arrow')
    varGrid=IntVar(value=False)
    bArrow=Radiobutton(fr2, text=chr(59568), width=3, command=setArrow, value='arrow', variable=varButton,
                          indicatoron=False)
    bArrow.grid(row=1, column=1, padx=2, pady=2)
    setThemeToButton(bArrow)
    bSelector=Radiobutton(fr2, text=chr(57609), width=3, command=setSelector, value='selector', variable=varButton,
                          indicatoron=False)
    bSelector.grid(row=1, column=2, padx=2, pady=2)
    setThemeToButton(bSelector)
    bChoosen=Radiobutton(fr2, text=chr(59882), width=3, command=setChoosen, value='choosen', variable=varButton,
                          indicatoron=False)
    bChoosen.grid(row=1, column=3, padx=2, pady=2)
    setThemeToButton(bChoosen)
    bPen=Radiobutton(fr2, text=chr(59151), width=3, command=setPen, value='pen', variable=varButton, 
                     indicatoron=False)
    bPen.grid(row=2, column=1, padx=2, pady=2)
    setThemeToButton(bPen)
    bErase=Radiobutton(fr2, text=chr(59228), width=3, command=setErase, value='erase', variable=varButton, 
                     indicatoron=False)
    bErase.grid(row=2, column=2, padx=2, pady=2)
    setThemeToButton(bErase)
    bGrid=Checkbutton(fr2, text=chr(59402), width=3, command=setGrid, variable=varGrid, 
                     indicatoron=False)
    bGrid.grid(row=2, column=3, padx=2, pady=2)
    setThemeToButton(bGrid)
    fr2.grid(row=1, column=3, sticky='w', padx=30)
    
    ########################################
    bLine=Button(fr3, text=chr(9586), width=3, command=setLine)
    bLine.grid(row=1, column=1, padx=2, pady=2)
    setThemeToButton(bLine)
    bPolygon=Button(fr3, text=chr(9626), width=3, command=setPolygon)
    bPolygon.grid(row=1, column=2, padx=2, pady=2)
    setThemeToButton(bPolygon)
    bTriaEq=Button(fr3, text=chr(9650), width=3, command=setTriangle1)
    bTriaEq.grid(row=1, column=3, padx=2, pady=2)
    setThemeToButton(bTriaEq)
    bTriaRec=Button(fr3, text=chr(9699), width=3, command=setTriangle2)
    bTriaRec.grid(row=1, column=4, padx=2, pady=2)
    setThemeToButton(bTriaRec)
    bSquare=Button(fr3, text=chr(9632), width=3, command=setSquare)
    bSquare.grid(row=1, column=5, padx=2, pady=2)
    setThemeToButton(bSquare)
    bPenta=Button(fr3, text=chr(11039), width=3, command=setPenta)
    bPenta.grid(row=1, column=6, padx=2, pady=2)
    setThemeToButton(bPenta)
    bHexa=Button(fr3, text=chr(11042), width=3, command=setHexa)
    bHexa.grid(row=2, column=1, padx=2, pady=2)
    setThemeToButton(bHexa)
    bOval=Button(fr3, text=chr(9899), width=3, command=setOval)
    bOval.grid(row=2, column=2, padx=2, pady=2)
    setThemeToButton(bOval)
    bArc=Button(fr3, text=chr(8978), width=3, command=setArc)
    bArc.grid(row=2, column=3, padx=2, pady=2)
    setThemeToButton(bArc)
    bText=Button(fr3, text='abc', width=3, command=setText)
    bText.grid(row=2, column=4, padx=2, pady=2)
    setThemeToButton(bText)
    bWindow=Button(fr3, text=chr(128377), width=3, command=setWindow)
    bWindow.grid(row=2, column=5, padx=2, pady=2)
    setThemeToButton(bWindow)
    bImage=Button(fr3, text=chr(59305), width=3, command=setImage)
    bImage.grid(row=2, column=6, padx=2, pady=2)
    setThemeToButton(bImage)
    fr3.grid(row=1, column=4, sticky='w', padx=10)
    
    pf.Assign(fen, back, ['Alt-Left'])
    pf.Assign(fen, forward, ['Alt-Right'])

def setCmd():
    global varButton
    bLift=Button(frCmd.frame, text=getLang('lift')+'\t'+chr(57490), width=20, command=liftObj)
    setThemeToButton(bLift)
    bLift.grid(row=1, column=1, sticky='w', padx=5, pady=5, columnspan=2)
    bClone=Button(frCmd.frame, text=getLang('duplicate')+'\t'+chr(57548), width=20, command=duplicateObj)
    setThemeToButton(bClone)
    bClone.grid(row=2, column=1, sticky='w', padx=5, pady=5, columnspan=2)
    bCopy=Button(frCmd.frame, text=getLang('copy')+'\t'+chr(59683), width=10, command=copyObj)
    setThemeToButton(bCopy)
    bCopy.grid(row=3, column=1, sticky='w', padx=0, pady=5)
    bPast=Button(frCmd.frame, text=getLang('past')+'\t'+chr(59689), width=10, command=pastObj)
    setThemeToButton(bPast)
    bPast.grid(row=3, column=2, sticky='w', padx=0, pady=5)
    bInvertX=Button(frCmd.frame, text=getLang('mirror')+' X\t'+chr(57549), width=14, command=setMirrorX)
    setThemeToButton(bInvertX)
    bInvertX.grid(row=4, column=1, sticky='nsew', padx=5, pady=5, columnspan=2)
    bInvertY=Button(frCmd.frame, text=getLang('mirror')+' Y\t'+chr(57549), width=14, command=setMirrorY)
    setThemeToButton(bInvertY)
    bInvertY.grid(row=5, column=1, sticky='nsew', padx=5, pady=0, columnspan=2)
    bInvertXY=Button(frCmd.frame, text=getLang('mirror')+' XY\t'+chr(57549), width=14, command=setMirrorXY)
    setThemeToButton(bInvertXY)
    bInvertXY.grid(row=6, column=1, sticky='nsew', padx=5, pady=5, columnspan=2)
    bVer=Button(frCmd.frame, text=getLang('edit')+'\t'+chr(60370), width=20, command=setPoint)
    setThemeToButton(bVer)
    bVer.grid(row=7, column=1, sticky='w', padx=5, pady=5, columnspan=2)
    bDel=Button(frCmd.frame, text=getLang('delete')+'\t'+chr(59213), width=20, command=deleteObj)
    setThemeToButton(bDel)
    bDel.grid(row=8, column=1, sticky='w', padx=5, pady=10, columnspan=2)
    bDel['fg']=pf.COLORS['--dark-red']
    pf.ActiveLeave(bDel, pf.COLORS['--dark-color-1'], 'red')
    
    pf.Assign(fen, deleteObj, ['Delete'])
    pf.Assign(fen, copyObj, ['Control-c', 'Control-C'])
    pf.Assign(fen, pastObj, ['Control-v', 'Control-V'])
    pf.Assign(fen, setPoint, ['Control-Shift-E', 'Control-Shift-e'])
    pf.Assign(fen, setMirrorX, ['Control-Shift-x', 'Control-Shift-X'])
    pf.Assign(fen, setMirrorY, ['Control-Shift-y', 'Control-Shift-Y'])
    pf.Assign(fen, setMirrorXY, ['Control-Shift-z', 'Control-Shift-Z'])
    pf.Assign(fen, duplicateObj, ['Control-Shift-d', 'Control-Shift-D'])
    pf.Assign(fen, liftObj, ['Control-Shift-m', 'Control-Shift-M'])

def setRend():
    global sizeX, sizeY, colorMode, bBg
    colorMode=IntVar(value=False)
    sizeX=StringVar(value=pf.Get(can).x())
    sizeY=StringVar(value=pf.Get(can).y())
    lab=Label(frRend.frame, text=getLang('background'), width=15)
    setThemeToButton(lab, False)
    lab.grid(row=1, column=1)
    bBg=Button(frRend.frame)
    setThemeToButton(bBg, False)
    bBg.config(text='', width=7, cursor='hand2', bg=can['bg'], command=lambda:setBgColor(bBg))
    bBg.grid(row=1, column=2, sticky='w', pady=5)
    lab=Label(frRend.frame, text=getLang('size'), width=15)
    setThemeToButton(lab, False)
    lab.grid(row=2, column=1)
    entrX=Entry(frRend.frame, width=7, textvariable=sizeX, insertbackground='white')
    entrY=Entry(frRend.frame, width=7, textvariable=sizeY, insertbackground='white')
    setThemeToButton(entrX)
    setThemeToButton(entrY)
    entrX.grid(row=2, column=2, sticky='w')
    entrY.grid(row=3, column=2, sticky='w')
    def setSize_(event):
        setSize([sizeX.get(), sizeY.get()])
    pf.Assign(entrX, setSize_, ['FocusOut', 'Return'])
    pf.Assign(entrY, setSize_, ['FocusOut', 'Return'])
    entry.add(entrX)
    entry.add(entrY)
    def t():
        global colorValue
        if colorMode.get()==False:
            colorValue=False
        else:
            colorValue=True
    bCMode=Checkbutton(frRend.frame, text=getLang('no color'), width=20, variable=colorMode, command=t)
    setThemeToButton(bCMode)
    bCMode.grid(row=4, column=1, sticky='w', padx=5, pady=5, columnspan=2)
    
def setMenu():
    menu=fen.menu
    fileMenu=Menu(menu, tearoff=False, bg=pf.COLORS['--dark-color'], fg='white', bd=0, relief='sunken')
    editMenu=Menu(menu, tearoff=False, bg=pf.COLORS['--dark-color'], fg='white', bd=0, relief='sunken')
    objMenu=Menu(menu, tearoff=False, bg=pf.COLORS['--dark-color'], fg='white', bd=0, relief='sunken')
    optMenu=Menu(menu, tearoff=False, bg=pf.COLORS['--dark-color'], fg='white', bd=0, relief='sunken')
    moreMenu=Menu(menu, tearoff=False, bg=pf.COLORS['--dark-color'], fg='white', bd=0, relief='sunken')
    langMenu=Menu(optMenu, tearoff=False, bg=pf.COLORS['--dark-color'], fg='white', bd=0, relief='sunken')
    menu.add_cascade(label=getLang('file'), menu=fileMenu)
    menu.add_cascade(label=getLang('edit'), menu=editMenu)
    menu.add_cascade(label=getLang('object'), menu=objMenu)
    menu.add_cascade(label=getLang('option'), menu=optMenu)
    menu.add_cascade(label=getLang('more'), menu=moreMenu)
    optMenu.add_cascade(label=getLang('langue'), menu=langMenu)
    fileMenu.add_command(label=getLang('new'), accelerator='Ctrl+N', command=checkNew)
    fileMenu.add_command(label=getLang('open'), accelerator='Ctrl+O', command=openFile)
    fileMenu.add_command(label=getLang('save'), accelerator='Ctrl+S', command=setSaveFile)
    fileMenu.add_command(label=getLang('saveas'), accelerator='Ctrl+Shift+S', command=saveAsFile)
    fileMenu.add_separator()
    fileMenu.add_command(label=getLang('exit'), accelerator='Alt+F4', command=exit)
    editMenu.add_command(label=getLang('render'), accelerator='F12', command=setCapture)
    objMenu.add_command(label=getLang('line'), accelerator=chr(9586), command=setLine)
    objMenu.add_command(label=getLang('polygon'), accelerator=chr(9626), command=setPolygon)
    objMenu.add_command(label=getLang('square'), accelerator=chr(9632), command=setSquare)
    objMenu.add_command(label=getLang('triangle')+' 1', accelerator=chr(9650), command=setTriangle1)
    objMenu.add_command(label=getLang('triangle')+' 2', accelerator=chr(9699), command=setTriangle2)
    objMenu.add_command(label=getLang('pentagon'), accelerator=chr(11039), command=setPenta)
    objMenu.add_command(label=getLang('hexagon'), accelerator=chr(11042), command=setHexa)
    objMenu.add_command(label=getLang('oval'), accelerator=chr(9899), command=setOval)
    objMenu.add_separator()
    objMenu.add_command(label=getLang('arc'), accelerator=chr(8978), command=setArc)
    objMenu.add_separator()
    objMenu.add_command(label=getLang('text'), accelerator='abc', command=setText)
    objMenu.add_separator()
    objMenu.add_command(label=getLang('widget'), accelerator=chr(128377), command=setWindow)
    objMenu.add_separator()
    objMenu.add_command(label=getLang('image'), accelerator=chr(59305), command=setImage)
    link='https://github.com/Ingene555/'
    moreMenu.add_command(label='Github', command=lambda arg=link: wb.open_new_tab(arg))
    moreMenu.add_command(label=getLang('help'), command=setHelp)
    var=StringVar(value=language.lang)
    l=list(dicoLANG_NAME.keys())
    l.sort()
    for ww in l:
        langMenu.add_radiobutton(label=ww, command=lambda arg =ww:setLangue(arg), value=dicoLANG_NAME[ww], variable=var, selectcolor='white')
    var.set(language.lang)
    
    pf.Assign(fen, checkNew, ['Control-n', 'Control-N'])
    pf.Assign(fen, openFile, ['Control-o', 'Control-O'])
    pf.Assign(fen, setSaveFile, ['Control-s', 'Control-S'])
    pf.Assign(fen, saveAsFile, ['Control-Shift-s', 'Control-Shift-S'])
    pf.Assign(fen, exit, ['Alt-F4'])
    pf.Assign(fen, setCapture, ['F12'])
    
def currentStatus(event):
    x=event.x
    y=event.y
    if select:
        if type(select)==type([]):
            obj='multiple'
        else:
            obj=select.obj.type+' - '+select.obj.name
    else:
        obj='none'
    fen.labCoords['text']='X: %s  Y: %s\tObject: %s'%(x, y, obj)
    can.focus_set()
    try:
        actualizeData()
    except Exception as e:print(e)

def setFocus(event):
    entr=[]
    entr.extend(entry.listEntry)
    if opt2D:
        entr.extend(opt2D.listE)
        if opt2D.obj.type=='window':
            entr.extend(opt2D.obj.option2W.listE)
            entr.append(opt2D.obj.window)
    if not event.widget in entr:
        can.focus_set() 

def startProgram():
    global ifOpen
    if not ifOpen:
        global fen, can, taskBar, listBar, frRend, frCmd, frOpt,selector, select, focus, element
        global fromX, fromY, toX, toY,backward, forward, lift, globale, grid, history, copy, entry
        global exec_func, currentLang
        ifOpen=True
        fen=MainWindow()
        with Image.open('icon.png') as photo:
            picture=ImageTk.PhotoImage(photo)
            fen.iconphoto(True, picture)
        can=fen.can
        taskBar, listBar, frRend, frCmd, frOpt=fen.getInterface()
        for ww in fen.getInterface():
            pf.Assign(ww, setScroll, ['Enter'])
            pf.Assign(ww, setNoScroll, ['Leave'])
        pf.Assign(can, currentStatus, ['Enter', 'Motion'])
        
        selector=None
        select=None
        focus=None
        element=Element(can)
        fromX=fromY=toX=toY=0
        backward=[]
        forward=[]
        lift=[]
        globale=None
        grid=GridSpace(can)
        history=History()
        copy=Copy()
        entry=LocalEntry()
        currentLang=language.lang
        setTaskBar()
        setCmd()
        setRend()
        setMenu()
        pf.Assign(fen, mother, ['Button', 'Key', 'Leave', 'Enter', 'KeyPress'])
        pf.Assign(fen, setFocus, ['Button-1'])
        pf.Assign(can, move, ['Button2-Motion'])
        pf.Assign(can, unmove, ['ButtonRelease-2'])
        #pf.Assign(fen, restartProgram, ['F4'])
        fen.protocol('WM_DELETE_WINDOW', exit)
        if exec_func:
            exec_func()
            exec_func=None
        fen.mainloop()

def restartProgram(event=None):
    global exec_func, ifOpen
    ifOpen=False
    el=[]
    hb=[]
    hw=[]
    li=[]
    fi=file
    if len(element.listObj)>0:
        for ww in element.listObj:
            el.append(ww.getAll())
        for ww in element.listLift:
            li.append([ww.type, ww.tag, ww.name])
    if len(history.listBack)>0:
        for ww in history.listBack:
            hb.append(ww)
    if len(history.listWard)>0:
        for ww in history.listWard:
            hw.append(ww)
    ci=[can['bg'], colorMode.get(), colorValue, sizeX.get(), sizeY.get()]
    sel=[]
    x=[]
    y=[]
    if select:
        if type(select)==type([]):
            x=[fromX, toX]
            y=[fromY, toY]
            for ww in select:
                sel.append([ww.obj.type, ww.obj.tag, ww.obj.name])
        else:
            sel=[select.obj.type, select.obj.tag, select.obj.name]
    cop=copy.listCopy.copy
    fen.destroy()
    language.actualize()
    def t():
        global fromX, toX, fromY, toY, colorValue, file, bBg
        if file:
            fen.title('Dynamic Draw - file:'+file)
        if len(el)>0:
            for ww in el:
                if ww[0]=='pen':
                    a=object2D.listOfObject[ww[0]](can)
                elif ww[0]=='window':
                    a=object2D.listOfObject[ww[0]](can, ww[1], ww[2], object2W.Button2W(can))
                elif ww[0]=='picture':
                    a=object2D.listOfObject[ww[0]](can, ww[1], ww[2], ww[3])
                else:
                    a=object2D.listOfObject[ww[0]](can, ww[1], ww[2])
                a.setAll(ww)
                element.addObj(a)
            del(element.listLift[:])
            for ww in li:
                for xx in element.listObj:
                    if xx.type!='pen':
                        if ww[0]==xx.type and ww[2]==xx.name:
                            element.listLift.append(xx)
                        break
        del(history.listBack[:])
        del(history.listWard[:])
        if len(hb)>0:
            for ww in hb:
                history.listBack.append(ww)
            bBack['stat']='normal'
        if len(hw)>0:
            for ww in hw:
                history.listWard.append(ww)
            bForward['stat']='normal'
        can['bg']=ci[0]
        bBg['bg']=ci[0]
        colorMode.set(ci[1])
        colorValue=ci[2]
        sizeX.set(ci[3])
        sizeY.set(ci[4])
        if len(sel)>0:
            fromX=x[0]
            toX=x[1]
            fromY=y[0]
            toY=y[1]
            if type(sel[0])==type([]):
                checkFromTo()
            else:
                for ww in element.listObj:
                    if ww.type!='pen':
                        if sel[0]==ww.type and sel[2]==ww.name:
                            manualChoosen(ww)
                            break
    exec_func=t
    startProgram()
                            
def mother(event=None):
    global select, focus, copy
    if select and type(select)!=type([]):
        x=min(select.obj.x)+(max(select.obj.x)-min(select.obj.x))/2
        y=min(select.obj.y)+(max(select.obj.y)-min(select.obj.y))/2
        if select.obj.type in ['line', 'polygon', 'arc', 'oval']:
            wdt=(max(select.obj.x)-min(select.obj.x))
            hgt=(max(select.obj.y)-min(select.obj.y))
        else:
            wdt=select.obj.width if select.obj.type!='text' else len(select.obj.text)*select.obj.size
            hgt=select.obj.height if select.obj.type!='text' else select.obj.size*select.obj.text.count('\n')
        select.setCoords(x, y)
        select.setSize(wdt, hgt)
    if len(element.listObj)>0:
        for ww in range(len(element.listObj)):
            if element.listObj[ww].type!='pen':
                if element.listEntry[ww][0].winfo_exists():
                    element.listEntry[ww][0].delete('0', 'end')
                    element.listEntry[ww][0].insert('end', element.listObj[ww].name)

def clearDir(dir):
    try:
        if os.path.isdir(dir):
            for filename in os.listdir(dir):
                file_path = os.path.join(dir, filename)
                if os.path.isfile(file_path):
                    os.remove(file_path)
    except:None

if __name__=='__main__':
    admin.associate_dynd_file_extension2()
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        exec_func=lambda arg=file_path:manualOpenFile(arg)
    if not os.path.exists('temps'):
        try:
            os.mkdir('temps')
        except Exception as e:
            print(e)
    try:
        clearDir('temps')
    except Exception as e:
        print(e)
    if not isOpen:
        startProgram()
        isOpen=True
    