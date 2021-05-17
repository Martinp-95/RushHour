# -*- coding: utf-8 -*-
"""
Created on Sun May 07 11:11:12 2017

@author: martin
"""
from tkinter import *
from pickle import dump, load
from random import *
import json
from user import *


class vehicule(user):
    def __init__(self,unite, x, y):
        self.unite = unite
        self.x = x
        self.y = y

    def Niveau(self,unite,x,y):
        try:
            with open('vehicule.json') as json_data_r:
                data_dict = json.load(json_data_r)

            #Rectangles (invisible) se trouvant sur le cote de la grille afin de bloquer les rectangles a l'interieur de celle ci
            self.ext1 = self.canvas.create_rectangle(x+(-0.3*unite),y+(-100.4*unite),x+(29.9*unite),y+(-0.01*unite), outline="")
            self.ext2 = self.canvas.create_rectangle(x+(-100.4*unite),y+(-0.3*unite),x+(-0.01*unite),y+(29.9*unite), outline="")
            self.ext3 = self.canvas.create_rectangle(x+(-0.3*unite),y+(29.61*unite),x+(29.9*unite),y+(130*unite), outline="")
            self.ext4 = self.canvas.create_rectangle(x+(29.61*unite),y+(14.7*unite),x+(130*unite),y+(29.9*unite), outline="")
            self.ext5 = self.canvas.create_rectangle(x+(29.61*unite),y+(-0.3*unite),x+(130*unite),y+(9.9*unite), outline="")
            self.bloq =  [self.ext1,self.ext2,self.ext3,self.ext4,self.ext5]
            
            self.rectH = []
            self.rectV = []

            situation = randint(0, (len(data_dict["niveau"+str(self.niveau)])-1))

            #Rectangles du "jeu" a proprement parlé
            for e in data_dict["niveau"+str(self.niveau)][str(situation)]:
                data_vehicule = data_dict["niveau"+str(self.niveau)][str(situation)][e]

                if e == "carreRouge":
                    self.carreRouge = self.canvas.create_rectangle(x+(data_vehicule["x1"]*unite),y+(data_vehicule["y1"]*unite),
                    x+(data_vehicule["x2"]*unite),y+(data_vehicule["y2"]*unite), fill=data_vehicule["couleur"])
                    self.rectH.append(self.carreRouge)

                else:
                    self.e = self.canvas.create_rectangle(x+(data_vehicule["x1"]*unite),y+(data_vehicule["y1"]*unite),
                    x+(data_vehicule["x2"]*unite),y+(data_vehicule["y2"]*unite), fill=data_vehicule["couleur"])

                if data_vehicule["orientation"] == "h":
                    self.rectH.append(self.e)
                else:
                    self.rectV.append(self.e)

                self.rectAll = self.rectH + self.rectV +self.bloq

        except FileNotFoundError:
            print("Fichier vehicule.json n'existe pas ")
                                
    # def permettant de selectionner et bouger les rectangles objets
    def mouseDown(self, event):
        self.x1, self.y1 = event.x, event.y
        self.selObject = self.canvas.find_closest(self.x1, self.y1) 
    
    #Fonction qui nous permet de bloquer les rectangles objets entre eux mais aussi de "gagner" lorsque le rectangle rouge atteint une certaine coordonée      
    def FreeToMove(self,X=0,Y=0):
        coord = self.canvas.coords(self.selObject[0])
        cond = True
        if self.varVictoire == 0:
            for rect in self.rectAll:
                coordR = self.canvas.coords(rect)
                if self.selObject[0] == rect and self.varVictoire == 0:
                    if self.canvas.coords(self.carreRouge)[0] >= 650:
                        print ("Gagné !")
                        self.varVictoire = 1
                        self.sauvegarde(self.pseudo,self.score)
                        self.niveausuivant(self.score)
                        break
                elif(coordR[0]<=coord[0]+X<=coordR[2] and coordR[1]<=coord[1]+Y<=coordR[3]) or\
                    (coordR[0]<=coord[2]+X<=coordR[2] and coordR[1]<=coord[3]+Y<=coordR[3]) or\
                    (coordR[0]<=coord[2]+X<=coordR[2] and coordR[1]<=coord[1]+Y<=coordR[3]) or\
                    (coordR[0]<=coord[0]+X<=coordR[2] and coordR[1]<=coord[3]+Y<=coordR[3]):
                    cond = False
                    break
        return cond
        
    # def permettant de selectionner et bouger les rectangles objets
    def mouseMove(self, event):
        x2, y2 = event.x, event.y
        dx, dy = x2 -self.x1, y2 -self.y1
        if self.selObject and self.varVictoire == 0:
            if self.selObject[0] in self.rectV:
                if self.FreeToMove(Y=dy):
                    self.canvas.move(self.selObject, 0, dy)
            elif self.selObject[0] in self.rectH:
                if self.FreeToMove(X=dx):
                    self.canvas.move(self.selObject, dx, 0)
            self.x1, self.y1 = x2, y2
     
    # def permettant de selectionner et bouger les rectangles objets
    def mouseUp(self, event):
        try:
            if self.selObject and self.varVictoire == 0:
                self.canvas.itemconfig(self.selObject[0], width = 1)
                self.selObject =None
        except:
            pass