import pyfunct as pf
from tkinter.font import Font
import math
from PIL import ImageTk, Image
import os
import option2W as opt2W
import object2W as obj2W



def getRotation(x, y, angle, a, b):
    ang = float(-angle) * 2 * math.pi / 360
    rotated = []
    for i in range(len(x)):
        rx = x[i] - a
        ry = y[i] - b
        fx = a + rx * math.cos(ang) - ry * math.sin(ang)
        fy = b + rx * math.sin(ang) + ry * math.cos(ang)
        rotated.extend([fx, fy])
    return rotated

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
        self.temp =os.path.join('temps', 'temps%s.%s'%(str(time.an())+str(time.mois())+str(time.jour())+str(time.heure())+str(time.minute())+str(time.seconde())+str(time.micros())+'yog', self.from_format))
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

class Line(object):
    def __init__(self, master, x, y):
        self.type='line'
        self.master=master
        self.x=x
        self.y=y
        self.pointx=min(self.x)+(max(self.x)-min(self.x))/2
        self.pointy=min(self.y)+(max(self.y)-min(self.y))/2
        self.coords=list()
        for ww in range(len(self.x)):
            self.coords.append(self.x[ww])
            self.coords.append(self.y[ww])
        self.object=self.master.create_line(self.coords)
        self.fragCoords=list()
        for ww in range(0, len(self.coords), 2):
            a=[]
            a.append(self.coords[ww])
            a.append(self.coords[ww+1])
            self.fragCoords.append(a)
        self.width=1
        self.activeWidth=1
        self.disabledWidth=1
        self.fill='black'
        self.activeFill='black'
        self.disabledFill='black'
        self.dash=()
        self.dashOffset=0
        self.arrow='none'   #first, last, both
        self.arrowShap=(8, 10, 3)
        self.capStyle='butt'   #butt, round, projecting
        self.joinStyle='miter'  #round, bevel, miter
        self.smooth=False
        self.splineSteps=12
        self.stipple=''
        self.tag=''
        self.stat='normal'  #normal, disabled, hidden
        self.angle=0
        self.name=''
    
    def getAll(self):
        return [self.type, self.x, self.y, self.width, self.activeWidth, self.disabledWidth,
           self.fill, self.activeFill, self.disabledFill, self.dash, self.dashOffset, self.arrow,
           self.arrowShap, self.capStyle, self.joinStyle, self.smooth, self.splineSteps,
           self.stipple, self.tag, self.stat, self.angle, self.name]
    
    def setAll(self, all):
        self.setCoords(all[1], all[2])
        self.setWidth(all[3])
        self.setActiveWidth(all[4])
        self.setDisabledWidth(all[5])
        self.setFill(all[6])
        self.setActiveFill(all[7])
        self.setDisabledFill(all[8])
        self.setDash(all[9])
        self.setDashOffset(all[10])
        self.setArrow(all[11])
        self.setArrowShap(all[12])
        self.setCapStyle(all[13])
        self.setJoinStyle(all[14])
        self.setSmooth(all[15])
        self.setSplineSteps(all[16])
        self.setStipple(all[17])
        self.setTag(all[18])
        self.setStat(all[19])
        self.rotate(all[20])
        self.setName(all[21])
    
    def setName(self, name=None):
        self.name=name if name else self.name
    
    def setStat(self, stat='normal'):
        self.stat=stat
        self.master.itemconfig(self.object, stat=self.stat)
    
    def setCoords(self, x, y):
        self.x=x
        self.y=y
        self.coords=list()
        for ww in range(len(self.x)):
            self.coords.append(self.x[ww])
            self.coords.append(self.y[ww])
        self.fragCoords=list()
        for ww in range(0, len(self.coords), 2):
            a=[]
            a.append(self.coords[ww])
            a.append(self.coords[ww+1])
            self.fragCoords.append(a)
        self.pointx=min(self.x)+(max(self.x)-min(self.x))/2
        self.pointy=min(self.y)+(max(self.y)-min(self.y))/2
        self.master.coords(self.object, self.coords)
    
    def moveTo(self, x, y):
        a, b=x-self.pointx, y-self.pointy
        self.master.move(self.object, a, b)
        for ww in range(0, len(self.coords), 2):
            self.coords[ww]+=a
            self.coords[ww+1]+=b
        for ww in self.fragCoords:
            ww[0]+=a
            ww[1]+=b
            self.x[self.fragCoords.index(ww)]+=a
            self.y[self.fragCoords.index(ww)]+=b
        self.pointx=min(self.x)+(max(self.x)-min(self.x))/2
        self.pointy=min(self.y)+(max(self.y)-min(self.y))/2
    
    def setPoint(self, x, y):
        a=x-(max(self.x)-min(self.x))/2
        b=y-(max(self.y)-min(self.y))/2
        self.moveTo(a,b)
    
    def horizontal(self, x):
        self.moveTo(self.pointx+x, self.pointy)
    
    def vertical(self, y):
        self.moveTo(self.pointx, self.pointy+y)
    
    def rotate(self, angle):
        coords=getRotation(self.x, self.y, angle, self.pointx, self.pointy)
        self.coords=coords
        x, y=list(), list()
        for ww in range(0, len(coords), 2):
            x.append(coords[ww])
            y.append(coords[ww+1])
        self.fragCoords=list()
        for ww in range(0, len(self.coords), 2):
            a=[]
            a.append(self.coords[ww])
            a.append(self.coords[ww+1])
            self.fragCoords.append(a)
        self.angle=angle
        self.master.coords(self.object, self.coords)
    
    def resize(self, x, y):
        x=x/2
        y=y/2
        rx=min(self.x)+(max(self.x)-min(self.x))/2
        ry=min(self.y)+(max(self.y)-min(self.y))/2
        for ww in range(0, len(self.coords), 2):
            if self.coords[ww]>=rx:
                self.coords[ww]+=x
            else:
                self.coords[ww]-=x
            if self.coords[ww+1]>=ry:
                self.coords[ww+1]+=y
            else:
                self.coords[ww+1]-=y
        self.fragCoords=list()
        self.x, self.y=list(), list()
        for ww in range(0, len(self.coords), 2):
            a=[]
            a.append(self.coords[ww])
            a.append(self.coords[ww+1])
            self.fragCoords.append(a)
            self.x.append(self.coords[ww])
            self.y.append(self.coords[ww+1])
        self.pointx=(max(self.x)-min(self.x))/2
        self.pointy=(max(self.y)-min(self.y))/2
        self.master.coords(self.object, self.coords)
    
    def setWidth(self, width=None):
        'width = Int'
        self.width=width if width else self.width
        self.master.itemconfig(self.object, width=self.width)
    
    def setActiveWidth(self, activeWidth=None):
        'activeWidth = Int'
        self.activeWidth=activeWidth if activeWidth else self.activeWidth
        self.master.itemconfig(self.object, activewidth=self.activeWidth)
    
    def  setDisabledWidth(self, disabledWidth=None):
        'disabledWidth = Int'
        self.disabledWidth=disabledWidth if disabledWidth else self.disabledWidth
        self.master.itemconfig(self.object, disabledwidth=self.disabledWidth)
    
    def setFill(self, fill=None):
        'fill = Str'
        self.fill=fill if fill else self.fill
        self.master.itemconfig(self.object, fill=self.fill)
    
    def setActiveFill(self, activeFill=None):
        'activeFill = Str'
        self.activeFill=activeFill if activeFill else None
        self.master.itemconfig(self.object, activefill=self.activeFill)
    
    def setDisabledFill(self, disabledFill=None):
        'disabledFill = Str'
        self.disabledFill=disabledFill if disabledFill else self.disabledFill
        self.master.itemconfig(self.object, disabledfill=self.disabledFill)
    
    def setDash(self, dash=None):
        'dash = (Int, Int, Int)'
        self.dash=dash if type(dash)!=type(None) else self.dash
        self.master.itemconfig(self.object, dash=self.dash)
    
    def setDashOffset(self, dashoffset=None):
        'dahsOffset = Int'
        self.dashOffset=dashoffset if dashoffset else self.dashOffset
        self.master.itemconfig(self.object, dashoffset=self.dashOffset)
    
    def setArrow(self, arrow=None):
        'arrow = Str'
        self.arrow=arrow
        self.master.itemconfig(self.object, arrow=self.arrow)
    
    def setArrowShap(self, arrowShap):
        'arrowShap = (Int, Int, Int)'
        self.arrowShap=arrowShap if arrowShap else self.arrowShap
        self.master.itemconfig(self.object, arrowshap=self.arrowShap)
    
    def setCapStyle(self, capStyle=None):
        'cappSTyle = Str'
        self.capStyle=capStyle if capStyle else self.capStyle
        self.master.itemconfig(self.object, capstyle=self.capStyle)
    
    def setJoinStyle(self, joinStyle=None):
        'joinStyle = Str'
        self.joinStyle=joinStyle if joinStyle else self.joinStyle
        self.master.itemconfig(self.object, joinstyle=self.joinStyle)
    
    def setSmooth(self, smooth=None):
        'smooth = Bool'
        self.smooth=smooth if type(smooth)!=type(None) else self.smooth
        self.master.itemconfig(self.object, smooth=self.smooth)
    
    def setSplineSteps(self, splineSteps=12):
        'splinStep = Int'
        self.splineSteps=splineSteps if splineSteps else self.splineSteps
        self.master.itemconfig(self.object, splinesteps=self.splineSteps)
    
    def setStipple(self, stipple = None):
        'stipple = Str'
        self.stipple=stipple
        self.master.itemconfig(self.object, stipple=self.stipple)

    def setTag(self, tag=None):
        'tag = Str'
        self.tag=tag if tag else self.tag

    def fragmentCoords(self, fragement):
        self.fragCoords=fragement
        self.x=list()
        self.y=list()
        self.coords=list()
        for ww in self.fragCoords:
            self.coords.extend(ww)
            self.x.append(ww[0])
            self.y.append(ww[1])
        self.pointx=(max(self.x)-min(self.x))/2
        self.pointy=(max(self.y)-min(self.y))/2
        self.master.coords(self.object, self.coords)

    def destroy(self):
        self.master.delete(self.object)

