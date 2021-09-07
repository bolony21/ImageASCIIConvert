import tkinter
from PIL import *
import tkinter as tk
from tkinter import Button, Entry, Image,Menu, Label, OptionMenu, StringVar, Toplevel,filedialog, ttk, NSEW
import PIL
from ttkthemes import themed_tk as tkt
import time
import os


# Free to use and edit - Credit to youtube and various websites for helping me build/troubleshoot the Ascii to Img mainframe, User Interface,Presets
# Customizable settings and improvements by @bolony21 on Github
# []- Some presets might not translate the image well, more fixes/improvements on the way for this, if none of the presets work, try the default option -[]






root = tkt.ThemedTk()
root.get_themes()
root.set_theme("black")
root.title("Image to ASCII")



root.resizable(True, True)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

sg = ttk.Sizegrip(root)
sg.grid(row=1, sticky=tk.SE)






root = ttk.Frame(root, padding=(12,12,12,12))
root.grid(row=0, column=0, sticky=NSEW)

Lab1 = tkt.ttk.Label(root,text="IMAGE TO ASCII ART CONVERTER") 
Lab1.grid(row=1,column=1,padx=10,pady=10)




# default Filepath 
filepath = r"{C:\tmp}"










Lab5 = tkt.ttk.Label(root,text="Image:") 
Lab5.grid(row=1,column=0,padx=10,pady=10)







Lab5 = tkt.ttk.Entry(root,text="C://") 
Lab5.grid(row=3,column=0,padx=10,pady=10)



LabS2 = tkt.ttk.Label(root,text="Conversion Delay:")
def DelayGet():
    global Delay
    Delay = int(DG.get())
    print(Delay)

DG = tkt.ttk.Spinbox(root,to=10,from_=1,increment=1,command=DelayGet,width=5)
DG.grid(row=5,column=3,padx=5,pady=5)

LabS2.grid(row=5,column=2,padx=10,pady=10)
LabS3 = tkt.ttk.Label(root,text="Output Filepath:")
LabS3.grid(row=7,column=2,padx=10,pady=10)
LabS3 = tkt.ttk.Label(root,text="Output File name:")
LabS3.grid(row=6,column=2,padx=10,pady=10)


LabS4 = tkt.ttk.Label(root,text="Conversion Presets:")
LabS4.grid(row=6,column=0,padx=10,pady=10)



def open_popup():
   top = tkt.ThemedTk()
   top.get_themes()
   top.set_theme("black")
   top.title("Converting Image..." )
   top = tkt.ttk.Frame(top, padding=(12,12,12,12))
   top.grid(row=0, column=0, sticky=NSEW)
   Bar1 = tkt.ttk.Progressbar(top,orient='horizontal',length=250)
   Bar1.start(interval=None)
   Bar1.grid(row=1,column=1,padx=20,pady=20)
   top.after(10000, lambda: top.destroy())
   top.update()

   
 
def ConvertStart1():
    print("Converting Image...")
    if Delay >= 0 :
     open_popup()
     time.sleep(Delay)
     namefetch()
     browsefuncCust1()
     
    else:
     namefetch()
     browsefuncCust1()
  
def ConvertStart2():
    print("Converting Image...")
    if Delay >= 0 :
     open_popup()
     time.sleep(Delay)
     namefetch()
     browsefuncCust2()
    else:
     namefetch()
     browsefuncCust2()




def ConvertStart3():
    print("Converting Image...")
    if Delay >= 0 :
     open_popup()
     time.sleep(Delay)
     namefetch()
     browsefuncCust3()
    else:
     namefetch()
     browsefuncCust3()




def ConvertStartDef():
    print("Converting Image...")
    namefetch()
    browsefuncD()



# Edit the file types to support additional image files outside of the default (Might not work though)

def selectfile():
    global filename

    filename = filedialog.askopenfilename(filetypes=(("png files","*.png"),("jpeg files","*.jpeg"),("All files","*.*")))
    Lab5.insert(0,str(filename))



ButtonSelect = tkt.ttk.Button(root,text="[Select Image]",command=selectfile,width=10)
ButtonSelect.grid(row=5,column=0,padx=10,pady=10)

ButtonGo = tkt.ttk.Button(root,text="Preset 3",command=ConvertStart3,width=10)
ButtonGo.grid(row=8,column=1,padx=10,pady=10)

ButtonGo = tkt.ttk.Button(root,text="Preset 2",command=ConvertStart2,width=10)
ButtonGo.grid(row=7,column=1,padx=10,pady=10)

ButtonGo = tkt.ttk.Button(root,text="Preset 1",command=ConvertStart1,width=10)
ButtonGo.grid(row=7,column=0,padx=10,pady=10)

ButtonGo = tkt.ttk.Button(root,text="Default",command=ConvertStartDef,width=10)
ButtonGo.grid(row=8,column=0,padx=10,pady=10)

