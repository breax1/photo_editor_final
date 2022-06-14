#-*- coding:utf-8-*-
from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showinfo
import cv2
import imutils
from PIL import Image
from PIL import ImageTk
from matplotlib.pyplot import gray
import numpy as np

# Pencere oluşturma kodları
window = Tk()
window.title("Photo Editor")
window.geometry("600x600+650+100")
window.resizable(height=False,width=False)
ico = PhotoImage(file='photoeditor.png')
window.tk.call('wm', 'iconphoto', window._w, ico)
bg=PhotoImage(file='background.png')
bglabel = Label(window,image=bg)
bglabel.place(x=0,y=0,relwidth=1,relheight=1)

#fonksiyon içindeki değişkenleri global yapmak için
im= None
image = cv2.imread('photoeditorlabelbg.png') #program ilk açıldığında çerçeve içlerini beyaz renk yapmak için değşkenin içine fotoğraf atadım
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
fotograf_yolu = 1

#program ilk çalıştığında çerçeve için özel fotoğrafı yerleştirmek için
photo_size= (image.shape[0])
imageToShow= imutils.resize(image, width=400)
imageToShow = cv2.cvtColor(imageToShow, cv2.COLOR_BGR2RGBA)
im = Image.fromarray(imageToShow )
img = ImageTk.PhotoImage(image=im)


#Fotoğraf önizlemesini tam ekran yapmak
def Fscreen(*args):
    if a>0 :
        cv2.imshow("Full Screen",siyahbeyazphotoab)
        cv2.waitKey(0)
    if b>0 :
        cv2.imshow("Full Screen",maviliab)
        cv2.waitKey(0)
    if c>0 :
        cv2.imshow("Full Screen",cizimab)
        cv2.waitKey(0)
    if d>0 :
        cv2.imshow("Full Screen",yesilliab)
        cv2.waitKey(0)      
    if e>0 :
        cv2.imshow("Full Screen",kirmiziliab)
        cv2.waitKey(0) 
    if f>0 :
        cv2.imshow("Full Screen",negatifab)
        cv2.waitKey(0)
        


#Programa atılan fotoğrafın çerçevesi ve önizlemesi
mainphoto= Label(window,height=180,width=280, bg="light gray",highlightbackground="black",highlightthickness=2,cursor='tcross',)
mainphoto.place(x=10,y=10)
mainphoto.configure(image=img)
mainphoto.image = img

#değiştirilem fotoğrafın çerçevesi ve önizlemesi
path = "@zoomin.cur" 
newphoto= Label(window,height=180,width=280,bg="light gray",highlightbackground="black",highlightthickness=2,cursor=path)
newphoto.place(x=302.5,y=10)
newphoto.bind("<Button-1>",Fscreen)
newphoto.configure(image=img)
newphoto.image = img


#fotoğrafı program içine atma
def fotograf_sec():
    filetypes=(('photo files', '*.png'),('photo files', '*.jpg'),('All files', '*.*'))
    fotograf_yolu = filedialog.askopenfilename(filetypes=filetypes)
    fotograf= open(fotograf_yolu,"r")
    showinfo(title="Fotoğraf Yükleme Başarılı",message=f"Dosya yolu:\n{fotograf_yolu}")
    
    #programa atılan fotoğrafı görüntüleme
    if len(fotograf_yolu)>0:
        global image
        global imager
        imager = cv2.imread(fotograf_yolu)
        image = cv2.imread(fotograf_yolu)
        imageToShow= imutils.resize(image, width=int(photo_size/2.3))
        imageToShow = cv2.cvtColor(imageToShow, cv2.COLOR_BGR2RGBA)
        im = Image.fromarray(imageToShow )
        img = ImageTk.PhotoImage(image=im)

        mainphoto.configure(image=img)
        mainphoto.image = img

#fotoğrafı kaydetme
def savefile():
    filetypes=(('PNG files', '*.png'),('JPG files', '*.jpg'),('All files', '*.*'))
    filename = filedialog.asksaveasfile(mode='wb', defaultextension=".jpg",filetypes=filetypes)
    if not filename:
        return
    ima.save(filename)

#Dosya seç butonu
dosyasecbutton = ImageTk.PhotoImage(file="dosyasec.png")
b1=Button(text="Dosya Seç",image= dosyasecbutton ,font="Arial 14 bold",bg="pink",fg="pink",cursor='hand2',width=280 ,height=30  ,command=fotograf_sec)
b1.place(x=10,y=215)

