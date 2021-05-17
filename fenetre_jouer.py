# -*- coding: utf-8 -*-
"""
@author: marti and cyril
"""

from tkinter import *
from fenetre_profil import *
import json



#Def qui permet de dire si un pseudo est deja enregisté

def verif_pseudo(canvas_jouer,fenetre_P,Fenetre_Jouer,pseudo,Fenetre_Principale):
    try:
        if pseudo == "":
            print("Vous n'avez pas rentrer de pseudo")
            message_info = Message(canvas_jouer,text="Vous n'avez pas rentrer de pseudo",width=300,bg='red')
            message_info.place(anchor=CENTER, x=450,y=400)

        else:
            with open('sauvegarde.json') as json_data_r:
                data_dict = json.load(json_data_r)
                
            if pseudo in data_dict.keys():
                Fenetre_profil(canvas_jouer,fenetre_P,Fenetre_Jouer,pseudo,Fenetre_Principale,0,NONE)
                        
            else:
                data_dict[pseudo] = {"historique":[0,0,0],"score":[0,0,0]}
                with open('sauvegarde.json','w') as json_data_w:
                    json.dump(data_dict,json_data_w)
                    print("Joueur ajouter")
                Fenetre_profil(canvas_jouer,fenetre_P,Fenetre_Jouer,pseudo,Fenetre_Principale,0,NONE)
    
    except FileNotFoundError:
        print("Fichier sauvegarde.json n'existe pas ")
        with open('sauvegarde.json','a') as json_data_c:
            json.dump({pseudo:{"historique":[0,0,0],"score":[0,0,0]}},json_data_c)
            print("Fichier sauvegarde.json a été crée")


 
   

#Fonction de la fenêtre Jouer
def Fenetre_Jouer(fenetre_P,Fenetre_Principale,canvas_general,canvas_profil,fenetre_destroy):
    print("Fenetre_Jouer")
    
    if fenetre_destroy == 0:
        canvas_general.destroy()
    if fenetre_destroy == 1:
        canvas_profil.destroy()

    canvas_jouer = Canvas(fenetre_P,width=900, height=800,bg='sky blue')
    canvas_jouer.pack(side=TOP, fill=BOTH, expand=YES)
    
    #Mise en page (Fenêtre, Titre, Texte, Entrée Texte, Boutons)
    fenetre_P['bg']='sky blue'
    fenetre_P.title('UNBLOCK THE BLOCK')
    
    label1 = Label(canvas_jouer, text="Règle du jeu",bg = 'sky blue',font="Arial 16 underline ")
    label2 = Label(canvas_jouer, text="    Le but du jeu est simple :\n\
    \n    Il faut faire sortir le Rectangle Rouge du PUZZLE dans le temps imparti.\
    \n    Vous commencerez avec un total de '2000 points' pour chaque niveaux.\
    \n    Votre but sera donc de terminer chaque niveau le plus vite possible afin d'avoir un maximum de points a la fin du niveau !\n\n\
    \n    Sachant que :\n\
    \n    - Pour le 'NIVEAU 1' vous perdrez 5 points toutes les secondes;\
    \n               - Pour le 'NIVEAU 2' vous perdrez 10 points toutes les secondes;\
    \n          - Pour le 'NIVEAU 3' vous perdrez 20 points toutes les secondes.",bg = 'sky blue',font="Arial 12")
    label3 = Label(canvas_jouer, text=" Entrez votre nom :",bg = 'sky blue',font="Arial 8 bold")
    
    label1.pack(padx=0,pady=35)
    label2.pack(padx=0,pady=30)
    label3.pack(padx=0,pady=10)
    
    pseudo = StringVar() 
    pseudo.set("")
    
    entree = Entry(canvas_jouer, textvariable=pseudo, width=20,bg='white')
    entree.pack(padx=0,pady=5)
    boutonGO = Button(canvas_jouer, text="Profil", command= lambda: verif_pseudo(canvas_jouer,fenetre_P,Fenetre_Jouer,pseudo.get(),Fenetre_Principale),fg ='black',bg = '#66EC62',activebackground='light green',font="Arial 11 bold",width =35, height = 1)
    boutonGO.pack(padx=0,pady=15)
    
    label4 = Label(canvas_jouer,text="     Le jeu a été réalisé par :\n\
    \n    PERDAENS Martin\
    \n  TONGRES Cyril",bg ='#A0E3F7',font="Arial 10")
    label4.pack(padx=0,pady=15)
    
    
    bRetour = Button(canvas_jouer, text="RETOUR AU MENU", command=lambda :Fenetre_Principale(fenetre_P,canvas_jouer,NONE,0),fg ='black',bg = '#FD4141',activebackground='#F96E6E',font="Arial 11 bold ",width =35, height = 1)
    bRetour.pack(padx=0,pady=15)
    fenetre_P.mainloop()

