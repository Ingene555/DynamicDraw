import pyfunct as pf
import tkinter as tk
import tkinter.ttk as ttk
from language import getLang, getLangKey, getLangWdt
from tkinter.font import Font
import object2D
import widgets as wd
import math
import bubblewidget as bbg
import symbols as sb
from tkinter import filedialog as fd
from tkinter import colorchooser as cc

def setName(class_, name, variable, command=None):
    if command:
            command()
    variable.set(name)
    class_.name=variable.get()

def setCoords(class_, val1, val2, var1, var2, command=None):
    try:
        if command:
            command()
        a=int(eval(str(val1)))
        b=int(eval(str(val2)))
        var1.set(str(a))
        var2.set(str(b))
        class_.moveTo(a, b)
    except Exception as e:print(e)

def setAngle(class_, value, variable, command=None):
    try:
        if command:
            command()
        a=int(eval(str(value)))
        variable.set(str(a))
        if class_.type=='picture':
            class_.setImage(angle=a)
        else:
            class_.rotate(a)
    except Exception as e: print(e)

def setScale(class_, value, variable, command=None):
    try:
        if command:
            command()
        a=int(eval(str(value)))
        variable.set(str(a))
        class_.resize(a, a)
    except Exception as e:print(e)

def setText(class_, value, variable, command=None):
    if command:
            command()
    variable.set(value)
    class_.setText(variable.get())

def setImage(class_, value, variable, command=None):
    try:
        if command:
            command()
        variable.set(value)
        class_.setImage(variable.get())
    except Exception as e:print(e)

def setFill(class_, value, variable, command=None):
    if command:
            command()
    variable.set(value)
    class_.setFill(variable.get())

def setOutline(class_, value, variable, command=None):
    if command:
            command()
    variable.set(value)
    class_.setOutline(variable.get())

def setStart(class_, value, variable, command=None):
    try:
        if command:
            command()
        a=int(eval(str(value)))
        variable.set(str(a))
        class_.setStart(a)
    except Exception as e:print(e, variable)

def setExtent(class_, value, variable, command=None):
    try:
        if command:
            command()
        a=int(eval(str(value)))
        variable.set(str(a))
        class_.setExtent(a)
    except Exception as e:print(e)

def setWidth(class_, value, variable, command=None):
    try:
        if command:
            command()
        a=int(eval(str(value)))
        if a<0:a=0
        variable.set(str(a))
        class_.setWidth(a)
    except Exception as e:print(e)

def setSize(class_, value, variable, command=None):
    try:
        if command:
            command()
        a=int(eval(str(value)))
        if a<1: a=1
        variable.set(str(a))
        class_.resize(a)
    except Exception as e:print(e)

def setFont(class_, font, weight, slant, var1, var2, var3, command=None):
    if command:
            command()
    w='bold' if weight==True else 'normal'
    s='italic' if slant==True else 'roman'
    class_.setFont(font)
    class_.setWeight(w)
    class_.setSlant(s)
    var1.set(font)
    var2.set(weight)
    var3.set(slant)

def setUnder(class_, value, variable, command=None):
    if command:
            command()
    variable.set(value)
    class_.setUnderline(value)

def setOver(class_, value, variable, command=None):
    if command:
            command()
    variable.set(value)
    class_.setOverstrike(value)

def setWdth(class_, value, variable, command=None):
    try:
        if command:
            command()
        a=int(eval(str(value)))
        variable.set(str(a))
        if class_.type=='picture':
            class_.setImage(width=a)
        else:
            class_.setWidth(a)
    except Exception as e:print(e)

def setHeight(class_, value, variable, command=None):
    try:
        if command:
            command()
        a=int(eval(str(value)))
        variable.set(str(a))
        if class_.type=='picture':
            class_.setImage(height=a)
        else:
            class_.setHeight(a)
    except Exception as e:print(e)

def setDash(class_, value, variable, command=None):
    try:
        if command:
            command()
        if len(value)>0 and variable:
            a=[]
            for ww in range(len(value)):
                a.append(int(eval(str(value[ww]))))
            a=tuple(a)
        else:
            a=()
        class_.setDash(a)
    except Exception as e:print(e)

def setDashOffset(class_, value, variable, command=None):
    try:
        if command:
            command()
        a=int(eval(str(value)))
        variable.set(str(a))
        class_.setDashOffset(a)
    except Exception as e:print(e)

def setArrow(class_, value, command=None):
    if command:
            command()
    class_.setArrow(value)

def setCap(class_, value, command=None):
    if command:
            command()
    class_.setCapStyle(value)

def setJoin(class_, value, command=None):
    if command:
            command()
    class_.setJoinStyle(value)

def setSmooth(class_, value, command=None):
    if command:
            command()
    class_.setSmooth(value)

def setSmoothV(class_, value, command=None):
    if command:
            command()
    class_.setSplineSteps(value)

def setAcnhor(class_, value, command=None):
    if command:
            command()
    class_.setAnchor(value)

def setJustify(class_, value, command=None):
    if command:
            command()
    class_.setJustify(value)

def setStyle(class_, value, command=None):
    if command:
            command()
    class_.setStyle(value)

def setStipple(class_, value, command=None):
    if command:
            command()
    class_.setStipple(value)

def setWindow(class_, value, master, theme, command=None):
    if command:
            command()
    class_.setWidget(value, master, theme)

class ScrollableFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.can = tk.Canvas(self, bd=0, highlightthickness=1, highlightcolor=pf.COLORS['--dark-purple'], relief=tk.FLAT,
                             width=self.cget('width'), height=self.cget('height'), bg=self['bg'])
        self.can.grid(row=1, column=1, sticky=tk.NSEW)
        self.can.grid_columnconfigure(1, weight=1)
        self.can.grid_rowconfigure(1, weight=1)
        self.v_scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.can.yview)
        self.v_scrollbar.grid(row=1, column=2, sticky=tk.NS)
        self.h_scrollbar = tk.Scrollbar(self, orient=tk.HORIZONTAL, command=self.can.xview)
        self.h_scrollbar.grid(row=2, column=1, sticky=tk.EW)
        self.can.configure(yscrollcommand=self.v_scrollbar.set, xscrollcommand=self.h_scrollbar.set)
        self.can.bind_all("<MouseWheel>", lambda event: self.can.yview_scroll(int(-1*(event.delta/120)), "units"))
        self.inner_frame = tk.Canvas(self.can, bg=self['bg'])
        self.frame=self.inner_frame
        self.window = self.can.create_window(int(pf.Get(self.inner_frame).x())/2, int(pf.Get(self.inner_frame).y())/2, window=self.inner_frame, anchor="center")
        self.inner_frame.bind("<Configure>", self.windowed)
        self.windowed()
    
    def windowed(self, event=None):
        self.can.configure(scrollregion=(0, 0, int(pf.Get(self.inner_frame).x()), int(pf.Get(self.inner_frame).y())))
        self.can.coords(self.window, int(pf.Get(self.inner_frame).x())/2, int(pf.Get(self.inner_frame).y())/2)
        self.can.coords(self.window, int(pf.Get(self.inner_frame).x())/2, int(pf.Get(self.inner_frame).y())/2)
        self.can.after(200, self.windowed)
    
    def resized(self, event=None):
        self.can['width']=self.cget('width')
        self.can['height']=self.cget('height')
    
    def setFrameSize(self, event=None):
        self.inner_frame['width']=self.can.cget('width')
        self.inner_frame['height']=self.can.cget('height')
    
    def setNoScroll(self):
        self.can.unbind_all('<MouseWheel>')
    
    def setScroll(self):
        self.can.bind_all("<MouseWheel>", lambda event: self.can.yview_scroll(int(-1*(event.delta/120)), "units"))