#dosya kaydet butonu
kaydetbutton = ImageTk.PhotoImage(file="kaydet.png")
save_button = Button(text="Kaydet",image= kaydetbutton ,font="Arial 14 bold",bg="pink",cursor='hand2',width=280 ,height=30 ,command=savefile)
save_button.place(x=305,y=215)

#fotoğrafları düzenlemek için fonksiyonlar
def photoedit(edit):
    global image
    global img
    global ima
    global im
    global siyahbeyazphotoab
    global maviliab
    global cizimab
    global kirmiziliab
    global yesilliab
    global negatifab
    global a
    global b
    global c
    global d
    global e
    global f
    
    #1.özellik fotoğrafın siyah-beyaz yapılması 
    if edit==1:
        siyahbeyazphoto= cv2.cvtColor(imager, cv2.COLOR_BGR2GRAY)
        siyahbeyazphotoa = imutils.resize(siyahbeyazphoto, width=int(photo_size/2.3))
        siyahbeyazphotoab = imutils.resize(siyahbeyazphoto, width=int(photo_size))
        
        cv2.imshow("Black and White",siyahbeyazphotoab)
        cv2.waitKey(0)
        
        # Fotoğrafın önizlemesini programa görüntü olarak verme
        ima = Image.fromarray(siyahbeyazphoto)
        im = Image.fromarray(siyahbeyazphotoa)
        img = ImageTk.PhotoImage(image=im)
        newphoto.configure(image=img),
        newphoto.image = img

        a = len(siyahbeyazphoto) #1. özelliğin seçildiğini programa anlatmak için len metodunu kullandım
        b = 0 #1. özellik seçilince diğer özellik seçimlerini iptal etmek için 0 yapıyorum
        c = 0
        d = 0
        e = 0
        f = 0
        
    #2. özellik fotoğrafa mavi tonlama yapılması    
    if edit==2:
        mavili= cv2.cvtColor(imager, cv2.COLOR_BGRA2RGB)
        mavilir = cv2.cvtColor(mavili, cv2.COLOR_BGRA2RGB) #mavi tonlama önizlemesi sorunlu olduğu için sadece bu özellik için 1 adet daha değişken ekledim
        mavilia = imutils.resize(mavilir, width=int(photo_size/2.3))
        maviliab = imutils.resize(mavili, width=int(photo_size))
        
        cv2.imshow("Blue",maviliab)
        cv2.waitKey(0)
        
        ima = Image.fromarray(mavilir)
        im = Image.fromarray(mavilia)
        img = ImageTk.PhotoImage(image=im)
        newphoto.configure(image=img)
        newphoto.image = img
        
        b = len(mavili)
        a = 0
        c = 0
        d = 0
        e = 0
        f = 0
        
    #3. özellik fotoğrafı çizim haline getirmesi
    if edit==3:
        grey= cv2.cvtColor(imager, cv2.COLOR_BGR2GRAY)
        grey= cv2.blur(grey,(2,1))
        edge = cv2.adaptiveThreshold(grey,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,11)
        color = cv2.bilateralFilter(imager,9,250,250)
        cizim = cv2.bitwise_and(color,color,mask=edge)
        cizimr = cv2.cvtColor(cizim, cv2.COLOR_BGR2RGB)
        cizima = imutils.resize(cizimr, width=int(photo_size/2.3))
        cizimab = imutils.resize(cizim, width=int(photo_size))
        
        cv2.imshow("Sketch",cizimab)
        cv2.waitKey(0)
        
        ima = Image.fromarray(cizimr)
        im = Image.fromarray(cizima)
        img = ImageTk.PhotoImage(image=im)
        newphoto.configure(image=img)
        newphoto.image = img
        
        resized = None
        c = len(cizim)
        a = 0
        b = 0
        d = 0
        e = 0
        f = 0
    
    #4. özellik fotoğrafa yeşil tonlama yapılması   
    if edit==4:
        green = np.full_like(imager,(0,255,0))
        yesilli = cv2.addWeighted(imager,0.5,green,0.5,0)
        yesillir = cv2.cvtColor(yesilli, cv2.COLOR_BGR2RGB)
        yesillia = imutils.resize(yesillir, width=int(photo_size/2.3))
        yesilliab = imutils.resize(yesilli, width=int(photo_size))
        
        cv2.imshow("Green",yesilli)
        cv2.waitKey(0)

        ima = Image.fromarray(yesillir)
        im = Image.fromarray(yesillia)
        img = ImageTk.PhotoImage(image=im)
        newphoto.configure(image=img)
        newphoto.image = img
        
        
        d = len(yesilli)
        a = 0
        b = 0
        c = 0
        e = 0
        f = 0
    
    #5. özellik fotoğrafa kırımızı tonlama yapılması    
    if edit==5:
        red = np.full_like(imager,(0,0,255))
        kirmizili = cv2.addWeighted(imager, 1 , red, 5 ,0)
        kirmizilir = cv2.cvtColor(kirmizili, cv2.COLOR_BGR2RGB)
        kirmizilia = imutils.resize(kirmizilir, width=int(photo_size/2.3))
        kirmiziliab = imutils.resize(kirmizili, width=int(photo_size))
        
        cv2.imshow("Red",kirmizili)
        cv2.waitKey(0)
        
        ima = Image.fromarray(kirmizilir)
        im = Image.fromarray(kirmizilia)
        img = ImageTk.PhotoImage(image=im)
        newphoto.configure(image=img)
        newphoto.image = img
        
        e = len(kirmizili)
        a = 0
        b = 0
        c = 0
        d = 0
        f = 0
        
    #6. özellik fotoğrafın negatif yapılması
    if edit==6:
        negatif = 1-imager
        negatifr = cv2.cvtColor(negatif, cv2.COLOR_BGR2RGB)

        negatifa = imutils.resize(negatifr, width=int(photo_size/2.3))
        negatifab = imutils.resize(negatif, width=int(photo_size))
                
        cv2.imshow("Negative",negatifab)
        cv2.waitKey(0) 
        
        ima = Image.fromarray(negatifr)
        im = Image.fromarray(negatifa)
        img = ImageTk.PhotoImage(image=im)
        newphoto.configure(image=img)
        newphoto.image = img
        
        f = len(negatif)
        a = 0
        b = 0
        c = 0
        d = 0
        e = 0

