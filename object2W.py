import tkinter as tk
import tkinter.ttk as ttk
from tkinter.scrolledtext import ScrolledText as Text
from tkinter.font import Font
import pyfunct as pf
from language import getLang

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

'''tk.Button(activebackground, activeforeground, anchor, bg, bd, bitmap, border, compound, cursor, font, 
          height, highlightbackground, highlightcolor, highlightthickness, image, justify, overrelief,
          padx, pady, relief, text, width, wraplength)'''

class Button2W(tk.Button):
   def __init__(self, master=None, *cnf, **kwargs):
      tk.Button.__init__(self, master, *cnf, **kwargs)
      self.type='button'
      self.config(text=getLang(self.type))
      self['font']=Font(family=pf.POLICE[0], size=11, weight='normal', slant='roman', underline=False, overstrike=False)
      self.activeBg=self['activebackground']
      self.activeFg=self['activeforeground']
      self.anchor=self['anchor']
      self.bg=self['bg']
      self.bd=self['bd']
      self.fg=self['fg']
      self.bitmap=self['bitmap'] #None, error, gray75, gray50, gray25, gray12, hourglass, info, questhead, question, warning
      self.compound=self['compound']   #top, bottom, left, right, center, none
      self.cursor=self['cursor']
      #Fontpart<
      self.font=pf.POLICE[0]
      self.size=11
      self.weight='normal'
      self.slant='roman'
      self.underline=False
      self.overstrike=False
      #Fontpart>
      self.height=self['height']
      self.highBg=self['highlightbackground']
      self.highFg=self['highlightcolor']
      self.highTn=self['highlightthickness']
      self.image=self['image']
      self.justify=self['justify']
      self.overrelief=self['overrelief']
      self.padx=self['padx']
      self.pady=self['pady']
      self.relief=self['relief'] #flat, raised, sunken, groove, ridge
      self.text=self['text']
      self.width=self['width']
      self.wraplength=self['wraplength']  #numerique
   
   def getAll(self):
      return [self.type, self.activeBg, self.activeFg, self.anchor, self.bg, self.bd, self.fg, self.bitmap,
              self.compound, self.cursor, self.font, self.size, self.weight, self.slant, self.underline,
              self.overstrike, self.height, self.highBg, self.highFg, self.highTn, self.image, self.justify,
              self.overrelief, self.padx, self.pady, self.relief, self.text, self.width, self.wraplength]
   
   def setAll(self, all):
      self.setActiveBg(all[1])
      self.setActiveFg(all[2])
      self.setAnchor(all[3])
      self.setBg(all[4])
      self.setBd(all[5])
      self.setFg(all[6])
      self.setBitmap(all[7])
      self.setCompound(all[8])
      self.setCursor(all[9])
      self.setFont(all[10])
      self.setSize(all[11])
      self.setWeigth(all[12])
      self.setSlant(all[13])
      self.setUnderline(all[14])
      self.setOverstrike(all[15])
      self.setHeight(all[16])
      self.setHighBg(all[17])
      self.setHighFg(all[18])
      self.setHighTn(all[19])
      self.setImage(all[20])
      self.setJustify(all[21])
      self.setOverrelief(all[22])
      self.setPadx(all[23])
      self.setPady(all[24])
      self.setRelief(all[25])
      self.setText(all[26])
      self.setWidth(all[27])
      self.setWraplength(all[28])
      
   def setActiveBg(self, value=None):
      self.activeBg=value if type(value)!=type(None) else self.activeBg
      self['activebackground']=self.activeBg
   
   def setActiveFg(self, value=None):
      self.activeFg=value if type(value)!=type(None) else self.activeFg
      self['activeforeground']=self.activeFg

   def setAnchor(self, value):
      self.anchor=value if type(value)!=type(None) else self.anchor
      self['anchor']=self.anchor

   def setBg(self, value=None):
      self.bg=value if type(value)!=type(None) else self.bg
      self['bg']=self.bg
   
   def setFg(self, value=None):
      self.fg=value if type(value)!=type(None) else self.fg
      self['fg']=self.fg

   def setBd(self, value=None):
      self.bd=value if type(value)!=type(None) else self.bd
      self['bd']=self.bd
   
   def setBitmap(self, value=None):
      self.bitmap=value
      self['bitmap']=self.bitmap

   def setCompound(self, value=None):
      self.compound=value if type(value)!=type(None) else self.compound
      self['compound']=self.compound
   
   def setCursor(self, value=None):
      self.cursor=value if type(value)!=type(None) else self.cursor
      self['cursor']=self.cursor
   
   def setFont(self, value=None):
      self.font=value if type(value)!=type(None) else self.font
      self['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)

   def setSize(self, value=None):
      self.size=value if type(value)!=type(None) else self.size
      self['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)
   
   def setWeigth(self, value=None):
      self.weight=value if type(value)!=type(None) else self.weight
      self['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)
   
   def setSlant(self, value=None):
      self.slant=value if type(value)!=type(None) else self.slant
      self['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)
   
   def setUnderline(self, value=None):
      self.underline=value if type(value)!=type(None) else self.underline
      self['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)
   
   def setOverstrike(self, value=None):
      self.overstrike=value if type(value)!=type(None) else self.overstrike
      self['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)

   def setHeight(self, value=None):
      self.height=value if type(value)!=type(None) else self.height
      self['height']=self.height
   
   def setHighBg(self, value=None):
      self.highBg=value if type(value)!=type(None) else self.highBg
      self['highlightbackground']=self.highBg
   
   def setHighFg(self, value=None):
      self.highFg=value if type(value)!=type(None) else self.highFg
      self['highlightcolor']=self.highFg

   def setHighTn(self, value=None):
      self.highTn=value if type(value)!=type(None) else self.highTn
      self['highlightthickness']=self.highTn
   
   def setImage(self, value=None):
      self.image=value
      self['image']=self.image
   
   def setJustify(self, value=None):
      self.justify=value if type(value)!=type(None) else self.justify
      self['justify']=self.justify

   def setOverrelief(self, value=None):
      self.overrelief=value if type(value)!=type(None) else self.overrelief
      self['overrelief']=self.overrelief
   
   def setPadx(self, value=None):
      self.padx=value if type(value)!=type(None) else self.padx
      self['padx']=self.padx
   
   def setPady(self, value=None):
      self.pady=value if type(value)!=type(None) else self.pady
      self['pady']=self.pady
   
   def setRelief(self, value=None):
      self.relief=value if type(value)!=type(None) else self.relief
      self['relief']=self.relief
   
   def setText(self, value=None):
      self.text=value if type(value)!=type(None) else self.text
      self['text']=self.text
   
   def setWidth(self, value=None):
      self.width=value if type(value)!=type(None) else self.width
      self['width']=self.width
   
   def setWraplength(self, value=None):
      self.wraplength=value if type(value)!=type(None) else self.wraplength
      self['wraplength']=self.wraplength

'''tk.Checkbutton(actbg, actfg, anchor, bg, bd, bmp, compound, cur, font, hbg,
               hcol, htckn, img, indicatoron, just, offrelief, overrel,
               padx, pady, rel, selectimage, selectcolor, txt, wpl, wdt)'''

class Checkbutton2W(tk.Checkbutton):
   def __init__(self, master=None, *cnf, **kwargs):
      tk.Checkbutton.__init__(self, master, *cnf, **kwargs)
      self.type='checkbutton'
      self.config(text=getLang(self.type))
      self['font']=Font(family=pf.POLICE[0], size=11, weight='normal', slant='roman', underline=False, overstrike=False)
      self.activeBg=self['activebackground']
      self.activeFg=self['activeforeground']
      self.anchor=self['anchor']
      self.bg=self['bg']
      self.bd=self['bd']
      self.fg=self['fg']
      self.bitmap=self['bitmap'] #None, error, gray75, gray50, gray25, gray12, hourglass, info, questhead, question, warning
      self.compound=self['compound']   #top, bottom, left, right, center, none
      self.cursor=self['cursor']
      #Fontpart<
      self.font=pf.POLICE[0]
      self.size=11
      self.weight='normal'
      self.slant='roman'
      self.underline=False
      self.overstrike=False
      #Fontpart>
      self.height=self['height']
      self.highBg=self['highlightbackground']
      self.highFg=self['highlightcolor']
      self.highTn=self['highlightthickness']
      self.image=self['image']
      self.justify=self['justify']
      self.overrelief=self['overrelief']
      self.padx=self['padx']
      self.pady=self['pady']
      self.relief=self['relief'] #flat, raised, sunken, groove, ridge
      self.text=self['text']
      self.width=self['width']
      self.wraplength=self['wraplength']  #numerique
      self.indicatoron=self['indicatoron']
      self.offrelief=self['offrelief']
      self.selectimage=self['selectimage']
      self.selectcolor=self['selectcolor']
   
   def getAll(self):
      return [self.type, self.activeBg, self.activeFg, self.anchor, self.bg, self.bd, self.fg, self.bitmap,
              self.compound, self.cursor, self.font, self.size, self.weight, self.slant, self.underline,
              self.overstrike, self.height, self.highBg, self.highFg, self.highTn, self.image, self.justify,
              self.overrelief, self.padx, self.pady, self.relief, self.text, self.width, self.wraplength,
              self.indicatoron, self.offrelief, self.selectimage, self.selectcolor]
   
   def setAll(self, all):
      self.setActiveBg(all[1])
      self.setActiveFg(all[2])
      self.setAnchor(all[3])
      self.setBg(all[4])
      self.setBd(all[5])
      self.setFg(all[6])
      self.setBitmap(all[7])
      self.setCompound(all[8])
      self.setCursor(all[9])
      self.setFont(all[10])
      self.setSize(all[11])
      self.setWeigth(all[12])
      self.setSlant(all[13])
      self.setUnderline(all[14])
      self.setOverstrike(all[15])
      self.setHeight(all[16])
      self.setHighBg(all[17])
      self.setHighFg(all[18])
      self.setHighTn(all[19])
      self.setImage(all[20])
      self.setJustify(all[21])
      self.setOverrelief(all[22])
      self.setPadx(all[23])
      self.setPady(all[24])
      self.setRelief(all[25])
      self.setText(all[26])
      self.setWidth(all[27])
      self.setWraplength(all[28])
      self.setIndicatoron(all[29])
      self.setOffrelief(all[30])
      self.setSelectimage(all[31])
      self.setSelectcolor(all[32])
   
   def setActiveBg(self, value=None):
      self.activeBg=value if type(value)!=type(None) else self.activeBg
      self['activebackground']=self.activeBg
   
   def setActiveFg(self, value=None):
      self.activeFg=value if type(value)!=type(None) else self.activeFg
      self['activeforeground']=self.activeFg

   def setAnchor(self, value):
      self.anchor=value if type(value)!=type(None) else self.anchor
      self['anchor']=self.anchor

   def setBg(self, value=None):
      self.bg=value if type(value)!=type(None) else self.bg
      self['bg']=self.bg
   
   def setFg(self, value=None):
      self.fg=value if type(value)!=type(None) else self.fg
      self['fg']=self.fg

   def setBd(self, value=None):
      self.bd=value if type(value)!=type(None) else self.bd
      self['bd']=self.bd
   
   def setBitmap(self, value=None):
      self.bitmap=value
      self['bitmap']=self.bitmap

   def setCompound(self, value=None):
      self.compound=value if type(value)!=type(None) else self.compound
      self['compound']=self.compound
   
   def setCursor(self, value=None):
      self.cursor=value if type(value)!=type(None) else self.cursor
      self['cursor']=self.cursor
   
   def setFont(self, value=None):
      self.font=value if type(value)!=type(None) else self.font
      self['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)

   def setSize(self, value=None):
      self.size=value if type(value)!=type(None) else self.size
      self['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)
   
   def setWeigth(self, value=None):
      self.weight=value if type(value)!=type(None) else self.weight
      self['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)
   
   def setSlant(self, value=None):
      self.slant=value if type(value)!=type(None) else self.slant
      self['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)

   def setUnderline(self, value=None):
      self.underline=value if type(value)!=type(None) else self.underline
      self['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)
   
   def setOverstrike(self, value=None):
      self.overstrike=value if type(value)!=type(None) else self.overstrike
      self['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)

   def setHeight(self, value=None):
      self.height=value if type(value)!=type(None) else self.height
      self['height']=self.height
   
   def setHighBg(self, value=None):
      self.highBg=value if type(value)!=type(None) else self.highBg
      self['highlightbackground']=self.highBg
   
   def setHighFg(self, value=None):
      self.highFg=value if type(value)!=type(None) else self.highFg
      self['highlightcolor']=self.highFg

   def setHighTn(self, value=None):
      self.highTn=value if type(value)!=type(None) else self.highTn
      self['highlightthickness']=self.highTn
   
   def setImage(self, value=None):
      self.image=value
      self['image']=self.image
   
   def setJustify(self, value=None):
      self.justify=value if type(value)!=type(None) else self.justify
      self['justify']=self.justify

   def setOverrelief(self, value=None):
      self.overrelief=value if type(value)!=type(None) else self.overrelief
      self['overrelief']=self.overrelief
   
   def setPadx(self, value=None):
      self.padx=value if type(value)!=type(None) else self.padx
      self['padx']=self.padx
   
   def setPady(self, value=None):
      self.pady=value if type(value)!=type(None) else self.pady
      self['pady']=self.pady
   
   def setRelief(self, value=None):
      self.relief=value if type(value)!=type(None) else self.relief
      self['relief']=self.relief
   
   def setText(self, value=None):
      self.text=value if type(value)!=type(None) else self.text
      self['text']=self.text
   
   def setWidth(self, value=None):
      self.width=value if type(value)!=type(None) else self.width
      self['width']=self.width
   
   def setWraplength(self, value=None):
      self.wraplength=value if type(value)!=type(None) else self.wraplength
      self['wraplength']=self.wraplength

   def setIndicatoron(self, value=None):
      self.indicatoron=value if type(value)!=type(None) else self.indicatoron
      self['indicatoron']=self.indicatoron
   
   def setOffrelief(self, value=None):
      self.offrelief=value if type(value)!=type(None) else self.offrelief
      self['offrelief']=self.offrelief
   
   def setSelectimage(self, value=None):
      self.selectimage=value
      self['selectimage']=self.selectimage

   def setSelectcolor(self, value=None):
      self.selectcolor=value
      self['selectcolor']=self.selectcolor

'''tk.Entry(bg, bd, cur, fg, font, hbg, hcol, htckn, insertbackground, insertborderwidth, 
         insertwidth, just, rel, selectbackground, selectborderwidth, 
         selectforeground, show, wdt)'''

class Entry2W(tk.Entry):
   def __init__(self, master=None, *cnf, **kwargs):
      tk.Entry.__init__(self, master, *cnf, **kwargs)
      self.type='entry'
      self.insert('end', getLang(self.type))
      self['font']=Font(family=pf.POLICE[0], size=11, weight='normal', slant='roman', underline=False, overstrike=False)
      self.bg=self['bg']
      self.bd=self['bd']
      self.fg=self['fg']
      self.cursor=self['cursor']
      #Fontpart<
      self.font=pf.POLICE[0]
      self.size=11
      self.weight='normal'
      self.slant='roman'
      self.underline=False
      self.overstrike=False
      #Fontpart>
      self.highBg=self['highlightbackground']
      self.highFg=self['highlightcolor']
      self.highTn=self['highlightthickness']
      self.justify=self['justify']
      self.relief=self['relief'] #flat, raised, sunken, groove, ridge
      self.width=self['width']
      self.insertBg=self['insertbackground']
      self.insertBdWidth=self['insertborderwidth']
      self.insertWidth=self['insertwidth']
      self.selectBg=self['selectbackground']
      self.selectBdwidth=self['selectborderwidth'] 
      self.selectFg=self['selectforeground']
      self.show=self['show']

   def getAll(self):
      return [self.type, self.bg, self.bd, self.fg, self.cursor, self.font, self.size,
              self.weight, self.slant, self.underline, self.overstrike, self.highBg,
              self.highFg, self.highTn, self.justify, self.relief, self.width, 
              self.insertBg, self.insertBdWidth, self.insertWidth, self.selectBg, self.selectBdwidth,
              self.selectFg, self.show]
   
   def setAll(self, all):
      self.setBg(all[1])
      self.setBd(all[2])
      self.setFg(all[3])
      self.setCursor(all[4])
      self.setFont(all[5])
      self.setSize(all[6])
      self.setWeigth(all[7])
      self.setSlant(all[8])
      self.setUnderline(all[9])
      self.setOverstrike(all[10])
      self.setHighBg(all[11])
      self.setHighFg(all[12])
      self.setHighTn(all[13])
      self.setJustify(all[14])
      self.setRelief(all[15])
      self.setWidth(all[16])
      self.setInsertBg(all[17])
      self.setInsertBdWidth(all[18])
      self.setInsertWidth(all[19])
      self.setSelectBg(all[20])
      self.setSelectBdWidth(all[21])
      self.setSelectFg(all[22])
      self.setShow(all[23])
   
   def setBg(self, value=None):
      self.bg=value if type(value)!=type(None) else self.bg
      self['bg']=self.bg
   
   def setFg(self, value=None):
      self.fg=value if type(value)!=type(None) else self.fg
      self['fg']=self.fg

   def setBd(self, value=None):
      self.bd=value if type(value)!=type(None) else self.bd
      self['bd']=self.bd
   
   def setCursor(self, value=None):
      self.cursor=value if type(value)!=type(None) else self.cursor
      self['cursor']=self.cursor
   
   def setFont(self, value=None):
      self.font=value if type(value)!=type(None) else self.font
      self['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)

   def setSize(self, value=None):
      self.size=value if type(value)!=type(None) else self.size
      self['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)
   
   def setWeigth(self, value=None):
      self.weight=value if type(value)!=type(None) else self.weight
      self['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)
   
   def setSlant(self, value=None):
      self.slant=value if type(value)!=type(None) else self.slant
      self['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)

   def setUnderline(self, value=None):
      self.underline=value if type(value)!=type(None) else self.underline
      self['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)
   
   def setOverstrike(self, value=None):
      self.overstrike=value if type(value)!=type(None) else self.overstrike
      self['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)

   def setHighBg(self, value=None):
      self.highBg=value if type(value)!=type(None) else self.highBg
      self['highlightbackground']=self.highBg
   
   def setHighFg(self, value=None):
      self.highFg=value if type(value)!=type(None) else self.highFg
      self['highlightcolor']=self.highFg

   def setHighTn(self, value=None):
      self.highTn=value if type(value)!=type(None) else self.highTn
      self['highlightthickness']=self.highTn
 
   def setJustify(self, value=None):
      self.justify=value if type(value)!=type(None) else self.justify
      self['justify']=self.justify

   def setRelief(self, value=None):
      self.relief=value if type(value)!=type(None) else self.relief
      self['relief']=self.relief

   def setWidth(self, value=None):
      self.width=value if type(value)!=type(None) else self.width
      self['width']=self.width

   def setInsertBg(self, value=None):
      self.insertBg=value if type(value)!=type(None) else self.insertBg
      self['insertbackground']=self.insertBg
   
   def setInsertBdWidth(self, value=None):
      self.insertBdWidth=value if type(value)!=type(None) else self.insertBdWidth
      self['insertborderwidth']=self.insertBdWidth
   
   def setInsertWidth(self, value=None):
      self.insertWidth=value if type(value)!=type(None) else self.insertWidth
      self['insertwidth']=self.insertWidth
   
   def setSelectBg(self, value=None):
      self.selectBg=value if type(value)!=type(None) else self.selectBg
      self['selectbackground']=self.selectBg
   
   def setSelectBdWidth(self, value=None):
      self.selectBdwidth=value if type(value)!=type(None) else self.selectBdwidth
      self['selectborderwidth']=self.selectBdwidth
   
   def setSelectFg(self, value=None):
      self.selectFg=value if type(value)!=type(None) else self.selectFg
      self['selectforeground']=self.selectFg
   
   def setShow(self, value=None):
      self.show=value
      self['show']=self.show

'''tk.Frame(bg, bd, cur, hgt, hbg, hcol, htckn, rel, wdt)'''

class Frame2W(tk.Frame):
   def __init__(self, master=None, *cnf, **kwargs):
      tk.Frame.__init__(self, master, *cnf, **kwargs)
      self.type='frame'
      self.config(width=100, height=100, bg='grey50')
      self.bg=self['bg']
      self.bd=self['bd']
      self.cursor=self['cursor']
      self.height=self['height']
      self.highBg=self['highlightbackground']
      self.highFg=self['highlightcolor']
      self.highTn=self['highlightthickness']
      self.relief=self['relief'] #flat, raised, sunken, groove, ridge
      self.width=self['width']
  
   def getAll(self):
      return [self.type, self.bg, self.bd, self.cursor, self.height, self.highBg, self.highFg,
              self.highTn, self.relief, self.width]
   
   def setAll(self, all):
      self.setBg(all[1])
      self.setBd(all[2])
      self.setCursor(all[3])
      self.setHeight(all[4])
      self.setHighBg(all[5])
      self.setHighFg(all[6])
      self.setHighTn(all[7])
      self.setRelief(all[8])
      self.setWidth(all[9])
  
   def setBg(self, value=None):
      self.bg=value if type(value)!=type(None) else self.bg
      self['bg']=self.bg

   def setBd(self, value=None):
      self.bd=value if type(value)!=type(None) else self.bd
      self['bd']=self.bd

   def setCursor(self, value=None):
      self.cursor=value if type(value)!=type(None) else self.cursor
      self['cursor']=self.cursor

   def setHeight(self, value=None):
      self.height=value if type(value)!=type(None) else self.height
      self['height']=self.height
   
   def setHighBg(self, value=None):
      self.highBg=value if type(value)!=type(None) else self.highBg
      self['highlightbackground']=self.highBg
   
   def setHighFg(self, value=None):
      self.highFg=value if type(value)!=type(None) else self.highFg
      self['highlightcolor']=self.highFg

   def setHighTn(self, value=None):
      self.highTn=value if type(value)!=type(None) else self.highTn
      self['highlightthickness']=self.highTn
 
   def setRelief(self, value=None):
      self.relief=value if type(value)!=type(None) else self.relief
      self['relief']=self.relief

   def setWidth(self, value=None):
      self.width=value if type(value)!=type(None) else self.width
      self['width']=self.width

'''tk.Label(actbg, actfg, anc, bg, bd, bmp, comp, cur, fg, font, hgt,
         hbg, hcol, htckn, img, just, padx, pady, rel, txt, wrap, wdt)'''

class Label2W(tk.Label):
   def __init__(self, master=None, *cnf, **kwargs):
      tk.Label.__init__(self, master, *cnf, **kwargs)
      self.type='label'
      self.config(text=getLang(self.type))
      self['font']=Font(family=pf.POLICE[0], size=11, weight='normal', slant='roman', underline=False, overstrike=False)
      self.activeBg=self['activebackground']
      self.activeFg=self['activeforeground']
      self.anchor=self['anchor']
      self.bg=self['bg']
      self.bd=self['bd']
      self.fg=self['fg']
      self.bitmap=self['bitmap'] #None, error, gray75, gray50, gray25, gray12, hourglass, info, questhead, question, warning
      self.compound=self['compound']   #top, bottom, left, right, center, none
      self.cursor=self['cursor']
      #Fontpart<
      self.font=pf.POLICE[0]
      self.size=11
      self.weight='normal'
      self.slant='roman'
      self.underline=False
      self.overstrike=False
      #Fontpart>
      self.height=self['height']
      self.highBg=self['highlightbackground']
      self.highFg=self['highlightcolor']
      self.highTn=self['highlightthickness']
      self.image=self['image']
      self.justify=self['justify']
      self.padx=self['padx']
      self.pady=self['pady']
      self.relief=self['relief'] #flat, raised, sunken, groove, ridge
      self.text=self['text']
      self.width=self['width']
      self.wraplength=self['wraplength']  #numerique
         
   def getAll(self):
      return [self.type, self.activeBg, self.activeFg, self.anchor, self.bg, self.bd, self.fg, self.bitmap,
              self.compound, self.cursor, self.font, self.size, self.weight, self.slant, self.underline,
              self.overstrike, self.height, self.highBg, self.highFg, self.highTn, self.image, self.justify,
              self.padx, self.pady, self.relief, self.text, self.width, self.wraplength]
   
   def setAll(self, all):
      self.setActiveBg(all[1])
      self.setActiveFg(all[2])
      self.setAnchor(all[3])
      self.setBg(all[4])
      self.setBd(all[5])
      self.setFg(all[6])
      self.setBitmap(all[7])
      self.setCompound(all[8])
      self.setCursor(all[9])
      self.setFont(all[10])
      self.setSize(all[11])
      self.setWeigth(all[12])
      self.setSlant(all[13])
      self.setUnderline(all[14])
      self.setOverstrike(all[15])
      self.setHeight(all[16])
      self.setHighBg(all[17])
      self.setHighFg(all[18])
      self.setHighTn(all[19])
      self.setImage(all[20])
      self.setJustify(all[21])
      self.setPadx(all[22])
      self.setPady(all[23])
      self.setRelief(all[24])
      self.setText(all[25])
      self.setWidth(all[26])
      self.setWraplength(all[27])
 
   def setActiveBg(self, value=None):
      self.activeBg=value if type(value)!=type(None) else self.activeBg
      self['activebackground']=self.activeBg
   
   def setActiveFg(self, value=None):
      self.activeFg=value if type(value)!=type(None) else self.activeFg
      self['activeforeground']=self.activeFg

   def setAnchor(self, value):
      self.anchor=value if type(value)!=type(None) else self.anchor
      self['anchor']=self.anchor

   def setBg(self, value=None):
      self.bg=value if type(value)!=type(None) else self.bg
      self['bg']=self.bg
   
   def setFg(self, value=None):
      self.fg=value if type(value)!=type(None) else self.fg
      self['fg']=self.fg

   def setBd(self, value=None):
      self.bd=value if type(value)!=type(None) else self.bd
      self['bd']=self.bd
   
   def setBitmap(self, value=None):
      self.bitmap=value
      self['bitmap']=self.bitmap

   def setCompound(self, value=None):
      self.compound=value if type(value)!=type(None) else self.compound
      self['compound']=self.compound
   
   def setCursor(self, value=None):
      self.cursor=value if type(value)!=type(None) else self.cursor
      self['cursor']=self.cursor
   
   def setFont(self, value=None):
      self.font=value if type(value)!=type(None) else self.font
      self['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)

   def setSize(self, value=None):
      self.size=value if type(value)!=type(None) else self.size
      self['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)
   
   def setWeigth(self, value=None):
      self.weight=value if type(value)!=type(None) else self.weight
      self['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)
   
   def setSlant(self, value=None):
      self.slant=value if type(value)!=type(None) else self.slant
      self['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)
 
   def setUnderline(self, value=None):
      self.underline=value if type(value)!=type(None) else self.underline
      self['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)
   
   def setOverstrike(self, value=None):
      self.overstrike=value if type(value)!=type(None) else self.overstrike
      self['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)

   def setHeight(self, value=None):
      self.height=value if type(value)!=type(None) else self.height
      self['height']=self.height
   
   def setHighBg(self, value=None):
      self.highBg=value if type(value)!=type(None) else self.highBg
      self['highlightbackground']=self.highBg
   
   def setHighFg(self, value=None):
      self.highFg=value if type(value)!=type(None) else self.highFg
      self['highlightcolor']=self.highFg

   def setHighTn(self, value=None):
      self.highTn=value if type(value)!=type(None) else self.highTn
      self['highlightthickness']=self.highTn
   
   def setImage(self, value=None):
      self.image=value
      self['image']=self.image
   
   def setJustify(self, value=None):
      self.justify=value if type(value)!=type(None) else self.justify
      self['justify']=self.justify

   def setOverrelief(self, value=None):
      self.overrelief=value if type(value)!=type(None) else self.overrelief
      self['overrelief']=self.overrelief
   
   def setPadx(self, value=None):
      self.padx=value if type(value)!=type(None) else self.padx
      self['padx']=self.padx
   
   def setPady(self, value=None):
      self.pady=value if type(value)!=type(None) else self.pady
      self['pady']=self.pady
   
   def setRelief(self, value=None):
      self.relief=value if type(value)!=type(None) else self.relief
      self['relief']=self.relief
   
   def setText(self, value=None):
      self.text=value if type(value)!=type(None) else self.text
      self['text']=self.text
   
   def setWidth(self, value=None):
      self.width=value if type(value)!=type(None) else self.width
      self['width']=self.width
   
   def setWraplength(self, value=None):
      self.wraplength=value if type(value)!=type(None) else self.wraplength
      self['wraplength']=self.wraplength

'''tk.LabelFrame(bg, bd, cur, font, fg, hgt, hbg, hcol, htckn, labelanchor, padx, pady, rel, text, wdt)'''

class LabelFrame2W(tk.LabelFrame):
   def __init__(self, master=None, *cnf, **kwargs):
      tk.LabelFrame.__init__(self, master, *cnf, **kwargs)
      self.type='labelframe'
      self.config(text=getLang(self.type), width=100, height=100, bg='grey50')
      self['font']=Font(family=pf.POLICE[0], size=11, weight='normal', slant='roman', underline=False, overstrike=False)
      self.bg=self['bg']
      self.bd=self['bd']
      self.fg=self['fg']
      self.cursor=self['cursor']
      #Fontpart<
      self.font=pf.POLICE[0]
      self.size=11
      self.weight='normal'
      self.slant='roman'
      self.underline=False
      self.overstrike=False
      #Fontpart>
      self.height=self['height']
      self.highBg=self['highlightbackground']
      self.highFg=self['highlightcolor']
      self.highTn=self['highlightthickness']
      self.padx=self['padx']
      self.pady=self['pady']
      self.relief=self['relief'] #flat, raised, sunken, groove, ridge
      self.text=self['text']
      self.width=self['width']
      self.labelanchor=self['labelanchor']
            
   def getAll(self):
      return [self.type, self.bg, self.bd, self.fg,
              self.cursor, self.font, self.size, self.weight, self.slant, self.underline,
              self.overstrike, self.height, self.highBg, self.highFg, self.highTn,
              self.padx, self.pady, self.relief, self.text, self.width, self.labelanchor]
   
   def setAll(self, all):
      self.setBg(all[1])
      self.setBd(all[2])
      self.setFg(all[3])
      self.setCursor(all[4])
      self.setFont(all[5])
      self.setSize(all[6])
      self.setWeigth(all[7])
      self.setSlant(all[8])
      self.setUnderline(all[9])
      self.setOverstrike(all[10])
      self.setHeight(all[11])
      self.setHighBg(all[12])
      self.setHighFg(all[13])
      self.setHighTn(all[14])
      self.setPadx(all[15])
      self.setPady(all[16])
      self.setRelief(all[17])
      self.setText(all[18])
      self.setWidth(all[19])
      self.setLabelanchor(all[20])
 
   def setLabelanchor(self, value):
      self.labelanchor=value if type(value)!=type(None) else self.labelanchor
      self['labelanchor']=self.labelanchor

   def setBg(self, value=None):
      self.bg=value if type(value)!=type(None) else self.bg
      self['bg']=self.bg
   
   def setFg(self, value=None):
      self.fg=value if type(value)!=type(None) else self.fg
      self['fg']=self.fg

   def setBd(self, value=None):
      self.bd=value if type(value)!=type(None) else self.bd
      self['bd']=self.bd

   def setCursor(self, value=None):
      self.cursor=value if type(value)!=type(None) else self.cursor
      self['cursor']=self.cursor
   
   def setFont(self, value=None):
      self.font=value if type(value)!=type(None) else self.font
      self['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)

   def setSize(self, value=None):
      self.size=value if type(value)!=type(None) else self.size
      self['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)
   
   def setWeigth(self, value=None):
      self.weight=value if type(value)!=type(None) else self.weight
      self['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)
   
   def setSlant(self, value=None):
      self.slant=value if type(value)!=type(None) else self.slant
      self['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)

   def setUnderline(self, value=None):
      self.underline=value if type(value)!=type(None) else self.underline
      self['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)
   
   def setOverstrike(self, value=None):
      self.overstrike=value if type(value)!=type(None) else self.overstrike
      self['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)

   def setHeight(self, value=None):
      self.height=value if type(value)!=type(None) else self.height
      self['height']=self.height
   
   def setHighBg(self, value=None):
      self.highBg=value if type(value)!=type(None) else self.highBg
      self['highlightbackground']=self.highBg
   
   def setHighFg(self, value=None):
      self.highFg=value if type(value)!=type(None) else self.highFg
      self['highlightcolor']=self.highFg

   def setHighTn(self, value=None):
      self.highTn=value if type(value)!=type(None) else self.highTn
      self['highlightthickness']=self.highTn

   def setPadx(self, value=None):
      self.padx=value if type(value)!=type(None) else self.padx
      self['padx']=self.padx
   
   def setPady(self, value=None):
      self.pady=value if type(value)!=type(None) else self.pady
      self['pady']=self.pady
   
   def setRelief(self, value=None):
      self.relief=value if type(value)!=type(None) else self.relief
      self['relief']=self.relief
   
   def setText(self, value=None):
      self.text=value if type(value)!=type(None) else self.text
      self['text']=self.text
   
   def setWidth(self, value=None):
      self.width=value if type(value)!=type(None) else self.width
      self['width']=self.width
 
'''tk.Listbox(bg, bd, cur, fg, font, hgt, hbg, hcol, htckn, just,
            rel, selectbackground, selectborderwidth, selectforeground, wdt)'''

class Listbox2W(tk.Listbox):
   def __init__(self, master=None, *cnf, **kwargs):
      tk.Listbox.__init__(self, master, *cnf, **kwargs)
      self.type='listbox'
      self['font']=Font(family=pf.POLICE[0], size=11, weight='normal', slant='roman', underline=False, overstrike=False)
      self.bg=self['bg']
      self.bd=self['bd']
      self.fg=self['fg']
      self.cursor=self['cursor']
      #Fontpart<
      self.font=pf.POLICE[0]
      self.size_=11
      self.weight='normal'
      self.slant='roman'
      self.underline=False
      self.overstrike=False
      #Fontpart>
      self.height=self['height']
      self.highBg=self['highlightbackground']
      self.highFg=self['highlightcolor']
      self.highTn=self['highlightthickness']
      self.justify=self['justify']
      self.relief=self['relief'] #flat, raised, sunken, groove, ridge
      self.width=self['width']
      self.selectBg=self['selectbackground']
      self.selectBdwidth=self['selectborderwidth'] 
      self.selectFg=self['selectforeground']
      self.listOption={}
   
   def getAll(self):
      return [self.type, self.bg, self.bd, self.fg, self.cursor, self.font, self.size_,
              self.weight, self.slant, self.underline, self.overstrike, self.height, self.highBg,
              self.highFg, self.highTn, self.justify, self.relief, self.width, 
              self.selectBg, self.selectBdwidth, self.selectFg, list(self.get(0, tk.END))]
   
   def setAll(self, all):
      self.setBg(all[1])
      self.setBd(all[2])
      self.setFg(all[3])
      self.setCursor(all[4])
      self.setFont(all[5])
      self.setSize(all[6])
      self.setWeigth(all[7])
      self.setSlant(all[8])
      self.setUnderline(all[9])
      self.setOverstrike(all[10])
      self.setHeight(all[11])
      self.setHighBg(all[12])
      self.setHighFg(all[13])
      self.setHighTn(all[14])
      self.setJustify(all[15])
      self.setRelief(all[16])
      self.setWidth(all[17])
      self.setSelectBg(all[18])
      self.setSelectBdWidth(all[19])
      self.setSelectFg(all[20])
      self.delete(0, tk.END)
      if len(all[21])>0:
         for ww in all[21]:
            self.insert(tk.END, ww)
  
   def setBg(self, value=None):
      self.bg=value if type(value)!=type(None) else self.bg
      self['bg']=self.bg
   
   def setFg(self, value=None):
      self.fg=value if type(value)!=type(None) else self.fg
      self['fg']=self.fg

   def setBd(self, value=None):
      self.bd=value if type(value)!=type(None) else self.bd
      self['bd']=self.bd

   def setCursor(self, value=None):
      self.cursor=value if type(value)!=type(None) else self.cursor
      self['cursor']=self.cursor
   
   def setFont(self, value=None):
      self.font=value if type(value)!=type(None) else self.font
      self['font']=Font(family=self.font, size=self.size_, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)

   def setSize(self, value=None):
      self.size_=value if type(value)!=type(None) else self.size_
      self['font']=Font(family=self.font, size=self.size_, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)
   
   def setWeigth(self, value=None):
      self.weight=value if type(value)!=type(None) else self.weight
      self['font']=Font(family=self.font, size=self.size_, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)
   
   def setSlant(self, value=None):
      self.slant=value if type(value)!=type(None) else self.slant
      self['font']=Font(family=self.font, size=self.size_, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)
      
   def setUnderline(self, value=None):
      self.underline=value if type(value)!=type(None) else self.underline
      self['font']=Font(family=self.font, size=self.size_, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)
   
   def setOverstrike(self, value=None):
      self.overstrike=value if type(value)!=type(None) else self.overstrike
      self['font']=Font(family=self.font, size=self.size_, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)

   def setHeight(self, value=None):
      self.height=value if type(value)!=type(None) else self.height
      self['height']=self.height
   
   def setHighBg(self, value=None):
      self.highBg=value if type(value)!=type(None) else self.highBg
      self['highlightbackground']=self.highBg
   
   def setHighFg(self, value=None):
      self.highFg=value if type(value)!=type(None) else self.highFg
      self['highlightcolor']=self.highFg

   def setHighTn(self, value=None):
      self.highTn=value if type(value)!=type(None) else self.highTn
      self['highlightthickness']=self.highTn

   def setJustify(self, value=None):
      self.justify=value if type(value)!=type(None) else self.justify
      self['justify']=self.justify

   def setRelief(self, value=None):
      self.relief=value if type(value)!=type(None) else self.relief
      self['relief']=self.relief

   def setWidth(self, value=None):
      self.width=value if type(value)!=type(None) else self.width
      self['width']=self.width
   
   def setSelectBg(self, value=None):
      self.selectBg=value if type(value)!=type(None) else self.selectBg
      self['selectbackground']=self.selectBg
   
   def setSelectBdWidth(self, value=None):
      self.selectBdwidth=value if type(value)!=type(None) else self.selectBdwidth
      self['selectborderwidth']=self.selectBdwidth
   
   def setSelectFg(self, value=None):
      self.selectFg=value if type(value)!=type(None) else self.selectFg
      self['selectforeground']=self.selectFg
   
'''tk.Menubutton(actbg, actfg, anc, bg, bd, bmp, comp, cur, 
              direction, fg, font, hgt, hbg, hfg, htckn, img,
              indicatoron, just, menu, padx, pady,rel, txt, wdt, wraplength)'''
   
class Menubutton2W(tk.Menubutton):
   def __init__(self, master=None, *cnf, **kwargs):
      tk.Menubutton.__init__(self, master, *cnf, **kwargs)
      self.type='menubutton'
      self.config(text=getLang(self.type))
      self['font']=Font(family=pf.POLICE[0], size=11, weight='normal', slant='roman', underline=False, overstrike=False)
      self.activeBg=self['activebackground']
      self.activeFg=self['activeforeground']
      self.anchor=self['anchor']
      self.bg=self['bg']
      self.bd=self['bd']
      self.fg=self['fg']
      self.bitmap=self['bitmap'] #None, error, gray75, gray50, gray25, gray12, hourglass, info, questhead, question, warning
      self.compound=self['compound']   #top, bottom, left, right, center, none
      self.cursor=self['cursor']
      self.direction=self['direction'] #below, above, left, right
      #Fontpart<
      self.font=pf.POLICE[0]
      self.size=11
      self.weight='normal'
      self.slant='roman'
      self.underline=False
      self.overstrike=False
      #Fontpart>
      self.height=self['height']
      self.highBg=self['highlightbackground']
      self.highFg=self['highlightcolor']
      self.highTn=self['highlightthickness']
      self.image=self['image']
      self.justify=self['justify']
      self.padx=self['padx']
      self.pady=self['pady']
      self.relief=self['relief'] #flat, raised, sunken, groove, ridge
      self.text=self['text']
      self.width=self['width']
      self.wraplength=self['wraplength']  #numerique
      self.indicatoron=self['indicatoron']
      self.menu=tk.Menu(self, tearoff=False,)
      self['menu']=self.menu
      self.option={}
      self.optindex=0
   
   def add_option(self, label, type='button'):
      self.option[label]=self.optindex
      if type=='button':
         self.optindex=self.menu.index(self.menu.add_command(label=label))
      else:
         self.optionindex=self.menu.index(self.menu.add_checkbutton(label=label))
      self.optindex+=1
   
   def add_separator(self):
      self.option[self.optindex]=self.optindex
      self.optindex=self.menu.index(self.menu.add_separator())
   
   def remove_option(self, label):
      if type(label)==type(''):self.menu.delete(self.option[label])
      else: self.menu.delete(label)
   
   def setActiveBg(self, value=None):
      self.activeBg=value if type(value)!=type(None) else self.activeBg
      self['activebackground']=self.activeBg
      self.menu['activebackground']=self.activeBg
   
   def setActiveFg(self, value=None):
      self.activeFg=value if type(value)!=type(None) else self.activeFg
      self['activeforeground']=self.activeFg
      self.menu['activeforeground']=self.activeFg

   def setAnchor(self, value):
      self.anchor=value if type(value)!=type(None) else self.anchor
      self['anchor']=self.anchor

   def setBg(self, value=None):
      self.bg=value if type(value)!=type(None) else self.bg
      self['bg']=self.bg
      self.menu['bg']=self.bg
   
   def setFg(self, value=None):
      self.fg=value if type(value)!=type(None) else self.fg
      self['fg']=self.fg
      self.menu['fg']=self.fg
      
   def setBd(self, value=None):
      self.bd=value if type(value)!=type(None) else self.bd
      self['bd']=self.bd
      self.menu['bd']=self.bd
   
   def setBitmap(self, value=None):
      self.bitmap=value
      self['bitmap']=self.bitmap

   def setCompound(self, value=None):
      self.compound=value if type(value)!=type(None) else self.compound
      self['compound']=self.compound
   
   def setCursor(self, value=None):
      self.cursor=value if type(value)!=type(None) else self.cursor
      self['cursor']=self.cursor
      self.menu['cursor']=self.cursor
   
   def setFont(self, value=None):
      self.font=value if type(value)!=type(None) else self.font
      self['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)
      self.menu['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)

   def setSize(self, value=None):
      self.size=value if type(value)!=type(None) else self.size
      self['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)
      self.menu['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)
   
   def setWeigth(self, value=None):
      self.weight=value if type(value)!=type(None) else self.weight
      self['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)
   
   def setSlant(self, value=None):
      self.slant=value if type(value)!=type(None) else self.slant
      self['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)
      self.menu['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)
   
   def setUnderline(self, value=None):
      self.underline=value if type(value)!=type(None) else self.underline
      self['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)
      self.menu['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)
   
   def setOverstrike(self, value=None):
      self.overstrike=value if type(value)!=type(None) else self.overstrike
      self['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)
      self.menu['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)

   def setHeight(self, value=None):
      self.height=value if type(value)!=type(None) else self.height
      self['height']=self.height
   
   def setHighBg(self, value=None):
      self.highBg=value if type(value)!=type(None) else self.highBg
      self['highlightbackground']=self.highBg
   
   def setHighFg(self, value=None):
      self.highFg=value if type(value)!=type(None) else self.highFg
      self['highlightcolor']=self.highFg

   def setHighTn(self, value=None):
      self.highTn=value if type(value)!=type(None) else self.highTn
      self['highlightthickness']=self.highTn
   
   def setImage(self, value=None):
      self.image=value
      self['image']=self.image
   
   def setJustify(self, value=None):
      self.justify=value if type(value)!=type(None) else self.justify
      self['justify']=self.justify

   def setPadx(self, value=None):
      self.padx=value if type(value)!=type(None) else self.padx
      self['padx']=self.padx
   
   def setPady(self, value=None):
      self.pady=value if type(value)!=type(None) else self.pady
      self['pady']=self.pady
   
   def setRelief(self, value=None):
      self.relief=value if type(value)!=type(None) else self.relief
      self['relief']=self.relief
      self.menu['relief']=self.relief
   
   def setText(self, value=None):
      self.text=value if type(value)!=type(None) else self.text
      self['text']=self.text
   
   def setWidth(self, value=None):
      self.width=value if type(value)!=type(None) else self.width
      self['width']=self.width
   
   def setWraplength(self, value=None):
      self.wraplength=value if type(value)!=type(None) else self.wraplength
      self['wraplength']=self.wraplength

   def setDirection(self, value=None):
      self.direction=value if type(value)!=type(None) else self.direction
      self['direction']=self.direction
   
   def setIndicatoron(self, value=None):
      self.indicatoron=value if type(value)!=type(None) else self.indicatoron
      self['indicatoron']=self.indicatoron

'''tk.Message(anc, aspect, bg, bd, cur, fg, font, hbg, hfg, htckn, just, padx, pady, rel, txt, wdt)'''

class Message2W(tk.Message):
   def __init__(self, master=None, *cnf, **kwargs):
      tk.Message.__init__(self, master, *cnf, **kwargs)
      self.type='message'
      self.config(text=getLang(self.type))
      self['font']=Font(family=pf.POLICE[0], size=11, weight='normal', slant='roman', underline=False, overstrike=False)
      self.bg=self['bg']
      self.bd=self['bd']
      self.fg=self['fg']
      self.anchor=self['anchor']
      self.aspect=self['aspect'] #numerique
      self.cursor=self['cursor']
      #Fontpart<
      self.font=pf.POLICE[0]
      self.size=11
      self.weight='normal'
      self.slant='roman'
      self.underline=False
      self.overstrike=False
      #Fontpart>
      self.highBg=self['highlightbackground']
      self.highFg=self['highlightcolor']
      self.highTn=self['highlightthickness']
      self.justify=self['justify']
      self.padx=self['padx']
      self.pady=self['pady']
      self.relief=self['relief'] #flat, raised, sunken, groove, ridge
      self.text=self['text']
      self.width=self['width']
         
   def getAll(self):
      return [self.type, self.anchor, self.aspect, self.bg, self.bd, self.fg,
              self.cursor, self.font, self.size, self.weight, self.slant, self.underline,
              self.overstrike, self.highBg, self.highFg, self.highTn, self.justify,
              self.padx, self.pady, self.relief, self.text, self.width]
   
   def setAll(self, all):
      self.setAnchor(all[1])
      self.setAspect(all[2])
      self.setBg(all[3])
      self.setBd(all[4])
      self.setFg(all[5])
      self.setCursor(all[6])
      self.setFont(all[7])
      self.setSize(all[8])
      self.setWeigth(all[9])
      self.setSlant(all[10])
      self.setUnderline(all[11])
      self.setOverstrike(all[12])
      self.setHighBg(all[13])
      self.setHighFg(all[14])
      self.setHighTn(all[15])
      self.setJustify(all[16])
      self.setPadx(all[17])
      self.setPady(all[18])
      self.setRelief(all[19])
      self.setText(all[20])
      self.setWidth(all[21])
 
   def setAnchor(self, value):
      self.anchor=value if type(value)!=type(None) else self.anchor
      self['anchor']=self.anchor

   def setBg(self, value=None):
      self.bg=value if type(value)!=type(None) else self.bg
      self['bg']=self.bg
   
   def setFg(self, value=None):
      self.fg=value if type(value)!=type(None) else self.fg
      self['fg']=self.fg

   def setBd(self, value=None):
      self.bd=value if type(value)!=type(None) else self.bd
      self['bd']=self.bd

   def setCursor(self, value=None):
      self.cursor=value if type(value)!=type(None) else self.cursor
      self['cursor']=self.cursor
   
   def setFont(self, value=None):
      self.font=value if type(value)!=type(None) else self.font
      self['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)

   def setSize(self, value=None):
      self.size=value if type(value)!=type(None) else self.size
      self['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)
   
   def setWeigth(self, value=None):
      self.weight=value if type(value)!=type(None) else self.weight
      self['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)
   
   def setSlant(self, value=None):
      self.slant=value if type(value)!=type(None) else self.slant
      self['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)
  
   def setUnderline(self, value=None):
      self.underline=value if type(value)!=type(None) else self.underline
      self['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)
   
   def setOverstrike(self, value=None):
      self.overstrike=value if type(value)!=type(None) else self.overstrike
      self['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)

   def setHighBg(self, value=None):
      self.highBg=value if type(value)!=type(None) else self.highBg
      self['highlightbackground']=self.highBg
   
   def setHighFg(self, value=None):
      self.highFg=value if type(value)!=type(None) else self.highFg
      self['highlightcolor']=self.highFg

   def setHighTn(self, value=None):
      self.highTn=value if type(value)!=type(None) else self.highTn
      self['highlightthickness']=self.highTn

   def setJustify(self, value=None):
      self.justify=value if type(value)!=type(None) else self.justify
      self['justify']=self.justify

   def setPadx(self, value=None):
      self.padx=value if type(value)!=type(None) else self.padx
      self['padx']=self.padx
   
   def setPady(self, value=None):
      self.pady=value if type(value)!=type(None) else self.pady
      self['pady']=self.pady
   
   def setRelief(self, value=None):
      self.relief=value if type(value)!=type(None) else self.relief
      self['relief']=self.relief
   
   def setText(self, value=None):
      self.text=value if type(value)!=type(None) else self.text
      self['text']=self.text
   
   def setWidth(self, value=None):
      self.width=value if type(value)!=type(None) else self.width
      self['width']=self.width
 
   def setAspect(self, value=None):
      self.aspect=value if type(value)!=type(None) else self.aspect
      self['aspect']=self.aspect

'''tk.Radiobutton(actbg, actfg, anc, bg, bd, bmp, compound, cur,
               fg, font, hgt, hbg, hfg, htckn, img, indicatoron, 
               just, offrelief, overrelief, padx, pady, rel, selectcolor,
               selectimage, txt, wdp, wraplength)'''

class Radiobutton2W(tk.Radiobutton):
   def __init__(self, master=None, *cnf, **kwargs):
      tk.Radiobutton.__init__(self, master, *cnf, **kwargs)
      self.type='radiobutton'
      self.config(text=getLang(self.type))
      self['font']=Font(family=pf.POLICE[0], size=11, weight='normal', slant='roman', underline=False, overstrike=False)
      self.activeBg=self['activebackground']
      self.activeFg=self['activeforeground']
      self.anchor=self['anchor']
      self.bg=self['bg']
      self.bd=self['bd']
      self.fg=self['fg']
      self.bitmap=self['bitmap'] #None, error, gray75, gray50, gray25, gray12, hourglass, info, questhead, question, warning
      self.compound=self['compound']   #top, bottom, left, right, center, none
      self.cursor=self['cursor']
      #Fontpart<
      self.font=pf.POLICE[0]
      self.size=11
      self.weight='normal'
      self.slant='roman'
      self.underline=False
      self.overstrike=False
      #Fontpart>
      self.height=self['height']
      self.highBg=self['highlightbackground']
      self.highFg=self['highlightcolor']
      self.highTn=self['highlightthickness']
      self.image=self['image']
      self.justify=self['justify']
      self.overrelief=self['overrelief']
      self.padx=self['padx']
      self.pady=self['pady']
      self.relief=self['relief'] #flat, raised, sunken, groove, ridge
      self.text=self['text']
      self.width=self['width']
      self.wraplength=self['wraplength']  #numerique
      self.indicatoron=self['indicatoron']
      self.offrelief=self['offrelief']
      self.selectimage=self['selectimage']
      self.selectcolor=self['selectcolor']
      self.varSelect=tk.IntVar(value=False)
      self.config(variable=self.varSelect, value=True)
      
   def getAll(self):
      return [self.type, self.activeBg, self.activeFg, self.anchor, self.bg, self.bd, self.fg, self.bitmap,
              self.compound, self.cursor, self.font, self.size, self.weight, self.slant, self.underline,
              self.overstrike, self.height, self.highBg, self.highFg, self.highTn, self.image, self.justify,
              self.overrelief, self.padx, self.pady, self.relief, self.text, self.width, self.wraplength,
              self.indicatoron, self.offrelief, self.selectimage, self.selectcolor]
   
   def setAll(self, all):
      self.setActiveBg(all[1])
      self.setActiveFg(all[2])
      self.setAnchor(all[3])
      self.setBg(all[4])
      self.setBd(all[5])
      self.setFg(all[6])
      self.setBitmap(all[7])
      self.setCompound(all[8])
      self.setCursor(all[9])
      self.setFont(all[10])
      self.setSize(all[11])
      self.setWeigth(all[12])
      self.setSlant(all[13])
      self.setUnderline(all[14])
      self.setOverstrike(all[15])
      self.setHeight(all[16])
      self.setHighBg(all[17])
      self.setHighFg(all[18])
      self.setHighTn(all[19])
      self.setImage(all[20])
      self.setJustify(all[21])
      self.setOverrelief(all[22])
      self.setPadx(all[23])
      self.setPady(all[24])
      self.setRelief(all[25])
      self.setText(all[26])
      self.setWidth(all[27])
      self.setWraplength(all[28])
      self.setIndicatoron(all[29])
      self.setOffrelief(all[30])
      self.setSelectimage(all[31])
      self.setSelectcolor(all[32])
  
   def setActiveBg(self, value=None):
      self.activeBg=value if type(value)!=type(None) else self.activeBg
      self['activebackground']=self.activeBg
   
   def setActiveFg(self, value=None):
      self.activeFg=value if type(value)!=type(None) else self.activeFg
      self['activeforeground']=self.activeFg

   def setAnchor(self, value):
      self.anchor=value if type(value)!=type(None) else self.anchor
      self['anchor']=self.anchor

   def setBg(self, value=None):
      self.bg=value if type(value)!=type(None) else self.bg
      self['bg']=self.bg
   
   def setFg(self, value=None):
      self.fg=value if type(value)!=type(None) else self.fg
      self['fg']=self.fg

   def setBd(self, value=None):
      self.bd=value if type(value)!=type(None) else self.bd
      self['bd']=self.bd
   
   def setBitmap(self, value=None):
      self.bitmap=value
      self['bitmap']=self.bitmap

   def setCompound(self, value=None):
      self.compound=value if type(value)!=type(None) else self.compound
      self['compound']=self.compound
   
   def setCursor(self, value=None):
      self.cursor=value if type(value)!=type(None) else self.cursor
      self['cursor']=self.cursor
   
   def setFont(self, value=None):
      self.font=value if type(value)!=type(None) else self.font
      self['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)

   def setSize(self, value=None):
      self.size=value if type(value)!=type(None) else self.size
      self['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)
   
   def setWeigth(self, value=None):
      self.weight=value if type(value)!=type(None) else self.weight
      self['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)
   
   def setSlant(self, value=None):
      self.slant=value if type(value)!=type(None) else self.slant
      self['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)
 
   def setUnderline(self, value=None):
      self.underline=value if type(value)!=type(None) else self.underline
      self['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)
   
   def setOverstrike(self, value=None):
      self.overstrike=value if type(value)!=type(None) else self.overstrike
      self['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)

   def setHeight(self, value=None):
      self.height=value if type(value)!=type(None) else self.height
      self['height']=self.height
   
   def setHighBg(self, value=None):
      self.highBg=value if type(value)!=type(None) else self.highBg
      self['highlightbackground']=self.highBg
   
   def setHighFg(self, value=None):
      self.highFg=value if type(value)!=type(None) else self.highFg
      self['highlightcolor']=self.highFg

   def setHighTn(self, value=None):
      self.highTn=value if type(value)!=type(None) else self.highTn
      self['highlightthickness']=self.highTn
   
   def setImage(self, value=None):
      self.image=value
      self['image']=self.image
   
   def setJustify(self, value=None):
      self.justify=value if type(value)!=type(None) else self.justify
      self['justify']=self.justify

   def setOverrelief(self, value=None):
      self.overrelief=value if type(value)!=type(None) else self.overrelief
      self['overrelief']=self.overrelief
   
   def setPadx(self, value=None):
      self.padx=value if type(value)!=type(None) else self.padx
      self['padx']=self.padx
   
   def setPady(self, value=None):
      self.pady=value if type(value)!=type(None) else self.pady
      self['pady']=self.pady
   
   def setRelief(self, value=None):
      self.relief=value if type(value)!=type(None) else self.relief
      self['relief']=self.relief
   
   def setText(self, value=None):
      self.text=value if type(value)!=type(None) else self.text
      self['text']=self.text
   
   def setWidth(self, value=None):
      self.width=value if type(value)!=type(None) else self.width
      self['width']=self.width
   
   def setWraplength(self, value=None):
      self.wraplength=value if type(value)!=type(None) else self.wraplength
      self['wraplength']=self.wraplength

   def setIndicatoron(self, value=None):
      self.indicatoron=value if type(value)!=type(None) else self.indicatoron
      self['indicatoron']=self.indicatoron
   
   def setOffrelief(self, value=None):
      self.offrelief=value if type(value)!=type(None) else self.offrelief
      self['offrelief']=self.offrelief
   
   def setSelectimage(self, value=None):
      self.selectimage=value
      self['selectimage']=self.selectimage

   def setSelectcolor(self, value=None):
      self.selectcolor=value
      self['selectcolor']=self.selectcolor

'''tk.Scale(actbg, actfg, bd, bg, cur, fg, font, from_, hbg, hfg,
         htckn, label, length, orient, rel, showvalue, sliderlength, 
         sliderrelief, to, troughcolor, wdt)'''

class Scale2W(tk.Scale):
   def __init__(self, master=None, *cnf, **kwargs):
      tk.Scale.__init__(self, master, *cnf, **kwargs)
      self.type='scale'
      self['font']=Font(family=pf.POLICE[0], size=11, weight='normal', slant='roman', underline=False, overstrike=False)
      self.activeBg=self['activebackground']
      self.bg=self['bg']
      self.bd=self['bd']
      self.fg=self['fg']
      self.cursor=self['cursor']
      #Fontpart<
      self.font=pf.POLICE[0]
      self.size=11
      self.weight='normal'
      self.slant='roman'
      self.underline=False
      self.overstrike=False
      #Fontpart>
      self.highBg=self['highlightbackground']
      self.highFg=self['highlightcolor']
      self.highTn=self['highlightthickness']
      self.relief=self['relief'] #flat, raised, sunken, groove, ridge
      self.width=self['width']
      self.from_=self['from']
      self.label=self['label']
      self.length=self['length']
      self.orient=self['orient']
      self.sliderlgt=self['sliderlength'], 
      self.sliderrelief=self['sliderrelief']
      self.to=self['to']
      self.troughcolor=self['troughcolor']
      self.showvalue=self['showvalue']
      
   def getAll(self):
      return [self.type, self.activeBg, self.bg, self.bd, self.fg,
              self.cursor, self.font, self.size, self.weight, self.slant, self.underline,
              self.overstrike, self.highBg, self.highFg, self.highTn,
              self.relief,self.width, self.from_, self.label, self.length, self.orient,
              self.sliderlgt, self.sliderrelief, self.to, self.troughcolor, self.showvalue]
   
   def setAll(self, all):
      self.setActiveBg(all[1])
      self.setBg(all[2])
      self.setBd(all[3])
      self.setFg(all[4])
      self.setCursor(all[5])
      self.setFont(all[6])
      self.setSize(all[7])
      self.setWeigth(all[8])
      self.setSlant(all[9])
      self.setUnderline(all[10])
      self.setOverstrike(all[11])
      self.setHighBg(all[12])
      self.setHighFg(all[13])
      self.setHighTn(all[14])
      self.setRelief(all[15])
      self.setWidth(all[16])
      self.setFrom(all[17])
      self.setLabel(all[18])
      self.setLength(all[19])
      self.setOrient(all[20])
      self.setSliderlength(all[21])
      self.setSliderrelief(all[22])
      self.setTo(all[23])
      self.setTroughcolor(all[24])
      self.setShowvalue(all[25])

   def setActiveBg(self, value=None):
      self.activeBg=value if type(value)!=type(None) else self.activeBg
      self['activebackground']=self.activeBg
   
   def setBg(self, value=None):
      self.bg=value if type(value)!=type(None) else self.bg
      self['bg']=self.bg
   
   def setFg(self, value=None):
      self.fg=value if type(value)!=type(None) else self.fg
      self['fg']=self.fg

   def setBd(self, value=None):
      self.bd=value if type(value)!=type(None) else self.bd
      self['bd']=self.bd

   def setCursor(self, value=None):
      self.cursor=value if type(value)!=type(None) else self.cursor
      self['cursor']=self.cursor
   
   def setFont(self, value=None):
      self.font=value if type(value)!=type(None) else self.font
      self['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)

   def setSize(self, value=None):
      self.size=value if type(value)!=type(None) else self.size
      self['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)
   
   def setWeigth(self, value=None):
      self.weight=value if type(value)!=type(None) else self.weight
      self['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)
   
   def setSlant(self, value=None):
      self.slant=value if type(value)!=type(None) else self.slant
      self['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)
   
   def setUnderline(self, value=None):
      self.underline=value if type(value)!=type(None) else self.underline
      self['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)
   
   def setOverstrike(self, value=None):
      self.overstrike=value if type(value)!=type(None) else self.overstrike
      self['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)

   def setHighBg(self, value=None):
      self.highBg=value if type(value)!=type(None) else self.highBg
      self['highlightbackground']=self.highBg
   
   def setHighFg(self, value=None):
      self.highFg=value if type(value)!=type(None) else self.highFg
      self['highlightcolor']=self.highFg

   def setHighTn(self, value=None):
      self.highTn=value if type(value)!=type(None) else self.highTn
      self['highlightthickness']=self.highTn
  
   def setRelief(self, value=None):
      self.relief=value if type(value)!=type(None) else self.relief
      self['relief']=self.relief
   
   def setLabel(self, value=None):
      self.label=value if type(value)!=type(None) else self.label
      self['label']=self.label
   
   def setWidth(self, value=None):
      self.width=value if type(value)!=type(None) else self.width
      self['width']=self.width
   
   def setLength(self, value=None):
      self.length=value if type(value)!=type(None) else self.length
      self['length']=self.length
   
   def setOrient(self, value=None):
      self.orient=value if type(value)!=type(None) else self.orient
      self['orient']=self.orient
   
   def setSliderlength(self, value=None):
      self.sliderlgt=value if type(value)!=type(None) else self.sliderlgt
      self['sliderlength']=self.sliderlgt
   
   def setSliderrelief(self, value=None):
      self.sliderrelief=value if type(value)!=type(None) else self.sliderrelief
      self['sliderrelief']=self.sliderrelief
   
   def setTo(self, value=None):
      self.to=value if type(value)!=type(None) else self.to
      self['to']=self.to
   
   def setFrom(self, value):
      self.from_=value if type(value)!=type(None) else self.from_
      self['from']=self.from_
   
   def setTroughcolor(self, value=None):
      self.troughcolor=value if type(value)!=type(None) else self.troughcolor
      self['troughcolor']=self.troughcolor
   
   def setShowvalue(self, value=None):
      self.showvalue=value if type(value)!=type(None) else self.showvalue
      self['showvalue']=self.showvalue

'''tk.Text(bg, bd, fg, cur, font, hgt, hbg, hfg, htckn, insertbackground, 
     insertborderwidth, insertwidth, padx, pady, rel, selectbg, 
     selectfg, selectwdt, wdt)'''

class Text2W(Text):
   def __init__(self, master=None, *cnf, **kwargs):
      Text.__init__(self, master, *cnf, **kwargs)
      self.type='text'
      self.insert(tk.END, getLang(self.type))
      self.config(width=25, height=10)
      self['font']=Font(family=pf.POLICE[0], size=11, weight='normal', slant='roman', underline=False, overstrike=False)
      self.bg=self['bg']
      self.bd=self['bd']
      self.fg=self['fg']
      self.cursor=self['cursor']
      #Fontpart<
      self.font=pf.POLICE[0]
      self.size=11
      self.weight='normal'
      self.slant='roman'
      self.underline=False
      self.overstrike=False
      #Fontpart>
      self.height=self['height']
      self.highBg=self['highlightbackground']
      self.highFg=self['highlightcolor']
      self.highTn=self['highlightthickness']
      self.relief=self['relief'] #flat, raised, sunken, groove, ridge
      self.width=self['width']
      self.insertBg=self['insertbackground']
      self.insertBdWidth=self['insertborderwidth']
      self.insertWidth=self['insertwidth']
      self.selectBg=self['selectbackground']
      self.selectBdwidth=self['selectborderwidth'] 
      self.selectFg=self['selectforeground']

   def getAll(self):
      return [self.type, self.bg, self.bd, self.fg, self.cursor, self.font, self.size,
              self.weight, self.slant, self.underline, self.overstrike, self.height, self.highBg,
              self.highFg, self.highTn, self.relief, self.width, 
              self.insertBg, self.insertBdWidth, self.insertWidth, self.selectBg, self.selectBdwidth,
              self.selectFg]
   
   def setAll(self, all):
      self.setBg(all[1])
      self.setBd(all[2])
      self.setFg(all[3])
      self.setCursor(all[4])
      self.setFont(all[5])
      self.setSize(all[6])
      self.setWeigth(all[7])
      self.setSlant(all[8])
      self.setUnderline(all[9])
      self.setOverstrike(all[10])
      self.setHeight(all[11])
      self.setHighBg(all[12])
      self.setHighFg(all[13])
      self.setHighTn(all[14])
      self.setRelief(all[15])
      self.setWidth(all[16])
      self.setInsertBg(all[17])
      self.setInsertBdWidth(all[18])
      self.setInsertWidth(all[19])
      self.setSelectBg(all[20])
      self.setSelectBdWidth(all[21])
      self.setSelectFg(all[22])
 
   def setBg(self, value=None):
      self.bg=value if type(value)!=type(None) else self.bg
      self['bg']=self.bg
   
   def setFg(self, value=None):
      self.fg=value if type(value)!=type(None) else self.fg
      self['fg']=self.fg

   def setBd(self, value=None):
      self.bd=value if type(value)!=type(None) else self.bd
      self['bd']=self.bd
   
   def setCursor(self, value=None):
      self.cursor=value if type(value)!=type(None) else self.cursor
      self['cursor']=self.cursor
   
   def setFont(self, value=None):
      self.font=value if type(value)!=type(None) else self.font
      self['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)

   def setSize(self, value=None):
      self.size=value if type(value)!=type(None) else self.size
      self['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)
   
   def setWeigth(self, value=None):
      self.weight=value if type(value)!=type(None) else self.weight
      self['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)
   
   def setSlant(self, value=None):
      self.slant=value if type(value)!=type(None) else self.slant
      self['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)
  
   def setUnderline(self, value=None):
      self.underline=value if type(value)!=type(None) else self.underline
      self['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)
   
   def setOverstrike(self, value=None):
      self.overstrike=value if type(value)!=type(None) else self.overstrike
      self['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)

   def setHeight(self, value=None):
      self.height=value if type(value)!=type(None) else self.height
      self['height']=self.height
   
   def setHighBg(self, value=None):
      self.highBg=value if type(value)!=type(None) else self.highBg
      self['highlightbackground']=self.highBg
   
   def setHighFg(self, value=None):
      self.highFg=value if type(value)!=type(None) else self.highFg
      self['highlightcolor']=self.highFg

   def setHighTn(self, value=None):
      self.highTn=value if type(value)!=type(None) else self.highTn
      self['highlightthickness']=self.highTn
 
   def setRelief(self, value=None):
      self.relief=value if type(value)!=type(None) else self.relief
      self['relief']=self.relief

   def setWidth(self, value=None):
      self.width=value if type(value)!=type(None) else self.width
      self['width']=self.width

   def setInsertBg(self, value=None):
      self.insertBg=value if type(value)!=type(None) else self.insertBg
      self['insertbackground']=self.insertBg
   
   def setInsertBdWidth(self, value=None):
      self.insertBdWidth=value if type(value)!=type(None) else self.insertBdWidth
      self['insertborderwidth']=self.insertBdWidth
   
   def setInsertWidth(self, value=None):
      self.insertWidth=value if type(value)!=type(None) else self.insertWidth
      self['insertwidth']=self.insertWidth
   
   def setSelectBg(self, value=None):
      self.selectBg=value if type(value)!=type(None) else self.selectBg
      self['selectbackground']=self.selectBg
   
   def setSelectBdWidth(self, value=None):
      self.selectBdwidth=value if type(value)!=type(None) else self.selectBdwidth
      self['selectborderwidth']=self.selectBdwidth
   
   def setSelectFg(self, value=None):
      self.selectFg=value if type(value)!=type(None) else self.selectFg
      self['selectforeground']=self.selectFg

'''ScrollableFrame(bg, bd, cur, hgt, hbg, hcol, htckn, rel, wdt)'''

class ScrollableFrame2W(ScrollableFrame):
   def __init__(self, master=None, *cnf, **kwargs):
      tk.Frame.__init__(self, master, *cnf, **kwargs)
      self.type='scrollableframe'
      self.config(width=100, height=100, bg='grey')
      self.bg=self['bg']
      self.bd=self['bd']
      self.cursor=self['cursor']
      self.height=self['height']
      self.highBg=self['highlightbackground']
      self.highFg=self['highlightcolor']
      self.highTn=self['highlightthickness']
      self.relief=self['relief'] #flat, raised, sunken, groove, ridge
      self.width=self['width']
  
   def setBg(self, value=None):
      self.bg=value if type(value)!=type(None) else self.bg
      self['bg']=self.bg

   def setBd(self, value=None):
      self.bd=value if type(value)!=type(None) else self.bd
      self['bd']=self.bd

   def setCursor(self, value=None):
      self.cursor=value if type(value)!=type(None) else self.cursor
      self['cursor']=self.cursor

   def setHeight(self, value=None):
      self.height=value if type(value)!=type(None) else self.height
      self['height']=self.height
   
   def setHighBg(self, value=None):
      self.highBg=value if type(value)!=type(None) else self.highBg
      self['highlightbackground']=self.highBg
   
   def setHighFg(self, value=None):
      self.highFg=value if type(value)!=type(None) else self.highFg
      self['highlightcolor']=self.highFg

   def setHighTn(self, value=None):
      self.highTn=value if type(value)!=type(None) else self.highTn
      self['highlightthickness']=self.highTn
 
   def setRelief(self, value=None):
      self.relief=value if type(value)!=type(None) else self.relief
      self['relief']=self.relief

   def setWidth(self, value=None):
      self.width=value if type(value)!=type(None) else self.width
      self['width']=self.width

'''tk.Spinbox(actbg, actfg, bd, bg, buttonbackground, buttoncursor, buttondownrelief, 
           buttonuprelief, cur, fg, font, from_, hbg, hfg, htckn, insertbg,
           insertbdwdt, insertwdt, just, rel, selectbg, selectfg, selectborderwidth, 
           to, wdt)'''

class Spinbox2W(tk.Spinbox):
   def __init__(self, master=None, *cnf, **kwargs):
      tk.Spinbox.__init__(self, master, *cnf, **kwargs)
      self.type='spinbox'
      self['font']=Font(family=pf.POLICE[0], size=11, weight='normal', slant='roman', underline=False, overstrike=False)
      self.bg=self['bg']
      self.bd=self['bd']
      self.fg=self['fg']
      self.cursor=self['cursor']
      #Fontpart<
      self.font=pf.POLICE[0]
      self.size=11
      self.weight='normal'
      self.slant='roman'
      self.underline=False
      self.overstrike=False
      #Fontpart>
      self.highBg=self['highlightbackground']
      self.highFg=self['highlightcolor']
      self.highTn=self['highlightthickness']
      self.justify=self['justify']
      self.relief=self['relief'] #flat, raised, sunken, groove, ridge
      self.width=self['width']
      self.insertBg=self['insertbackground']
      self.insertBdWidth=self['insertborderwidth']
      self.insertWidth=self['insertwidth']
      self.selectBg=self['selectbackground']
      self.selectBdwidth=self['selectborderwidth'] 
      self.selectFg=self['selectforeground']
      self.buttonBg=self['buttonbackground']
      self.buttonCur=self['buttoncursor']
      self.buttonDrel=self['buttondownrelief'] 
      self.buttonUrel=self['buttonuprelief']
      self.from_=self['from']
      self.to=self['to']

   def getAll(self):
      return [self.type, self.bg, self.bd, self.fg, self.cursor, self.font, self.size,
              self.weight, self.slant, self.underline, self.overstrike, self.highBg,
              self.highFg, self.highTn, self.justify, self.relief, self.width, 
              self.insertBg, self.insertBdWidth, self.insertWidth, self.selectBg, self.selectBdwidth,
              self.selectFg, self.buttonBg, self.buttonCur, self.buttonDrel, self.buttonUrel,
              self.from_, self.to]
   
   def setAll(self, all):
      self.setBg(all[1])
      self.setBd(all[2])
      self.setFg(all[3])
      self.setCursor(all[4])
      self.setFont(all[5])
      self.setSize(all[6])
      self.setWeigth(all[7])
      self.setSlant(all[8])
      self.setUnderline(all[9])
      self.setOverstrike(all[10])
      self.setHighBg(all[11])
      self.setHighFg(all[12])
      self.setHighTn(all[13])
      self.setJustify(all[14])
      self.setRelief(all[15])
      self.setWidth(all[16])
      self.setInsertBg(all[17])
      self.setInsertBdWidth(all[18])
      self.setInsertWidth(all[19])
      self.setSelectBg(all[20])
      self.setSelectBdWidth(all[21])
      self.setSelectFg(all[22])
      self.setButtonBg(all[23])
      self.setButtonCursor(all[24])
      self.setButtonDrel(all[25])
      self.setButtonUrel(all[26])
      self.setFrom(all[27])
      self.setTo(all[28])
 
   def setBg(self, value=None):
      self.bg=value if type(value)!=type(None) else self.bg
      self['bg']=self.bg
   
   def setFg(self, value=None):
      self.fg=value if type(value)!=type(None) else self.fg
      self['fg']=self.fg

   def setBd(self, value=None):
      self.bd=value if type(value)!=type(None) else self.bd
      self['bd']=self.bd
   
   def setCursor(self, value=None):
      self.cursor=value if type(value)!=type(None) else self.cursor
      self['cursor']=self.cursor
   
   def setFont(self, value=None):
      self.font=value if type(value)!=type(None) else self.font
      self['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)

   def setSize(self, value=None):
      self.size=value if type(value)!=type(None) else self.size
      self['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)
   
   def setWeigth(self, value=None):
      self.weight=value if type(value)!=type(None) else self.weight
      self['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)
   
   def setSlant(self, value=None):
      self.slant=value if type(value)!=type(None) else self.slant
      self['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)
   
   def setUnderline(self, value=None):
      self.underline=value if type(value)!=type(None) else self.underline
      self['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)
   
   def setOverstrike(self, value=None):
      self.overstrike=value if type(value)!=type(None) else self.overstrike
      self['font']=Font(family=self.font, size=self.size, weight=self.weight, 
                        slant=self.slant, underline=self.underline, overstrike=self.overstrike)

   def setHighBg(self, value=None):
      self.highBg=value if type(value)!=type(None) else self.highBg
      self['highlightbackground']=self.highBg
   
   def setHighFg(self, value=None):
      self.highFg=value if type(value)!=type(None) else self.highFg
      self['highlightcolor']=self.highFg

   def setHighTn(self, value=None):
      self.highTn=value if type(value)!=type(None) else self.highTn
      self['highlightthickness']=self.highTn
 
   def setJustify(self, value=None):
      self.justify=value if type(value)!=type(None) else self.justify
      self['justify']=self.justify

   def setRelief(self, value=None):
      self.relief=value if type(value)!=type(None) else self.relief
      self['relief']=self.relief

   def setWidth(self, value=None):
      self.width=value if type(value)!=type(None) else self.width
      self['width']=self.width

   def setInsertBg(self, value=None):
      self.insertBg=value if type(value)!=type(None) else self.insertBg
      self['insertbackground']=self.insertBg
   
   def setInsertBdWidth(self, value=None):
      self.insertBdWidth=value if type(value)!=type(None) else self.insertBdWidth
      self['insertborderwidth']=self.insertBdWidth
   
   def setInsertWidth(self, value=None):
      self.insertWidth=value if type(value)!=type(None) else self.insertWidth
      self['insertwidth']=self.insertWidth
   
   def setSelectBg(self, value=None):
      self.selectBg=value if type(value)!=type(None) else self.selectBg
      self['selectbackground']=self.selectBg
   
   def setSelectBdWidth(self, value=None):
      self.selectBdwidth=value if type(value)!=type(None) else self.selectBdwidth
      self['selectborderwidth']=self.selectBdwidth
   
   def setSelectFg(self, value=None):
      self.selectFg=value if type(value)!=type(None) else self.selectFg
      self['selectforeground']=self.selectFg
   
   def setButtonBg(self, value=None):
      self.buttonBg=value if type(value)!=type(None) else self.buttonBg
      self['buttonbackground']=self.buttonBg
   
   def setButtonCursor(self, value=None):
      self.buttonCur=value if type(value)!=type(None) else self.buttonCur
      self['buttoncursor']=self.buttonCur
   
   def setButtonDrel(self, value=None):
      self.buttonDrel=value if type(value)!=type(None) else self.buttonDrel
      self['buttondownrelief']=self.buttonDrel
   
   def setButtonUrel(self, value=None):
      self.buttonUrel=value if type(value)!=type(None) else self.buttonUrel
      self['buttonuprelief']=self.buttonUrel
   
   def setFrom(self, value=None):
      self.from_=value if type(value)!=type(None) else self.from_
      self['from']=self.from_
   
   def setTo(self, value=None):
      self.to=value if type(value)!=type(None) else self.to
      self['to']=self.to



listOfWidget={'Button': Button2W, 
   'Checkbutton': Checkbutton2W, 
   'Entry': Entry2W, 
   'Frame': Frame2W,
   'Label': Label2W,
   'LabelFrame': LabelFrame2W,
   'Listbox': Listbox2W,
   'Menubutton': Menubutton2W,
   'Message': Message2W,
   'Radiobutton': Radiobutton2W,
   'Scale': Scale2W, 
   'ScrolledText':Text2W, 
   'ScrollableFrame': ScrollableFrame2W, 
   'Spinbox': Spinbox2W
}
['activebackground', 'activeforeground', 'anchor', 'aspect',
   'bd', 'bg', 'bitmap', 'border', 'buttonbackground', 'buttoncursor', 
   'buttondownrelief', 'buttonuprelief', 'compound', 'cursor', 'direction', 
   'offrelief', 'font', 'from_', 'height', 'highlightbackground', 'highlightcolor', 
   'highlightthickness', 'image', 'indicatoron', 'insertbackground', 'insertborderwidth', 
   'insertwidth', 'justify', 'label', 'labelanchor', 'length', 'orient', 'overrelief', 
   'padx', 'pady', 'relief', 'selectbackground', 'selectborderwidth',
   'selectcolor', 'selectforeground', 'selectimage', 'show', 'showvalue', 
   'sliderlength', 'sliderrelief', 'text', 'to', 'troughcolor', 'width', 'wraplength']