class Polygon(object):
    def __init__(self, master, x, y):
        self.type='polygon'
        self.master=master
        self.x=x
        self.y=y
        self.pointx=min(self.x)+(max(self.x)-min(self.x))/2
        self.pointy=min(self.y)+(max(self.y)-min(self.y))/2
        self.coords=list()
        for ww in range(len(self.x)):
            self.coords.append(self.x[ww])
            self.coords.append(self.y[ww])
        self.object=self.master.create_polygon(self.coords, fill='', width=1, outline='black')
        self.fragCoords=list()
        for ww in range(0, len(self.coords), 2):
            a=[]
            a.append(self.coords[ww])
            a.append(self.coords[ww+1])
            self.fragCoords.append(a)
        self.width=1
        self.activeWidth=1
        self.disabledWidth=1
        self.fill=''
        self.activeFill=''
        self.disabledFill=''
        self.outline='black'
        self.disabledOutline='black'
        self.dash=()
        self.dashOffset=0
        self.smooth=False
        self.splineSteps=12
        self.stipple=''
        self.tag=''
        self.stat='normal'  #normal, disabled, hidden
        self.angle=0
        self.name=''
    
    def getAll(self):
        return [self.type, self.x, self.y, self.width, self.activeWidth, self.disabledWidth, self.fill,
           self.activeFill, self.disabledFill, self.outline, self.disabledOutline, self.dash, self.dashOffset,
           self.smooth, self.splineSteps, self.stipple, self.tag, self.stat, self.angle, self.name]
    
    def setAll(self, all):
        self.setCoords(all[1], all[2])
        self.setWidth(all[3])
        self.setActiveWidth(all[4])
        self.setDisabledWidth(all[5])
        self.setFill(all[6])
        self.setActiveFill(all[7])
        self.setDisabledFill(all[8])
        self.setOutline(all[9])
        self.setDisabledOutline(all[10])
        self.setDash(all[11])
        self.setDashOffset(all[12])
        self.setSmooth(all[13])
        self.setSplineSteps(all[14])
        self.setStipple(all[15])
        self.setTag(all[16])
        self.setStat(all[17])
        self.rotate(all[18])
        self.setName(all[19])
    
    def setName(self, name=None):
        self.name=name if name else self.name
    
    def setStat(self, stat='normal'):
        self.stat=stat
        self.master.itemconfig(self.object, stat=self.stat)
    
    def setCoords(self, x, y):
        self.x=x
        self.y=y
        self.coords=list()
        for ww in range(len(self.x)):
            self.coords.append(self.x[ww])
            self.coords.append(self.y[ww])
        self.fragCoords=list()
        for ww in range(0, len(self.coords), 2):
            a=[]
            a.append(self.coords[ww])
            a.append(self.coords[ww+1])
            self.fragCoords.append(a)
        self.pointx=min(self.x)+(max(self.x)-min(self.x))/2
        self.pointy=min(self.y)+(max(self.y)-min(self.y))/2
        self.master.coords(self.object, self.coords)
    
    def moveTo(self, x, y):
        a, b=x-self.pointx, y-self.pointy
        self.master.move(self.object, a, b)
        for ww in range(0, len(self.coords), 2):
            self.coords[ww]+=a
            self.coords[ww+1]+=b
        for ww in self.fragCoords:
            ww[0]+=a
            ww[1]+=b
            self.x[self.fragCoords.index(ww)]+=a
            self.y[self.fragCoords.index(ww)]+=b
        self.pointx=min(self.x)+(max(self.x)-min(self.x))/2
        self.pointy=min(self.y)+(max(self.y)-min(self.y))/2
    
    def setPoint(self, x, y):
        a=x-(max(self.x)-min(self.x))/2
        b=y-(max(self.y)-min(self.y))/2
        self.moveTo(a,b)
    
    def horizontal(self, x):
        self.moveTo(self.pointx+x, self.pointy)
    
    def vertical(self, y):
        self.moveTo(self.pointx, self.pointy+y)
    
    def rotate(self, angle):
        coords=getRotation(self.x, self.y, angle, self.pointx, self.pointy)
        self.coords=coords
        x, y=list(), list()
        for ww in range(0, len(coords), 2):
            x.append(coords[ww])
            y.append(coords[ww+1])
        self.fragCoords=list()
        for ww in range(0, len(self.coords), 2):
            a=[]
            a.append(self.coords[ww])
            a.append(self.coords[ww+1])
            self.fragCoords.append(a)
        self.angle=angle
        self.master.coords(self.object, self.coords)
    
    def resize(self, x, y):
        x=x/2
        y=y/2
        rx=min(self.x)+(max(self.x)-min(self.x))/2
        ry=min(self.y)+(max(self.y)-min(self.y))/2
        for ww in range(0, len(self.coords), 2):
            if self.coords[ww]>=rx:
                self.coords[ww]+=x
            else:
                self.coords[ww]-=x
            if self.coords[ww+1]>=ry:
                self.coords[ww+1]+=y
            else:
                self.coords[ww+1]-=y
        self.fragCoords=list()
        self.x, self.y=list(), list()
        for ww in range(0, len(self.coords), 2):
            a=[]
            a.append(self.coords[ww])
            a.append(self.coords[ww+1])
            self.fragCoords.append(a)
            self.x.append(self.coords[ww])
            self.y.append(self.coords[ww+1])
        self.pointx=(max(self.x)-min(self.x))/2
        self.pointy=(max(self.y)-min(self.y))/2
        self.master.coords(self.object, self.coords)
    
    def setWidth(self, width=None):
        'width = Int'
        self.width=width if width else self.width
        self.master.itemconfig(self.object, width=self.width)
    
    def setActiveWidth(self, activeWidth=None):
        'activeWidth = Int'
        self.activeWidth=activeWidth if activeWidth else self.activeWidth
        self.master.itemconfig(self.object, activewidth=self.activeWidth)
    
    def  setDisabledWidth(self, disabledWidth=None):
        'disabledWidth = Int'
        self.disabledWidth=disabledWidth if disabledWidth else self.disabledWidth
        self.master.itemconfig(self.object, disabledwidth=self.disabledWidth)
    
    def setFill(self, fill=None):
        'fill = Str'
        self.fill=fill if type(fill)!=type(None) else self.fill
        self.master.itemconfig(self.object, fill=self.fill)
    
    def setActiveFill(self, activeFill=None):
        'activeFill = Str'
        self.activeFill=activeFill if activeFill else None
        self.master.itemconfig(self.object, activefill=self.activeFill)
    
    def setDisabledFill(self, disabledFill=None):
        'disabledFill = Str'
        self.disabledFill=disabledFill if disabledFill else self.disabledFill
        self.master.itemconfig(self.object, disabledfill=self.disabledFill)
    
    def setOutline(self, outline=None):
        'outline = Str'
        self.outline=outline if outline else self.outline
        self.master.itemconfig(self.object, outline=self.outline)
    
    def setDisabledOutline(self, disabledOutline=None):
        'disabledOutline = Str'
        self.disabledOutline=disabledOutline if disabledOutline else self.disabledOutline
        self.master.itemconfig(self.object, disabledoutline=self.disabledOutline)
    
    def setDash(self, dash=None):
        'dash = (Int, Int)'
        self.dash=dash if type(dash)!=type(None) else self.dash
        self.master.itemconfig(self.object, dash=self.dash)
    
    def setDashOffset(self, dashoffset=None):
        'dahsOffset = Int'
        self.dashOffset=dashoffset if dashoffset else self.dashOffset
        self.master.itemconfig(self.object, dashoffset=self.dashOffset)
    
    def setCapStyle(self, capStyle=None):
        'cappSTyle = Str'
        self.capStyle=capStyle if capStyle else self.capStyle
        self.master.itemconfig(self.object, capstyle=self.capStyle)
    
    def setJoinStyle(self, joinStyle=None):
        'joinStyle = Str'
        self.joinStyle=joinStyle if joinStyle else self.joinStyle
        self.master.itemconfig(self.object, joinstyle=self.joinStyle)
    
    def setSmooth(self, smooth=None):
        'smooth = Bool'
        self.smooth=smooth if type(smooth)!=type(None) else self.smooth
        self.master.itemconfig(self.object, smooth=self.smooth)
    
    def setSplineSteps(self, splineSteps=12):
        'splinStep = Int'
        self.splineSteps=splineSteps if splineSteps else self.splineSteps
        self.master.itemconfig(self.object, splinesteps=self.splineSteps)
    
    def setStipple(self, stipple = None):
        'stipple = Str'
        self.stipple=stipple
        self.master.itemconfig(self.object, stipple=self.stipple)

    def setTag(self, tag=None):
        'tag = Str'
        self.tag=tag if tag else self.tag

    def fragmentCoords(self, fragement):
        self.fragCoords=fragement
        self.x=list()
        self.y=list()
        self.coords=list()
        for ww in self.fragCoords:
            self.coords.extend(ww)
            self.x.append(ww[0])
            self.y.append(ww[1])
        self.pointx=(max(self.x)-min(self.x))/2
        self.pointy=(max(self.y)-min(self.y))/2
        self.master.coords(self.object, self.coords)

    def destroy(self):
        self.master.delete(self.object)