#buton fotoğrafları        
blackandwhitebutton = ImageTk.PhotoImage(file="blackandwhite.png")   
bluebutton = ImageTk.PhotoImage(file="blue.png")   
sketchbutton = ImageTk.PhotoImage(file="sketch.png")   
greenbutton = ImageTk.PhotoImage(file="green.png")   
redbutton = ImageTk.PhotoImage(file="red.png")   
negativebutton = ImageTk.PhotoImage(file="negative.png") 
  
#fotoğraf düzenleme butonları
sec1=Button(window,image=blackandwhitebutton ,text='Black and White',font='Times 15 bold ',bg='gray',activebackground='gray',activeforeground='white',cursor='hand2', width=185,height=50,command=lambda:photoedit(1))
sec1.place(x=10,y=320)

sec2=Button(window,image=bluebutton , text='Blue',font='Times 15 bold ',bg='lightblue',activebackground='blue',activeforeground='lightblue',cursor='hand2', width=185,height=50,command=lambda:photoedit(2))
sec2.place(x=400,y=520)

sec3=Button(window,image=sketchbutton ,text='Sketch',font='Times 15 bold ',bg='gray',activebackground='gray',activeforeground='white',cursor='hand2', width=185,height=50,command=lambda:photoedit(3))
sec3.place(x=10,y=420)

sec4=Button(window,image=greenbutton , text='Green',font='Times 15 bold ',bg='lightgreen',activebackground='green',activeforeground='lightgreen',cursor='hand2', width=185,height=50,command=lambda:photoedit(4))
sec4.place(x=400,y=420)

sec5=Button(window,image=redbutton , text='Red',font='Times 15 bold ',bg='pink',activebackground='red',activeforeground='pink',cursor='hand2', width=185,height=50,command=lambda:photoedit(5))
sec5.place(x=400,y=320)

sec6=Button(window,image=negativebutton, text='Negative',font='Times 15 bold ',bg='gray',activebackground='gray',activeforeground='white',cursor='hand2', width=185,height=50,command=lambda:photoedit(6))
sec6.place(x=10,y=520)
        
        
window.mainloop()
