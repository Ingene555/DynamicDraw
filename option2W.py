import pyfunct as pf
import tkinter as tk
import tkinter.ttk as ttk
from language import getLang, getLangKey
from tkinter.font import Font
import widgets as wd
import math
import symbols as sb
from tkinter import filedialog as fd
from tkinter import colorchooser as cc
from PIL import Image, ImageTk
import os

def setActiveBg(class_, value, command=None):
    if command:
        command()
    class_.setActiveBg(value)

def setActiveFg(class_, value, command=None):
    if command:
        command()
    class_.setActiveFg(value)

def setAnchor(class_, value, command=None):
    if command:
        command()
    class_.setAnchor(value)

def setAspect(class_,  value, command=None):
    try:
        if command:
            command()
        a=int(eval(str(value)))
        class_.setAspect(a)
    except Exception as e:print(e)

def setBd(class_,  value, command=None):
    try:
        if command:
            command()
        a=int(eval(str(value)))
        class_.setBd(a)
    except Exception as e:print(e)

def setBg(class_,  value, command=None):
    if command:
        command()
    class_.setBg(value)

def setBitmap(class_,  value, command=None):
    if command:
        command()
    class_.setBitmap(value)

def setButtonBg(class_,  value, command=None):
    if command:
        command()
    class_.setButtonBg(value)

def setButtonCur(class_,  value, command=None):
    if command:
        command()
    class_.setButtonCursor(value)

def setButtonDrel(class_,  value, command=None):
    if command:
        command()
    class_.setButtonDrel(value)

def setButtonUrel(class_,  value, command=None):
    if command:
        command()
    class_.setButtonUrel(value)

def setCompound(class_,  value, command=None):
    if command:
        command()
    class_.setCompound(value)

def setCursor(class_,  value, command=None):
    if command:
        command()
    class_.setCursor(value)

def setDirection(class_,  value, command=None):
    if command:
        command()
    class_.setDirection(value)

def setOffrelief(class_,  value, command=None):
    if command:
        command()
    class_.setOffrelief(value)

def setFont(class_, font, weight, slant, under, over, command=None):
    if command:
            command()
    class_.setFont(font)
    class_.setWeigth('bold' if weight==True else 'normal')
    class_.setSlant('italic' if slant==True else 'roman')
    class_.setUnderline(under)
    class_.setOverstrike(over)

def setSize(class_,  value, command=None):
    try:
        if command:
            command()
        a=int(eval(str(value)))
        class_.setSize(a)
    except Exception as e:print(a)

def setFrom(class_,  value, command=None):
    try:
        if command:
            command()
        a=int(eval(str(value)))
        class_.setFrom(a)
    except Exception as e:print(e)

def setFg(class_,  value, command=None):
    if command:
        command()
    class_.setFg(value)

def setHeight(class_,  value, command=None):
    try:
        if command:
            command()
        a=int(eval(str(value)))
        class_.setHeight(a)
    except Exception as e:print(e)

def setHighBg(class_,  value, command=None):
    if command:
        command()
    class_.setHighBg(value)

def setHighFg(class_,  value, command=None):
    if command:
        command()
    class_.setHighFg(value)

def setHighTn(class_,  value, command=None):
    try:
        if command:
            command()
        a=int(eval(str(value)))
        class_.setHighTn(a)
    except Exception as e:print(e)

def setImage(class_,  value, command=None):
    try:
        if command:
            command()
        if value.strip()!='':
            time=pf.Temps()
            path=os.path.join('temps', 'temps%s.%s'%(str(time.an())+str(time.mois())+str(time.jour())+str(time.heure())+str(time.minute())+str(time.seconde())+str(time.micros()), 'png'))
            a=ImgToImg(value).toPNG(path)
            a=ModSize(a).setSize(class_.winfo_width(), class_.winfo_height())[1][0]
            image = Image.open(a)
            photo = ImageTk.PhotoImage(image)
        else:photo=''
        class_.setImage(photo)
    except Exception as e:print(e)

def setIndicatoron(class_,  value, command=None):
    if command:
        command()
    class_.setIndicatoron(value)

def setInsertBg(class_,  value, command=None):
    if command:
        command()
    class_.setInsertBg(value)

def setInsertBdWdt(class_,  value, command=None):
    try:
        if command:
            command()
        a=int(eval(str(value)))
        class_.setInsertBdWidth(a)
    except Exception as e:print(e)

def setInsertWdth(class_,  value, command=None):
    try:
        if command:
            command()
        a=int(eval(str(value)))
        class_.setInsertWidth(a)
    except Exception as e:print(e)

def setJustify(class_,  value, command=None):
    if command:
        command()
    class_.setJustify(value)

def setLabel(class_,  value, command=None):
    if command:
        command()
    class_.setLabel(value)

def setLabelanchor(class_,  value, command=None):
    if command:
        command()
    class_.setLabelanchor(value)

def setLength(class_,  value, command=None):
    try:
        if command:
            command()
        a=int(eval(str(value)))
        class_.setLength(a)
    except Exception as e:print(e)

def setOrient(class_,  value, command=None):
    if command:
        command()
    class_.setOrient(value)

def setOverrelief(class_,  value, command=None):
    if command:
        command()
    class_.setOverrelief(value)

def setPadx(class_,  value, command=None):
    try:
        if command:
            command()
        a=int(eval(str(value)))
        class_.setPadx(a)
    except Exception as e:print(e)

def setPady(class_,  value, command=None):
    try:
        if command:
            command()
        a=int(eval(str(value)))
        class_.setPady(a)
    except Exception as e:print(e)

def setRelief(class_,  value, command=None):
    if command:
        command()
    class_.setRelief(value)

def setSelectBg(class_,  value, command=None):
    if command:
        command()
    class_.setSelectBg(value)

def setSelectBdWdt(class_,  value, command=None):
    try:
        if command:
            command()
        a=int(eval(str(value)))
        class_.setSelectBdWidth(a)
    except Exception as e:print(e)

def setSelectFg(class_,  value, command=None):
    if command:
        command()
    class_.setSelectFg(value)

def setSelectImg(class_,  value, command=None):
    try:
        if command:
            command()
        class_.setSelectimage(value)
    except Exception as e:print(e)

def setShow(class_,  value, command=None):
    if command:
        command()
    class_.setShow(value)

def setShowvalue(class_,  value, command=None):
    if command:
        command()
    class_.setShowvalue(value)

def setSliderlgt(class_,  value, command=None):
    try:
        if command:
            command()
        a=int(eval(str(value)))
        class_.setSliderlength(a)
    except Exception as e:print(e)

def setSliderrel(class_,  value, command=None):
    if command:
        command()
    class_.setSliderrelief(value)

def setText(class_,  value, command=None):
    if command:
        command()
    class_.setText(value)

def setTo(class_,  value, command=None):
    try:
        if command:
            command()
        a=int(eval(str(value)))
        class_.setTo(a)
    except Exception as e:print(e)

def setTroughcolor(class_,  value, command=None):
    if command:
        command()
    class_.setTroughcolor(value)

def setWidth(class_,  value, command=None):
    try:
        if command:
            command()
        a=int(eval(str(value)))
        class_.setWidth(a)
    except Exception as e:print(e)

def setWraplength(class_,  value, command=None):
    try:
        if command:
            command()
        a=int(eval(str(value)))
        class_.setWraplength(a)
    except Exception as e:print(e)

class ImgToImg:
    def __init__(self, image, format_ = None):
        self.from_img = image
        if not format_:
            self.from_format = image.rsplit('.')[len(image.rsplit('.')[:])-1]
        else:self.from_format = format_
        self.from_format = self.from_format.lower()

    def toPNG(self, path):
        if self.from_format!='png':
            with Image.open(self.from_img) as img:
                    output_file = os.path.splitext(path)[0] + ".png"
                    img.save(output_file)

            return path
        else:
            return self.from_img

class ModSize:
    def __init__(self, image, format_ = None):
        self.from_image = image
        if not format_:
            self.from_format = image.rsplit('.')[len(image.rsplit('.')[:])-1]
        else:self.from_format = format_
        self.from_format = self.from_format.lower()
        
    def setSize(self, width = None, height = None, angle = None):
        time=pf.Temps()
        self.temp =os.path.join('temps', 'temps%s.%s'%(str(time.an())+str(time.mois())+str(time.jour())+str(time.heure())+str(time.minute())+str(time.seconde())+str(time.micros()), self.from_format))
        image = Image.open(self.from_image)
        initWidth=image.width
        initHeight=image.height
        self.wdt = width if width else image.width
        self.hgt = height if height else image.height
        self.ang = angle if angle else 0
        resized_image = image.resize((self.wdt, self.hgt))
        rotated_image = resized_image.rotate(self.ang, expand=True)
        rotated_image.save(self.temp)
        return [[self.from_image, initWidth, initHeight, 0], [self.temp, self.wdt, self.hgt, self.ang]]

class ScrollableFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.can = tk.Canvas(self, bd=0, highlightthickness=1, highlightcolor=pf.COLORS['--dark-purple'], relief=tk.FLAT,
                             width=self.cget('width'), height=self.cget('height'), bg=self['bg'])
        self.can.grid(row=1, column=1, sticky=tk.NSEW)
        self.can.grid_columnconfigure(1, weight=1)
        self.can.grid_rowconfigure(1, weight=1)
        self.v_scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.can.yview, width=9)
        self.v_scrollbar.grid(row=1, column=2, sticky=tk.NS)
        self.h_scrollbar = tk.Scrollbar(self, orient=tk.HORIZONTAL, command=self.can.xview, width=9)
        self.h_scrollbar.grid(row=2, column=1, sticky=tk.EW)
        self.can.configure(yscrollcommand=self.v_scrollbar.set, xscrollcommand=self.h_scrollbar.set)
        self.can.bind_all("<MouseWheel>", lambda event: self.can.yview_scroll(int(-1*(event.delta/120)), "units"))
        self.inner_frame = tk.Canvas(self.can, bg=self['bg'])
        self.frame=self.inner_frame
        self.window = self.can.create_window(int(pf.Get(self.inner_frame).x())/2, int(pf.Get(self.inner_frame).y())/2, window=self.inner_frame, anchor="center")
        self.inner_frame.bind("<Configure>", self.windowed)
        self.can.after(150, lambda: self.can.coords(self.window, int(pf.Get(self.inner_frame).x())/2, int(pf.Get(self.inner_frame).y())/2))
    
    def windowed(self, event):
        self.can.configure(scrollregion=(0, 0, int(pf.Get(self.inner_frame).x()), int(pf.Get(self.inner_frame).y())))
        self.can.coords(self.window, int(pf.Get(self.inner_frame).x())/2, int(pf.Get(self.inner_frame).y())/2)
    
    def resized(self, event=None):
        self.can['width']=self.cget('width')
        self.can['height']=self.cget('height')
    
    def setFrameSize(self, event=None):
        self.inner_frame['width']=self.can.cget('width')
        self.inner_frame['height']=self.can.cget('height')