class Oval(object):
    def __init__(self, master, x, y):
        self.type='oval'
        self.master=master
        self.x=x
        self.y=y
        self.pointx=min(self.x)+(max(self.x)-min(self.x))//2
        self.pointy=min(self.y)+(max(self.y)-min(self.y))//2
        self.coords=list()
        for ww in range(len(self.x)):
            self.coords.append(self.x[ww])
            self.coords.append(self.y[ww])
        self.object=self.master.create_oval(self.coords, fill='', width=1, outline='black')
        self.fragCoords=list()
        for ww in range(0, len(self.coords), 2):
            a=[]
            a.append(self.coords[ww])
            a.append(self.coords[ww+1])
            self.fragCoords.append(a)
        self.width=1
        self.activeWidth=1
        self.disabledWidth=1
        self.fill=''
        self.activeFill=''
        self.disabledFill=''
        self.outline='black'
        self.disabledOutline='black'
        self.dash=()
        self.dashOffset=0
        self.stipple=''
        self.tag=''
        self.stat='normal'  #normal, disabled, hidden
        self.angle=0
        self.name=''
    
    def getAll(self):
        return [self.type, self.x, self.y, self.width, self.activeWidth, self.disabledWidth, self.fill,
           self.activeFill, self.disabledFill, self.outline, self.disabledOutline, self.dash,
           self.dashOffset, self.stipple, self.tag, self.stat, self.angle, self.name]
    
    def setAll(self, all):
        self.setCoords(all[1], all[2])
        self.setWidth(all[3])
        self.setActiveWidth(all[4])
        self.setDisabledWidth(all[5])
        self.setFill(all[6])
        self.setActiveFill(all[7])
        self.setDisabledFill(all[8])
        self.setOutline(all[9])
        self.setDisabledOutline(all[10])
        self.setDash(all[11])
        self.setDashOffset(all[12])
        self.setStipple(all[13])
        self.setTag(all[14])
        self.setStat(all[15])
        self.rotate(all[16])
        self.setName(all[17])
    
    def setName(self, name=None):
        self.name=name if name else self.name
    
    def setStat(self, stat='normal'):
        self.stat=stat
        self.master.itemconfig(self.object, stat=self.stat)
    
    def setCoords(self, x, y):
        self.x=x
        self.y=y
        self.coords=list()
        for ww in range(len(self.x)):
            self.coords.append(self.x[ww])
            self.coords.append(self.y[ww])
        self.fragCoords=list()
        for ww in range(0, len(self.coords), 2):
            a=[]
            a.append(self.coords[ww])
            a.append(self.coords[ww+1])
            self.fragCoords.append(a)
        self.pointx=min(self.x)+(max(self.x)-min(self.x))//2
        self.pointy=min(self.y)+(max(self.y)-min(self.y))//2
        self.master.coords(self.object, self.coords)
    
    def moveTo(self, x, y):
        a, b=x-self.pointx, y-self.pointy
        self.master.move(self.object, a, b)
        for ww in range(0, len(self.coords), 2):
            self.coords[ww]+=a
            self.coords[ww+1]+=b
        for ww in self.fragCoords:
            ww[0]+=a
            ww[1]+=b
            self.x[self.fragCoords.index(ww)]+=a
            self.y[self.fragCoords.index(ww)]+=b
        self.pointx=min(self.x)+(max(self.x)-min(self.x))/2
        self.pointy=min(self.y)+(max(self.y)-min(self.y))/2
    
    def setPoint(self, x, y):
        a=x-(max(self.x)-min(self.x))/2
        b=y-(max(self.y)-min(self.y))/2
        self.moveTo(a,b)
    
    def horizontal(self, x):
        self.moveTo(self.pointx+x, self.pointy)
    
    def vertical(self, y):
        self.moveTo(self.pointx, self.pointy+y)
    
    def rotate(self, angle):
        coords=getRotation(self.x, self.y, angle, self.pointx, self.pointy)
        self.coords=coords
        x, y=list(), list()
        for ww in range(0, len(coords), 2):
            x.append(coords[ww])
            y.append(coords[ww+1])
        self.fragCoords=list()
        for ww in range(0, len(self.coords), 2):
            a=[]
            a.append(self.coords[ww])
            a.append(self.coords[ww+1])
            self.fragCoords.append(a)
        self.angle=angle
        self.master.coords(self.object, self.coords)
    
    def resize(self, x, y):
        x=x/2
        y=y/2
        rx=min(self.x)+(max(self.x)-min(self.x))/2
        ry=min(self.y)+(max(self.y)-min(self.y))/2
        for ww in range(0, len(self.coords), 2):
            if self.coords[ww]>=rx:
                self.coords[ww]+=x
            else:
                self.coords[ww]-=x
            if self.coords[ww+1]>=ry:
                self.coords[ww+1]+=y
            else:
                self.coords[ww+1]-=y
        self.fragCoords=list()
        self.x, self.y=list(), list()
        for ww in range(0, len(self.coords), 2):
            a=[]
            a.append(self.coords[ww])
            a.append(self.coords[ww+1])
            self.fragCoords.append(a)
            self.x.append(self.coords[ww])
            self.y.append(self.coords[ww+1])
        self.pointx=(max(self.x)-min(self.x))/2
        self.pointy=(max(self.y)-min(self.y))/2
        self.master.coords(self.object, self.coords)
    
    def setWidth(self, width=None):
        'width = Int'
        self.width=width if width else self.width
        self.master.itemconfig(self.object, width=self.width)
    
    def setActiveWidth(self, activeWidth=None):
        'activeWidth = Int'
        self.activeWidth=activeWidth if activeWidth else self.activeWidth
        self.master.itemconfig(self.object, activewidth=self.activeWidth)
    
    def  setDisabledWidth(self, disabledWidth=None):
        'disabledWidth = Int'
        self.disabledWidth=disabledWidth if disabledWidth else self.disabledWidth
        self.master.itemconfig(self.object, disabledwidth=self.disabledWidth)
    
    def setFill(self, fill=None):
        'fill = Str'
        self.fill=fill if type(fill)!=type(None) else self.fill
        self.master.itemconfig(self.object, fill=self.fill)
    
    def setActiveFill(self, activeFill=None):
        'activeFill = Str'
        self.activeFill=activeFill if activeFill else None
        self.master.itemconfig(self.object, activefill=self.activeFill)
    
    def setDisabledFill(self, disabledFill=None):
        'disabledFill = Str'
        self.disabledFill=disabledFill if disabledFill else self.disabledFill
        self.master.itemconfig(self.object, disabledfill=self.disabledFill)
    
    def setOutline(self, outline=None):
        'outline = Str'
        self.outline=outline if outline else self.outline
        self.master.itemconfig(self.object, outline=self.outline)
    
    def setDisabledOutline(self, disabledOutline=None):
        'disabledOutline = Str'
        self.disabledOutline=disabledOutline if disabledOutline else self.disabledOutline
        self.master.itemconfig(self.object, disabledoutline=self.disabledOutline)
    
    def setDash(self, dash=None):
        'dash = (Int, Int)'
        self.dash=dash if type(dash)!=type(None) else self.dash
        self.master.itemconfig(self.object, dash=self.dash)
    
    def setDashOffset(self, dashoffset=None):
        'dahsOffset = Int'
        self.dashOffset=dashoffset if dashoffset else self.dashOffset
        self.master.itemconfig(self.object, dashoffset=self.dashOffset)
    
    def setStipple(self, stipple = None):
        'stipple = Str'
        self.stipple=stipple
        self.master.itemconfig(self.object, stipple=self.stipple)

    def setTag(self, tag=None):
        'tag = Str'
        self.tag=tag if tag else self.tag

    def fragmentCoords(self, fragement):
        self.fragCoords=fragement
        self.x=list()
        self.y=list()
        self.coords=list()
        for ww in self.fragCoords:
            self.coords.extend(ww)
            self.x.append(ww[0])
            self.y.append(ww[1])
        self.pointx=(max(self.x)-min(self.x))/2
        self.pointy=(max(self.y)-min(self.y))/2
        self.master.coords(self.object, self.coords)

    def destroy(self):
        self.master.delete(self.object)