NameFr = tkt.ttk.Entry(root,width=10)
PATHFr = tkt.ttk.Entry(root,width=10)

NameFr.grid(row=6,column=3,padx=10,pady=10)
PATHFr.grid(row=7,column=3,padx=10,pady=10)
LabErr1 = tkt.ttk.Label(root,text="Error Console: None ")
LabErr1.grid(row=11,column=0,padx=10,pady=10)


# Preset/Default ASCII characters, Change the presets as you like, (Changing default ascii may make the program unusable)

ASCII_CHARS        = ['@','#',"!","$",'%','&','*','.',',',';',':']



CUSTOM_ASCII_CHAR1 = ['.',';',',',':','::','"','*','∘','〇','•','◦','●'] # preset 1
CUSTOM_ASCII_CHAR2 = ['=','-','_','~','☰','╴','╶','⎯','☱','☴','═','⁃'] # preset 2
CUSTOM_ASCII_CHAR3 = ['[]','■','□','▪','▫','◼','◻','◼','▇','▉','◻','▮'] # preset 3

   





Nwidth = int(100)




def browsefuncD(Nwidth=100):
    try:
     image = PIL.Image.open(filename)
    except:
     print(filename,"is not a compatible file") 

    new_image_data = PixtoASCDEF(grayscale(resize_image(image)))

    pixel_count = len(new_image_data)

    ASCII_IMAGED = "\n".join(new_image_data[i:(i+Nwidth)] for i in range(0,pixel_count,Nwidth))

    print(ASCII_IMAGED)

    f = open("'RESULTDEF.txt'","w+")
    f.write(ASCII_IMAGED)



def namefetch():
 global NameF
 NameF = NameFr.get()
 global filep
 filep = PATHFr.get()
 print('Filename:'+ NameF)
 print('Path:' + filep)
 global filepath
 filepath = os.path.join(filep, f'{NameF}.txt')

 print(filep)
 

    







def browsefuncCust1(Nwidth=100):
    try:
     image = PIL.Image.open(filename)
    except:
     print(filename,"is not a compatible file") 

    new_image_data = PixtoASCP1(grayscale(resize_imageC(image)))

    pixel_count = len(new_image_data)

    ASCII_IMAGEC = "\n".join(new_image_data[i:(i+Nwidth)] for i in range(0,pixel_count,Nwidth))

    print(ASCII_IMAGEC)

    f = open(filepath,"w+")
    f.write(ASCII_IMAGEC)


def browsefuncCust2(Nwidth=100):
    try:
     image = PIL.Image.open(filename)
    except:
     print(filename,"is not a compatible file") 

    new_image_data = PixtoASCP2(grayscale(resize_imageC(image)))

    pixel_count = len(new_image_data)

    ASCII_IMAGEC2 = "\n".join(new_image_data[i:(i+Nwidth)] for i in range(0,pixel_count,Nwidth))

    print(ASCII_IMAGEC2)

    f = open(filepath,"w+")
    f.write(ASCII_IMAGEC2)



def browsefuncCust3(Nwidth=100):
    try:
     image = PIL.Image.open(filename)
    except:
     print(filename,"is not a compatible file") 

    new_image_data = PixtoASCP3(grayscale(resize_imageC(image)))

    pixel_count = len(new_image_data)

    ASCII_IMAGEC3 = "\n".join(new_image_data[i:(i+Nwidth)] for i in range(0,pixel_count,Nwidth))

    print(ASCII_IMAGEC3)

    f = open(filepath,"w+")
    f.write(ASCII_IMAGEC3)







def resize_image(image,NWidth=100):
    width,height = image.size
    ratio = height / width
    new_height = int(Nwidth * ratio)
    resized_image = image.resize((Nwidth,new_height))
    image.load()
    return(resized_image)



def resize_imageC(image,Nwitdh=100):
    width,height = image.size
    ratio = height / width
    new_height = int(Nwidth * ratio)
    resized_image = image.resize((Nwidth,new_height))
    image.load()
    return(resized_image)


def grayscale(image):
    grayscale_image = image.convert("L")
    image.load()
    return(grayscale_image)


def grayscaleC(image):

    grayscale_image = image.convert("L")
    image.load()
    return(grayscale_image)



def PixtoASCDEF(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    image.load()
    return characters


def PixtoASCP1(image):
    pixels = image.getdata()
    characters = "".join([CUSTOM_ASCII_CHAR1[pixel//25] for pixel in pixels])
    image.load()
    return characters

def PixtoASCP2(image):
    pixels = image.getdata()
    characters = "".join([CUSTOM_ASCII_CHAR2[pixel//25] for pixel in pixels])
    image.load()
    return characters


def PixtoASCP3(image):
    pixels = image.getdata()
    characters = "".join([CUSTOM_ASCII_CHAR3[pixel//25] for pixel in pixels])
    image.load()
    return characters













root.mainloop()