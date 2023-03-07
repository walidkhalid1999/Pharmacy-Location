from tkinter import *
from tkintermapview import TkinterMapView


root = Tk()
root.geometry("1000x500")
root.title("Pharmacy")
root.configure(background="white")
title1 = Label(root ,
               text="Pharmacies" , 
               fg="white",
               bg="gray",
               font=("calibri" , 18) )
title1.pack(fill=X)

#=========Functions for Buttons============
def EmanPharm():
    map = TkinterMapView(root,
                         height=400,
                         width=500,
                         corner_radius=0
                         )
    map.place(x=450 , y=50)
    map.set_zoom(15)
    map.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga" , max_zoom=22)
    map.set_position(30.109904398780174, 31.344739847059323)
    marker=map.set_marker(30.109904398780174, 31.344739847059323)
    marker.set_text("Eman Pharmacy")
def Pharm19011():
    map = TkinterMapView(root,
                         height=400,
                         width=500,
                         corner_radius=0
                         )
    map.place(x=450 , y=50)
    map.set_zoom(15)
    map.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga" , max_zoom=22)
    map.set_position(30.06652402012913, 31.27823691786921)
    marker=map.set_marker(30.06652402012913, 31.27823691786921)
    marker.set_text("19011 Pharmacy")
def EzzabyPharm():
    map = TkinterMapView(root,
                         height=400,
                         width=500,
                         corner_radius=0
                         )
    map.place(x=450 , y=50)
    map.set_zoom(15)
    map.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga" , max_zoom=22)
    map.set_position(30.047316000000087, 31.238505236921377)
    marker=map.set_marker(30.047316000000087, 31.238505236921377)
    marker.set_text("Ezzaby Pharmacy")
def SeifPharm():
    map = TkinterMapView(root,
                         height=400,
                         width=500,
                         corner_radius=0
                         )
    map.place(x=450 , y=50)
    map.set_zoom(15)
    map.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga" , max_zoom=22)
    map.set_position(30.064386758985588, 31.21637510000189)
    marker=map.set_marker(30.064386758985588, 31.21637510000189)
    marker.set_text("Seif Pharmacy")
def AliAliPahrm():
    map = TkinterMapView(root,
                         height=400,
                         width=500,
                         corner_radius=0
                         )
    map.place(x=450 , y=50)
    map.set_zoom(15)
    map.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga" , max_zoom=22)
    map.set_position(30.027168258331333, 31.23235932944964)
    marker=map.set_marker(30.027168258331333, 31.23235932944964)
    marker.set_text("Ali&Ali Pharmacy")
def Radypharm():
    map = TkinterMapView(root,
                         height=400,
                         width=500,
                         corner_radius=0
                         )
    map.place(x=450 , y=50)
    map.set_zoom(15)
    map.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga" , max_zoom=22)
    map.set_position(30.142200397084114, 31.38490449062049)
    marker=map.set_marker(30.142200397084114, 31.38490449062049)
    marker.set_text("Rady Pharmacy")
def AdelKhalidPharm():
    map = TkinterMapView(root,
                         height=400,
                         width=500,
                         corner_radius=0
                         )
    map.place(x=450 , y=50)
    map.set_zoom(15)
    map.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga" , max_zoom=22)
    map.set_position(30.14228822808564, 31.38371128886215)
    marker=map.set_marker(30.14228822808564, 31.38371128886215)
    marker.set_text("Adel Khalid Pharmacy")
def FardousPharm():
    map = TkinterMapView(root,
                         height=400,
                         width=500,
                         corner_radius=0
                         )
    map.place(x=450 , y=50)
    map.set_zoom(15)
    map.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga" , max_zoom=22)
    map.set_position(30.139778159677252, 31.385140173963105)
    marker=map.set_marker(30.139778159677252, 31.385140173963105)
    marker.set_text("Fardous Pharmacy")