class Text(object):
    def __init__(self, master, x, y, text='Text'):
        self.type='text'
        self.master=master
        self.x=x
        self.y=y
        self.text=text
        self.coords=list()
        self.pointx=min(self.x)+(max(self.x)-min(self.x))/2
        self.pointy=min(self.y)+(max(self.y)-min(self.y))/2
        for ww in range(len(self.x)):
            self.coords.append(self.x[ww])
            self.coords.append(self.y[ww])
        self.object=self.master.create_text(self.coords, text=self.text, font=Font(size=10, family=pf.POLICE[0]))
        self.fragCoords=list()
        for ww in range(0, len(self.coords), 2):
            a=[]
            a.append(self.coords[ww])
            a.append(self.coords[ww+1])
            self.fragCoords.append(a)
        self.size=10
        self.font=pf.POLICE[0]
        self.activeFont=pf.POLICE[0]
        self.disabledFont=pf.POLICE[0]
        self.fill='black'
        self.activeFill='black'
        self.disabledFill='black'
        self.weight='normal'
        self.slant='roman'
        self.underline=False
        self.overstrike=False
        self.anchor='center'
        self.justify='left'
        self.width=math.inf
        self.stipple=''
        self.tag=''
        self.stat='normal'  #normal, disabled, hidden
        self.angle=0
        self.name=''
    
    def getAll(self):
        return [self.type, self.x, self.y, self.text, self.size, self.font, self.activeFont, self.disabledFont,
           self.fill, self.activeFill, self.disabledFill, self.weight, self.slant, self.underline,
           self.overstrike, self.anchor, self.justify, self.width, self.stipple, self.tag, self.stat,
           self.angle, self.name]
    
    def setAll(self, all):
        self.setCoords(all[1], all[2])
        self.setText(all[3])
        self.setSize(all[4])
        self.setFont(all[5])
        self.setActiveFont
        self.setDisabledFont
        self.setFill(all[8])
        self.setActiveFill(all[9])
        self.setDisabledFill(all[10])
        self.setWeight(all[11])
        self.setSlant(all[12])
        self.setUnderline(all[13])
        self.setOverstrike(all[14])
        self.setAnchor(all[15])
        self.setJustify(all[16])
        self.setWidth(all[17])
        self.setStipple(all[18])
        self.setTag(all[19])
        self.setStat(all[20])
        self.rotate(all[21])
        self.setName(all[22])
            
    def setName(self, name=None):
        self.name=name if name else self.name
    
    def setStat(self, stat='normal'):
        self.stat=stat
        self.master.itemconfig(self.object, stat=self.stat)
    
    def setText(self, text='Text'):
        self.text=text
        self.master.itemconfig(self.object, text=self.text)
    
    def setCoords(self, x, y):
        self.x=x
        self.y=y
        self.coords=list()
        self.pointx=min(self.x)+(max(self.x)-min(self.x))/2
        self.pointy=min(self.y)+(max(self.y)-min(self.y))/2
        for ww in range(len(self.x)):
            self.coords.append(self.x[ww])
            self.coords.append(self.y[ww])
        self.fragCoords=list()
        for ww in range(0, len(self.coords), 2):
            a=[]
            a.append(self.coords[ww])
            a.append(self.coords[ww+1])
            self.fragCoords.append(a)
        self.master.coords(self.object, self.coords)
    
    def moveTo(self, x, y):
        a, b=x-self.x[0], y-self.y[0]
        self.master.move(self.object, a, b)
        for ww in range(0, len(self.coords), 2):
            self.coords[ww]+=a
            self.coords[ww+1]+=b
        for ww in self.fragCoords:
            ww[0]+=a
            ww[1]+=b
            self.x[self.fragCoords.index(ww)]+=a
            self.y[self.fragCoords.index(ww)]+=b
        self.pointx=min(self.x)+(max(self.x)-min(self.x))/2
        self.pointy=min(self.y)+(max(self.y)-min(self.y))/2
    
    def setPoint(self, x, y):
        self.moveTo(x,y)
    
    def horizontal(self, x):
        self.moveTo(self.x[0]+x, self.y[0])
    
    def vertical(self, y):
        self.moveTo(self.x[0], self.y[0]+y)
    
    def rotate(self, angle):
        self.angle=angle
        self.master.itemconfig(self.object, angle=self.angle)
    
    def resize(self, size):
        self.size=size
        self.master.itemconfig(self.object, font=Font(size=self.size, family=self.font, weight=self.weight,
                                                      slant=self.slant, underline=self.underline, overstrike=self.overstrike))
    
    def setFont(self, font=None):
        'font = Str'
        self.font=font if font else self.font
        self.master.itemconfig(self.object, font=Font(size=self.size, family=self.font, weight=self.weight,
                                                      slant=self.slant, underline=self.underline, overstrike=self.overstrike))
    
    def setActiveFont(self, activeFont=None):
        'activeFont = Str'
        self.activeFont=activeFont if activeFont else self.activeFont
        self.master.itemconfig(self.object, activefont=Font(size=self.size, family=self.activeFont, weight=self.weight,
                                                      slant=self.slant, underline=self.underline, overstrike=self.overstrike))
    
    def setDisabledFont(self, disabledFont=None):
        'disabledFont = Str'
        self.disabledFont=disabledFont if disabledFont else self.disabledFont
        self.master.itemconfig(self.object, disabledfont=Font(size=self.size, family=self.disabledFont, weight=self.weight,
                                                      slant=self.slant, underline=self.underline, overstrike=self.overstrike))
    
    def setUnderline(self, underline=None):
        'underline = Bool'
        self.underline=underline if type(underline)!=type(None) else self.underline
        self.master.itemconfig(self.object, font=Font(size=self.size, family=self.font, weight=self.weight,
                                                      slant=self.slant, underline=self.underline, overstrike=self.overstrike))
    
    def setWeight(self, weight=None):
        'weight = Str'
        self.weight=weight if weight else self.weight
        self.master.itemconfig(self.object, font=Font(size=self.size, family=self.font, weight=self.weight,
                                                      slant=self.slant, underline=self.underline, overstrike=self.overstrike))
    
    def setSize(self, size=None):
        'size = Int'
        self.size=size if size else self.size
        self.master.itemconfig(self.object, font=Font(size=self.size, family=self.font, weight=self.weight,
                                                      slant=self.slant, underline=self.underline, overstrike=self.overstrike))
    
    def setSlant(self, slant=None):
        'slant = Str'
        self.slant=slant if slant else self.slant
        self.master.itemconfig(self.object, font=Font(size=self.size, family=self.font, weight=self.weight,
                                                      slant=self.slant, underline=self.underline, overstrike=self.overstrike))
    
    def setOverstrike(self, overstrike=None):
        'overstrike = Bool'
        self.overstrike=overstrike if type(overstrike)!=type(None) else self.overstrike
        self.master.itemconfig(self.object, font=Font(size=self.size, family=self.font, weight=self.weight,
                                                      slant=self.slant, underline=self.underline, overstrike=self.overstrike))
    
    def setWidth(self, width=None):
        'width = Int'
        self.width=width if width else self.width
        self.master.itemconfig(self.object, width=self.width)
    
    def setFill(self, fill=None):
        'fill = Str'
        self.fill=fill if fill else self.fill
        self.master.itemconfig(self.object, fill=self.fill)
    
    def setActiveFill(self, activeFill=None):
        'activeFill = Str'
        self.activeFill=activeFill if activeFill else None
        self.master.itemconfig(self.object, activefill=self.activeFill)
    
    def setDisabledFill(self, disabledFill=None):
        'disabledFill = Str'
        self.disabledFill=disabledFill if disabledFill else self.disabledFill
        self.master.itemconfig(self.object, disabledfill=self.disabledFill)
    
    def setAnchor(self, anchor=None):
        'anchor = Str'
        self.anchor=anchor if anchor else self.anchor
        self.master.itemconfig(self.object, anchor=self.anchor)
    
    def setJustify(self, justify=None):
        'justify = Str'
        self.justify=justify if justify else self.justify
        self.master.itemconfig(self.object, justify=self.justify)
    
    def setStipple(self, stipple = None):
        'stipple = Str'
        self.stipple=stipple if stipple in ['none', 'gray25', 'gray50', 'gray75'] else ''
        self.master.itemconfig(self.object, stipple=self.stipple)

    def setTag(self, tag=None):
        'tag = Str'
        self.tag=tag if tag else self.tag

    def fragmentCoords(self, fragement):
        self.fragCoords=fragement
        self.x=list()
        self.y=list()
        self.coords=list()
        for ww in self.fragCoords:
            self.coords.extend(ww)
            self.x.append(ww[0])
            self.y.append(ww[1])
        self.pointx=(max(self.x)-min(self.x))/2
        self.pointy=(max(self.y)-min(self.y))/2
        self.master.coords(self.object, self.coords)

    def destroy(self):
        self.master.delete(self.object)

