# -*- coding: utf-8 -*-
"""
@author: marti and cyril
"""

from tkinter import *
from niveau_1 import *
from niveau_2 import *
from niveau_3 import *
import json
from user import *

#Fonction de la fenêtre Jouer
def Fenetre_profil(canvas_jouer,fenetre_P,Fenetre_Jouer,pseudo,Fenetre_Principale,fenetre_d,canvas_level):
    try:
        print("Fenetre_profil")

        if fenetre_d == 0:
            canvas_jouer.destroy()
        if fenetre_d == 1:
            canvas_level.destroy()

        canvas_profil = Canvas(fenetre_P,width=900, height=800,bg='sky blue')
        canvas_profil.pack(side=TOP, fill=BOTH, expand=YES)
        
        #Mise en page (Fenêtre, Titre, Texte, Entrée Texte, Boutons)
        fenetre_P['bg']='sky blue'
        fenetre_P.title('UNBLOCK THE BLOCK')
        joueur = user(pseudo)


        label1 = Label(canvas_profil, text="Profil de {0}".format(pseudo),bg = 'sky blue',font="Arial 16 underline ")
        label1.pack(padx=0,pady=35)

        boutonGO = Button(canvas_profil, text="Jouer", command= lambda: ApplicationNv1(10, 300,  125,score,fenetre_P,canvas_profil,joueur.pseudo,Fenetre_profil,Fenetre_Principale,Fenetre_Jouer),fg ='black',bg = '#66EC62',activebackground='light green',font="Arial 11 bold",width =35, height = 1)
        boutonGO.pack(padx=0,pady=15)

        bRetour = Button(canvas_profil, text="RETOUR AU MENU", command=lambda :Fenetre_Jouer(fenetre_P,Fenetre_Principale,NONE,canvas_profil,1),fg ='black',bg = '#FD4141',activebackground='#F96E6E',font="Arial 11 bold ",width =35, height = 1)
        bRetour.pack(padx=0,pady=15)
        
        label2 = Label(canvas_profil, text="Sauvegarde",bg = 'sky blue',font="Arial 16 underline ")
        label2.pack(padx=0,pady=0)

        #Partie pour récuperer les données du fichier json sauvegarde
        with open('sauvegarde.json') as json_data_r:
            data_dict = json.load(json_data_r)

        Frame1 = Frame(canvas_profil,width=900, height=550, bg="sky blue")
        Frame1.pack(padx=0,pady=0) #mettre une scroobar

        index_chargement = 0
        varY = 100

        for x in data_dict:
            if x == pseudo:
                for y in range(len(data_dict[x]["historique"])):
                    #print(y)
                    li_sauvegarde = data_dict[x]["historique"]
                    if data_dict[x]["historique"][index_chargement] != 0:
                        if data_dict[x]["historique"][index_chargement] == 1:
                            niveau = lambda: ApplicationNv1(10, 300,  125,score,fenetre_P,canvas_profil,pseudo,Fenetre_profil,Fenetre_Principale,Fenetre_Jouer)
                        elif data_dict[x]["historique"][index_chargement] == 2:
                            niveau = lambda: ApplicationNv2(10, 300,  125,score,fenetre_P,canvas_profil,pseudo,Fenetre_profil,Fenetre_Principale,Fenetre_Jouer)
                        else:
                            niveau = lambda: ApplicationNv3(10, 300,  125,score,fenetre_P,canvas_profil,pseudo,Fenetre_profil,Fenetre_Principale,Fenetre_Jouer)

                        sauvegardeJ= "Niveau: "+str(data_dict[x]["historique"][index_chargement])
                        bSave = Button(Frame1, text=sauvegardeJ,command=  niveau,fg ='black',
                        bg = '#FEA347',activebackground='grey',font="Arial 11 bold ",width =35, height = 2).place(anchor=CENTER, x=250, y=varY)
                        
                        bDelete = Button(Frame1, text="Supprimer \nla Sauvegarde n°"+str(y+1),command= lambda y=y: joueur.delete(li_sauvegarde,pseudo,data_dict,y),
                        fg ='red',bg = '#FEA347',activebackground='grey',font="Arial 11 bold ",width =35, height = 2).place(anchor=CENTER, x=650, y=varY)

                        varY += 100
                    index_chargement += 1

        fenetre_P.mainloop()
        
    except FileNotFoundError:
        print("Fichier sauvegarde.json n'existe pas ")

