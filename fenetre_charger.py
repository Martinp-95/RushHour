# -*- coding: utf-8 -*-
"""
@author: marti and cyril
"""

from tkinter import *
from PIL import Image
import pandas as pd
import json

#Fonction de la fenêtre Charger
def Fenetre_Charger(fenetre_P, Fenetre_Principale,canvas_general):
    try:
        canvas_general.destroy()
        print("Fenetre_Classement")

        #Partie pour récuperer les données du fichier json sauvegarde
        with open('sauvegarde.json') as json_data_r:
            data_dict = json.load(json_data_r)
        
        #structure des données pour les joueurs par niveau avec leurs scores
        indice = 0
        dict_classement1={"joueur":{},"niveau 1":{}}
        dict_classement2={"joueur":{},"niveau 2":{}}
        dict_classement3={"joueur":{},"niveau 3":{}}

        for e in data_dict:
            dict_classement1["joueur"][indice]=e
            dict_classement1["niveau 1"][indice]=data_dict[e]["score"][0]
            dict_classement2["joueur"][indice]=e
            dict_classement2["niveau 2"][indice]=data_dict[e]["score"][1]
            dict_classement3["joueur"][indice]=e
            dict_classement3["niveau 3"][indice]=data_dict[e]["score"][2]
            indice += 1

        #print(dict_classement1)
        #print(dict_classement2)
        #print(dict_classement3)

        data1 = pd.DataFrame.from_dict(dict_classement1)
        data2 = pd.DataFrame.from_dict(dict_classement2)
        data3 = pd.DataFrame.from_dict(dict_classement3)

        #trier l'ordre de classement sur les scores par niveau
        data1 = data1.sort_values(by=["niveau 1"], ascending=False)
        data1 = data1.reset_index(inplace=False)
        del data1["index"]
        data2 = data2.sort_values(by=["niveau 2"], ascending=False)
        data2 = data2.reset_index(inplace=False)
        del data2["index"]
        data3 = data3.sort_values(by=["niveau 3"], ascending=False)
        data3 = data3.reset_index(inplace=False)
        del data3["index"]

        #print(data2)
        
        #Mise en page (Fenêtre, Titre, Texte, Boutons)
        canvas_classement = Canvas(fenetre_P,width=900, height=800,bg='sky blue')
        canvas_classement.pack(side=TOP, fill=BOTH, expand=YES)
        fenetre_P['bg']='sky blue'
        fenetre_P.geometry("900x800")
        fenetre_P.title('UNBLOCK THE BLOCK')

        label = Label(canvas_classement, text="Classement",bg = 'sky blue',font="Arial 16 underline ")
        label.pack(padx=0,pady=50)

        #mise en page des colonnes pour les classements
        labelNiveau1 = Label(canvas_classement, text=data1, bg='sky blue', font = "Arial 13")
        labelNiveau2 = Label(canvas_classement, text=data2, bg='sky blue', font = "Arial 13")
        labelNiveau3 = Label(canvas_classement, text=data3, bg='sky blue', font = "Arial 13")
        
        labelNiveau1.place(anchor=CENTER, x=150, y=150)
        labelNiveau2.place(anchor=CENTER, x=450, y=150)
        labelNiveau3.place(anchor=CENTER, x=750, y=150)

        bRetour = Button(canvas_classement, text="RETOUR AU MENU", command=lambda :Fenetre_Principale(fenetre_P,NONE,canvas_classement,1),fg ='black',bg = '#FD4141',activebackground='#F96E6E',font="Arial 11 bold ",width =35, height = 1)
        bRetour.place(anchor=CENTER, x=450, y=600)
        fenetre_P.mainloop()

    except FileNotFoundError:
        print("Fichier sauvegarde.json n'existe pas ")