class Picture(object):
    def __init__(self, master, x, y, image):
        self.type='picture'
        self.master=master
        self.x=x
        self.y=y
        self.defaultImage=image
        time=pf.Temps()
        a='temps%s'%(str(time.an())+str(time.mois())+str(time.jour())+str(time.heure())+str(time.minute())+str(time.seconde())+str(time.micros()))
        self.img=ModSize(ImgToImg(image).toPNG(os.path.join('temps', a+'.png'))).setSize(200, 200)
        self.image=self.img[1]
        self.coords=list()
        self.pointx=min(self.x)+(max(self.x)-min(self.x))/2
        self.pointy=min(self.y)+(max(self.y)-min(self.y))/2
        for ww in range(len(self.x)):
            self.coords.append(self.x[ww])
            self.coords.append(self.y[ww])
        with Image.open(self.image[0]) as img:
            self.imag=ImageTk.PhotoImage(img)
            self.object=self.master.create_image(self.coords, image=self.imag)
        self.fragCoords=list()
        for ww in range(0, len(self.coords), 2):
            a=[]
            a.append(self.coords[ww])
            a.append(self.coords[ww+1])
            self.fragCoords.append(a)
        self.anchor='center'
        self.width=self.image[1]
        self.height=self.image[2]
        self.tag=''
        self.stat='normal'  #normal, disabled, hidden
        self.angle=0
        self.name=''
    
    def getAll(self):
        return [self.type, self.x, self.y, self.defaultImage, self.anchor, self.width, self.height, self.tag, 
           self.stat, self.angle, self.name]
    
    def setAll(self, all):
        self.setCoords(all[1], all[2])
        self.setImage(all[3], all[5], all[6], all[9])
        self.setAnchor(all[4])
        self.setTag(all[7])
        self.setStat(all[8])
        self.setName(all[10])
    
    def setName(self, name=None):
        self.name=name if name else self.name
    
    def setStat(self, stat='normal'):
        self.stat=stat
        self.master.itemconfig(self.object, stat=self.stat)
        
    def setCoords(self, x, y):
        self.x=x
        self.y=y
        self.coords=list()
        for ww in range(len(self.x)):
            self.coords.append(self.x[ww])
            self.coords.append(self.y[ww])
        self.fragCoords=list()
        for ww in range(0, len(self.coords), 2):
            a=[]
            a.append(self.coords[ww])
            a.append(self.coords[ww+1])
            self.fragCoords.append(a)
        self.master.coords(self.object, self.coords)
        self.pointx=min(self.x)+(max(self.x)-min(self.x))/2
        self.pointy=min(self.y)+(max(self.y)-min(self.y))/2
    
    def moveTo(self, x, y):
        a, b=x-self.x[0], y-self.y[0]
        self.master.move(self.object, a, b)
        for ww in range(0, len(self.coords), 2):
            self.coords[ww]+=a
            self.coords[ww+1]+=b
        for ww in self.fragCoords:
            ww[0]+=a
            ww[1]+=b
            self.x[self.fragCoords.index(ww)]+=a
            self.y[self.fragCoords.index(ww)]+=b
        self.pointx=min(self.x)+(max(self.x)-min(self.x))/2
        self.pointy=min(self.y)+(max(self.y)-min(self.y))/2
    
    def setPoint(self, x, y):
        self.moveTo(x,y)
    
    def horizontal(self, x):
        self.moveTo(self.x[0]+x, self.y[0])
    
    def vertical(self, y):
        self.moveTo(self.x[0], self.y[0]+y)
    
    def setImage(self, image=None, width=None, height=None, angle=None):
        time=pf.Temps()
        self.defaultImage=image if image else self.defaultImage
        a='temps%s'%(str(time.an())+str(time.mois())+str(time.jour())+str(time.heure())+str(time.minute())+str(time.seconde())+str(time.micros()))
        var=ModSize(ImgToImg(image).toPNG(os.path.join('temps', a+'.png'))) if image else ModSize(self.img[0][0])
        self.width=width if width else self.width
        self.height=height if height else self.height
        self.angle=angle if angle else self.angle
        self.img=var.setSize(self.width, self.height, self.angle)
        self.image=self.img[1]
        with Image.open(self.image[0]) as img:
            self.master.delete(self.object)
            self.imag=ImageTk.PhotoImage(img)
            self.object=self.master.create_image(self.coords, image=self.imag)
    
    def setAnchor(self, anchor=None):
        'anchor = Str'
        self.anchor=anchor if anchor else self.anchor
        self.master.itemconfig(self.object, anchor=self.anchor)

    def setTag(self, tag=None):
        'tag = Str'
        self.tag=tag if tag else self.tag
   
    def fragmentCoords(self, fragement):
        self.fragCoords=fragement
        self.x=list()
        self.y=list()
        self.coords=list()
        for ww in self.fragCoords:
            self.coords.extend(ww)
            self.x.append(ww[0])
            self.y.append(ww[1])
        self.pointx=(max(self.x)-min(self.x))/2
        self.pointy=(max(self.y)-min(self.y))/2
        self.master.coords(self.object, self.coords)

    def destroy(self):
        self.master.delete(self.object)

