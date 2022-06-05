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


mainphoto= Label(window,height=180,width=280, bg="light gray",highlightbackground="black",highlightthickness=2,cursor='tcross',)
mainphoto.place(x=10,y=10)


path = "@zoomin.cur"
newphoto= Label(window,height=180,width=280,bg="light gray",highlightbackground="black",highlightthickness=2,cursor=path)
newphoto.place(x=310,y=10)

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

window.mainloop()