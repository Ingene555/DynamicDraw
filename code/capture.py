import ctypes
from PIL import ImageGrab
from PIL import Image
import win32api
import os


def masquer_souris(event=None):
    ctypes.windll.user32.ShowCursor(False)


def afficher_souris(event=None):
    ctypes.windll.user32.ShowCursor(True)


def capturer_canvas(fen, can, path):
    masquer_souris()
    fen.update()
    fen_x = fen.winfo_rootx()
    fen_y = fen.winfo_rooty()
    can_x = can.winfo_x() + fen_x
    can_y = can.winfo_y() + fen_y
    can_width = can.winfo_width()
    wdt=can_width*5/100
    can_height = can.winfo_height()
    fen.attributes('-topmost', True)
    capture = ImageGrab.grab(bbox=(can_x, can_y, can_x + can_width-wdt, can_y + can_height))
    capture.save(path)
    fen.attributes('-topmost', False)
    afficher_souris()

class ImgToImg:
    def __init__(self, image, format_ = None):
        self.from_img = image
        if not format_:
            self.from_format = image.rsplit('.')[len(image.rsplit('.')[:])-1]
        else:self.from_format = format_
        self.from_format = self.from_format.lower()

    def toGIF(self, path):
        a = self.toPNG('temps\\gif_temp.png')
        output_file = os.path.splitext(path)[0] + ".gif"
        with Image.open(a) as img:
            img.save(output_file)
        return path

    def toCUR(self, path):
        try:os.remove(path)
        except:pass
        a = self.toICO('temps\\cur_temp.ico')
        win32api.CopyFile(a, path, True)
        return path

    def toICO(self, path):
        a = self.toPNG('temps\\ico_temp.png')
        with Image.open(a) as img:
            img = img.convert("RGBA")
            img.save(path, format='ICO')
        return path

    def toBMP(self, path):
        a = self.toPNG('temps\\bmp_temp.png')
        image = Image.open(a)
        image.save(path)
        return path

    def toPNG(self, path):
        if True:
            with Image.open(self.from_img) as img:
                output_file = os.path.splitext(path)[0] + ".png"
                img.save(output_file)

        return path

    def toJPEG(self, path):
        a = self.toPNG('temps\\jpeg_temp.png')
        with Image.open(a) as img:
            rgb_img = img.convert('RGB')
            rgb_img.save(path, format='JPEG')
        return path

    def toJPG(self, path):
        a = self.toPNG('temps\\jpg_temp.png')
        with Image.open(a) as img:
            rgb_img = img.convert('RGB')
            rgb_img.save(path, format='JPEG')
        return path

    def toTIF(self, path):
        a = self.toPNG('temps\\tif_temps.png')
        with Image.open(a) as img:
            img.save(path, format='TIFF')
        return path

    def toTIFF(self, path):
        a = self.toPNG('temps\\tiff_temps.png')
        with Image.open(a) as img:
            img.save(path, format='TIFF')
        return path

    def toWEBP(self, path):
        a = self.toPNG('temps\\webp_temps.png')
        with Image.open(a) as img:
            img.save(path, format='WEBP')
        return path
    
    def toIMG(self, path):
        fr=path.rsplit('.')[len(path.rsplit('.')[:])-1]
        a=fr.upper()
        exec(f'self.to{a}("{path}")')
        return path

class BlackWhite:
    def __init__(self, image, format_ = None):
        self.from_image = image
        self.from_format = format_ if format_ else image[image.rfind('.')+1:]

    def toIMG(self, path):
        f = path[path.rfind('.')+1:]
        temp_from = 'temps\\wb_temp.png'
        ImgToImg(self.from_image).toPNG(temp_from)
        temp_to = 'temps\\bw_temp.png'
        with Image.open(temp_from) as image:
            image_noir_blanc = image.convert("L")
            chemin_image_noir_blanc = temp_to
            image_noir_blanc.save(chemin_image_noir_blanc)
        exec(f"ImgToImg(r'{temp_to}').to{f.upper()}(r'{path}')")
        return path