class Arc(object):
    def __init__(self, master, x, y):
        self.type='arc'
        self.master=master
        self.x=x
        self.y=y
        self.pointx=min(self.x)+(max(self.x)-min(self.x))/2
        self.pointy=min(self.y)+(max(self.y)-min(self.y))/2
        self.coords=list()
        for ww in range(len(self.x)):
            self.coords.append(self.x[ww])
            self.coords.append(self.y[ww])
        self.object=self.master.create_arc(self.coords, fill='', width=1, outline='black')
        self.fragCoords=list()
        for ww in range(0, len(self.coords), 2):
            a=[]
            a.append(self.coords[ww])
            a.append(self.coords[ww+1])
            self.fragCoords.append(a)
        self.start=0
        self.extent=90
        self.width=1
        self.activeWidth=1
        self.disabledWidth=1
        self.fill=''
        self.activeFill=''
        self.disabledFill=''
        self.outline='black'
        self.disabledOutline='black'
        self.dash=()
        self.dashOffset=0
        self.stipple=''
        self.tag=''
        self.stat='normal'  #normal, disabled, hidden
        self.style='pieslice' #piecelice, chord, arc
        self.name=''
    
    def getAll(self):
        return [self.type, self.x, self.y, self.start, self.extent, self.width, self.activeWidth, self.disabledWidth,
           self.fill, self.activeFill, self.disabledFill, self.outline, self.disabledOutline, self.dash, self.dashOffset, 
           self.stipple, self.tag, self.stat, self.style, self.name]
    
    def setAll(self, all):
        self.setCoords(all[1], all[2])
        self.setStart(all[3])
        self.setExtent(all[4])
        self.setWidth(all[5])
        self.setActiveWidth(all[6])
        self.setDisabledWidth(all[7])
        self.setFill(all[8])
        self.setActiveFill(all[9])
        self.setDisabledFill(all[10])
        self.setOutline(all[11])
        self.setDisabledOutline(all[12])
        self.setDash(all[13])
        self.setDashOffset(all[14])
        self.setStipple(all[15])
        self.setTag(all[16])
        self.setStat(all[17])
        self.setStyle(all[18])
        self.setName(all[19])
    
    def setName(self, name=None):
        self.name=name if name else self.name
    
    def setStat(self, stat='normal'):
        self.stat=stat
        self.master.itemconfig(self.object, stat=self.stat)
    
    def setCoords(self, x, y):
        self.x=x
        self.y=y
        self.coords=list()
        for ww in range(len(self.x)):
            self.coords.append(self.x[ww])
            self.coords.append(self.y[ww])
        self.fragCoords=list()
        for ww in range(0, len(self.coords), 2):
            a=[]
            a.append(self.coords[ww])
            a.append(self.coords[ww+1])
            self.fragCoords.append(a)
        self.pointx=min(self.x)+(max(self.x)-min(self.x))/2
        self.pointy=min(self.y)+(max(self.y)-min(self.y))/2
        self.master.coords(self.object, self.coords)
    
    def moveTo(self, x, y):
        a, b=x-self.pointx, y-self.pointy
        self.master.move(self.object, a, b)
        for ww in range(0, len(self.coords), 2):
            self.coords[ww]+=a
            self.coords[ww+1]+=b
        for ww in self.fragCoords:
            ww[0]+=a
            ww[1]+=b
            self.x[self.fragCoords.index(ww)]+=a
            self.y[self.fragCoords.index(ww)]+=b
        self.pointx=min(self.x)+(max(self.x)-min(self.x))/2
        self.pointy=min(self.y)+(max(self.y)-min(self.y))/2
    
    def setPoint(self, x, y):
        a=x-(max(self.x)-min(self.x))/2
        b=y-(max(self.y)-min(self.y))/2
        self.moveTo(a,b)
    
    def horizontal(self, x):
        self.moveTo(self.pointx+x, self.pointy)
    
    def vertical(self, y):
        self.moveTo(self.pointx, self.pointy+y)
    
    def resize(self, x, y):
        x=x/2
        y=y/2
        rx=min(self.x)+(max(self.x)-min(self.x))/2
        ry=min(self.y)+(max(self.y)-min(self.y))/2
        for ww in range(0, len(self.coords), 2):
            if self.coords[ww]>=rx:
                self.coords[ww]+=x
            else:
                self.coords[ww]-=x
            if self.coords[ww+1]>=ry:
                self.coords[ww+1]+=y
            else:
                self.coords[ww+1]-=y
        self.fragCoords=list()
        self.x, self.y=list(), list()
        for ww in range(0, len(self.coords), 2):
            a=[]
            a.append(self.coords[ww])
            a.append(self.coords[ww+1])
            self.fragCoords.append(a)
            self.x.append(self.coords[ww])
            self.y.append(self.coords[ww+1])
        self.pointx=(max(self.x)-min(self.x))/2
        self.pointy=(max(self.y)-min(self.y))/2
        self.master.coords(self.object, self.coords)
    
    def setStart(self, start=None):
        'start = Int'
        self.start=start if start else self.start
        self.master.itemconfig(self.object, start=self.start)
    
    def setExtent(self, extent=None):
        'extent = Str'
        self.extent=extent if extent else self.extent
        self.master.itemconfig(self.object, extent=self.extent)
    
    def setStyle(self, style=None):
        'style = Str'
        self.style=style if style else self.style
        self.master.itemconfig(self.object, style=self.style)
    
    def setWidth(self, width=None):
        'width = Int'
        self.width=width if width else self.width
        self.master.itemconfig(self.object, width=self.width)
    
    def setActiveWidth(self, activeWidth=None):
        'activeWidth = Int'
        self.activeWidth=activeWidth if activeWidth else self.activeWidth
        self.master.itemconfig(self.object, activewidth=self.activeWidth)
    
    def  setDisabledWidth(self, disabledWidth=None):
        'disabledWidth = Int'
        self.disabledWidth=disabledWidth if disabledWidth else self.disabledWidth
        self.master.itemconfig(self.object, disabledwidth=self.disabledWidth)
    
    def setFill(self, fill=None):
        'fill = Str'
        self.fill=fill if type(fill)!=type(None) else self.fill
        self.master.itemconfig(self.object, fill=self.fill)
    
    def setActiveFill(self, activeFill=None):
        'activeFill = Str'
        self.activeFill=activeFill if activeFill else None
        self.master.itemconfig(self.object, activefill=self.activeFill)
    
    def setDisabledFill(self, disabledFill=None):
        'disabledFill = Str'
        self.disabledFill=disabledFill if disabledFill else self.disabledFill
        self.master.itemconfig(self.object, disabledfill=self.disabledFill)
    
    def setOutline(self, outline=None):
        'outline = Str'
        self.outline=outline if outline else self.outline
        self.master.itemconfig(self.object, outline=self.outline)
    
    def setDisabledOutline(self, disabledOutline=None):
        'disabledOutline = Str'
        self.disabledOutline=disabledOutline if disabledOutline else self.disabledOutline
        self.master.itemconfig(self.object, disabledoutline=self.disabledOutline)
    
    def setDash(self, dash=None):
        'dash = (Int, Int)'
        self.dash=dash if type(dash)!=type(None) else self.dash
        self.master.itemconfig(self.object, dash=self.dash)
    
    def setDashOffset(self, dashoffset=None):
        'dahsOffset = Int'
        self.dashOffset=dashoffset if dashoffset else self.dashOffset
        self.master.itemconfig(self.object, dashoffset=self.dashOffset)
    
    def setStipple(self, stipple = None):
        'stipple = Str'
        self.stipple=stipple
        self.master.itemconfig(self.object, stipple=self.stipple)

    def setTag(self, tag=None):
        'tag = Str'
        self.tag=tag if tag else self.tag

    def fragmentCoords(self, fragement):
        self.fragCoords=fragement
        self.x=list()
        self.y=list()
        self.coords=list()
        for ww in self.fragCoords:
            self.coords.extend(ww)
            self.x.append(ww[0])
            self.y.append(ww[1])
        self.pointx=(max(self.x)-min(self.x))/2
        self.pointy=(max(self.y)-min(self.y))/2
        self.master.coords(self.object, self.coords)

    def destroy(self):
        self.master.delete(self.object)

