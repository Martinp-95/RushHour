# -*- coding: utf-8 -*-
"""
@author: marti and cyril
"""

from tkinter import *
from pickle import dump, load
from fenetre_charger import *
from fenetre_jouer import *    

#----------------------------------Programme Fenetre Principale-----------------------------------------

#Fonction de la fenêtre principale
def Fenetre_Principale(fenetre_P,canvas_jouer, canvas_classement,fenetre_destroy):

    if fenetre_destroy == 0:
        canvas_jouer.destroy()
    if fenetre_destroy == 1:
        canvas_classement.destroy()    
    
    #Mise en page de la fenetre (Titre, Canvas, Image, Boutons)
    canvas_general = Canvas(fenetre_P,width=900, height=800,bg='light yellow')
    canvas_general.pack(side=TOP, fill=BOTH, expand=YES)

    
    label = Label(canvas_general, text="Unblock The Block",font="Arial 20 italic underline",bg='light yellow',fg ='brown')
    label.pack(padx=0,pady=20)
    
    photo = PhotoImage(file="Image_Grille_page_de_garde_.gif")
    
    canvas = Canvas(canvas_general,width=505, height=397,bg='white')
    canvas.create_image(5, 5, anchor=NW, image=photo)
    canvas.pack(padx=0,pady=5)
    # NORMAL ou DISABLED
    boutonQ = Button(canvas_general, text="QUITTER", bd =10, command = fenetre_P.destroy, font="Arial 16 bold",bg= 'tomato',activebackground='tomato3',relief="groove", width =20, height =1)
    boutonC = Button(canvas_general, text="CLASSEMENT", bd =10,state = NORMAL, command = lambda: Fenetre_Charger(fenetre_P,Fenetre_Principale,canvas_general), font="Arial 16 bold",bg= 'sky blue',activebackground='sky blue',relief="groove", width = 20, height =1)
    boutonJ = Button(canvas_general, text="JOUER", bd =10, command = lambda: Fenetre_Jouer(fenetre_P,Fenetre_Principale,canvas_general,NONE,0), font="Arial 16 bold",bg= '#66EC62',activebackground='light green',relief="groove", width =20, height =1)
    boutonQ.pack(side = BOTTOM,padx=0, pady=20)
    boutonC.pack(side = BOTTOM,padx=0, pady=0)
    boutonJ.pack(side = BOTTOM,padx=0, pady=20)


    fenetre_P.mainloop()
#----------------------------------------------------------------------------------------------

#----------------------------------Programme Principal-----------------------------------------
fenetre_P = Tk()
fenetre_P.minsize(width=900, height=800)
fenetre_P.maxsize(width=900, height=800)
fenetre_P['bg']='light yellow'
fenetre_P.title('UNBLOCK THE BLOCK')
fenetre_P.iconbitmap("image_grille_page_de_garde.ico")
Fenetre_Principale(fenetre_P,NONE,NONE,NONE)
#----------------------------------------------------------------------------------------------