class Option2D:
    def __init__(self, master, object2d, theme=[pf.COLORS['--dark-color'], 'white', pf.COLORS['--dark-color-1'], pf.COLORS['--light-color-1']], command=None):
        self.master=master
        self.obj=object2d
        self.theme=theme
        self.dict={'line':lambda :self.setLine(self.obj),
                   'polygon': lambda:self.setPolygon(self.obj),
                   'oval':lambda:self.setOval(self.obj),
                   'arc':lambda:self.setArc(self.obj),
                   'picture':lambda:self.setPicture(self.obj),
                   'text':lambda:self.setText(self.obj),
                   'window':lambda:self.setWindow(self.obj),
                   'pen':lambda:self.setPen(self.obj)}
        self.listW=[]
        self.listE=[]
        self.command=command
    
    def setOption(self):
        for ww in self.master.winfo_children():
            ww.destroy()
        self.listW=[]
        self.listE=[]
        self.listCB=[]
        self.fr0=tk.Frame(self.master, bg=self.theme[0], border=0, highlightthickness=0, relief=tk.FLAT, width=120)
        self.varName=tk.StringVar()
        self.entrName=wd.Entrytk(self.fr0, bg=self.theme[2], fg=self.theme[1], border=0, highlightcolor=pf.COLORS['--dark-blue'],highlightthickness=1,
                               disabledbackground=self.theme[3], disabledforeground=self.theme[1], insertbackground=self.theme[1],
                               font=Font(family=pf.POLICE[0], size=12, weight='bold'), textvariable=self.varName)
        self.entrName._grid(row=1, column=2, sticky=tk.EW)
        self.entrName.frame.config(bg=self.theme[0], border=0, highlightthickness=0, relief=tk.FLAT)
        self.entrName.add_button(text=chr(937), relief=tk.FLAT, bd=0, highlightthickness=0,font=Font(family=pf.POLICE[0], size=10, weight='bold'),
                                bg=self.theme[2], activebackground=self.theme[3], cursor='hand2', command=lambda:sb.Container(self.master, self.entrName, self.theme))
        self.labName=tk.Label(self.fr0, text=getLang('title'), bg=self.theme[0], fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        self.entrName.grid_columnconfigure(0, weight=1)
        self.labName.grid(row=1, column=1)
        
        self.fr1=tk.Frame(self.master, bg=self.theme[0], border=0, highlightthickness=0, relief=tk.FLAT, width=100)
        self.varX=tk.StringVar()
        self.entrX=tk.Entry(self.fr1, bg=self.theme[2], fg=self.theme[1], border=0, highlightcolor=pf.COLORS['--dark-blue'],highlightthickness=0,
                               disabledbackground=self.theme[3], disabledforeground=self.theme[1], insertbackground=self.theme[1],
                               font=Font(family=pf.POLICE[0], size=11, weight='bold'), textvariable=self.varX, width=20)
        self.entrX.grid(row=1, column=2, sticky=tk.W, padx=2, pady=2)
        self.labX=tk.Label(self.fr1, text='X', bg=self.theme[0], fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        self.labX.grid(row=1, column=1, padx=2, pady=2)
        self.varY=tk.StringVar()
        self.entrY=tk.Entry(self.fr1, bg=self.theme[2], fg=self.theme[1], border=0, highlightcolor=pf.COLORS['--dark-blue'],highlightthickness=0,
                               disabledbackground=self.theme[3], disabledforeground=self.theme[1], insertbackground=self.theme[1],
                               font=Font(family=pf.POLICE[0], size=11, weight='bold'), textvariable=self.varY, width=20)
        self.entrY.grid(row=2, column=2, sticky=tk.W, padx=2, pady=2)
        self.labY=tk.Label(self.fr1, text='Y', bg=self.theme[0], fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        self.labY.grid(row=2, column=1, padx=2, pady=2)
        self.varAngle=tk.StringVar()
        self.spnAngle=tk.Entry(self.fr1, bg=self.theme[2], fg=self.theme[1], border=0, highlightcolor=pf.COLORS['--dark-blue'],highlightthickness=0,
                               disabledbackground=self.theme[3], disabledforeground=self.theme[1], insertbackground=self.theme[1],
                               font=Font(family=pf.POLICE[0], size=11, weight='bold'), textvariable=self.varAngle, width=20,)
        self.spnAngle.grid(row=3, column=2, sticky=tk.W, padx=2, pady=2)
        self.labAngle=tk.Label(self.fr1, text=getLang('angle'), bg=self.theme[0], fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        self.labAngle.grid(row=3, column=1, padx=2, pady=2)
        self.varScale=tk.StringVar()
        self.spnScale=tk.Spinbox(self.fr1, bg=self.theme[2], fg=self.theme[1], border=0, highlightcolor=pf.COLORS['--dark-blue'],highlightthickness=0,
                               disabledbackground=self.theme[3], disabledforeground=self.theme[1], insertbackground=self.theme[1],
                               font=Font(family=pf.POLICE[0], size=11, weight='bold'), textvariable=self.varScale, width=20, from_=-math.inf, to=math.inf,
                               buttonbackground=self.theme[3], buttoncursor='hand2', buttondownrelief=tk.FLAT, buttonuprelief=tk.FLAT)
        self.spnScale.grid(row=4, column=2, sticky=tk.W, padx=2, pady=2)
        self.labScale=tk.Label(self.fr1, text=getLang('scale'), bg=self.theme[0], fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        self.labScale.grid(row=4, column=1, padx=2, pady=2)
        
        self.fr2=tk.Frame(self.master, bg=self.theme[0], border=0, highlightthickness=0, relief=tk.FLAT, width=100)
        self.varText=tk.StringVar()
        self.entrText=wd.Entrytk(self.fr2, bg=self.theme[2], fg=self.theme[1], border=0, highlightcolor=pf.COLORS['--dark-blue'],highlightthickness=0,
                               disabledbackground=self.theme[3], disabledforeground=self.theme[1], insertbackground=self.theme[1],
                               font=Font(family=pf.POLICE[0], size=11, weight='bold'), textvariable=self.varText, width=15)
        self.entrText._grid(row=1, column=2, sticky=tk.W, padx=2, pady=2)
        self.entrText.frame.config(bg=self.theme[0], border=0, highlightthickness=0, relief=tk.FLAT)
        self.entrText.add_button(text=chr(937), relief=tk.FLAT, bd=0, highlightthickness=0,font=Font(family=pf.POLICE[0], size=10, weight='bold'),
                                bg=self.theme[2], activebackground=self.theme[3], cursor='hand2', command=lambda:sb.Container(self.master, self.entrText, self.theme))
        self.labText=tk.Label(self.fr2, text=getLang('text'), bg=self.theme[0], fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        self.labText.grid(row=1, column=1)
        self.varImg=tk.StringVar()
        self.entrImg=wd.Entrytk(self.fr2, bg=self.theme[2], fg=self.theme[1], border=0, highlightcolor=pf.COLORS['--dark-blue'],highlightthickness=0,
                               disabledbackground=self.theme[3], disabledforeground=self.theme[1], insertbackground=self.theme[1],
                               font=Font(family=pf.POLICE[0], size=10, weight='normal'), textvariable=self.varImg, width=15)
        self.entrImg.frame.config(bg=self.theme[0], border=0, highlightthickness=0, relief=tk.FLAT, width=100)
        def setImage_():
            a=fd.askopenfilename(title=getLang('select an image'),
                                                              filetypes=[
                                                                        ("Images", "*.png *.jpg *.jpeg *.gif *.bmp  *.webp *.cur"),
                                                                        ("PNG files", "*.png"),
                                                                        ("JPEG files", "*.jpg *.jpeg"),
                                                                        ("GIF files", "*.gif"),
                                                                        ("BMP files", "*.bmp"),
                                                                        ("WEBP files", "*.webp"),
                                                                        ("CUR files", "*.cur")
                                                                        ])
            if a:
                setImage(self.obj, a, self.varImg, self.command)
        self.entrImg.add_button(text=chr(60709), relief=tk.FLAT, bd=0, highlightthickness=0,
                                bg=self.theme[2], activebackground=self.theme[3], cursor='hand2',
                                command=setImage_)
        self.entrImg._grid(row=2, column=2, sticky=tk.W, padx=2, pady=2)
        self.labImg=tk.Label(self.fr2, text=getLang('image'), bg=self.theme[0], fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        self.labImg.grid(row=2, column=1)
        self.varFill=tk.StringVar()
        def setFill_():
            if not self.obj.type in ['window', 'picture']:
                a=cc.askcolor(title=getLang("choose a color"), initialcolor=self.bFill['bg'])[1]
                if a:
                    self.bFill['bg']=a
                    setFill(self.obj, a, self.varFill, self.command)
        self.bFill=tk.Button(self.fr2, width=17, relief=tk.FLAT, bd=0, highlightthickness=0,
                                bg='black', activebackground=self.theme[3], cursor='hand2',
                                command=setFill_)
        self.labFill=tk.Label(self.fr2, text=getLang('fill'), bg=self.theme[0], fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        self.labFill.grid(row=3, column=1)
        self.bFill.grid(row=3, column=2, sticky=tk.W, padx=2, pady=2)
        self.varOutline=tk.StringVar()
        def setOutline_():
            if not self.obj.type in ['window', 'picture', 'text', 'line']:
                a=cc.askcolor(title=getLang("choose a color"), initialcolor=self.bOutline['bg'])[1]
                if a:
                    self.bOutline['bg']=a
                    setOutline(self.obj, a, self.varOutline, self.command)
        self.bOutline=tk.Button(self.fr2, width=17, relief=tk.FLAT, bd=0, highlightthickness=0,
                                bg='black', activebackground=self.theme[3], cursor='hand2',
                                command=setOutline_)
        self.labOutline=tk.Label(self.fr2, text=getLang('outline'), bg=self.theme[0], fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        self.labOutline.grid(row=4, column=1)
        self.bOutline.grid(row=4, column=2, padx=2, pady=2, sticky=tk.W)
        self.varStart=tk.StringVar()
        self.spnStart=tk.Spinbox(self.fr2, bg=self.theme[2], fg=self.theme[1], border=0, highlightcolor=pf.COLORS['--dark-blue'],highlightthickness=0,
                               disabledbackground=self.theme[3], disabledforeground=self.theme[1], insertbackground=self.theme[1],
                               font=Font(family=pf.POLICE[0], size=11, weight='bold'), textvariable=self.varStart, width=20, from_=-math.inf, to=math.inf,
                               buttonbackground=self.theme[3], buttoncursor='hand2', buttondownrelief=tk.FLAT, buttonuprelief=tk.FLAT,
                               command=lambda: setStart(self.obj, self.spnStart.get(), self.varStart, self.command))
        self.labStart=tk.Label(self.fr2, text=getLang('start'), bg=self.theme[0], fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        self.labStart.grid(row=5, column=1)
        self.spnStart.grid(row=5, column=2, sticky=tk.W, padx=2, pady=2)
        self.varExtent=tk.StringVar()
        self.spnExtent=tk.Spinbox(self.fr2, bg=self.theme[2], fg=self.theme[1], border=0, highlightcolor=pf.COLORS['--dark-blue'],highlightthickness=0,
                               disabledbackground=self.theme[3], disabledforeground=self.theme[1], insertbackground=self.theme[1],
                               font=Font(family=pf.POLICE[0], size=11, weight='bold'), textvariable=self.varExtent, width=20, from_=-math.inf, to=math.inf,
                               buttonbackground=self.theme[3], buttoncursor='hand2', buttondownrelief=tk.FLAT, buttonuprelief=tk.FLAT,
                                command=lambda:setExtent(self.obj, self.spnExtent.get(), self.varExtent, self.command))
        self.labExtent=tk.Label(self.fr2, text=getLang('extent'), bg=self.theme[0], fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        self.labExtent.grid(row=6, column=1)
        self.spnExtent.grid(row=6, column=2, sticky=tk.W, padx=2, pady=2)
        self.varWidth=tk.StringVar()
        self.entrWidth=tk.Entry(self.fr2, bg=self.theme[2], fg=self.theme[1], border=0, highlightcolor=pf.COLORS['--dark-blue'],highlightthickness=0,
                               disabledbackground=self.theme[3], disabledforeground=self.theme[1], insertbackground=self.theme[1],
                               font=Font(family=pf.POLICE[0], size=12, weight='bold'), textvariable=self.varWidth, width=20)
        self.labWidth=tk.Label(self.fr2, text=getLang('width'), bg=self.theme[0], fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        self.labWidth.grid(row=7, column=1)
        self.entrWidth.grid(row=7, column=2, sticky=tk.W, padx=2, pady=2)
        self.style = ttk.Style()
        self.style.configure('ComboMod.TCombobox',
                            background=self.theme[2],
                            fieldbackground=self.theme[0],
                            listbackground=self.theme[0],
                            listforeground=self.theme[1],
                            width=20,
                            border=0,
                            highlighthickness=0,
                            relief=tk.FLAT,
                            font=(pf.POLICE[0], 12, 'bold'),
                            state='readonly')
        self.varFont = tk.StringVar()
        self.cbFont = ttk.Combobox(self.fr2, style='ComboMod.TCombobox', values=pf.POLICE, textvariable=self.varFont, width=17, state='readonly', cursor='hand2')
        self.labFont=tk.Label(self.fr2, text=getLang('family'), bg=self.theme[0], fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        self.labFont.grid(row=8, column=1)
        self.cbFont.grid(row=8, column=2, sticky=tk.W, padx=2, pady=2)
        self.varSize=tk.StringVar()
        self.spnSize=tk.Spinbox(self.fr2, bg=self.theme[2], fg=self.theme[1], border=0, highlightcolor=pf.COLORS['--dark-blue'],highlightthickness=0,
                               disabledbackground=self.theme[3], disabledforeground=self.theme[1], insertbackground=self.theme[1],
                               font=Font(family=pf.POLICE[0], size=11, weight='bold'), textvariable=self.varSize, width=20, from_=1,to=math.inf,
                               buttonbackground=self.theme[3], buttoncursor='hand2', buttondownrelief=tk.FLAT, buttonuprelief=tk.FLAT,
                              command=lambda:setSize(self.obj, self.spnSize.get(), self.varSize, self.command))
        self.labSize=tk.Label(self.fr2, text=getLang('size'), bg=self.theme[0], fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        self.labSize.grid(row=9, column=1)
        self.spnSize.grid(row=9, column=2, sticky=tk.W, padx=2, pady=2)
        self.varWeight=tk.IntVar()
        self.chWeight=tk.Checkbutton(self.fr2, width=15, relief=tk.FLAT, bd=0, highlightthickness=0, bg=self.theme[0], fg=self.theme[1], cursor='hand2',
                                     borderwidth=0, variable=self.varWeight, text=getLang('weight'), activebackground=self.theme[0],anchor='w',justify='center',
                                     highlightbackground=self.theme[0], activeforeground=self.theme[1], selectcolor=self.theme[0],
                                     command=lambda:setFont(self.obj, self.cbFont.get(), self.varWeight.get(), self.varItalic.get(),
                                                            self.varFont, self.varWeight, self.varItalic, self.command))
        self.varItalic=tk.IntVar()
        self.chItalic=tk.Checkbutton(self.fr2, width=15, relief=tk.FLAT, bd=0, highlightthickness=0, bg=self.theme[0], fg=self.theme[1], cursor='hand2',
                                     borderwidth=0, variable=self.varItalic, text=getLang('italic'), activebackground=self.theme[0],anchor='w',justify='center',
                                     highlightbackground=self.theme[0], activeforeground=self.theme[1], selectcolor=self.theme[0],
                                     command=lambda:setFont(self.obj, self.cbFont.get(), self.varWeight.get(), self.varItalic.get(),
                                                            self.varFont, self.varWeight, self.varItalic, self.command))
        self.chWeight.grid(row=10, column=1, sticky=tk.W, padx=2, pady=2)
        self.chItalic.grid(row=10, column=2, sticky=tk.W, padx=2, pady=2)
        self.varUnderline=tk.IntVar()
        self.chUnderline=tk.Checkbutton(self.fr2, width=15, relief=tk.FLAT, bd=0, highlightthickness=0, bg=self.theme[0], fg=self.theme[1], cursor='hand2',
                                     borderwidth=0, variable=self.varUnderline, text=getLang('underline'), activebackground=self.theme[0],anchor='w',justify='center',
                                     highlightbackground=self.theme[0], activeforeground=self.theme[1], selectcolor=self.theme[0],
                                     command=lambda:setUnder(self.obj, self.varUnderline.get(), self.varUnderline, self.command))
        self.varOverstrike=tk.IntVar()
        self.chOverstrike=tk.Checkbutton(self.fr2, width=15, relief=tk.FLAT, bd=0, highlightthickness=0, bg=self.theme[0], fg=self.theme[1], cursor='hand2',
                                     borderwidth=0, variable=self.varOverstrike, text=getLang('overstrike'), activebackground=self.theme[0],anchor='w',justify='center',
                                     highlightbackground=self.theme[0], activeforeground=self.theme[1], selectcolor=self.theme[0],
                                     command=lambda:setOver(self.obj, self.varOverstrike.get(), self.varOverstrike, self.command))
        self.chUnderline.grid(row=11, column=1, sticky=tk.W, padx=2, pady=2)
        self.chOverstrike.grid(row=11, column=2, sticky=tk.W, padx=2, pady=2)
        self.varWdt=tk.StringVar()
        self.entrWdt=tk.Entry(self.fr2, bg=self.theme[2], fg=self.theme[1], border=0, highlightcolor=pf.COLORS['--dark-blue'],highlightthickness=0,
                               disabledbackground=self.theme[3], disabledforeground=self.theme[1], insertbackground=self.theme[1],
                               font=Font(family=pf.POLICE[0], size=12, weight='bold'), textvariable=self.varWdt, width=20)
        self.labWdt=tk.Label(self.fr2, text=getLang('long'), bg=self.theme[0], fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        self.labWdt.grid(row=12, column=1)
        self.entrWdt.grid(row=12, column=2, sticky=tk.W, padx=2, pady=2)
        self.varHeight=tk.StringVar()
        self.entrHeight=tk.Entry(self.fr2, bg=self.theme[2], fg=self.theme[1], border=0, highlightcolor=pf.COLORS['--dark-blue'],highlightthickness=0,
                               disabledbackground=self.theme[3], disabledforeground=self.theme[1], insertbackground=self.theme[1],
                               font=Font(family=pf.POLICE[0], size=12, weight='bold'), textvariable=self.varHeight, width=20)
        self.labHeight=tk.Label(self.fr2, text=getLang('height'), bg=self.theme[0], fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        self.labHeight.grid(row=13, column=1)
        self.entrHeight.grid(row=13, column=2, sticky=tk.W, padx=2, pady=2)
        
        self.fr3=tk.Frame(self.master, bg=self.theme[0], border=0, highlightthickness=0, relief=tk.FLAT, width=100)
        self.varDash=tk.IntVar()
        def setDash_():
            if self.varDash.get()==True:
                self.frameDash.grid(row=1, column=2, rowspan=4)
                self.varDash1.set('1')
                self.varDash2.set('1')
                self.varDash3.set('1')
                setDash(self.obj, [self.varDash1.get(), self.varDash2.get(), self.varDash3.get()],
                        [self.varDash1, self.varDash2, self.varDash3], self.command)
            else:
                self.frameDash.grid_forget()
                setDash(self.obj, (), None)
        self.chDash=tk.Checkbutton(self.fr3, width=15, relief=tk.FLAT, bd=0, highlightthickness=0, bg=self.theme[0], fg=self.theme[1], cursor='hand2',
                                     borderwidth=0, variable=self.varDash, text=getLang('dash'), activebackground=self.theme[0],anchor='w',justify='center',
                                     highlightbackground=self.theme[0], activeforeground=self.theme[1], selectcolor=self.theme[0],
                                     command=setDash_)
        self.chDash.grid(row=1, column=1, sticky=tk.W, padx=2, pady=2)
        #
        self.frameDash=tk.Frame(self.fr3, bg=self.theme[0], border=0, highlightthickness=0, relief=tk.FLAT, width=35)
        self.frameDash.grid(row=1, column=2, rowspan=4)
        self.varDash1=tk.StringVar()
        self.varDash2=tk.StringVar()
        self.varDash3=tk.StringVar()
        def setDash__():
            setDash(self.obj, [self.varDash1.get(), self.varDash2.get(), self.varDash3.get()],
                    [self.varDash1, self.varDash2, self.varDash3], self.command)
        self.spnDash1=tk.Spinbox(self.frameDash, bg=self.theme[2], fg=self.theme[1], border=0, highlightcolor=pf.COLORS['--dark-blue'],highlightthickness=0,
                               disabledbackground=self.theme[3], disabledforeground=self.theme[1], insertbackground=self.theme[1],
                               font=Font(family=pf.POLICE[0], size=11, weight='bold'), textvariable=self.varDash1, width=20, from_=1,to=20,
                               buttonbackground=self.theme[3], buttoncursor='hand2', buttondownrelief=tk.FLAT, buttonuprelief=tk.FLAT,
                               command=lambda:setDash__())
        self.spnDash2=tk.Spinbox(self.frameDash, bg=self.theme[2], fg=self.theme[1], border=0, highlightcolor=pf.COLORS['--dark-blue'],highlightthickness=0,
                               disabledbackground=self.theme[3], disabledforeground=self.theme[1], insertbackground=self.theme[1],
                               font=Font(family=pf.POLICE[0], size=11, weight='bold'), textvariable=self.varDash2, width=20, from_=1, to=20,
                               buttonbackground=self.theme[3], buttoncursor='hand2', buttondownrelief=tk.FLAT, buttonuprelief=tk.FLAT,
                               command=lambda:setDash__())
        self.spnDash3=tk.Spinbox(self.frameDash, bg=self.theme[2], fg=self.theme[1], border=0, highlightcolor=pf.COLORS['--dark-blue'],highlightthickness=0,
                               disabledbackground=self.theme[3], disabledforeground=self.theme[1], insertbackground=self.theme[1],
                               font=Font(family=pf.POLICE[0], size=11, weight='bold'), textvariable=self.varDash3, width=20, from_=1, to=20,
                               buttonbackground=self.theme[3], buttoncursor='hand2', buttondownrelief=tk.FLAT, buttonuprelief=tk.FLAT,
                               command=lambda:setDash__())
        self.labDash1=tk.Label(self.frameDash, text=1, bg=self.theme[0], fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        self.labDash2=tk.Label(self.frameDash, text=2, bg=self.theme[0], fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        self.labDash3=tk.Label(self.frameDash, text=3, bg=self.theme[0], fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        self.labDash1.grid(row=2, column=1)
        self.labDash2.grid(row=3, column=1)
        self.labDash3.grid(row=4, column=1)
        self.spnDash1.grid(row=2, column=2, sticky=tk.EW, padx=2, pady=0)
        self.spnDash2.grid(row=3, column=2, sticky=tk.EW, padx=2, pady=1)
        self.spnDash3.grid(row=4, column=2, sticky=tk.EW, padx=2, pady=0)
        self.varDashOffset=tk.StringVar()
        self.spnDashOffset=tk.Spinbox(self.frameDash, bg=self.theme[2], fg=self.theme[1], border=0, highlightcolor=pf.COLORS['--dark-blue'],highlightthickness=0,
                               disabledbackground=self.theme[3], disabledforeground=self.theme[1], insertbackground=self.theme[1],
                               font=Font(family=pf.POLICE[0], size=11, weight='bold'), textvariable=self.varDashOffset, width=5, from_=1, to=20,
                               buttonbackground=self.theme[3], buttoncursor='hand2', buttondownrelief=tk.FLAT, buttonuprelief=tk.FLAT,
                               command=lambda: setDashOffset(self.obj, self.spnDashOffset.get(), self.varDashOffset, self.command))
        self.labDashOffset=tk.Label(self.frameDash, text=getLang('dash offset'), bg=self.theme[0], fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        self.labDashOffset.grid(row=1, column=1)
        self.spnDashOffset.grid(row=1, column=2, sticky=tk.W, padx=1, pady=2)
        #
        self.varArrow = tk.StringVar()
        l=[getLang('None'), getLang('first'), getLang('last'), getLang('both')]
        self.cbArrow = ttk.Combobox(self.fr3, style='ComboMod.TCombobox', values=l, textvariable=self.varArrow, width=17, state='readonly', cursor='hand2')
        self.labArrow=tk.Label(self.fr3, text=getLang('arrow'), bg=self.theme[0], fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        self.labArrow.grid(row=5, column=1)
        self.cbArrow.grid(row=5, column=2, sticky=tk.W, padx=2, pady=2)
        self.varCapStyle = tk.StringVar()
        l=[getLang('butt'), getLang('round'), getLang('projecting')]
        self.cbCapStyle = ttk.Combobox(self.fr3, style='ComboMod.TCombobox', values=l, textvariable=self.varCapStyle, width=17, state='readonly', cursor='hand2')
        self.labCapStyle=tk.Label(self.fr3, text=getLang('cap'), bg=self.theme[0], fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        self.labCapStyle.grid(row=6, column=1)
        self.cbCapStyle.grid(row=6, column=2, sticky=tk.W, padx=2, pady=2)
        self.varJoinStyle = tk.StringVar()
        l=[getLang('miter'), getLang('round'), getLang('bevel')]
        self.cbJoinStyle = ttk.Combobox(self.fr3, style='ComboMod.TCombobox', values=l, textvariable=self.varJoinStyle, width=17, state='readonly', cursor='hand2')
        self.labJoinStyle=tk.Label(self.fr3, text=getLang('join'), bg=self.theme[0], fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        self.labJoinStyle.grid(row=7, column=1)
        self.cbJoinStyle.grid(row=7, column=2, sticky=tk.W, padx=2, pady=2)
        self.varSmooth=tk.IntVar()
        def setSmooth_():
            if self.varSmooth.get()==1:
                self.canSV.grid(row=8, column=2)
                self.varSmoothValue.set(self.obj.splineSteps)
                self.scSmooth.value=int(self.varSmoothValue.get())
                self.scSmooth.default_position()
            else:
                self.canSV.grid_forget()
                
            setSmooth(self.obj, self.varSmooth.get(), self.command)
        self.chSmooth=tk.Checkbutton(self.fr3, width=15, relief=tk.FLAT, bd=0, highlightthickness=0, bg=self.theme[0], fg=self.theme[1], cursor='hand2',
                                     borderwidth=0, variable=self.varSmooth, text=getLang('smooth'), activebackground=self.theme[0],anchor='w',justify='center',
                                     highlightbackground=self.theme[0], activeforeground=self.theme[1], selectcolor=self.theme[0],
                                     command=setSmooth_)
        self.chSmooth.grid(row=8, column=1, sticky=tk.W, padx=2, pady=2)
        self.varSmoothValue=tk.StringVar()
        def setSmoothV_():
            setSmoothV(self.obj, int(eval(str(self.varSmoothValue.get()))), self.command)
        self.canSV=tk.Canvas(self.fr3, bg=self.theme[0], border=0, highlightthickness=0, relief=tk.FLAT, width=240, height=55)
        self.scSmooth=bbg.BubbleScale(self.canSV, 110, 40, self.theme[2], self.theme[1], self.theme[0],
                                      self.theme[2], self.theme[0], 0, 100, 0, 
                                      1, variable=self.varSmoothValue, command=setSmoothV_)
        self.canSV.grid(row=8, column=2)
        self.varAnchor=tk.StringVar()
        l=[getLang('center'), getLang('n'), getLang('s'), getLang('e'), getLang('w'), getLang('ne'), getLang('nw'), getLang('se'), getLang('sw')]
        self.cbAnchor = ttk.Combobox(self.fr3, style='ComboMod.TCombobox', values=l, textvariable=self.varAnchor, width=17, state='readonly', cursor='hand2')
        self.labAnchor=tk.Label(self.fr3, text=getLang('anchor'), bg=self.theme[0], fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        self.labAnchor.grid(row=9, column=1)
        self.cbAnchor.grid(row=9, column=2, sticky=tk.W, padx=2, pady=2)
        self.varJustify=tk.StringVar()
        l=[getLang('left'), getLang('center'), getLang('right')]
        self.cbJustify = ttk.Combobox(self.fr3, style='ComboMod.TCombobox', values=l, textvariable=self.varJustify, width=17, state='readonly', cursor='hand2')
        self.labJustify=tk.Label(self.fr3, text=getLang('justify'), bg=self.theme[0], fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        self.labJustify.grid(row=10, column=1)
        self.cbJustify.grid(row=10, column=2, sticky=tk.W, padx=2, pady=2)
        self.varStyle=tk.StringVar()
        l=[getLang('pieslice'), getLang('chord'), getLang('arc')]
        self.cbStyle = ttk.Combobox(self.fr3, style='ComboMod.TCombobox', values=l, textvariable=self.varStyle, width=17, state='readonly', cursor='hand2')
        self.labStyle=tk.Label(self.fr3, text=getLang('style'), bg=self.theme[0], fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        self.labStyle.grid(row=11, column=1)
        self.cbStyle.grid(row=11, column=2, sticky=tk.W, padx=2, pady=2)
        self.varWindow=tk.StringVar()
        l=[getLang('button'), getLang('checkbutton'), getLang('entry'), getLang('frame'),
           getLang('label'), getLang('labelframe'), getLang('listbox'), getLang('message'),
           getLang('radiobutton'), getLang('scale'), getLang('scrolledtext'), getLang('spinbox'), ]
        self.cbWindow = ttk.Combobox(self.fr3, style='ComboMod.TCombobox', values=l, textvariable=self.varWindow, width=17, state='readonly', cursor='hand2')
        self.labWindow=tk.Label(self.fr3, text=getLang('window'), bg=self.theme[0], fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        self.labWindow.grid(row=12, column=1)
        self.cbWindow.grid(row=12, column=2, sticky=tk.W, padx=2, pady=2)
        
        self.fr4=tk.Frame(self.master, bg=self.theme[0], border=0, highlightthickness=0, relief=tk.FLAT, width=100)
        self.varStipple=tk.StringVar()
        l=[getLang(''), getLang('gray25'), getLang('gray50'), getLang('gray75')]
        self.cbStipple = ttk.Combobox(self.fr4, style='ComboMod.TCombobox', values=l, textvariable=self.varStipple, width=17, state='readonly', cursor='hand2')
        self.labStipple=tk.Label(self.fr4, text=getLang('stipple'), bg=self.theme[0], fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        self.labStipple.grid(row=1, column=1)
        self.cbStipple.grid(row=1, column=2, sticky=tk.W, padx=2, pady=2)
        
        self.fr5=tk.Frame(self.master, bg=self.theme[0], border=0, highlightthickness=0, relief=tk.FLAT, width=100)
        
        self.fr0.grid(pady=5)
        self.fr1.grid(pady=5, sticky=tk.W)
        self.fr2.grid(pady=5, sticky=tk.W)
        self.fr3.grid(pady=5, sticky=tk.W)
        self.fr4.grid(pady=5, sticky=tk.W)
        self.fr5.grid(pady=5, sticky=tk.W)
        self.setList()
        self.setObjFunction()
        self.dict[self.obj.type]()
        
        if self.obj.type in ['line', 'polygon'] and self.obj.smooth==True:
                self.canSV.grid(row=8, column=2)
                self.varSmoothValue.set(self.obj.splineSteps)
                self.scSmooth.value=int(self.varSmoothValue.get())
                self.scSmooth.default_position()
        
    def setObjFunction(self):
        def toName(event):
            setName(self.obj, self.entrName.get(), self.varName, self.command)
            #self.master.focus_set()
        pf.Assign(self.entrName, toName, ['Return', 'FocusOut'])
        if self.obj.type!='pen':
            self.varName.set(self.obj.name)
        
        def toCoords(event):
            setCoords(self.obj, self.entrX.get(), self.entrY.get(), self.varX, self.varY, self.command)
            #self.master.focus_set()
        pf.Assign(self.entrX, toCoords, ['Return', 'FocusOut'])
        pf.Assign(self.entrY, toCoords, ['Return', 'FocusOut'])
        if self.obj.type!='pen':
            self.varX.set(self.obj.pointx)
            self.varY.set(self.obj.pointy)
        
        def toAngle(event=None):
            setAngle(self.obj, self.spnAngle.get(), self.varAngle, self.command)
            #self.master.focus_set()
        pf.Assign(self.spnAngle, toAngle, ['Return', 'FocusOut'])
        if not self.obj.type in ['window', 'pen', 'arc']:
            self.varAngle.set(self.obj.angle)
        
        def toScale(event=None):
            setScale(self.obj, self.spnScale.get(), self.varScale, self.command)
            #self.master.focus_set()
        pf.Assign(self.spnScale, toScale, ['Return', 'FocusOut'])
        self.spnScale['command']=toScale
        if not self.obj.type in ['window', 'text', 'picture', 'pen']:
            self.varScale.set(0)
        
        def toText(event):
            setText(self.obj, self.entrText.get(), self.varText, self.command)
            #self.master.focus_set()
        def toSize(event):
            setSize(self.obj, self.spnSize.get(), self.varSize, self.command)
            #self.master.focus_set()
        def toFont(event):
            setFont(self.obj, self.cbFont.get(), self.varWeight.get(), self.varItalic.get(), self.varFont, self.varWeight, self.varItalic, self.command)
            #self.master.focus_set()
        def toJustify(event):
            a=getLangKey(self.varJustify.get())
            setJustify(self.obj, a, self.command)
            #self.master.focus_set()
        pf.Assign(self.entrText, toText, ['Return', 'FocusOut'])
        pf.Assign(self.spnSize, toSize, ['Return', 'FocusOut'])
        pf.Assign(self.cbFont, toFont, ['FocusOut', 'Return', '<ComboboxSelected>'])
        pf.Assign(self.cbJustify, toJustify, ['FocusOut', 'Return', '<ComboboxSelected>'])
        if self.obj.type=='text':
            self.varText.set(self.obj.text)
            self.varSize.set(self.obj.size)
            self.varFont.set(self.obj.font)
            self.varWeight.set(1 if self.obj.weight=='bold' else 0)
            self.varItalic.set(1 if self.obj.slant=='italic' else 0)
            self.varUnderline.set(self.obj.underline)
            self.varOverstrike.set(self.obj.overstrike)
            self.varJustify.set(getLang(self.obj.justify))
            
        def toImage(event):
            setImage(self.obj, self.entrImg.get(), self.varImg, self.command)
            #self.master.focus_set()
        pf.Assign(self.entrImg, toImage, ['Return', 'FocusOut'])
        if self.obj.type=='picture':
            self.varImg.set(self.obj.img[0][0])
            
        def toFill(event):
            if not self.obj.type in ['window', 'picture', 'text', 'line']:
                if self.command:
                    self.command()
                self.bFill['bg']='black'
                self.obj.setFill('')
        if not self.obj.type in ['line', 'pen']:
            pf.Assign(self.bFill, toFill, ['Button-3'])
        if not self.obj.type in ['window', 'picture']:
            self.varFill.set(self.obj.fill)
            self.bFill['bg']=self.varFill.get() if self.varFill.get()!='' else 'black'
        if not self.obj.type in ['window', 'picture', 'text', 'line', 'pen']:
            self.varOutline.set(self.obj.outline)
            self.bOutline['bg']=self.varOutline.get()
        
        def toStart(event):
            setStart(self.obj, self.spnStart.get(), self.varStart, self.command)
            #self.master.focus_set()
        def toExtent(event):
            setExtent(self.obj, self.spnExtent.get(), self.varExtent, self.command)
            #self.master.focus_set()
        def toStyle(event):
            a=getLangKey(self.varStyle.get())
            setStyle(self.obj, a, self.command)
            #self.master.focus_set()
        pf.Assign(self.spnStart, toStart, ['Return', 'FocusOut'])
        pf.Assign(self.spnExtent, toExtent, ['Return', 'FocusOut'])
        pf.Assign(self.cbStyle, toStyle, ['FocusOut', 'Return', '<ComboboxSelected>'])
        if self.obj.type=='arc':
            self.varStart.set(self.obj.start)
            self.varExtent.set(self.obj.extent)
            self.varStyle.set(getLang(self.obj.style))
        
        def toWidth(event):
            setWidth(self.obj, self.entrWidth.get(), self.varWidth, self.command)
            #self.master.focus_set()
        pf.Assign(self.entrWidth, toWidth, ['Return', 'FocusOut'])
        if not self.obj.type in ['window', 'picture', 'text']:
            self.varWidth.set(self.obj.width)
        
        def toWdt(event):
            setWdth(self.obj, self.entrWdt.get(), self.varWdt, self.command)
            #self.master.focus_set()
        def toHeight(event):
            setHeight(self.obj, self.entrHeight.get(), self.varHeight, self.command)
            #self.master.focus_set()
        pf.Assign(self.entrWdt, toWdt, ['Return', 'FocusOut'])
        pf.Assign(self.entrHeight, toHeight, ['Return', 'FocusOut'])
        if self.obj.type in ['window', 'picture', 'text']:
            self.varWdt.set(self.obj.width)
            if self.obj.type!='text':
                self.varHeight.set(self.obj.height)
        
        def toDash(event):
            setDash(self.obj, [self.varDash1.get(), self.varDash2.get(), self.varDash3.get()],
                    [self.varDash1, self.varDash2, self.varDash3], self.command)
            #self.master.focus_set()
        def toDashO(event):
            setDashOffset(self.obj, self.spnDashOffset.get(), self.varDashOffset, self.command)
            #self.master.focus_set()
        pf.Assign(self.spnDash1, toDash, ['Return', 'FocusOut'])
        pf.Assign(self.spnDash2, toDash, ['Return', 'FocusOut'])
        pf.Assign(self.spnDash3, toDash, ['Return', 'FocusOut'])
        pf.Assign(self.spnDashOffset, toDashO, ['Return', 'FocusOut'])
        if not self.obj.type in ['window', 'picture', 'text', 'pen']:
            self.varDash.set(True if len(self.obj.dash)>1 else False)
            if self.varDash.get()==True:
                self.varDash1.set(self.obj.dash[0])
                self.varDash2.set(self.obj.dash[1])
                self.varDash3.set(self.obj.dash[2])
            self.varDash.set(self.obj.dashOffset)
        
        def toArrow(event):
            a=getLangKey(self.varArrow.get())
            if a=='':a='none'
            if a=='start':a='first'
            if a=='extent':a='last'
            setArrow(self.obj, a, self.command)
            #self.master.focus_set()
        pf.Assign(self.cbArrow, toArrow, ['Return', 'FocusOut', '<ComboboxSelected>'])
        if self.obj.type=='line':
            self.varArrow.set(getLang(self.obj.arrow))
            
        def toCap(event):
            a=getLangKey(self.varCapStyle.get())
            if a=='cap':a='butt'
            setCap(self.obj, a, self.command)
            #self.master.focus_set()
        def toJoin(event):
            a=getLangKey(self.varJoinStyle.get())
            setJoin(self.obj, a, self.command)
            #self.master.focus_set()
        pf.Assign(self.cbCapStyle, toCap, ['Return', 'FocusOut', '<ComboboxSelected>'])
        pf.Assign(self.cbJoinStyle, toJoin, ['Return', 'FocusOut', '<ComboboxSelected>'])
        if self.obj.type in ['line', 'pen']:
            self.varCapStyle.set(getLang(self.obj.capStyle))
            self.varJoinStyle.set(getLang(self.obj.joinStyle))
        
        def toAnchor(event):
            a=getLangKey(self.varAnchor.get())
            setAcnhor(self.obj, a, self.command)
            #self.master.focus_set()
        pf.Assign(self.cbAnchor, toAnchor, ['Return', 'FocusOut', '<ComboboxSelected>'])
        if self.obj.type in ['window', 'picture', 'text']:
            self.varAnchor.set(getLang(self.obj.anchor))
        
        def toStipple(event):
            a=self.varStipple.get()
            if a.lower()=='none':a=''
            setStipple(self.obj, a.lower(), self.command)
            #self.master.focus_set()
        pf.Assign(self.cbStipple, toStipple, ['FocusOut', 'Return', '<ComboboxSelected>'])
        if not self.obj.type in ['window', 'picture', 'pen']:
            self.varStipple.set(self.obj.stipple)
        
        if self.obj.type in ['line', 'polygon']:
            self.varSmooth.set(self.obj.smooth)
            
        def toWindow(event):
            a=self.varWindow.get()
            if a!=self.winH:
                a=getLangKey(a)
                a=getLangWdt(a)
                setWindow(self.obj, a, self.fr5, self.theme, self.command)
                self.winH=self.varWindow.get()
                a=self.obj.setOption2W(self.fr5, self.theme)
                a.setOption()
                
            #self.master.focus_set()
        pf.Assign(self.cbWindow, toWindow, ['FocusOut', 'Return', '<ComboboxSelected>'])
        if self.obj.type=='window':
            self.varWindow.set(getLang(self.obj.windowName))
            self.winH=self.varWindow.get()
       
    def setList(self):
        self.listW.extend([[self.labName, self.entrName.frame], [self.labX, self.entrX],
                           [self.labY, self.entrY], [self.labAngle, self.spnAngle],
                           [self.labScale, self.spnScale],[self.labImg, self.entrImg.frame],
                           [self.labFill, self.bFill], [self.labOutline, self.bOutline],
                           [self.labStart, self.spnStart], [self.labExtent, self.spnExtent],
                           [self.labWidth, self.entrWidth],[self.labFont, self.cbFont],
                           [self.labSize, self.spnSize],[None, self.chWeight], [self.labText, self.entrText.frame],
                           [None, self.chItalic], [None, self.chUnderline], [None, self.chOverstrike],
                           [self.labWdt, self.entrWdt], [self.labHeight, self.entrHeight],
                           [None, self.chDash], [None, self.frameDash], [self.labArrow, self.cbArrow],
                           [self.labCapStyle, self.cbCapStyle], [self.labJoinStyle, self.cbJoinStyle],
                           [None, self.chSmooth], [None, self.canSV], [self.labAnchor, self.cbAnchor],
                           [self.labJustify, self.cbJustify], [self.labStyle, self.cbStyle],
                           [self.labWindow, self.cbWindow], [self.labStipple, self.cbStipple]])
        self.listE.extend([self.entrName, self.entrX, self.entrY, self.spnSize, self.spnScale, self.spnAngle, self.entrImg,
                           self.spnStart, self.spnExtent, self.entrWidth, self.cbFont, self.spnSize, self.entrText,
                           self.entrWdt, self.entrHeight, self.spnDashOffset, self.spnDash1, self.spnDash2,
                           self.spnDash3, self.cbArrow, self.cbCapStyle, self.cbJoinStyle, self.cbAnchor,
                           self.cbJustify, self.cbStyle, self.cbStipple, self.cbWindow])
        self.listCB.extend([ self.cbFont, self.cbArrow, self.cbCapStyle, self.cbJoinStyle, self.cbAnchor,
                           self.cbJustify, self.cbStyle, self.cbStipple, self.cbWindow])
        
    def setLine(self, obj):
        l=[self.entrName.frame, self.entrX, self.entrY, self.spnAngle, self.spnScale, self.bFill, self.entrWidth,
           self.chDash, self.cbArrow, self.cbCapStyle, self.cbJoinStyle, self.chSmooth, self.cbStipple]
        for ww in self.listW:
            if not ww[1] in l:
                if ww[0]:
                    ww[0].grid_forget()
                ww[1].grid_forget()
 
    def setPolygon(self, obj):
        l=[self.entrName.frame, self.entrX, self.entrY, self.spnAngle, self.spnScale, self.bFill, self.entrWidth,
           self.chDash,self.bOutline, self.chSmooth, self.cbStipple]
        for ww in self.listW:
            if not ww[1] in l:
                if ww[0]:
                    ww[0].grid_forget()
                ww[1].grid_forget()
    
    def setOval(self, obj):
        l=[self.entrName.frame, self.entrX, self.entrY, self.spnAngle, self.spnScale, self.bFill, self.entrWidth,
           self.chDash,self.bOutline, self.cbStipple]
        for ww in self.listW:
            if not ww[1] in l:
                if ww[0]:
                    ww[0].grid_forget()
                ww[1].grid_forget()
    
    def setArc(self, obj):
        l=[self.entrName.frame, self.entrX, self.entrY, self.spnScale, self.bFill, self.entrWidth,
           self.chDash,self.bOutline, self.cbStipple,
           self.spnStart, self.spnExtent, self.cbStyle]
        for ww in self.listW:
            if not ww[1] in l:
                if ww[0]:
                    ww[0].grid_forget()
                ww[1].grid_forget()
    
    def setPicture(self, obj):
        l=[self.entrName.frame, self.entrX, self.entrY, self.spnAngle, self.entrImg.frame,
            self.entrWdt, self.entrHeight, self.cbAnchor]
        for ww in self.listW:
            if not ww[1] in l:
                if ww[0]:
                    ww[0].grid_forget()
                ww[1].grid_forget()
    
    def setText(self, obj):
        l=[self.entrName.frame, self.entrX, self.entrY, self.spnAngle, self.bFill, self.entrWdt, self.spnSize,
           self.cbStipple, self.chItalic, self.chOverstrike, self.chUnderline, self.chWeight, self.cbAnchor,
           self.cbJustify, self.cbFont, self.entrText.frame]
        for ww in self.listW:
            if not ww[1] in l:
                if ww[0]:
                    ww[0].grid_forget()
                ww[1].grid_forget()
    
    def setWindow(self, obj):
        l=[self.entrName.frame, self.entrX, self.entrY, self.cbAnchor, self.entrWdt, self.entrHeight, self.cbWindow]
        for ww in self.listW:
            if not ww[1] in l:
                if ww[0]:
                    ww[0].grid_forget()
                ww[1].grid_forget()
    
    def setPen(self, obj):
        l=[self.bFill, self.entrWidth, self.cbJoinStyle,
           self.cbCapStyle]
        for ww in self.listW:
            if not ww[1] in l:
                if ww[0]:
                    ww[0].grid_forget()
                ww[1].grid_forget()

if __name__=='__main__':
    import object2W
    fen=tk.Tk()
    can=ScrollableFrame(fen, width=500, height=500, bg=pf.COLORS['--dark-color'])
    c=tk.Canvas(fen, width=500, height=500, bg='white')
    b=object2D.Line(c, [100, 300, 200], [100, 200, 300])
    a=Option2D(can.frame, b)
    a.setOption()
    can.grid()
    c.grid(row=0, column=2)
    def u(event):
        xx=a.listE.copy()
        if not event.widget in xx:
            fen.focus_set()
    pf.Assign(fen, u, ['Button-1'])
    fen.mainloop()