class Window(object):
    def __init__(self, master, x, y, window):
        self.type='window'
        self.master=master
        self.x=x
        self.y=y
        self.window=window
        self.coords=list()
        self.pointx=min(self.x)+(max(self.x)-min(self.x))/2
        self.pointy=min(self.y)+(max(self.y)-min(self.y))/2
        for ww in range(len(self.x)):
            self.coords.append(self.x[ww])
            self.coords.append(self.y[ww])
        self.object=self.master.create_window(self.coords, window=self.window)
        self.fragCoords=list()
        for ww in range(0, len(self.coords), 2):
            a=[]
            a.append(self.coords[ww])
            a.append(self.coords[ww+1])
            self.fragCoords.append(a)
        self.bordermode='inside'    #outside
        self.anchor='center'
        self.master.update_idletasks()
        self.width=0
        self.height=0
                
        self.tag=''
        self.stat='normal'  #normal, disabled, hidden
        self.name=''
        self.windowName=self.window.type
        self.option2W=None
    
    def getAll(self):
        return [self.type, self.x, self.y, self.window, self.bordermode, self.anchor, self.width, self.height, self.tag,
                self.stat, self.name, self.window.getAll()]
    
    def setAll(self, all):
        self.setCoords(all[1], all[2])
        self.setWindow(obj2W.listOfWidget[all[11][0].capitalize()](self.master))
        self.setBordermode
        self.setAnchor(all[5])
        self.setWidth(all[6])
        self.setHeight(all[7])
        self.setTag(all[8])
        self.setStat(all[9])
        self.setName(all[10])
        self.setWindow(self.window)
        self.window.setAll(all[11])
    
    def setName(self, name=None):
        self.name=name if name else self.name
    
    def setStat(self, stat='normal'):
        self.stat=stat
        self.master.itemconfig(self.object, stat=self.stat)
    
    def setWindow(self, window=None):
        self.window=window if window else self.window
        self.windowName=self.window.type
        self.master.itemconfig(self.object, window=self.window)
    
    def setCoords(self, x, y):
        self.x=x
        self.y=y
        self.coords=list()
        for ww in range(len(self.x)):
            self.coords.append(self.x[ww])
            self.coords.append(self.y[ww])
        self.fragCoords=list()
        for ww in range(0, len(self.coords), 2):
            a=[]
            a.append(self.coords[ww])
            a.append(self.coords[ww+1])
            self.fragCoords.append(a)
        self.master.coords(self.object, self.coords)
        self.pointx=min(self.x)+(max(self.x)-min(self.x))/2
        self.pointy=min(self.y)+(max(self.y)-min(self.y))/2
    
    def moveTo(self, x, y):
        a, b=x-self.x[0], y-self.y[0]
        self.master.move(self.object, a, b)
        for ww in range(0, len(self.coords), 2):
            self.coords[ww]+=a
            self.coords[ww+1]+=b
        for ww in self.fragCoords:
            ww[0]+=a
            ww[1]+=b
            self.x[self.fragCoords.index(ww)]+=a
            self.y[self.fragCoords.index(ww)]+=b
        self.pointx=min(self.x)+(max(self.x)-min(self.x))/2
        self.pointy=min(self.y)+(max(self.y)-min(self.y))/2
    
    def setPoint(self, x, y):
        self.moveTo(x,y)
    
    def horizontal(self, x):
        self.moveTo(self.x[0]+x, self.y[0])
    
    def vertical(self, y):
        self.moveTo(self.x[0], self.y[0]+y)
    
    def setWidth(self, width=None):
        'width = Int'
        self.width=width if width else self.width
        self.master.itemconfig(self.object, width=self.width)
    
    def setHeight(self, height=None):
        'height = Int'
        self.height=height if height else self.height
        self.master.itemconfig(self.object, height=self.height)

    def setBordermode(self, bordermode=None):
        'bordermode = Str'
        self.bordermode=bordermode if bordermode else self.bordermode
        self.master.itemconfig(self.object, bordermode=self.bordermode)

    def setAnchor(self, anchor=None):
        'anchor = Str'
        self.anchor=anchor if anchor else self.anchor
        self.master.itemconfig(self.object, anchor=self.anchor)
    
    def setTag(self, tag=None):
        'tag = Str'
        self.tag=tag if tag else self.tag

    def fragmentCoords(self, fragement):
        self.fragCoords=fragement
        self.x=list()
        self.y=list()
        self.coords=list()
        for ww in self.fragCoords:
            self.coords.extend(ww)
            self.x.append(ww[0])
            self.y.append(ww[1])
        self.pointx=(max(self.x)-min(self.x))/2
        self.pointy=(max(self.y)-min(self.y))/2
        self.master.coords(self.object, self.coords)

    def destroy(self):
        self.master.delete(self.object)
    
    def setWidget(self, name, master, theme=None):
        window=obj2W.listOfWidget[name](self.master)
        self.setWindow(window)
        self.option2W=opt2W.Option2W(master, window, theme)
        self.windowName=self.window.type
    
    def setOption2W(self, master, theme=None, command=None):
        self.option2W=opt2W.Option2W(master, self.window, theme, command)
        return self.option2W

