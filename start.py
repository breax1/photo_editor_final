#-*- coding:utf-8-*-
from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showinfo
import cv2
import imutils
from PIL import Image
from PIL import ImageTk


window = Tk()
window.title("Photo Editor")
window.geometry("600x800+650+100")
window.resizable(height=False,width=False)
ico = PhotoImage(file='photoicon.ico')
window.tk.call('wm', 'iconphoto', window._w, ico)
window.configure(bg="light gray")

im= None
image = cv2.imread('white.brx')
siyahbeyazphoto = None
mavili = None
resized = None
a = 0
b = 0
c = 0
fotograf_yolu = 1

def Fscreen(*args):
    if a>0 :
        cv2.imshow("Full Screen",siyahbeyazphoto)
        cv2.waitKey(0)
    if b>0 :
        cv2.imshow("Full Screen",mavili)
        cv2.waitKey(0)
    if c>0 :
        cv2.imshow("Full Screen",resized)
        cv2.waitKey(0)
        

mainphoto= Label(window,height=180,width=280, bg="light gray",highlightbackground="black",highlightthickness=2,cursor='tcross',)
mainphoto.place(x=10,y=10)


path = "@zoomin.cur"
imageToShow= imutils.resize(image, width=500)
imageToShow = cv2.cvtColor(imageToShow, cv2.COLOR_BGR2RGBA)
im = Image.fromarray(imageToShow )
img = ImageTk.PhotoImage(image=im)

mainphoto.configure(image=img)
mainphoto.image = img
newphoto= Label(window,height=180,width=280,bg="light gray",highlightbackground="black",highlightthickness=2,cursor=path)
newphoto.place(x=310,y=10)

newphoto.bind("<Button-1>",Fscreen)

im = Image.fromarray(imageToShow)
img = ImageTk.PhotoImage(image=im)
newphoto.configure(image=img)
newphoto.image = img


def fotograf_sec():
    filetypes=(('photo files', '*.png'),('photo files', '*.jpg'),('All files', '*.*'))
    fotograf_yolu = filedialog.askopenfilename(filetypes=filetypes)
    fotograf= open(fotograf_yolu,"r")
    showinfo(title="Fotoğraf Yükleme Başarılı",message=f"Dosya yolu:\n{fotograf_yolu}")
    
    if len(fotograf_yolu)>0:
        global image
        global imager
        imager = cv2.imread(fotograf_yolu)
        image = cv2.imread(fotograf_yolu)
        image= imutils.resize(image, height=380)

        imageToShow= imutils.resize(image, width=180)
        imageToShow = cv2.cvtColor(imageToShow, cv2.COLOR_BGR2RGBA)
        im = Image.fromarray(imageToShow )
        img = ImageTk.PhotoImage(image=im)

        mainphoto.configure(image=img)
        mainphoto.image = img

def savefile():
    filetypes=(('PNG files', '*.png'),('JPG files', '*.jpg'),('All files', '*.*'))
    filename = filedialog.asksaveasfile(mode='wb', defaultextension=".jpg",filetypes=filetypes)
    if not filename:
        return
    im.save(filename)


b1=Button(text="Dosya Seç",font="Arial 14 bold",bg="red",fg="white",cursor='hand2' ,command=fotograf_sec)
b1.place(x=10,y=200)

save_button = Button(window, text="Kaydet",font="Arial 14 bold",bg="red",fg="white",cursor='hand2' , command=savefile)
save_button.place(x=510,y=200)

def photoedit(edit):
    global image
    global img
    global im
    global siyahbeyazphoto
    global mavili
    global resized
    global a
    global b
    global c
    
    if edit==1:
        siyahbeyazphoto= cv2.cvtColor(imager, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Siyah Beyaz",siyahbeyazphoto)
        cv2.waitKey(0)

        # GUİ
        im = Image.fromarray(siyahbeyazphoto)
        img = ImageTk.PhotoImage(image=im)
        newphoto.configure(image=img),
        newphoto.image = img
        mavili = None
        resized = None
        a = len(siyahbeyazphoto)
        b = 0
        c = 0
        
    if edit==2:
        mavili= cv2.cvtColor(imager, cv2.COLOR_BGRA2RGB)
        cv2.imshow("Mavili",mavili)
        cv2.waitKey(0)
        mavilia = cv2.cvtColor(mavili, cv2.COLOR_BGRA2RGB)

        im = Image.fromarray(mavilia)
        img = ImageTk.PhotoImage(image=im)
        newphoto.configure(image=img)
        newphoto.image = img
        
        siyahbeyazphoto = None
        resized = None
        b = len(mavili)
        a = 0
        c = 0
        
        
        
    if edit==3:
        giris1=Entry(window,width=10)
        giris1.place(x=200,y=490)
        giris1.insert(0,"En Giriniz")
        
        

        giris2=Entry(window,width=10)
        giris2.place(x=200,y=510)
        giris2.insert(0,"Boy Giriniz")
        giris2.bind('<Return>')
        
        en= int(giris1.get())
        boy= int(giris2.get())
        dim = (en,boy)
        resized = cv2.resize(img,dim,interpolation = cv2.INTER_AREA)
        cv2.imshow("Yeni Boyut",resized)
        cv2.waitKey(0)
        cv2.imwrite("Yeni Boyut.jpg",resized)
        
        im = Image.fromarray(resized)
        img = ImageTk.PhotoImage(image=im)
        newphoto.configure(image=img)
        newphoto.image = img
        
        siyahbeyazphoto = None
        mavili = None
        c = len(resized)
        a = 0
        b = 0
sec1=Button(window, text='Siyah Beyaz',font='Times 15 bold ',bg='pink',activebackground='black',activeforeground='white',cursor='hand2', width=15,height=1,command=lambda:photoedit(1))
sec1.place(x=1,y=350)

sec2=Button(window, text='Mavili',font='Times 15 bold ',bg='pink',activebackground='black',activeforeground='white',cursor='hand2', width=15,height=1,command=lambda:photoedit(2))
sec2.place(x=1,y=420)

sec3=Button(window, text='Yeniden Boyutlandır',font='Times 15 bold ',bg='pink',activebackground='black',activeforeground='white',cursor='hand2', width=15,height=1,command=lambda:photoedit(3))
sec3.place(x=1,y=490)
        
        
window.mainloop()