def NozhaPharm():
    map = TkinterMapView(root,
                         height=400,
                         width=500,
                         corner_radius=0
                         )
    map.place(x=450 , y=50)
    map.set_zoom(15)
    map.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga" , max_zoom=22)
    map.set_position(30.106562634696736, 31.344518900238622)
    marker=map.set_marker(30.106562634696736, 31.344518900238622)
    marker.set_text("Nozha Pharmacy")
def cu():
    country = En.get()
    map.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga" , max_zoom=22)
    map.set_address(country , marker=True)


#============logo=============
logo = PhotoImage(file="images.png")
lab_log = Label(root , 
                image=logo , 
                bd=0 , 
                bg="white")
lab_log.place(x=30 , y=40)

#============= Label + Entry + Button  ================
l = Label(root ,
          text="Country" , 
          fg="Black",
          bg="white",
          font=("calibri" , 18) )
l.place(x=10 , y= 280)

En = Entry(root ,
           width=10 , 
           fg="Black",
           bd=3,
           font=("calibri" , 18),
           relief=GROOVE )
En.place(x=150 , y=285)

B1 = Button(root ,
            text="Get Country" , 
            fg="white",
            bg="gray",
            bd=1,
            font=("calibri" , 13),
            cursor="hand2",
            relief=SOLID,
            width=10,
            command=cu    )
B1.place(x=300 , y=285)

#==========Pharmacy Buttons=============
b1 = Button(root ,
            text="ايمان" , 
            fg="black",
            bg="white",
            bd=1,
            font=("calibri" , 13),
            cursor="hand2",
            relief=SOLID,
            width=13,
            command=EmanPharm 
            )
b1.place(x=10 , y=330)

b2 = Button(root ,
            text="19011" , 
            fg="black",
            bg="white",
            bd=1,
            font=("calibri" , 13),
            cursor="hand2",
            relief=SOLID,
            width=13,
            command=Pharm19011  )
b2.place(x=150 , y=330)

b3 = Button(root ,
            text="العزبى" , 
            fg="black",
            bg="white",
            bd=1,
            font=("calibri" , 13),
            cursor="hand2",
            relief=SOLID,
            width=13,
              command=EzzabyPharm  )
b3.place(x=290 , y=330)

b4 = Button(root ,
            text="على على" , 
            fg="black",
            bg="white",
            bd=1,
            font=("calibri" , 13),
            cursor="hand2",
            relief=SOLID,
            width=13,
            command=AliAliPahrm  )
b4.place(x=10 , y=370)

b5 = Button(root ,
            text="سيف" , 
            fg="black",
            bg="white",
            bd=1,
            font=("calibri" , 13),
            cursor="hand2",
            relief=SOLID,
            width=13,
            command=SeifPharm  )
b5.place(x=150 , y=370)

b6 = Button(root ,
            text="راضى" , 
            fg="black",
            bg="white",
            bd=1,
            font=("calibri" , 13),
            cursor="hand2",
            relief=SOLID,
            width=13,
            command=Radypharm  )
b6.place(x=290 , y=370)

b7 = Button(root ,
            text="عادل و خالد" , 
            fg="black",
            bg="white",
            bd=1,
            font=("calibri" , 13),
            cursor="hand2",
            relief=SOLID,
            width=13,
            command=AdelKhalidPharm  )
b7.place(x=10 , y=410)

b8 = Button(root ,
            text="الفردوس" , 
            fg="black",
            bg="white",
            bd=1,
            font=("calibri" , 13),
            cursor="hand2",
            relief=SOLID,
            width=13,
            command=FardousPharm  )
b8.place(x=150 , y=410)

b9 = Button(root ,
            text="النزهه" , 
            fg="black",
            bg="white",
            bd=1,
            font=("calibri" , 13),
            cursor="hand2",
            relief=SOLID,
            width=13,
            command=NozhaPharm  )
b9.place(x=290 , y=410)

map=TkinterMapView(root,
                   corner_radius=1,
                   width=500,
                   height=400,
                   )
map.place(x=450 , y=50)

root.mainloop()