class Pen(object):
    def __init__(self, master):
        self.type='pen'
        self.master=master
        self.fill='black'
        self.width=1
        self.smooth=False
        self.splineSteps=12
        self.capStyle='butt'   #butt, round, projecting
        self.joinStyle='miter'  #round, bevel, miter
        self.listPen=[]
        self.listAll=[]
        self.x=[]
        self.y=[]
        self.dx=[]
        self.dy=[]
        self.dPen=[]
        self.dAll=[]
        self.config=[]
        self.assign()
    
    def getAll(self):
        return [self.type, self.x, self.y, self.listPen, self.config]
    
    def setAll(self, all):
        self.x=all[1]
        self.y=all[2]
        self.listPen=[]
        self.config=all[4]
        for ww in range(len(self.config)):
            l=[]
            for xx in range(len(self.x[ww])):
                try:
                    x=[self.x[ww][xx], self.x[ww][xx+1]]
                    y=[self.y[ww][xx], self.y[ww][xx+1]]
                except:
                    x=[self.x[ww][xx], self.x[ww][xx-1]]
                    y=[self.y[ww][xx], self.y[ww][xx-1]]
                l.append(self.master.create_line(x[0], y[0], x[1], y[1], fill=self.config[ww][0],
                                       width=self.config[ww][1], smooth=self.config[ww][2],
                                       splinesteps=self.config[ww][3], capstyle=self.config[ww][4],
                                       joinstyle=self.config[ww][5]))
            self.listPen.append(l)
        self.fill=self.config[-1][0]
        self.width=self.config[-1][1]
        self.smooth=self.config[-1][2]
        self.splineSteps=self.config[-1][3]
        self.capStyle=self.config[-1][4]
        self.joinStyle=self.config[-1][5]
        
    def setFill(self, fill=None):
        self.fill=fill if fill else self.fill
    
    def setWidth(self, width=None):
        self.width=width if width else self.width
    
    def setSmooth(self, smooth=None):
        self.smooth=smooth if smooth else self.smooth
    
    def setSplineSteps(self, splineSteps=None):
        self.splineSteps=splineSteps if splineSteps else self.splineSteps
    
    def setCapStyle(self, capStyle=None):
        self.capStyle=capStyle if capStyle else self.capStyle
    
    def setJoinStyle(self, joinStyle=None):
        self.joinStyle=joinStyle if joinStyle else self.joinStyle
        
    def draw(self, event):
        x=event.x
        y=event.y
        if len(self.dx)>0:
            self.dPen.append(self.master.create_line(self.dx[-1], self.dy[-1], x, y, fill=self.fill, width=self.width,
                                                         smooth=self.smooth, splinesteps=self.splineSteps,
                                                         capstyle=self.capStyle, joinstyle=self.joinStyle))
        else:
            self.dPen.append(self.master.create_line(x, y, x, y, fill=self.fill, width=self.width,
                                                         smooth=self.smooth, splinesteps=self.splineSteps,
                                                         capstyle=self.capStyle, joinstyle=self.joinStyle))
        self.dx.append(x)
        self.dy.append(y)
    
    def penUp(self, event):
        if(len(self.dPen)>0):
            self.x.append(self.dx)
            self.y.append(self.dy)
            self.listAll.append(self.dAll)
            self.listPen.append(self.dPen)
            self.dx=[]
            self.dy=[]
            self.dAll=[]
            self.dPen=[]
            self.config.append([self.fill, self.width, self.smooth, self.splineSteps,
                                self.capStyle, self.joinStyle, ])

    def assign(self):
        pf.Assign(self.master, self.draw, ['B1-Motion', 'Button-1'])
        pf.Assign(self.master, self.penUp, ['ButtonRelease-1'])

    def destroy(self):
        for ww in self.listPen:
            for xx in ww:
                self.master.delete(xx)

listOfObject={
    'line':Line,
    'polygon':Polygon,
    'oval':Oval,
    'text':Text,
    'picture':Picture,
    'arc':Arc,
    'window':Window,
    'pen':Pen
}
    