class Option2W:
    def __init__(self, master, object2w, theme=None, command=None):
        self.master=master
        self.obj=object2w
        self.command=command
        self.theme=theme if theme else [pf.COLORS['--dark-color'], 'white', pf.COLORS['--dark-color-1'], pf.COLORS['--light-color-1']]
        self.dico={
            'button':self.setButton,
            'checkbutton':self.setCheckbutton,
            'entry':self.setEntry,
            'frame':self.setFrame,
            'label':self.setLabel,
            'labelframe':self.setLabelFrame,
            'listbox':self.setListbox,
            'message':self.setMessage,
            'menubutton':self.setMenubutton,
            'radiobutton':self.setRadiobutton,
            'scale':self.setScale,
            'text':self.setText,
            'scrollableframe':self.setScrollableframe,
            'spinbox':self.setSpinbox
        }
    
    def setOption(self):
        for ww in self.master.winfo_children():
            ww.destroy()
        self.listW=[]
        self.listE=[]
        self.listCB=[]
        
        def setActiveBg_():
            a=cc.askcolor(title=getLang("choose a color"), initialcolor=self.bActiveBg['bg'])[1]
            if a:
                self.varActiveBg.set(a)
                self.bActiveBg['bg']=a
                setActiveBg(self.obj, a, self.command)
        self.varActiveBg=tk.StringVar()
        self.bActiveBg=tk.Button(self.master, width=17, relief=tk.FLAT, bd=0, highlightthickness=0,
                                bg='black', activebackground=self.theme[3], cursor='hand2', command=setActiveBg_)
        self.labActiveBg=tk.Label(self.master, text=getLang('activebackground'), bg=self.theme[0], 
                                  fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        def setActiveFg_():
            a=cc.askcolor(title=getLang("choose a color"), initialcolor=self.bActiveFg['bg'])[1]
            if a:
                self.varActiveFg.set(a)
                self.bActiveFg['bg']=a
                setActiveFg(self.obj, a, self.command)
        self.varActiveFg=tk.StringVar()
        self.bActiveFg=tk.Button(self.master, width=17, relief=tk.FLAT, bd=0, highlightthickness=0,
                                bg='black', activebackground=self.theme[3], cursor='hand2', command=setActiveFg_)
        self.labActiveFg=tk.Label(self.master, text=getLang('activeforeground'), bg=self.theme[0], 
                                  fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        self.varAnchor=tk.StringVar()
        l=[getLang('center'), getLang('n'), getLang('s'), getLang('e'), getLang('w'), getLang('ne'), getLang('nw'), getLang('se'), getLang('sw')]
        self.cbAnchor = ttk.Combobox(self.master, style='ComboMod.TCombobox', values=l, textvariable=self.varAnchor, width=17, state='readonly', cursor='hand2')
        self.labAnchor=tk.Label(self.master, text=getLang('anchor'), bg=self.theme[0], fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        self.varAspect=tk.StringVar()
        self.spnAspect=tk.Spinbox(self.master, bg=self.theme[2], fg=self.theme[1], border=0, highlightcolor=pf.COLORS['--dark-blue'],highlightthickness=0,
                               disabledbackground=self.theme[3], disabledforeground=self.theme[1], insertbackground=self.theme[1],
                               font=Font(family=pf.POLICE[0], size=11, weight='bold'), textvariable=self.varAspect, width=20, from_=0, to=math.inf,
                               buttonbackground=self.theme[3], buttoncursor='hand2', buttondownrelief=tk.FLAT, buttonuprelief=tk.FLAT,
                               command=lambda: setAspect(self.obj, self.varAspect.get(), self.command))
        self.labAspect=tk.Label(self.master, text=getLang('aspect'), bg=self.theme[0], fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        self.varBd=tk.StringVar()
        self.spnBd=tk.Spinbox(self.master, bg=self.theme[2], fg=self.theme[1], border=0, highlightcolor=pf.COLORS['--dark-blue'],highlightthickness=0,
                               disabledbackground=self.theme[3], disabledforeground=self.theme[1], insertbackground=self.theme[1],
                               font=Font(family=pf.POLICE[0], size=11, weight='bold'), textvariable=self.varBd, width=20, from_=0, to=math.inf,
                               buttonbackground=self.theme[3], buttoncursor='hand2', buttondownrelief=tk.FLAT, buttonuprelief=tk.FLAT,
                               command=lambda:setBd(self.obj, self.varBd.get(), self.command))
        self.labBd=tk.Label(self.master, text=getLang('border'), bg=self.theme[0], fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        def setBg_():
            a=cc.askcolor(title=getLang("choose a color"), initialcolor=self.bBg['bg'])[1]
            if a:
                self.varBg.set(a)
                self.bBg['bg']=a
                setBg(self.obj, a, self.command)
        self.varBg=tk.StringVar()
        self.bBg=tk.Button(self.master, width=17, relief=tk.FLAT, bd=0, highlightthickness=0,
                                bg='black', activebackground=self.theme[3], cursor='hand2',
                                command=setBg_)
        self.labBg=tk.Label(self.master, text=getLang('background'), bg=self.theme[0], 
                                  fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
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
        self.varBitmap = tk.StringVar()
        l=['', 'error', 'gray75', 'gray50', 'gray25', 'gray12', 'hourglass', 'info', 'questhead', 'question', 'warning']
        self.cbBitmap = ttk.Combobox(self.master, style='ComboMod.TCombobox', values=l, textvariable=self.varBitmap, width=17, state='readonly', cursor='hand2')
        self.labBitmap=tk.Label(self.master, text='Bitmap', bg=self.theme[0], fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        def setBBg_():
            a=cc.askcolor(title=getLang("choose a color"), initialcolor=self.bButtonBg['bg'])[1]
            if a:
                self.varButtonBg.set(a)
                self.bButtonBg['bg']=a
                setButtonBg(self.obj, a, self.command)
        self.varButtonBg=tk.StringVar()
        self.bButtonBg=tk.Button(self.master, width=17, relief=tk.FLAT, bd=0, highlightthickness=0,
                                bg='black', activebackground=self.theme[3], cursor='hand2', command=setBBg_)
        self.labButtonBg=tk.Label(self.master, text=getLang('buttonbackground'), bg=self.theme[0], 
                                  fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        self.varButtonCur = tk.StringVar()
        self.cbButtonCur = ttk.Combobox(self.master, style='ComboMod.TCombobox', values=pf.CURSEURS, textvariable=self.varButtonCur, width=17, state='readonly', cursor='hand2')
        self.labButtonCur=tk.Label(self.master, text=getLang('buttoncursor'), bg=self.theme[0], fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        self.varButtonDRel = tk.StringVar()
        l=[getLang(''), getLang('flat'), getLang('raised'), getLang('sunken'), getLang('groove'), getLang('ridge')]
        self.cbButtonDRel = ttk.Combobox(self.master, style='ComboMod.TCombobox', values=l, textvariable=self.varButtonDRel, width=17, state='readonly', cursor='hand2')
        self.labButtonDRel=tk.Label(self.master, text=getLang('buttondownrelief'), bg=self.theme[0], fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        self.varButtonURel = tk.StringVar()
        l=[getLang(''), getLang('flat'), getLang('raised'), getLang('sunken'), getLang('groove'), getLang('ridge')]
        self.cbButtonURel = ttk.Combobox(self.master, style='ComboMod.TCombobox', values=l, textvariable=self.varButtonURel, width=17, state='readonly', cursor='hand2')
        self.labButtonURel=tk.Label(self.master, text=getLang('buttonuprelief'), bg=self.theme[0], fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        self.varCompound = tk.StringVar()
        l=[getLang('top'), getLang('bottom'), getLang('left'), getLang('right'), getLang('center')]
        self.cbCompound = ttk.Combobox(self.master, style='ComboMod.TCombobox', values=l, textvariable=self.varCompound, width=17, state='readonly', cursor='hand2')
        self.labCompound=tk.Label(self.master, text=getLang('compound'), bg=self.theme[0], fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        self.varCursor = tk.StringVar()
        self.cbCursor = ttk.Combobox(self.master, style='ComboMod.TCombobox', values=pf.CURSEURS, textvariable=self.varCursor, width=17, state='readonly', cursor='hand2')
        self.labCursor=tk.Label(self.master, text=getLang('cursor'), bg=self.theme[0], fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        self.varDirection = tk.StringVar()
        l=[getLang('below'), getLang('above'), getLang('left'), getLang('right')]
        self.cbDirection = ttk.Combobox(self.master, style='ComboMod.TCombobox', values=l, textvariable=self.varDirection, width=17, state='readonly', cursor='hand2')
        self.labDirection=tk.Label(self.master, text=getLang('direction'), bg=self.theme[0], fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        self.varOffrelief = tk.StringVar()
        l=[getLang('flat'), getLang('raised'), getLang('sunken'), getLang('groove'), getLang('ridge')]
        self.cbOffrelief = ttk.Combobox(self.master, style='ComboMod.TCombobox', values=l, textvariable=self.varOffrelief, width=17, state='readonly', cursor='hand2')
        self.labOffrelief=tk.Label(self.master, text=getLang('offrelief'), bg=self.theme[0], fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        self.varFont = tk.StringVar()
        self.cbFont = ttk.Combobox(self.master, style='ComboMod.TCombobox', values=pf.POLICE, textvariable=self.varFont, width=17, state='readonly', cursor='hand2')
        self.labFont=tk.Label(self.master, text=getLang('family'), bg=self.theme[0], fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        self.varSize=tk.StringVar()
        self.spnSize=tk.Spinbox(self.master, bg=self.theme[2], fg=self.theme[1], border=0, highlightcolor=pf.COLORS['--dark-blue'],highlightthickness=0,
                               disabledbackground=self.theme[3], disabledforeground=self.theme[1], insertbackground=self.theme[1],
                               font=Font(family=pf.POLICE[0], size=11, weight='bold'), textvariable=self.varSize, width=20, from_=1,to=math.inf,
                               buttonbackground=self.theme[3], buttoncursor='hand2', buttondownrelief=tk.FLAT, buttonuprelief=tk.FLAT,
                               command=lambda:setSize(self.obj, self.varSize.get(), self.command))
        self.labSize=tk.Label(self.master, text=getLang('size'), bg=self.theme[0], fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        self.varWeight=tk.IntVar()
        self.chWeight=tk.Checkbutton(self.master, width=15, relief=tk.FLAT, bd=0, highlightthickness=0, bg=self.theme[0], fg=self.theme[1], cursor='hand2',
                                     borderwidth=0, variable=self.varWeight, text=getLang('weight'), activebackground=self.theme[0],anchor='w',justify='center',
                                     highlightbackground=self.theme[0], activeforeground=self.theme[1], selectcolor=self.theme[0],
                                     command=lambda:setFont(self.obj, self.varFont.get(), self.varWeight.get(), self.varSlant.get(), self.varUnderline.get(), self.varOverstrike.get(), self.command))
        self.varSlant=tk.IntVar()
        self.chSlant=tk.Checkbutton(self.master, width=15, relief=tk.FLAT, bd=0, highlightthickness=0, bg=self.theme[0], fg=self.theme[1], cursor='hand2',
                                     borderwidth=0, variable=self.varSlant, text=getLang('italic'), activebackground=self.theme[0],anchor='w',justify='center',
                                     highlightbackground=self.theme[0], activeforeground=self.theme[1], selectcolor=self.theme[0],
                                     command=lambda:setFont(self.obj, self.varFont.get(), self.varWeight.get(), self.varSlant.get(), self.varUnderline.get(), self.varOverstrike.get(), self.command))
        self.varUnderline=tk.IntVar()
        self.chUnderline=tk.Checkbutton(self.master, width=15, relief=tk.FLAT, bd=0, highlightthickness=0, bg=self.theme[0], fg=self.theme[1], cursor='hand2',
                                     borderwidth=0, variable=self.varUnderline, text=getLang('underline'), activebackground=self.theme[0],anchor='w',justify='center',
                                     highlightbackground=self.theme[0], activeforeground=self.theme[1], selectcolor=self.theme[0],
                                     command=lambda:setFont(self.obj, self.varFont.get(), self.varWeight.get(), self.varSlant.get(), self.varUnderline.get(), self.varOverstrike.get(), self.command))
        self.varOverstrike=tk.IntVar()
        self.chOverstrike=tk.Checkbutton(self.master, width=15, relief=tk.FLAT, bd=0, highlightthickness=0, bg=self.theme[0], fg=self.theme[1], cursor='hand2',
                                     borderwidth=0, variable=self.varOverstrike, text=getLang('overstrike'), activebackground=self.theme[0],anchor='w',justify='center',
                                     highlightbackground=self.theme[0], activeforeground=self.theme[1], selectcolor=self.theme[0],
                                     command=lambda:setFont(self.obj, self.varFont.get(), self.varWeight.get(), self.varSlant.get(), self.varUnderline.get(), self.varOverstrike.get(), self.command))
        def setFg_():
            a=cc.askcolor(title=getLang("choose a color"), initialcolor=self.bFg['bg'])[1]
            if a:
                self.varFg=a
                self.bFg['bg']=a
                setFg(self.obj, a, self.command)
        self.varFg=tk.StringVar()
        self.bFg=tk.Button(self.master, width=17, relief=tk.FLAT, bd=0, highlightthickness=0,
                                bg='black', activebackground=self.theme[3], cursor='hand2', command=setFg_)
        self.labFg=tk.Label(self.master, text=getLang('foreground'), bg=self.theme[0], fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        self.varFrom=tk.StringVar()
        self.spnFrom=tk.Spinbox(self.master, bg=self.theme[2], fg=self.theme[1], border=0, highlightcolor=pf.COLORS['--dark-blue'],highlightthickness=0,
                               disabledbackground=self.theme[3], disabledforeground=self.theme[1], insertbackground=self.theme[1],
                               font=Font(family=pf.POLICE[0], size=11, weight='bold'), textvariable=self.varFrom, width=20, from_=-math.inf, to=math.inf,
                               buttonbackground=self.theme[3], buttoncursor='hand2', buttondownrelief=tk.FLAT, buttonuprelief=tk.FLAT,
                               command=lambda: setFrom(self.obj, self.varFrom.get(), self.command))
        self.labFrom=tk.Label(self.master, text=getLang('from'), bg=self.theme[0], fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        self.varHeight=tk.StringVar()
        self.entrHeight=tk.Entry(self.master, bg=self.theme[2], fg=self.theme[1], border=0, highlightcolor=pf.COLORS['--dark-blue'],highlightthickness=0,
                               disabledbackground=self.theme[3], disabledforeground=self.theme[1], insertbackground=self.theme[1],
                               font=Font(family=pf.POLICE[0], size=12, weight='bold'), textvariable=self.varHeight, width=20)
        self.labHeight=tk.Label(self.master, text=getLang('height'), bg=self.theme[0], fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        def setHighBg_():
            a=cc.askcolor(title=getLang("choose a color"), initialcolor=self.bHighBg['bg'])[1]
            if a:
                self.varHighBg.set(a)
                self.bHighBg['bg']=a
                setHighBg(self.obj, a, self.command)
        self.varHighBg=tk.StringVar()
        self.bHighBg=tk.Button(self.master, width=17, relief=tk.FLAT, bd=0, highlightthickness=0,
                                bg='black', activebackground=self.theme[3], cursor='hand2', command=setHighBg_)
        self.labHighBg=tk.Label(self.master, text=getLang('highlightbackground'), bg=self.theme[0], 
                                  fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        def setHighFg_():
            a=cc.askcolor(title=getLang("choose a color"), initialcolor=self.bHighFg['bg'])[1]
            if a:
                self.varHighFg.set(a)
                self.bHighFg['bg']=a
                setHighFg(self.obj, a, self.command)
        self.varHighFg=tk.StringVar()
        self.bHighFg=tk.Button(self.master, width=17, relief=tk.FLAT, bd=0, highlightthickness=0,
                                bg='black', activebackground=self.theme[3], cursor='hand2', command=setHighFg_)
        self.labHighFg=tk.Label(self.master, text=getLang('highlightcolor'), bg=self.theme[0], 
                                  fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        self.varHighTn=tk.StringVar()
        self.spnHighTn=tk.Spinbox(self.master, bg=self.theme[2], fg=self.theme[1], border=0, highlightcolor=pf.COLORS['--dark-blue'],highlightthickness=0,
                               disabledbackground=self.theme[3], disabledforeground=self.theme[1], insertbackground=self.theme[1],
                               font=Font(family=pf.POLICE[0], size=11, weight='bold'), textvariable=self.varHighTn, width=20, from_=0,to=math.inf,
                               buttonbackground=self.theme[3], buttoncursor='hand2', buttondownrelief=tk.FLAT, buttonuprelief=tk.FLAT,
                               command=lambda:setHighTn(self.obj, self.varHighTn.get(), self.command))
        self.labHighTn=tk.Label(self.master, text=getLang('highlightthickness'), bg=self.theme[0], fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        self.varImg=tk.StringVar()
        self.entrImg=wd.Entrytk(self.master, bg=self.theme[2], fg=self.theme[1], border=0, highlightcolor=pf.COLORS['--dark-blue'],highlightthickness=0,
                               disabledbackground=self.theme[3], disabledforeground=self.theme[1], insertbackground=self.theme[1],
                               font=Font(family=pf.POLICE[0], size=10, weight='normal'), textvariable=self.varImg, width=15)
        self.entrImg.frame.config(bg=self.theme[0], border=0, highlightthickness=0, relief=tk.FLAT, width=70)
        def setImage_():
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
                setImage(self.obj, a, self.command)
                self.varImg.set(a)
        self.entrImg.add_button(text=chr(60709), relief=tk.FLAT, bd=0, highlightthickness=0,
                                bg=self.theme[2], activebackground=self.theme[3], cursor='hand2', command=setImage_)
        self.labImg=tk.Label(self.master, text=getLang('image'), bg=self.theme[0], fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        self.varIndicatoron=tk.IntVar()
        self.chIndicatoron=tk.Checkbutton(self.master, width=15, relief=tk.FLAT, bd=0, highlightthickness=0, bg=self.theme[0], fg=self.theme[1], cursor='hand2',
                                     borderwidth=0, variable=self.varIndicatoron, text=getLang('indicatoron'), activebackground=self.theme[0],anchor='w',justify='center',
                                     highlightbackground=self.theme[0], activeforeground=self.theme[1], selectcolor=self.theme[0],
                                     command=lambda:setIndicatoron(self.obj, self.varIndicatoron.get(), self.command))
        def setInsertBg_():
            a=cc.askcolor(title=getLang("choose a color"), initialcolor=self.bInsertBg['bg'])[1]
            if a:
                self.varInsertBg.set(a)
                self.bInsertBg['bg']=a
                setInsertBg(self.obj, a, self.command)
        self.varInsertBg=tk.StringVar()
        self.bInsertBg=tk.Button(self.master, width=17, relief=tk.FLAT, bd=0, highlightthickness=0,
                                bg='black', activebackground=self.theme[3], cursor='hand2',
                                command=setInsertBg_)
        self.labInsertBg=tk.Label(self.master, text=getLang('insertbackground'), bg=self.theme[0], fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        self.varInsertBdWdt=tk.StringVar()
        self.spnInsertBdWdt=tk.Spinbox(self.master, bg=self.theme[2], fg=self.theme[1], border=0, highlightcolor=pf.COLORS['--dark-blue'],highlightthickness=0,
                               disabledbackground=self.theme[3], disabledforeground=self.theme[1], insertbackground=self.theme[1],
                               font=Font(family=pf.POLICE[0], size=11, weight='bold'), textvariable=self.varInsertBdWdt, width=20, from_=0,to=math.inf,
                               buttonbackground=self.theme[3], buttoncursor='hand2', buttondownrelief=tk.FLAT, buttonuprelief=tk.FLAT,
                               command=lambda:setInsertBdWdt(self.obj, self.varInsertBdWdt.get(), self.command))
        self.labInsertBdWt=tk.Label(self.master, text=getLang('insertborderwidth'), bg=self.theme[0], fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        self.varInsertWidth=tk.StringVar()
        self.spnInsertWidth=tk.Spinbox(self.master, bg=self.theme[2], fg=self.theme[1], border=0, highlightcolor=pf.COLORS['--dark-blue'],highlightthickness=0,
                               disabledbackground=self.theme[3], disabledforeground=self.theme[1], insertbackground=self.theme[1],
                               font=Font(family=pf.POLICE[0], size=11, weight='bold'), textvariable=self.varInsertWidth, width=20, from_=1,to=math.inf,
                               buttonbackground=self.theme[3], buttoncursor='hand2', buttondownrelief=tk.FLAT, buttonuprelief=tk.FLAT,
                               command=lambda:setInsertWdth(self.obj, self.varInsertWidth.get(), self.command))
        self.labInsertWith=tk.Label(self.master, text=getLang('insertwidth'), bg=self.theme[0], fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        self.varJustify=tk.StringVar()
        l=[getLang('left'), getLang('center'), getLang('right')]
        self.cbJustify = ttk.Combobox(self.master, style='ComboMod.TCombobox', values=l, textvariable=self.varJustify, width=17, state='readonly', cursor='hand2')
        self.labJustify=tk.Label(self.master, text=getLang('justify'), bg=self.theme[0], fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        self.varText=tk.StringVar()
        self.entrText=wd.Entrytk(self.master, bg=self.theme[2], fg=self.theme[1], border=0, highlightcolor=pf.COLORS['--dark-blue'],highlightthickness=0,
                               disabledbackground=self.theme[3], disabledforeground=self.theme[1], insertbackground=self.theme[1],
                               font=Font(family=pf.POLICE[0], size=11, weight='bold'), textvariable=self.varText, width=15)
        self.entrText.frame.config(bg=self.theme[0], border=0, highlightthickness=0, relief=tk.FLAT)
        self.entrText.add_button(text=chr(937), relief=tk.FLAT, bd=0, highlightthickness=0,font=Font(family=pf.POLICE[0], size=10, weight='bold'),
                                bg=self.theme[2], activebackground=self.theme[3], cursor='hand2', command=lambda:sb.Container(self.master, self.entrText, self.theme))
        self.labText=tk.Label(self.master, text=getLang('text'), bg=self.theme[0], fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        self.varLabelanchor=tk.StringVar()
        l=[getLang('e'), getLang('en'), getLang('es'), getLang('n'), getLang('ne'), 
           getLang('nw'), getLang('s'), getLang('se'), getLang('sw'), getLang('w'),
           getLang('wn'), getLang('ws')]
        self.cbLabelanchor = ttk.Combobox(self.master, style='ComboMod.TCombobox', values=l, textvariable=self.varLabelanchor, width=17, state='readonly', cursor='hand2')
        self.labLabelanchor=tk.Label(self.master, text=getLang('labelanchor'), bg=self.theme[0], fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        self.varLength=tk.StringVar()
        self.spnLength=tk.Spinbox(self.master, bg=self.theme[2], fg=self.theme[1], border=0, highlightcolor=pf.COLORS['--dark-blue'],highlightthickness=0,
                               disabledbackground=self.theme[3], disabledforeground=self.theme[1], insertbackground=self.theme[1],
                               font=Font(family=pf.POLICE[0], size=11, weight='bold'), textvariable=self.varLength, width=20, from_=0,to=math.inf,
                               buttonbackground=self.theme[3], buttoncursor='hand2', buttondownrelief=tk.FLAT, buttonuprelief=tk.FLAT,
                               command=lambda:setLength(self.obj, self.varLength.get(), self.command))
        self.labLength=tk.Label(self.master, text=getLang('length'), bg=self.theme[0], fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        self.varOrient=tk.StringVar()
        l=[getLang('horizontal'), getLang('vertical')]
        self.cbOrient = ttk.Combobox(self.master, style='ComboMod.TCombobox', values=l, textvariable=self.varOrient, width=17, state='readonly', cursor='hand2')
        self.labOrient=tk.Label(self.master, text=getLang('orient'), bg=self.theme[0], fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        self.varOverRel = tk.StringVar()
        l=[getLang(''), getLang('flat'), getLang('raised'), getLang('sunken'), getLang('groove'), getLang('ridge')]
        self.cbOverRel = ttk.Combobox(self.master, style='ComboMod.TCombobox', values=l, textvariable=self.varOverRel, width=17, state='readonly', cursor='hand2')
        self.labOverRel=tk.Label(self.master, text=getLang('overrelief'), bg=self.theme[0], fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        self.varPadx=tk.StringVar()
        self.spnPadx=tk.Spinbox(self.master, bg=self.theme[2], fg=self.theme[1], border=0, highlightcolor=pf.COLORS['--dark-blue'],highlightthickness=0,
                               disabledbackground=self.theme[3], disabledforeground=self.theme[1], insertbackground=self.theme[1],
                               font=Font(family=pf.POLICE[0], size=11, weight='bold'), textvariable=self.varPadx, width=20, from_=0,to=math.inf,
                               buttonbackground=self.theme[3], buttoncursor='hand2', buttondownrelief=tk.FLAT, buttonuprelief=tk.FLAT,
                               command=lambda:setPadx(self.obj, self.varPadx.get(), self.command))
        self.labPadx=tk.Label(self.master, text='Padx', bg=self.theme[0], fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        self.varPady=tk.StringVar()
        self.spnPady=tk.Spinbox(self.master, bg=self.theme[2], fg=self.theme[1], border=0, highlightcolor=pf.COLORS['--dark-blue'],highlightthickness=0,
                               disabledbackground=self.theme[3], disabledforeground=self.theme[1], insertbackground=self.theme[1],
                               font=Font(family=pf.POLICE[0], size=11, weight='bold'), textvariable=self.varPady, width=20, from_=0,to=math.inf,
                               buttonbackground=self.theme[3], buttoncursor='hand2', buttondownrelief=tk.FLAT, buttonuprelief=tk.FLAT,
                               command=lambda:setPady(self.obj, self.varPady.get(), self.command))
        self.labPady=tk.Label(self.master, text='Pady', bg=self.theme[0], fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        self.varRelief = tk.StringVar()
        l=[getLang('flat'), getLang('raised'), getLang('sunken'), getLang('groove'), getLang('ridge')]
        self.cbRelief = ttk.Combobox(self.master, style='ComboMod.TCombobox', values=l, textvariable=self.varRelief, width=17, state='readonly', cursor='hand2')
        self.labRelief=tk.Label(self.master, text=getLang('relief'), bg=self.theme[0], fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        def setSelectBg_():
            a=cc.askcolor(title=getLang("choose a color"), initialcolor=self.bSelectBg['bg'])[1]
            if a:
                self.varSelectBg.set(a)
                self.bSelectBg['bg']=a
                setSelectBg(self.obj, a, self.command)
        self.varSelectBg=tk.StringVar()
        self.bSelectBg=tk.Button(self.master, width=17, relief=tk.FLAT, bd=0, highlightthickness=0,
                                bg='black', activebackground=self.theme[3], cursor='hand2', command=setSelectBg_)
        self.labSelectBg=tk.Label(self.master, text=getLang('selectbackground'), bg=self.theme[0], fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        self.varSelectBdWdt=tk.StringVar()
        self.spnSelectBdWdt=tk.Spinbox(self.master, bg=self.theme[2], fg=self.theme[1], border=0, highlightcolor=pf.COLORS['--dark-blue'],highlightthickness=0,
                               disabledbackground=self.theme[3], disabledforeground=self.theme[1], insertbackground=self.theme[1],
                               font=Font(family=pf.POLICE[0], size=11, weight='bold'), textvariable=self.varSelectBdWdt, width=20, from_=0,to=math.inf,
                               buttonbackground=self.theme[3], buttoncursor='hand2', buttondownrelief=tk.FLAT, buttonuprelief=tk.FLAT,
                               command=lambda:setSelectBdWdt(self.obj, self.varSelectBdWdt.get(), self.command))
        self.labSelectBdWt=tk.Label(self.master, text=getLang('selectborderwidth'), bg=self.theme[0], fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        def setSelectFg_():
            a=cc.askcolor(title=getLang("choose a color"), initialcolor=self.bSelectFg['bg'])[1]
            if a:
                self.varSelectFg.set(a)
                self.bSelectFg['bg']=a
                setSelectFg(self.obj, a, self.command)
        self.varSelectFg=tk.StringVar()
        self.bSelectFg=tk.Button(self.master, width=17, relief=tk.FLAT, bd=0, highlightthickness=0,
                                bg='black', activebackground=self.theme[3], cursor='hand2',
                                command=setSelectFg_)
        self.labSelectFg=tk.Label(self.master, text=getLang('selectcolor'), bg=self.theme[0], fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        self.varSelectImg=tk.StringVar()
        self.entrSelectImg=wd.Entrytk(self.master, bg=self.theme[2], fg=self.theme[1], border=0, highlightcolor=pf.COLORS['--dark-blue'],highlightthickness=0,
                               disabledbackground=self.theme[3], disabledforeground=self.theme[1], insertbackground=self.theme[1],
                               font=Font(family=pf.POLICE[0], size=10, weight='normal'), textvariable=self.varSelectImg, width=15)
        self.entrSelectImg.frame.config(bg=self.theme[0], border=0, highlightthickness=0, relief=tk.FLAT, width=70)
        self.entrSelectImg.add_button(text=chr(60709), relief=tk.FLAT, bd=0, highlightthickness=0,
                                bg=self.theme[2], activebackground=self.theme[3], cursor='hand2')
        self.labSelectImg=tk.Label(self.master, text=getLang('selectimage'), bg=self.theme[0], fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        self.varShow = tk.StringVar()
        l=['', '*', chr(1421), chr(1422), '#', '@', '-', '+', chr(176)]
        self.cbShow = ttk.Combobox(self.master, style='ComboMod.TCombobox', values=l, textvariable=self.varShow, width=17, state='readonly', cursor='hand2')
        self.labShow=tk.Label(self.master, text=getLang('show'), bg=self.theme[0], fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        self.varShowvalue=tk.IntVar()
        self.chShowvalue=tk.Checkbutton(self.master, width=15, relief=tk.FLAT, bd=0, highlightthickness=0, bg=self.theme[0], fg=self.theme[1], cursor='hand2',
                                     borderwidth=0, variable=self.varShowvalue, text=getLang('showvalue'), activebackground=self.theme[0],anchor='w',justify='center',
                                     highlightbackground=self.theme[0], activeforeground=self.theme[1], selectcolor=self.theme[0],
                                     command=lambda:setShowvalue(self.obj, self.varShowvalue.get(), self.command))
        self.varSliderlength=tk.StringVar()
        self.spnSliderlength=tk.Spinbox(self.master, bg=self.theme[2], fg=self.theme[1], border=0, highlightcolor=pf.COLORS['--dark-blue'],highlightthickness=0,
                               disabledbackground=self.theme[3], disabledforeground=self.theme[1], insertbackground=self.theme[1],
                               font=Font(family=pf.POLICE[0], size=11, weight='bold'), textvariable=self.varSliderlength, width=20, from_=0,to=math.inf,
                               buttonbackground=self.theme[3], buttoncursor='hand2', buttondownrelief=tk.FLAT, buttonuprelief=tk.FLAT,
                               command=lambda:setSliderlgt(self.obj, self.varSliderlength.get(), self.command))
        self.labSliderlength=tk.Label(self.master, text=getLang('sliderlength'), bg=self.theme[0], fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        self.varSliderRel = tk.StringVar()
        l=[getLang('flat'), getLang('raised'), getLang('sunken'), getLang('groove'), getLang('ridge')]
        self.cbSliderRel = ttk.Combobox(self.master, style='ComboMod.TCombobox', values=l, textvariable=self.varSliderRel, width=17, state='readonly', cursor='hand2')
        self.labSliderRel=tk.Label(self.master, text=getLang('sliderrelief'), bg=self.theme[0], fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        self.varLabel=tk.StringVar()
        self.entrLabel=wd.Entrytk(self.master, bg=self.theme[2], fg=self.theme[1], border=0, highlightcolor=pf.COLORS['--dark-blue'],highlightthickness=0,
                               disabledbackground=self.theme[3], disabledforeground=self.theme[1], insertbackground=self.theme[1],
                               font=Font(family=pf.POLICE[0], size=11, weight='bold'), textvariable=self.varLabel, width=15)
        self.entrLabel.frame.config(bg=self.theme[0], border=0, highlightthickness=0, relief=tk.FLAT)
        self.entrLabel.add_button(text=chr(937), relief=tk.FLAT, bd=0, highlightthickness=0,font=Font(family=pf.POLICE[0], size=10, weight='bold'),
                                bg=self.theme[2], activebackground=self.theme[3], cursor='hand2', command=lambda:sb.Container(self.master, self.entrText, self.theme))
        self.labLabel=tk.Label(self.master, text=getLang('label'), bg=self.theme[0], fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        self.varTo=tk.StringVar()
        self.spnTo=tk.Spinbox(self.master, bg=self.theme[2], fg=self.theme[1], border=0, highlightcolor=pf.COLORS['--dark-blue'],highlightthickness=0,
                               disabledbackground=self.theme[3], disabledforeground=self.theme[1], insertbackground=self.theme[1],
                               font=Font(family=pf.POLICE[0], size=11, weight='bold'), textvariable=self.varTo, width=20, from_=-math.inf, to=math.inf,
                               buttonbackground=self.theme[3], buttoncursor='hand2', buttondownrelief=tk.FLAT, buttonuprelief=tk.FLAT,
                               command=lambda:setTo(self.obj, self.varTo.get(), self.command))
        self.labTo=tk.Label(self.master, text=getLang('to'), bg=self.theme[0], fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        def setTroughcolor_():
            a=cc.askcolor(title=getLang("choose a color"), initialcolor=self.bTroughcolor['bg'])[1]
            if a:
                self.varTroughcolor.set(a)
                self.bTroughcolor['bg']=a
                setTroughcolor(self.obj, a, self.command)
        self.varTroughcolor=tk.StringVar()
        self.bTroughcolor=tk.Button(self.master, width=17, relief=tk.FLAT, bd=0, highlightthickness=0,
                                bg='black', activebackground=self.theme[3], cursor='hand2', command=setTroughcolor_)
        self.labTroughcolor=tk.Label(self.master, text=getLang('troughcolor'), bg=self.theme[0], fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        self.varWidth=tk.StringVar()
        self.entrWidth=tk.Entry(self.master, bg=self.theme[2], fg=self.theme[1], border=0, highlightcolor=pf.COLORS['--dark-blue'],highlightthickness=0,
                               disabledbackground=self.theme[3], disabledforeground=self.theme[1], insertbackground=self.theme[1],
                               font=Font(family=pf.POLICE[0], size=12, weight='bold'), textvariable=self.varWidth, width=20)
        self.labWidth=tk.Label(self.master, text=getLang('width'), bg=self.theme[0], fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        self.varWrap=tk.StringVar()
        self.spnWrap=tk.Spinbox(self.master, bg=self.theme[2], fg=self.theme[1], border=0, highlightcolor=pf.COLORS['--dark-blue'],highlightthickness=0,
                               disabledbackground=self.theme[3], disabledforeground=self.theme[1], insertbackground=self.theme[1],
                               font=Font(family=pf.POLICE[0], size=11, weight='bold'), textvariable=self.varWrap, width=20, from_=0, to=math.inf,
                               buttonbackground=self.theme[3], buttoncursor='hand2', buttondownrelief=tk.FLAT, buttonuprelief=tk.FLAT,
                               command=lambda:setWraplength(self.obj, self.varWrap.get(), self.command))
        self.labWrap=tk.Label(self.master, text=getLang('wraplength'), bg=self.theme[0], fg=self.theme[1], bd=0, relief=tk.FLAT, highlightthickness=0, width=20)
        
        self.setList()
        self.setObjFunction()
        self.dico[self.obj.type]()
    
    def setList(self):
        self.entrAdd='entrAdd'
        self.listE.extend([self.cbAnchor, self.spnAspect, self.spnBd, self.cbBitmap, self.cbCursor, self.cbButtonCur,
                           self.cbButtonDRel, self.cbButtonURel, self.cbCompound, self.cbDirection, self.cbOffrelief,
                           self.cbFont, self.spnFrom, self.entrHeight, self.spnHighTn, self.entrImg, self.spnInsertBdWdt,
                           self.spnInsertWidth, self.cbJustify, self.entrLabel, self.cbLabelanchor, self.spnLength, self.cbOrient,
                           self.cbOverRel, self.cbRelief, self.spnSelectBdWdt, self.entrSelectImg, self.cbShow, self.entrAdd,
                           self.spnSliderlength, self.cbSliderRel, self.entrText, self.spnTo, self.entrWidth, self.spnWrap])
        
        self.listCB.extend([self.cbAnchor, self.cbBitmap, self.cbCursor, self.cbButtonCur,
                           self.cbButtonDRel, self.cbButtonURel, self.cbCompound, self.cbDirection, self.cbOffrelief,
                           self.cbFont, self.cbJustify, self.cbLabelanchor, self.cbOrient,
                           self.cbOverRel, self.cbRelief, self.cbShow, self.cbSliderRel])
    
    def setObjFunction(self):
        if not self.obj.type in ['entry', 'frame', 'labelframe', 'listbox', 'message', 'text', 'scrollableframe', 'spinbox']:
            self.varActiveBg.set(self.obj.activeBg)
            self.varActiveFg.set(self.obj.activeFg if self.obj.type!='scale' else '')
            self.bActiveBg['bg']=self.varActiveBg.get()
            self.bActiveFg['bg']=self.varActiveFg.get() if self.obj.type!='scale' else 'black'
        def toAnchor(event):
            a=self.varAnchor.get()
            setAnchor(self.obj, getLangKey(a), self.command)
        pf.Assign(self.cbAnchor, toAnchor, ['FocusOut', 'Return', '<ComboboxSelected>'])
        if not self.obj.type in ['entry', 'frame', 'labelframe', 'listbox', 'scale', 'text', 'scrollableframe', 'spinbox']:
            self.varAnchor.set(getLang(self.obj.anchor))
        def toAspect(event):
            setAspect(self.obj, self.varAspect.get(), self.command)
        pf.Assign(self.spnAspect, toAspect, ['Return', 'FocusOut'])
        if self.obj.type=='message':
            self.varAspect.set(self.obj.aspect)
        def toBd(event):
            setBd(self.obj, self.varBd.get(), self.command)
        pf.Assign(self.spnBd, toBd, ['Return', 'FocusOut'])
        self.varBd.set(self.obj.bd)
        self.varBg.set(self.obj.bg)
        self.bBg['bg']=self.varBg.get()
        def toBitmap(event):
            setBitmap(self.obj, self.varBitmap.get(), self.command)
        pf.Assign(self.cbBitmap, toBitmap, ['Return', 'FocusOut', '<ComboboxSelected>'])
        if self.obj.type in ['button', 'checkbutton', 'label', 'menubutton', 'radiobutton']:
            self.varBitmap.set(self.obj.bitmap)
        def toBCur(event):
            setButtonCur(self.obj, self.varButtonCur.get(), self.command)
        def toBDrel(event):
            a=self.varButtonDRel.get()
            setButtonDrel(self.obj, getLangKey(a), self.command)
        def toBUrel(event):
            a=self.varButtonURel.get()
            setButtonUrel(self.obj, getLangKey(a), self.command)
        pf.Assign(self.cbButtonCur, toBCur, ['Return', 'FocusOut', '<ComboboxSelected>'])
        pf.Assign(self.cbButtonDRel, toBDrel, ['Return', 'FocusOut', '<ComboboxSelected>'])
        pf.Assign(self.cbButtonURel, toBUrel, ['Return', 'FocusOut', '<ComboboxSelected>'])
        if self.obj.type=='spinbox':
            self.varButtonCur.set(self.obj.buttonCur)
            self.varButtonBg.set(self.obj.buttonBg)
            self.varButtonDRel.set(getLang(self.obj.buttonDrel))
            self.varButtonURel.set(getLang(self.obj.buttonUrel))
            self.bButtonBg['bg']=self.varButtonBg.get()
        def toCompoud(event):
            a=self.varCompound.get()
            a=getLangKey(a)
            if a=='':a='none'
            setCompound(self.obj,a, self.command)
        pf.Assign(self.cbCompound, toCompoud, ['Return', 'FocusOut', '<ComboboxSelected>'])
        if self.obj.type in ['button', 'checkbutton', 'label', 'menubutton', 'radiobutton']:
            self.varCompound.set(getLang(self.obj.compound))
        def toCursor(event):
            setCursor(self.obj, self.varCursor.get(), self.command)
        pf.Assign(self.cbCursor, toCursor, ['Return', 'FocusOut', '<ComboboxSelected>'])
        self.varCursor.set(self.obj.cursor)
        def toDirection(event):
            a=self.varDirection.get()
            setDirection(self.obj, getLangKey(a), self.command)
        pf.Assign(self.cbDirection, toDirection, ['Return', 'FocusOut', '<ComboboxSelected>'])
        if self.obj.type=='menubutton':
            self.varDirection.set(getLang(self.obj.direction))
        def toOffrelief(event):
            a=self.varOffrelief.get()
            setOffrelief(self.obj, getLangKey(a), self.command)
        pf.Assign(self.cbOffrelief, toOffrelief, ['Return', 'FocusOut', '<ComboboxSelected>'])
        if self.obj.type in ['radiobutton', 'checkbutton']:
            self.varOffrelief.set(getLang(self.obj.offrelief))
        def toFont(event):
            setFont(self.obj, self.varFont.get(), self.varWeight.get(), self.varSlant.get(), self.varUnderline.get(), self.varOverstrike.get(), self.command)
        pf.Assign(self.cbFont, toFont, ['Return', 'FocusOut', '<ComboboxSelected>'])
        if not self.obj.type in ['frame', 'scrollableframe']:
            self.varFont.set(self.obj.font)
            self.varSize.set(self.obj.size)
            self.varWeight.set(True if self.obj.weight=='bold' else False)
            self.varSlant.set(True if self.obj.slant=='italic' else False)
            self.varUnderline.set(self.obj.underline)
            self.varOverstrike.set(self.obj.overstrike)
            if self.obj.type=='listbox':
                self.varSize.set(self.obj.size_)
        def toSize(event):
            setSize(self.obj, self.varSize.get(), self.command)
        pf.Assign(self.spnSize, toSize, ['Return', 'FocusOut'])
        def toFrom(event):
            setFrom(self.obj, self.varFrom.get(), self.command)
        pf.Assign(self.spnFrom, toFrom, ['Return', 'FocusOut'])
        if self.obj.type in ['spinbox', 'scale']:
            self.varFrom.set(self.obj.from_)
        def toHeight(event):
            setHeight(self.obj, self.varHeight.get(), self.command)
        pf.Assign(self.entrHeight, toHeight, ['Return', 'FocusOut'])
        if not self.obj.type in ['entry', 'message', 'spinbox', 'scale']:
            self.varHeight.set(self.obj.height)
        def toHighTn(event):
            setHighTn(self.obj, self.varHighTn.get(), self.command)
        pf.Assign(self.spnHighTn, toHighTn, ['Return', 'FocusOut'])
        self.varHighBg.set(self.obj.highBg)
        self.varHighFg.set(self.obj.highFg)
        self.varHighTn.set(self.obj.highTn)
        self.bHighBg['bg']=self.varHighBg.get()
        self.bHighFg['bg']=self.varHighFg.get()
        def toImage(event):
            setImage(self.obj, self.varImg.get(), self.command)
        pf.Assign(self.entrImg, toImage, ['Return', 'FocusOut'])
        if self.obj.type in ['button', 'checkbutton', 'rabiobutton', 'label']:
            self.varImg.set(self.obj.image)
        if self.obj.type in ['checkbutton', 'radiobutton', 'menubutton']:
            self.varIndicatoron.set(self.obj.indicatoron)
        if self.obj.type in ['entry', 'text', 'spinbox']:
            self.varInsertBdWdt.set(self.obj.insertBdWidth)
            self.varInsertBg.set(self.obj.insertBg)
            self.varInsertWidth.set(self.obj.insertWidth)
        def toInsertBdWdt(event):
            setInsertBdWdt(self.obj, self.varInsertBdWdt.get(), self.command)
        def toInsertWdt(event):
            setInsertWdth(self.obj, self.varInsertWidth.get(), self.command)
        pf.Assign(self.spnInsertBdWdt, toInsertBdWdt, ['Return', 'FocusOut'])
        pf.Assign(self.spnInsertWidth, toInsertWdt, ['Return', 'FocusOut'])
        def toJustify(event):
            a=self.varJustify.get()
            setJustify(self.obj, getLangKey(a), self.command)
        pf.Assign(self.cbJustify, toJustify, ['Return', 'FocusOut', '<ComboboxSelected>'])
        if not self.obj.type in ['frame', 'labelframe', 'scale', 'text', 'scrollableframe']:
            self.varJustify.set(getLang(self.obj.justify))
        def toLabel(event):
            setLabel(self.obj, self.varLabel.get(), self.command)
        pf.Assign(self.entrLabel, toLabel, ['Return', 'FocusOut'])
        if self.obj.type in ['scale']:
            self.varLabel.set(self.obj.label)
        def toLabelanchor(event):
            a=self.varLabelanchor.get()
            setLabelanchor(self.obj, getLangKey(a), self.command)
        pf.Assign(self.cbLabelanchor, toLabelanchor, ['Return', 'FocusOut', '<ComboboxSelected>'])
        if self.obj.type=='labelframe':
            self.varLabelanchor.set(getLang(self.obj.labelanchor))
        def toLength(event):
            setLength(self.obj, self.varLength.get(), self.command)
        pf.Assign(self.spnLength, toLength, ['Return', 'FocusOut'])
        if self.obj.type=='scale':
            self.varLength.set(self.obj.length)
            self.varOrient.set(self.obj.orient)
        def toOrient(event):
            setOrient(self.obj, getLangKey(self.varOrient.get()), self.command)
        pf.Assign(self.cbOrient, toOrient, ['Return', 'FocusOut', '<ComboboxSelected>'])
        def toOverrelief(event):
            a=self.varOverRel.get()
            a=getLangKey(a)
            if a=='none':a=''
            setOverrelief(self.obj,a, self.command)
        pf.Assign(self.cbOverRel, toOverrelief, ['Return', 'FocusOut', '<ComboboxSelected>'])
        if self.obj.type in ['button', 'radiobutton', 'checkbutton']:
            self.varOverRel.set(getLang(self.obj.overrelief))
        def toPadx(event):
            setPadx(self.obj, self.varPadx.get(), self.command)
        def toPady(event):
            setPady(self.obj, self.varPady.get(), self.command)
        pf.Assign(self.spnPadx, toPadx, ['Return', 'FocusOut'])
        pf.Assign(self.spnPady, toPady, ['Return', 'FocusOut'])
        if self.obj.type in ['button', 'checkbutton', 'menubutton', 'radiobutton', 'label']:
            self.varPadx.set(self.obj.padx)
            self.varPady.set(self.obj.pady)
        def toRelief(event):
            a=self.varRelief.get()
            setRelief(self.obj, getLangKey(a), self.command)
        pf.Assign(self.cbRelief, toRelief, ['Return', 'FocusOut', '<ComboboxSelected>'])
        self.varRelief.set(getLang(self.obj.relief))
        def toSelectBdWdt(event):
            setSelectBdWdt(self.obj, self.varSelectBdWdt.get(), self.command)
        pf.Assign(self.spnSelectBdWdt, toSelectBdWdt, ['Return', 'FocusOut'])
        if self.obj.type in ['entry','text', 'spinbox', 'listbox']:
            self.varSelectBdWdt.set(self.obj.selectBdwidth)
            self.varSelectBg.set(self.obj.selectBg)
            self.varSelectFg.set(self.obj.selectFg)
            self.bSelectBg['bg']=self.varSelectBg.get()
            self.bSelectFg['bg']=self.varSelectFg.get()
        def toSelectImg(event):
            setSelectImg(self.obj, self.varSelectImg.get(), self.command)
        pf.Assign(self.entrSelectImg, toSelectImg, ['Return', 'FocusOut'])
        if self.obj.type in ['radiobutton', 'checkbutton']:
            self.varSelectImg,set(self.obj.selectimage)
        def toShow(event):
            setShow(self.obj, self.varShow.get(), self.command)
        pf.Assign(self.cbShow, toShow, ['Return', 'FocusOut', '<ComboboxSelected>'])
        if self.obj.type=='entry':
            self.varShow.set(self.obj.show)
        def toSliderL(event):
            setSliderlgt(self.obj, self.varSliderlength.get(), self.command)
        def toSliderR(event):
            a=self.varSliderRel.get()
            setSliderrel(self.obj, getLangKey(a), self.command)
        pf.Assign(self.spnSliderlength, toSliderL, ['Return', 'FocusOut'])
        pf.Assign(self.cbSliderRel, toSliderR, ['Return', 'FocusOut', '<ComboboxSelected>'])
        if self.obj.type=='scale':
            self.varSliderlength.set(self.obj.sliderlgt)
            self.varSliderRel.set(getLang(self.obj.sliderrelief))
        def toText(event):
            setText(self.obj, self.varText.get(), self.command)
        pf.Assign(self.entrText, toText, ['Return', 'FocusOut'])
        if self.obj.type in ['button', 'checkbutton', 'radiobutton', 'label', 'menubutton', 'message', 'labelframe']:
            self.varText.set(self.obj.text)
        def toTo(event):
            setTo(self.obj, self.varTo.get(), self.command)
        pf.Assign(self.spnTo, toTo, ['Return', 'FocusOut'])
        if self.obj.type in ['spinbox', 'scale']:
            self.varTo.set(self.obj.to)
        if self.obj.type=='scale':
            self.varTroughcolor.set(self.obj.troughcolor)
            self.bTroughcolor['bg']=self.varTroughcolor.get()
            self.varShowvalue.set(self.obj.showvalue)
            self.varOrient.set(getLang(self.obj.orient))
            print(self.varTroughcolor.get())
        def toWidth(event):
                setWidth(self.obj, self.varWidth.get(), self.command)
        pf.Assign(self.entrWidth, toWidth, ['Return', 'FocusOut'])
        self.varWidth.set(self.obj.width)
        def toWrap(event):
            setWraplength(self.obj, self.varWrap.get(), self.command)
        pf.Assign(self.spnWrap, toWrap, ['Return', 'FocusOut'])
        if self.obj.type in ['button', 'checkbutton', 'label', 'menubutton', 'radiobutton']:
            self.varWrap.set(self.obj.wraplength)
    
    def setButton(self):
        tk.Label(self.master, text=getLang(self.obj.type), bg=self.theme[0], fg=self.theme[1], 
                 font=Font(size=15, family='system', weight='bold', underline=True)).grid(row=0, column=1, columnspan=2, sticky='ew', pady=10)
        self.labText.grid(row=1, column=1)
        self.entrText._grid(row=1, column=2, sticky='w', padx=2, pady=2)
        self.labBg.grid(row=2, column=1)
        self.bBg.grid(row=2, column=2, sticky='w', padx=2, pady=2)
        self.labFg.grid(row=3, column=1)
        self.bFg.grid(row=3, column=2, sticky='w', padx=2, pady=2)
        self.labActiveBg.grid(row=4, column=1)
        self.bActiveBg.grid(row=4, column=2, sticky='w', padx=2, pady=2)
        self.labActiveFg.grid(row=5, column=1)
        self.bActiveFg.grid(row=5, column=2, sticky='w', padx=2, pady=2)
        self.labHighBg.grid(row=6, column=1)
        self.bHighBg.grid(row=6, column=2, sticky='w', padx=2, pady=2)
        self.labHighFg.grid(row=7, column=1)
        self.bHighFg.grid(row=7, column=2, sticky='w', padx=2, pady=2)
        self.labImg.grid(row=8, column=1)
        self.entrImg._grid(row=8, column=2, sticky='w', padx=2, pady=2)
        self.labBitmap.grid(row=9, column=1)
        self.cbBitmap.grid(row=9, column=2, sticky='w', padx=2, pady=2)
        self.labFont.grid(row=10, column=1)
        self.cbFont.grid(row=10, column=2, sticky='w', padx=2, pady=2)
        self.labSize.grid(row=11, column=1)
        self.spnSize.grid(row=11, column=2, sticky='w', padx=2, pady=2)
        self.chWeight.grid(row=12, column=1, sticky='w', padx=2, pady=2)
        self.chSlant.grid(row=12, column=2, sticky='w', padx=2, pady=2)
        self.chUnderline.grid(row=13, column=1, sticky='w', padx=2, pady=2)
        self.chOverstrike.grid(row=13, column=2, sticky='w', padx=2, pady=2)
        self.labJustify.grid(row=14, column=1)
        self.cbJustify.grid(row=14, column=2, sticky='w', padx=2, pady=2)
        self.labRelief.grid(row=15, column=1)
        self.cbRelief.grid(row=15, column=2, sticky='w', padx=2, pady=2)
        self.labOverRel.grid(row=16, column=1)
        self.cbOverRel.grid(row=16, column=2, sticky='w', padx=2, pady=2)
        self.labBd.grid(row=17, column=1)
        self.spnBd.grid(row=17, column=2, sticky='w', padx=2, pady=2)
        self.labHighTn.grid(row=18, column=1)
        self.spnHighTn.grid(row=18, column=2, sticky='w', padx=2, pady=2)
        self.labPadx.grid(row=19, column=1)
        self.spnPadx.grid(row=19, column=2, sticky='w', padx=2, pady=2)
        self.labPady.grid(row=20, column=1)
        self.spnPady.grid(row=20, column=2, sticky='w', padx=2, pady=2)
        self.labAnchor.grid(row=21, column=1)
        self.cbAnchor.grid(row=21, column=2, sticky='w', padx=2, pady=2)
        self.labCursor.grid(row=22, column=1)
        self.cbCursor.grid(row=22, column=2, sticky='w', padx=2, pady=2)
        self.labCompound.grid(row=23, column=1)
        self.cbCompound.grid(row=23, column=2, sticky='w', padx=2, pady=2)
        self.labWidth.grid(row=24, column=1)
        self.entrWidth.grid(row=24, column=2, sticky='w', padx=2, pady=2)
        self.labHeight.grid(row=25, column=1)
        self.entrHeight.grid(row=25, column=2, sticky='w', padx=2, pady=2)
        self.labWrap.grid(row=26, column=1)
        self.spnWrap.grid(row=26, column=2, sticky='w', padx=2, pady=2)

    def setCheckbutton(self):
        tk.Label(self.master, text=getLang(self.obj.type), bg=self.theme[0], fg=self.theme[1], 
                 font=Font(size=15, family='system', weight='bold', underline=True)).grid(row=0, column=1, columnspan=2, sticky='ew', pady=10)
        self.labText.grid(row=1, column=1)
        self.entrText._grid(row=1, column=2, sticky='w', padx=2, pady=2)
        self.labBg.grid(row=2, column=1)
        self.bBg.grid(row=2, column=2, sticky='w', padx=2, pady=2)
        self.labFg.grid(row=3, column=1)
        self.bFg.grid(row=3, column=2, sticky='w', padx=2, pady=2)
        self.labActiveBg.grid(row=4, column=1)
        self.bActiveBg.grid(row=4, column=2, sticky='w', padx=2, pady=2)
        self.labActiveFg.grid(row=5, column=1)
        self.bActiveFg.grid(row=5, column=2, sticky='w', padx=2, pady=2)
        self.labHighBg.grid(row=6, column=1)
        self.bHighBg.grid(row=6, column=2, sticky='w', padx=2, pady=2)
        self.labHighFg.grid(row=7, column=1)
        self.bHighFg.grid(row=7, column=2, sticky='w', padx=2, pady=2)
        self.labImg.grid(row=8, column=1)
        self.entrImg._grid(row=8, column=2, sticky='w', padx=2, pady=2)
        self.labBitmap.grid(row=9, column=1)
        self.cbBitmap.grid(row=9, column=2, sticky='w', padx=2, pady=2)
        self.labFont.grid(row=10, column=1)
        self.cbFont.grid(row=10, column=2, sticky='w', padx=2, pady=2)
        self.labSize.grid(row=11, column=1)
        self.spnSize.grid(row=11, column=2, sticky='w', padx=2, pady=2)
        self.chWeight.grid(row=12, column=1, sticky='w', padx=2, pady=2)
        self.chSlant.grid(row=12, column=2, sticky='w', padx=2, pady=2)
        self.chUnderline.grid(row=13, column=1, sticky='w', padx=2, pady=2)
        self.chOverstrike.grid(row=13, column=2, sticky='w', padx=2, pady=2)
        self.labJustify.grid(row=14, column=1)
        self.cbJustify.grid(row=14, column=2, sticky='w', padx=2, pady=2)
        self.labRelief.grid(row=15, column=1)
        self.cbRelief.grid(row=15, column=2, sticky='w', padx=2, pady=2)
        self.labOffrelief.grid(row=16, column=1)
        self.cbOffrelief.grid(row=16, column=2, sticky='w', padx=2, pady=2)
        self.labOverRel.grid(row=17, column=1)
        self.cbOverRel.grid(row=17, column=2, sticky='w', padx=2, pady=2)
        self.labBd.grid(row=18, column=1)
        self.spnBd.grid(row=18, column=2, sticky='w', padx=2, pady=2)
        self.labHighTn.grid(row=19, column=1)
        self.spnHighTn.grid(row=19, column=2, sticky='w', padx=2, pady=2)
        self.labPadx.grid(row=20, column=1)
        self.spnPadx.grid(row=20, column=2, sticky='w', padx=2, pady=2)
        self.labPady.grid(row=21, column=1)
        self.spnPady.grid(row=21, column=2, sticky='w', padx=2, pady=2)
        self.labAnchor.grid(row=22, column=1)
        self.cbAnchor.grid(row=22, column=2, sticky='w', padx=2, pady=2)
        self.labCursor.grid(row=23, column=1)
        self.cbCursor.grid(row=23, column=2, sticky='w', padx=2, pady=2)
        self.labCompound.grid(row=24, column=1)
        self.cbCompound.grid(row=24, column=2, sticky='w', padx=2, pady=2)
        self.labWidth.grid(row=25, column=1)
        self.entrWidth.grid(row=25, column=2, sticky='w', padx=2, pady=2)
        self.labHeight.grid(row=26, column=1)
        self.entrHeight.grid(row=26, column=2, sticky='w', padx=2, pady=2)
        self.labWrap.grid(row=27, column=1)
        self.spnWrap.grid(row=27, column=2, sticky='w', padx=2, pady=2)
        self.chIndicatoron.grid(row=28, column=1, sticky='w', padx=2, pady=2)

    def setEntry(self):
        tk.Label(self.master, text=getLang(self.obj.type), bg=self.theme[0], fg=self.theme[1], 
                 font=Font(size=15, family='system', weight='bold', underline=True)).grid(row=0, column=1, columnspan=2, sticky='ew', pady=10)
        self.labBg.grid(row=2, column=1)
        self.bBg.grid(row=2, column=2, sticky='w', padx=2, pady=2)
        self.labFg.grid(row=3, column=1)
        self.bFg.grid(row=3, column=2, sticky='w', padx=2, pady=2)
        self.labHighBg.grid(row=4, column=1)
        self.bHighBg.grid(row=4, column=2, sticky='w', padx=2, pady=2)
        self.labSelectBg.grid(row=5, column=1)
        self.bSelectBg.grid(row=5, column=2, sticky='w', padx=2, pady=2)
        self.labHighFg.grid(row=6, column=1)
        self.bHighFg.grid(row=6, column=2, sticky='w', padx=2, pady=2)
        self.labSelectFg.grid(row=7, column=1)
        self.bSelectFg.grid(row=7, column=2, sticky='w', padx=2, pady=2)
        self.labInsertBg.grid(row=8, column=1)
        self.bInsertBg.grid(row=8, column=2, sticky='w', padx=2, pady=2)
        self.labFont.grid(row=9, column=1)
        self.cbFont.grid(row=9, column=2, sticky='w', padx=2, pady=2)
        self.labSize.grid(row=10, column=1)
        self.spnSize.grid(row=10, column=2, sticky='w', padx=2, pady=2)
        self.chWeight.grid(row=11, column=1, sticky='w', padx=2, pady=2)
        self.chSlant.grid(row=11, column=2, sticky='w', padx=2, pady=2)
        self.chUnderline.grid(row=12, column=1, sticky='w', padx=2, pady=2)
        self.chOverstrike.grid(row=12, column=2, sticky='w', padx=2, pady=2)
        self.labJustify.grid(row=13, column=1)
        self.cbJustify.grid(row=13, column=2, sticky='w', padx=2, pady=2)
        self.labRelief.grid(row=14, column=1)
        self.cbRelief.grid(row=14, column=2, sticky='w', padx=2, pady=2)
        self.labBd.grid(row=15, column=1)
        self.spnBd.grid(row=15, column=2, sticky='w', padx=2, pady=2)
        self.labHighTn.grid(row=16, column=1)
        self.spnHighTn.grid(row=16, column=2, sticky='w', padx=2, pady=2)
        self.labCursor.grid(row=17, column=1)
        self.cbCursor.grid(row=17, column=2, sticky='w', padx=2, pady=2)
        self.labWidth.grid(row=18, column=1)
        self.entrWidth.grid(row=18, column=2, sticky='w', padx=2, pady=2)
        self.labSelectBdWt.grid(row=19, column=1)
        self.spnSelectBdWdt.grid(row=19, column=2, sticky='w', padx=2, pady=2)
        self.labInsertWith.grid(row=20, column=1)
        self.spnInsertWidth.grid(row=20, column=2, sticky='w', padx=2, pady=2)
        self.labInsertBdWt.grid(row=21, column=1)
        self.spnInsertBdWdt.grid(row=21, column=2, sticky='w', padx=2, pady=2)
        self.labShow.grid(row=22, column=1)
        self.cbShow.grid(row=22, column=2, sticky='w', padx=2, pady=2)

    def setFrame(self):
        tk.Label(self.master, text=getLang(self.obj.type), bg=self.theme[0], fg=self.theme[1], 
                 font=Font(size=15, family='system', weight='bold', underline=True)).grid(row=0, column=1, columnspan=2, sticky='ew', pady=10)
        self.labBg.grid(row=2, column=1)
        self.bBg.grid(row=2, column=2, sticky='w', padx=2, pady=2)
        self.labHighBg.grid(row=3, column=1)
        self.bHighBg.grid(row=3, column=2, sticky='w', padx=2, pady=2)
        self.labHighFg.grid(row=4, column=1)
        self.bHighFg.grid(row=4, column=2, sticky='w', padx=2, pady=2)
        self.labRelief.grid(row=5, column=1)
        self.cbRelief.grid(row=5, column=2, sticky='w', padx=2, pady=2)
        self.labBd.grid(row=6, column=1)
        self.spnBd.grid(row=6, column=2, sticky='w', padx=2, pady=2)
        self.labHighTn.grid(row=7, column=1)
        self.spnHighTn.grid(row=7, column=2, sticky='w', padx=2, pady=2)
        self.labCursor.grid(row=8, column=1)
        self.cbCursor.grid(row=8, column=2, sticky='w', padx=2, pady=2)
        self.labWidth.grid(row=9, column=1)
        self.entrWidth.grid(row=9, column=2, sticky='w', padx=2, pady=2)
        self.labHeight.grid(row=10, column=1)
        self.entrHeight.grid(row=10, column=2, sticky='w', padx=2, pady=2)
    
    def setLabel(self):
        tk.Label(self.master, text=getLang(self.obj.type), bg=self.theme[0], fg=self.theme[1], 
                 font=Font(size=15, family='system', weight='bold', underline=True)).grid(row=0, column=1, columnspan=2, sticky='ew', pady=10)
        self.labText.grid(row=1, column=1)
        self.entrText._grid(row=1, column=2, sticky='w', padx=2, pady=2)
        self.labBg.grid(row=2, column=1)
        self.bBg.grid(row=2, column=2, sticky='w', padx=2, pady=2)
        self.labFg.grid(row=3, column=1)
        self.bFg.grid(row=3, column=2, sticky='w', padx=2, pady=2)
        self.labActiveBg.grid(row=4, column=1)
        self.bActiveBg.grid(row=4, column=2, sticky='w', padx=2, pady=2)
        self.labActiveFg.grid(row=5, column=1)
        self.bActiveFg.grid(row=5, column=2, sticky='w', padx=2, pady=2)
        self.labHighBg.grid(row=6, column=1)
        self.bHighBg.grid(row=6, column=2, sticky='w', padx=2, pady=2)
        self.labHighFg.grid(row=7, column=1)
        self.bHighFg.grid(row=7, column=2, sticky='w', padx=2, pady=2)
        self.labImg.grid(row=8, column=1)
        self.entrImg._grid(row=8, column=2, sticky='w', padx=2, pady=2)
        self.labBitmap.grid(row=9, column=1)
        self.cbBitmap.grid(row=9, column=2, sticky='w', padx=2, pady=2)
        self.labFont.grid(row=10, column=1)
        self.cbFont.grid(row=10, column=2, sticky='w', padx=2, pady=2)
        self.labSize.grid(row=11, column=1)
        self.spnSize.grid(row=11, column=2, sticky='w', padx=2, pady=2)
        self.chWeight.grid(row=12, column=1, sticky='w', padx=2, pady=2)
        self.chSlant.grid(row=12, column=2, sticky='w', padx=2, pady=2)
        self.chUnderline.grid(row=13, column=1, sticky='w', padx=2, pady=2)
        self.chOverstrike.grid(row=13, column=2, sticky='w', padx=2, pady=2)
        self.labJustify.grid(row=14, column=1)
        self.cbJustify.grid(row=14, column=2, sticky='w', padx=2, pady=2)
        self.labRelief.grid(row=15, column=1)
        self.cbRelief.grid(row=15, column=2, sticky='w', padx=2, pady=2)
        self.labBd.grid(row=16, column=1)
        self.spnBd.grid(row=16, column=2, sticky='w', padx=2, pady=2)
        self.labHighTn.grid(row=17, column=1)
        self.spnHighTn.grid(row=17, column=2, sticky='w', padx=2, pady=2)
        self.labPadx.grid(row=18, column=1)
        self.spnPadx.grid(row=18, column=2, sticky='w', padx=2, pady=2)
        self.labPady.grid(row=19, column=1)
        self.spnPady.grid(row=19, column=2, sticky='w', padx=2, pady=2)
        self.labAnchor.grid(row=20, column=1)
        self.cbAnchor.grid(row=20, column=2, sticky='w', padx=2, pady=2)
        self.labCursor.grid(row=21, column=1)
        self.cbCursor.grid(row=21, column=2, sticky='w', padx=2, pady=2)
        self.labCompound.grid(row=22, column=1)
        self.cbCompound.grid(row=22, column=2, sticky='w', padx=2, pady=2)
        self.labWidth.grid(row=23, column=1)
        self.entrWidth.grid(row=23, column=2, sticky='w', padx=2, pady=2)
        self.labHeight.grid(row=24, column=1)
        self.entrHeight.grid(row=24, column=2, sticky='w', padx=2, pady=2)
        self.labWrap.grid(row=25, column=1)
        self.spnWrap.grid(row=25, column=2, sticky='w', padx=2, pady=2)
      
    def setLabelFrame(self):
        tk.Label(self.master, text=getLang(self.obj.type), bg=self.theme[0], fg=self.theme[1], 
                 font=Font(size=15, family='system', weight='bold', underline=True)).grid(row=0, column=1, columnspan=2, sticky='ew', pady=10)
        self.labText.grid(row=1, column=1)
        self.entrText._grid(row=1, column=2, sticky='w', padx=2, pady=2)
        self.labBg.grid(row=2, column=1)
        self.bBg.grid(row=2, column=2, sticky='w', padx=2, pady=2)
        self.labFg.grid(row=3, column=1)
        self.bFg.grid(row=3, column=2, sticky='w', padx=2, pady=2)
        self.labHighBg.grid(row=4, column=1)
        self.bHighBg.grid(row=4, column=2, sticky='w', padx=2, pady=2)
        self.labHighFg.grid(row=5, column=1)
        self.bHighFg.grid(row=5, column=2, sticky='w', padx=2, pady=2)
        self.labFont.grid(row=6, column=1)
        self.cbFont.grid(row=6, column=2, sticky='w', padx=2, pady=2)
        self.labSize.grid(row=7, column=1)
        self.spnSize.grid(row=7, column=2, sticky='w', padx=2, pady=2)
        self.chWeight.grid(row=8, column=1, sticky='w', padx=2, pady=2)
        self.chSlant.grid(row=8, column=2, sticky='w', padx=2, pady=2)
        self.chUnderline.grid(row=9, column=1, sticky='w', padx=2, pady=2)
        self.chOverstrike.grid(row=9, column=2, sticky='w', padx=2, pady=2)
        self.labJustify.grid(row=10, column=1)
        self.cbJustify.grid(row=10, column=2, sticky='w', padx=2, pady=2)
        self.labRelief.grid(row=11, column=1)
        self.cbRelief.grid(row=11, column=2, sticky='w', padx=2, pady=2)
        self.labBd.grid(row=12, column=1)
        self.spnBd.grid(row=12, column=2, sticky='w', padx=2, pady=2)
        self.labHighTn.grid(row=13, column=1)
        self.spnHighTn.grid(row=13, column=2, sticky='w', padx=2, pady=2)
        self.labPadx.grid(row=14, column=1)
        self.spnPadx.grid(row=14, column=2, sticky='w', padx=2, pady=2)
        self.labPady.grid(row=15, column=1)
        self.spnPady.grid(row=15, column=2, sticky='w', padx=2, pady=2)
        self.labLabelanchor.grid(row=16, column=1)
        self.cbLabelanchor.grid(row=16, column=2, sticky='w', padx=2, pady=2)
        self.labCursor.grid(row=17, column=1)
        self.cbCursor.grid(row=17, column=2, sticky='w', padx=2, pady=2)
        self.labWidth.grid(row=18, column=1)
        self.entrWidth.grid(row=18, column=2, sticky='w', padx=2, pady=2)
        self.labHeight.grid(row=19, column=1)
        self.entrHeight.grid(row=19, column=2, sticky='w', padx=2, pady=2)
        
    def setListbox(self):
        tk.Label(self.master, text=getLang(self.obj.type), bg=self.theme[0], fg=self.theme[1], 
                 font=Font(size=15, family='system', weight='bold', underline=True)).grid(row=0, column=1, columnspan=2, sticky='ew', pady=10)
        self.labBg.grid(row=2, column=1)
        self.bBg.grid(row=2, column=2, sticky='w', padx=2, pady=2)
        self.labFg.grid(row=3, column=1)
        self.bFg.grid(row=3, column=2, sticky='w', padx=2, pady=2)
        self.labHighBg.grid(row=4, column=1)
        self.bHighBg.grid(row=4, column=2, sticky='w', padx=2, pady=2)
        self.labHighFg.grid(row=5, column=1)
        self.bHighFg.grid(row=5, column=2, sticky='w', padx=2, pady=2)
        self.labSelectBg.grid(row=6, column=1)
        self.bSelectBg.grid(row=6, column=2, sticky='w', padx=2, pady=2)
        self.labHighFg.grid(row=7, column=1)
        self.bHighFg.grid(row=7, column=2, sticky='w', padx=2, pady=2)
        self.labFont.grid(row=8, column=1)
        self.cbFont.grid(row=8, column=2, sticky='w', padx=2, pady=2)
        self.labSize.grid(row=9, column=1)
        self.spnSize.grid(row=9, column=2, sticky='w', padx=2, pady=2)
        self.chWeight.grid(row=10, column=1, sticky='w', padx=2, pady=2)
        self.chSlant.grid(row=10, column=2, sticky='w', padx=2, pady=2)
        self.chUnderline.grid(row=11, column=1, sticky='w', padx=2, pady=2)
        self.chOverstrike.grid(row=11, column=2, sticky='w', padx=2, pady=2)
        self.labJustify.grid(row=12, column=1)
        self.cbJustify.grid(row=12, column=2, sticky='w', padx=2, pady=2)
        self.labRelief.grid(row=13, column=1)
        self.cbRelief.grid(row=13, column=2, sticky='w', padx=2, pady=2)
        self.labBd.grid(row=14, column=1)
        self.spnBd.grid(row=14, column=2, sticky='w', padx=2, pady=2)
        self.labHighTn.grid(row=15, column=1)
        self.spnHighTn.grid(row=15, column=2, sticky='w', padx=2, pady=2)
        self.labCursor.grid(row=16, column=1)
        self.cbCursor.grid(row=16, column=2, sticky='w', padx=2, pady=2)
        self.labWidth.grid(row=17, column=1)
        self.entrWidth.grid(row=17, column=2, sticky='w', padx=2, pady=2)
        self.labHeight.grid(row=18, column=1)
        self.entrHeight.grid(row=18, column=2, sticky='w', padx=2, pady=2)
        self.labSelectBdWt.grid(row=19, column=1)
        self.spnSelectBdWdt.grid(row=19, column=2, sticky='w', padx=2, pady=2)
        self.varInsertValue=tk.StringVar()
        entr=wd.Entrytk(self.master, bg=self.theme[2], fg=self.theme[1], border=0, highlightcolor=pf.COLORS['--dark-blue'],highlightthickness=0,
                               disabledbackground=self.theme[3], disabledforeground=self.theme[1], insertbackground=self.theme[1],
                               font=Font(family=pf.POLICE[0], size=10, weight='normal'), width=15, textvariable=self.varInsertValue)
        entr.add_button(text=chr(937), relief=tk.FLAT, bd=0, highlightthickness=0,font=Font(family=pf.POLICE[0], size=10, weight='bold'),
                                bg=self.theme[2], activebackground=self.theme[3], cursor='hand2', command=lambda:sb.Container(self.master, entr, self.theme))
        def t(event=None):
            if len(entr.get().strip())>0:
                self.obj.insert(tk.END, entr.get())
            self.varInsertValue.set('')
                
        entr.add_button(text=chr(59152), relief=tk.FLAT, bd=0, highlightthickness=0,font=Font(family=pf.POLICE[0], size=10, weight='bold'),
                                bg=self.theme[2], activebackground=self.theme[3], cursor='hand2', command=t)
        pf.Assign(entr, t, ['Return', 'FocusOut'])
        entr.frame.config(bg=self.theme[0], bd=0, relief=tk.FLAT, highlightthickness=0)
        entr._grid(row=29, column=2,sticky='w', padx=2, pady=2)
        self.listE[self.listE.index(self.entrAdd)]=entr
      
    def setMessage(self):
        tk.Label(self.master, text=getLang(self.obj.type), bg=self.theme[0], fg=self.theme[1], 
                 font=Font(size=15, family='system', weight='bold', underline=True)).grid(row=0, column=1, columnspan=2, sticky='ew', pady=10)
        self.labText.grid(row=1, column=1)
        self.entrText._grid(row=1, column=2, sticky='w', padx=2, pady=2)
        self.labBg.grid(row=2, column=1)
        self.bBg.grid(row=2, column=2, sticky='w', padx=2, pady=2)
        self.labFg.grid(row=3, column=1)
        self.bFg.grid(row=3, column=2, sticky='w', padx=2, pady=2)
        self.labHighBg.grid(row=4, column=1)
        self.bHighBg.grid(row=4, column=2, sticky='w', padx=2, pady=2)
        self.labHighFg.grid(row=5, column=1)
        self.bHighFg.grid(row=5, column=2, sticky='w', padx=2, pady=2)
        self.labFont.grid(row=6, column=1)
        self.cbFont.grid(row=6, column=2, sticky='w', padx=2, pady=2)
        self.labSize.grid(row=7, column=1)
        self.spnSize.grid(row=7, column=2, sticky='w', padx=2, pady=2)
        self.chWeight.grid(row=8, column=1, sticky='w', padx=2, pady=2)
        self.chSlant.grid(row=8, column=2, sticky='w', padx=2, pady=2)
        self.chUnderline.grid(row=9, column=1, sticky='w', padx=2, pady=2)
        self.chOverstrike.grid(row=9, column=2, sticky='w', padx=2, pady=2)
        self.labRelief.grid(row=10, column=1)
        self.cbRelief.grid(row=10, column=2, sticky='w', padx=2, pady=2)
        self.labBd.grid(row=11, column=1)
        self.spnBd.grid(row=11, column=2, sticky='w', padx=2, pady=2)
        self.labHighTn.grid(row=12, column=1)
        self.spnHighTn.grid(row=12, column=2, sticky='w', padx=2, pady=2)
        self.labPadx.grid(row=13, column=1)
        self.spnPadx.grid(row=13, column=2, sticky='w', padx=2, pady=2)
        self.labPady.grid(row=14, column=1)
        self.spnPady.grid(row=14, column=2, sticky='w', padx=2, pady=2)
        self.labAnchor.grid(row=15, column=1)
        self.cbAnchor.grid(row=15, column=2, sticky='w', padx=2, pady=2)
        self.labCursor.grid(row=16, column=1)
        self.cbCursor.grid(row=16, column=2, sticky='w', padx=2, pady=2)
        self.labWidth.grid(row=17, column=1)
        self.entrWidth.grid(row=17, column=2, sticky='w', padx=2, pady=2)
        self.labAspect.grid(row=18, column=1)
        self.spnAspect.grid(row=18, column=2, sticky='w', padx=2, pady=2)
      
    def setMenubutton(self):
        tk.Label(self.master, text=getLang(self.obj.type), bg=self.theme[0], fg=self.theme[1], 
                 font=Font(size=15, family='system', weight='bold', underline=True)).grid(row=0, column=1, columnspan=2, sticky='ew', pady=10)
        self.labText.grid(row=1, column=1)
        self.entrText._grid(row=1, column=2, sticky='w', padx=2, pady=2)
        self.labBg.grid(row=2, column=1)
        self.bBg.grid(row=2, column=2, sticky='w', padx=2, pady=2)
        self.labFg.grid(row=3, column=1)
        self.bFg.grid(row=3, column=2, sticky='w', padx=2, pady=2)
        self.labActiveBg.grid(row=4, column=1)
        self.bActiveBg.grid(row=4, column=2, sticky='w', padx=2, pady=2)
        self.labActiveFg.grid(row=5, column=1)
        self.bActiveFg.grid(row=5, column=2, sticky='w', padx=2, pady=2)
        self.labHighBg.grid(row=6, column=1)
        self.bHighBg.grid(row=6, column=2, sticky='w', padx=2, pady=2)
        self.labHighFg.grid(row=7, column=1)
        self.bHighFg.grid(row=7, column=2, sticky='w', padx=2, pady=2)
        self.labImg.grid(row=8, column=1)
        self.entrImg._grid(row=8, column=2, sticky='w', padx=2, pady=2)
        self.labBitmap.grid(row=9, column=1)
        self.cbBitmap.grid(row=9, column=2, sticky='w', padx=2, pady=2)
        self.labFont.grid(row=10, column=1)
        self.cbFont.grid(row=10, column=2, sticky='w', padx=2, pady=2)
        self.labSize.grid(row=11, column=1)
        self.spnSize.grid(row=11, column=2, sticky='w', padx=2, pady=2)
        self.chWeight.grid(row=12, column=1, sticky='w', padx=2, pady=2)
        self.chSlant.grid(row=12, column=2, sticky='w', padx=2, pady=2)
        self.chUnderline.grid(row=13, column=1, sticky='w', padx=2, pady=2)
        self.chOverstrike.grid(row=13, column=2, sticky='w', padx=2, pady=2)
        self.labJustify.grid(row=14, column=1)
        self.cbJustify.grid(row=14, column=2, sticky='w', padx=2, pady=2)
        self.labRelief.grid(row=15, column=1)
        self.cbRelief.grid(row=15, column=2, sticky='w', padx=2, pady=2)
        self.labBd.grid(row=16, column=1)
        self.spnBd.grid(row=16, column=2, sticky='w', padx=2, pady=2)
        self.labHighTn.grid(row=17, column=1)
        self.spnHighTn.grid(row=17, column=2, sticky='w', padx=2, pady=2)
        self.labPadx.grid(row=18, column=1)
        self.spnPadx.grid(row=18, column=2, sticky='w', padx=2, pady=2)
        self.labPady.grid(row=19, column=1)
        self.spnPady.grid(row=19, column=2, sticky='w', padx=2, pady=2)
        self.labAnchor.grid(row=20, column=1)
        self.cbAnchor.grid(row=20, column=2, sticky='w', padx=2, pady=2)
        self.labCursor.grid(row=21, column=1)
        self.cbCursor.grid(row=21, column=2, sticky='w', padx=2, pady=2)
        self.labCompound.grid(row=22, column=1)
        self.cbCompound.grid(row=22, column=2, sticky='w', padx=2, pady=2)
        self.labWidth.grid(row=23, column=1)
        self.entrWidth.grid(row=23, column=2, sticky='w', padx=2, pady=2)
        self.labHeight.grid(row=24, column=1)
        self.entrHeight.grid(row=24, column=2, sticky='w', padx=2, pady=2)
        self.labWrap.grid(row=25, column=1)
        self.spnWrap.grid(row=25, column=2, sticky='w', padx=2, pady=2)
        self.labDirection.grid(row=26, column=1)
        self.cbDirection.grid(row=26, column=2, sticky='w', padx=2, pady=2)
        self.chIndicatoron.grid(row=27, column=1, sticky='w', padx=2, pady=2)
        
    def setRadiobutton(self):
        tk.Label(self.master, text=getLang(self.obj.type), bg=self.theme[0], fg=self.theme[1], 
                 font=Font(size=15, family='system', weight='bold', underline=True)).grid(row=0, column=1, columnspan=2, sticky='ew', pady=10)
        self.labText.grid(row=1, column=1)
        self.entrText._grid(row=1, column=2, sticky='w', padx=2, pady=2)
        self.labBg.grid(row=2, column=1)
        self.bBg.grid(row=2, column=2, sticky='w', padx=2, pady=2)
        self.labFg.grid(row=3, column=1)
        self.bFg.grid(row=3, column=2, sticky='w', padx=2, pady=2)
        self.labActiveBg.grid(row=4, column=1)
        self.bActiveBg.grid(row=4, column=2, sticky='w', padx=2, pady=2)
        self.labActiveFg.grid(row=5, column=1)
        self.bActiveFg.grid(row=5, column=2, sticky='w', padx=2, pady=2)
        self.labHighBg.grid(row=6, column=1)
        self.bHighBg.grid(row=6, column=2, sticky='w', padx=2, pady=2)
        self.labHighFg.grid(row=7, column=1)
        self.bHighFg.grid(row=7, column=2, sticky='w', padx=2, pady=2)
        self.labImg.grid(row=8, column=1)
        self.entrImg._grid(row=8, column=2, sticky='w', padx=2, pady=2)
        self.labBitmap.grid(row=9, column=1)
        self.cbBitmap.grid(row=9, column=2, sticky='w', padx=2, pady=2)
        self.labFont.grid(row=10, column=1)
        self.cbFont.grid(row=10, column=2, sticky='w', padx=2, pady=2)
        self.labSize.grid(row=11, column=1)
        self.spnSize.grid(row=11, column=2, sticky='w', padx=2, pady=2)
        self.chWeight.grid(row=12, column=1, sticky='w', padx=2, pady=2)
        self.chSlant.grid(row=12, column=2, sticky='w', padx=2, pady=2)
        self.chUnderline.grid(row=13, column=1, sticky='w', padx=2, pady=2)
        self.chOverstrike.grid(row=13, column=2, sticky='w', padx=2, pady=2)
        self.labJustify.grid(row=14, column=1)
        self.cbJustify.grid(row=14, column=2, sticky='w', padx=2, pady=2)
        self.labRelief.grid(row=15, column=1)
        self.cbRelief.grid(row=15, column=2, sticky='w', padx=2, pady=2)
        self.labOffrelief.grid(row=16, column=1)
        self.cbOffrelief.grid(row=16, column=2, sticky='w', padx=2, pady=2)
        self.labOverRel.grid(row=17, column=1)
        self.cbOverRel.grid(row=17, column=2, sticky='w', padx=2, pady=2)
        self.labBd.grid(row=18, column=1)
        self.spnBd.grid(row=18, column=2, sticky='w', padx=2, pady=2)
        self.labHighTn.grid(row=19, column=1)
        self.spnHighTn.grid(row=19, column=2, sticky='w', padx=2, pady=2)
        self.labPadx.grid(row=20, column=1)
        self.spnPadx.grid(row=20, column=2, sticky='w', padx=2, pady=2)
        self.labPady.grid(row=21, column=1)
        self.spnPady.grid(row=21, column=2, sticky='w', padx=2, pady=2)
        self.labAnchor.grid(row=22, column=1)
        self.cbAnchor.grid(row=22, column=2, sticky='w', padx=2, pady=2)
        self.labCursor.grid(row=23, column=1)
        self.cbCursor.grid(row=23, column=2, sticky='w', padx=2, pady=2)
        self.labCompound.grid(row=24, column=1)
        self.cbCompound.grid(row=24, column=2, sticky='w', padx=2, pady=2)
        self.labWidth.grid(row=25, column=1)
        self.entrWidth.grid(row=25, column=2, sticky='w', padx=2, pady=2)
        self.labHeight.grid(row=26, column=1)
        self.entrHeight.grid(row=26, column=2, sticky='w', padx=2, pady=2)
        self.labWrap.grid(row=27, column=1)
        self.spnWrap.grid(row=27, column=2, sticky='w', padx=2, pady=2)
        self.chIndicatoron.grid(row=28, column=1, sticky='w', padx=2, pady=2)
        tk.Checkbutton(self.master, width=15, relief=tk.FLAT, bd=0, highlightthickness=0, bg=self.theme[0], fg=self.theme[1], cursor='hand2',
                        borderwidth=0, text=getLang('select'), activebackground=self.theme[0],anchor='w',justify='center',
                         highlightbackground=self.theme[0], activeforeground=self.theme[1], selectcolor=self.theme[0],
                         variable=self.obj.varSelect).grid(row=29, column=1, sticky='w', padx=2, pady=2)

    def setScale(self):
        tk.Label(self.master, text=getLang(self.obj.type), bg=self.theme[0], fg=self.theme[1], 
                 font=Font(size=15, family='system', weight='bold', underline=True)).grid(row=0, column=1, columnspan=2, sticky='ew', pady=10)
        self.labLabel.grid(row=1, column=1)
        self.entrLabel._grid(row=1, column=2, sticky='w', padx=2, pady=2)
        self.labBg.grid(row=2, column=1)
        self.bBg.grid(row=2, column=2, sticky='w', padx=2, pady=2)
        self.labFg.grid(row=3, column=1)
        self.bFg.grid(row=3, column=2, sticky='w', padx=2, pady=2)
        self.labTroughcolor.grid(row=4, column=1)
        self.bTroughcolor.grid(row=4, column=2, sticky='w', padx=2, pady=2)
        self.labActiveBg.grid(row=5, column=1)
        self.bActiveBg.grid(row=5, column=2, sticky='w', padx=2, pady=2)
        self.labHighBg.grid(row=6, column=1)
        self.bHighBg.grid(row=6, column=2, sticky='w', padx=2, pady=2)
        self.labHighFg.grid(row=7, column=1)
        self.bHighFg.grid(row=7, column=2, sticky='w', padx=2, pady=2)
        self.labFont.grid(row=8, column=1)
        self.cbFont.grid(row=8, column=2, sticky='w', padx=2, pady=2)
        self.labSize.grid(row=9, column=1)
        self.spnSize.grid(row=9, column=2, sticky='w', padx=2, pady=2)
        self.chWeight.grid(row=10, column=1, sticky='w', padx=2, pady=2)
        self.chSlant.grid(row=10, column=2, sticky='w', padx=2, pady=2)
        self.chUnderline.grid(row=11, column=1, sticky='w', padx=2, pady=2)
        self.chOverstrike.grid(row=11, column=2, sticky='w', padx=2, pady=2)
        self.labRelief.grid(row=12, column=1)
        self.cbRelief.grid(row=12, column=2, sticky='w', padx=2, pady=2)
        self.labSliderRel.grid(row=13, column=1)
        self.cbSliderRel.grid(row=13, column=2, sticky='w', padx=2, pady=2)
        self.labOrient.grid(row=14, column=1)
        self.cbOrient.grid(row=14, column=2, sticky='w', padx=2, pady=2)
        self.labBd.grid(row=15, column=1)
        self.spnBd.grid(row=15, column=2, sticky='w', padx=2, pady=2)
        self.labHighTn.grid(row=16, column=1)
        self.spnHighTn.grid(row=16, column=2, sticky='w', padx=2, pady=2)
        self.labCursor.grid(row=17, column=1)
        self.cbCursor.grid(row=17, column=2, sticky='w', padx=2, pady=2)
        self.labWidth.grid(row=18, column=1)
        self.entrWidth.grid(row=18, column=2, sticky='w', padx=2, pady=2)
        self.labLength.grid(row=19, column=1)
        self.spnLength.grid(row=19, column=2, sticky='w', padx=2, pady=2)
        self.labSliderlength.grid(row=20, column=1)
        self.spnSliderlength.grid(row=20, column=2, sticky='w', padx=2, pady=2)
        self.labFrom.grid(row=21, column=1)
        self.spnFrom.grid(row=21, column=2, sticky='w', padx=2, pady=2)
        self.labTo.grid(row=22, column=1)
        self.spnTo.grid(row=22, column=2, sticky='w', padx=2, pady=2)
        self.chShowvalue.grid(row=23, column=1, sticky='w',padx=2, pady=2)
      
    def setText(self):
        tk.Label(self.master, text=getLang(self.obj.type), bg=self.theme[0], fg=self.theme[1], 
                 font=Font(size=15, family='system', weight='bold', underline=True)).grid(row=0, column=1, columnspan=2, sticky='ew', pady=10)
        self.labBg.grid(row=2, column=1)
        self.bBg.grid(row=2, column=2, sticky='w', padx=2, pady=2)
        self.labFg.grid(row=3, column=1)
        self.bFg.grid(row=3, column=2, sticky='w', padx=2, pady=2)
        self.labHighBg.grid(row=4, column=1)
        self.bHighBg.grid(row=4, column=2, sticky='w', padx=2, pady=2)
        self.labSelectBg.grid(row=5, column=1)
        self.bSelectBg.grid(row=5, column=2, sticky='w', padx=2, pady=2)
        self.labHighFg.grid(row=6, column=1)
        self.bHighFg.grid(row=6, column=2, sticky='w', padx=2, pady=2)
        self.labSelectFg.grid(row=7, column=1)
        self.bSelectFg.grid(row=7, column=2, sticky='w', padx=2, pady=2)
        self.labInsertBg.grid(row=8, column=1)
        self.bInsertBg.grid(row=8, column=2, sticky='w', padx=2, pady=2)
        self.labFont.grid(row=9, column=1)
        self.cbFont.grid(row=9, column=2, sticky='w', padx=2, pady=2)
        self.labSize.grid(row=10, column=1)
        self.spnSize.grid(row=10, column=2, sticky='w', padx=2, pady=2)
        self.chWeight.grid(row=11, column=1, sticky='w', padx=2, pady=2)
        self.chSlant.grid(row=11, column=2, sticky='w', padx=2, pady=2)
        self.chUnderline.grid(row=12, column=1, sticky='w', padx=2, pady=2)
        self.chOverstrike.grid(row=12, column=2, sticky='w', padx=2, pady=2)
        self.labRelief.grid(row=13, column=1)
        self.cbRelief.grid(row=13, column=2, sticky='w', padx=2, pady=2)
        self.labBd.grid(row=14, column=1)
        self.spnBd.grid(row=14, column=2, sticky='w', padx=2, pady=2)
        self.labHighTn.grid(row=15, column=1)
        self.spnHighTn.grid(row=15, column=2, sticky='w', padx=2, pady=2)
        self.labCursor.grid(row=16, column=1)
        self.cbCursor.grid(row=16, column=2, sticky='w', padx=2, pady=2)
        self.labWidth.grid(row=17, column=1)
        self.entrWidth.grid(row=17, column=2, sticky='w', padx=2, pady=2)
        self.labHeight.grid(row=18, column=1)
        self.entrHeight.grid(row=18, column=2, sticky='w', padx=2, pady=2)
        self.labSelectBdWt.grid(row=19, column=1)
        self.spnSelectBdWdt.grid(row=19, column=2, sticky='w', padx=2, pady=2)
        self.labInsertWith.grid(row=20, column=1)
        self.spnInsertWidth.grid(row=20, column=2, sticky='w', padx=2, pady=2)
        self.labInsertBdWt.grid(row=21, column=1)
        self.spnInsertBdWdt.grid(row=21, column=2, sticky='w', padx=2, pady=2)

    def setScrollableframe(self):
        tk.Label(self.master, text=getLang(self.obj.type), bg=self.theme[0], fg=self.theme[1], 
                 font=Font(size=15, family='system', weight='bold', underline=True)).grid(row=0, column=1, columnspan=2, sticky='ew', pady=10)
        self.labBg.grid(row=2, column=1)
        self.bBg.grid(row=2, column=2, sticky='w', padx=2, pady=2)
        self.labHighBg.grid(row=3, column=1)
        self.bHighBg.grid(row=3, column=2, sticky='w', padx=2, pady=2)
        self.labHighFg.grid(row=4, column=1)
        self.bHighFg.grid(row=4, column=2, sticky='w', padx=2, pady=2)
        self.labRelief.grid(row=5, column=1)
        self.cbRelief.grid(row=5, column=2, sticky='w', padx=2, pady=2)
        self.labBd.grid(row=6, column=1)
        self.spnBd.grid(row=6, column=2, sticky='w', padx=2, pady=2)
        self.labHighTn.grid(row=7, column=1)
        self.spnHighTn.grid(row=7, column=2, sticky='w', padx=2, pady=2)
        self.labCursor.grid(row=8, column=1)
        self.cbCursor.grid(row=8, column=2, sticky='w', padx=2, pady=2)
        self.labWidth.grid(row=9, column=1)
        self.entrWidth.grid(row=9, column=2, sticky='w', padx=2, pady=2)
        self.labHeight.grid(row=10, column=1)
        self.entrHeight.grid(row=10, column=2, sticky='w', padx=2, pady=2)
    
    def setSpinbox(self):
        tk.Label(self.master, text=getLang(self.obj.type), bg=self.theme[0], fg=self.theme[1], 
                 font=Font(size=15, family='system', weight='bold', underline=True)).grid(row=0, column=1, columnspan=2, sticky='ew', pady=10)
        self.labBg.grid(row=2, column=1)
        self.bBg.grid(row=2, column=2, sticky='w', padx=2, pady=2)
        self.labFg.grid(row=3, column=1)
        self.bFg.grid(row=3, column=2, sticky='w', padx=2, pady=2)
        self.labSelectBg.grid(row=4, column=1)
        self.bSelectBg.grid(row=4, column=2, sticky='w', padx=2, pady=2)
        self.labButtonBg.grid(row=7, column=1)
        self.bButtonBg.grid(row=7, column=2, sticky='w', padx=2, pady=2)
        self.labHighBg.grid(row=8, column=1)
        self.bHighBg.grid(row=8, column=2, sticky='w', padx=2, pady=2)
        self.labHighFg.grid(row=9, column=1)
        self.bHighFg.grid(row=9, column=2, sticky='w', padx=2, pady=2)
        self.labSelectFg.grid(row=10, column=1)
        self.bSelectFg.grid(row=10, column=2, sticky='w', padx=2, pady=2)
        self.labInsertBg.grid(row=11, column=1)
        self.bInsertBg.grid(row=11, column=2, sticky='w', padx=2, pady=2)
        self.labFont.grid(row=12, column=1)
        self.cbFont.grid(row=12, column=2, sticky='w', padx=2, pady=2)
        self.labSize.grid(row=13, column=1)
        self.spnSize.grid(row=13, column=2, sticky='w', padx=2, pady=2)
        self.chWeight.grid(row=14, column=1, sticky='w', padx=2, pady=2)
        self.chSlant.grid(row=14, column=2, sticky='w', padx=2, pady=2)
        self.chUnderline.grid(row=15, column=1, sticky='w', padx=2, pady=2)
        self.chOverstrike.grid(row=15, column=2, sticky='w', padx=2, pady=2)
        self.labJustify.grid(row=16, column=1)
        self.cbJustify.grid(row=16, column=2, sticky='w', padx=2, pady=2)
        self.labRelief.grid(row=17, column=1)
        self.cbRelief.grid(row=17, column=2, sticky='w', padx=2, pady=2)
        self.labButtonDRel.grid(row=18, column=1)
        self.cbButtonDRel.grid(row=18, column=2, sticky='w', padx=2, pady=2)
        self.labButtonURel.grid(row=19, column=1)
        self.cbButtonURel.grid(row=19, column=2, sticky='w', padx=2, pady=2)
        self.labBd.grid(row=20, column=1)
        self.spnBd.grid(row=20, column=2, sticky='w', padx=2, pady=2)
        self.labHighTn.grid(row=21, column=1)
        self.spnHighTn.grid(row=21, column=2, sticky='w', padx=2, pady=2)
        self.labCursor.grid(row=22, column=1)
        self.cbCursor.grid(row=22, column=2, sticky='w', padx=2, pady=2)
        self.labButtonCur.grid(row=23, column=1)
        self.cbButtonCur.grid(row=23, column=2, sticky='w', padx=2, pady=2)
        self.labWidth.grid(row=24, column=1)
        self.entrWidth.grid(row=24, column=2, sticky='w', padx=2, pady=2)
        self.labSelectBdWt.grid(row=25, column=1)
        self.spnSelectBdWdt.grid(row=25, column=2, sticky='w', padx=2, pady=2)
        self.labInsertWith.grid(row=26, column=1)
        self.spnInsertWidth.grid(row=26, column=2, sticky='w', padx=2, pady=2)
        self.labInsertBdWt.grid(row=27, column=1)
        self.spnInsertBdWdt.grid(row=27, column=2, sticky='w', padx=2, pady=2)
        self.labFrom.grid(row=28, column=1)
        self.spnFrom.grid(row=28, column=2, sticky='w', padx=2, pady=2)
        self.labTo.grid(row=29, column=1)
        self.spnTo.grid(row=29, column=2, sticky='w', padx=2, pady=2)

        
['activebackground', 'activeforeground', 'anchor', 'aspect',
   'bd', 'bg', 'bitmap', 'border', 'buttonbackground', 'buttoncursor', 
   'buttondownrelief', 'buttonuprelief', 'compound', 'cursor', 'direction', 
   'offrelief', 'font', 'from_', 'height', 'highlightbackground', 'highlightcolor', 
   'highlightthickness', 'image', 'indicatoron', 'insertbackground', 'insertborderwidth', 
   'insertwidth', 'justify', 'label', 'labelanchor', 'length', 'orient', 'overrelief', 
   'padx', 'pady', 'relief', 'selectbackground', 'selectborderwidth',
   'selectcolor', 'selectforeground', 'selectimage', 'show', 'showvalue', 
   'sliderlength', 'sliderrelief', 'text', 'to', 'troughcolor', 'width', 'wraplength']

