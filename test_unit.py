import unittest
from fenetre_jouer import *
from fenetre_charger import *
from user import *


with open('vehicule.json') as json_data_r:
        data_car = json.load(json_data_r)

def verif_pseudo(canvas_jouer,fenetre_P,Fenetre_Jouer,pseudo,Fenetre_Principale):
    if pseudo == "":
        #print("Vous n'avez pas rentrer de pseudo")
        #message_info = Message(canvas_jouer,text="Vous n'avez pas rentrer de pseudo",width=300,bg='red')
        #message_info.place(anchor=CENTER, x=450,y=400)
        return ""


    else:
        return pseudo
    

class TestProjet(unittest.TestCase):
    def __init__(self, methodName):
        super().__init__(methodName)
        self.varVictoire = 0
        self.pseudo = ""

        self.data_dict= {"martin": {"historique": [1, 2, 3], "score": [1960, 1740, 1180]}, 
        "cyril": {"historique": [0, 0, 0], "score": [0, 0, 2000]}, 
        "tata": {"historique": [1, 0, 0], "score": [1960, 0, 0]}}

        self.data_dict_delete= {"martin": {"historique": [1, 2, 3], "score": [1960, 1740, 1180]}, 
        "cyril": {"historique": [0, 0, 0], "score": [0, 0, 2000]}, 
        "tata": {"historique": [1, 0, 0], "score": [1960, 0, 0]}}

        self.dict_classement1={'joueur': {0: 'martin', 1: 'cyril', 2: 'tata'}, 'niveau 1': {0: 1960, 1: 0, 2: 1960}}
        self.dict_classement2={'joueur': {0: 'martin', 1: 'cyril', 2: 'tata'}, 'niveau 2': {0: 1740, 1: 0, 2: 0}}
        self.dict_classement3={'joueur': {0: 'martin', 1: 'cyril', 2: 'tata'}, 'niveau 3': {0: 1180, 1: 0, 2: 0}}
    
    def ScoreJoueur(self):
    #Def permettant d'ajuster l'enlevement des points par niveau et par secondes        
        if self.score > 0 and self.varVictoire == 0:
            self.score -= 20

    def delete(self,li_sauvegarde,pseudo,data_dict,index_delete):
        
        self.historique = li_sauvegarde
        for y in self.historique:
            self.historique[index_delete] = 0
            break
            data_dict_delete[pseudo]["historique"] = self.historique



#=================================================================================
    def test_Fenetre_Charger (self):
        self.assertEqual(type(self.dict_classement1), dict)
        self.assertEqual(type(self.dict_classement2), dict)
        self.assertEqual(type(self.dict_classement3), dict)
        self.assertEqual(self.dict_classement1["joueur"][0], "martin")
        
    def test_jsonProfil (self):
        self.assertEqual(self.data_dict["martin"]["historique"][0], 1)
        self.assertEqual(self.data_dict["cyril"]["score"][0], 0)
        self.assertEqual(type(self.data_dict["martin"]["historique"]), list)
        self.assertEqual(type(self.data_dict["cyril"]["score"]), list)
        self.assertEqual(type(self.data_dict["cyril"]["score"][0]), int)

        self.assertIsNot(type(self.data_dict["martin"]["historique"]), dict)
        self.assertIsNot(self.data_dict["cyril"]["score"][0], 1)

    def test_jsonCar (self):
        self.assertEqual(type(data_car["niveau1"]["0"]["v1"]["couleur"]), str)
        self.assertEqual(type(data_car["niveau1"]["0"]["v1"]["orientation"]), str)
        self.assertEqual(data_car["niveau1"]["0"]["v1"]["orientation"], "h")

        self.assertIsNot(data_car["niveau1"]["0"]["v1"]["orientation"], "v")
        self.assertIsNot(type(data_car["niveau1"]["0"]["v1"]["orientation"]), int)
    
    def test_classementValue(self):
        self.assertGreater(self.data_dict["martin"]["score"][0], self.data_dict["cyril"]["score"][0])
        self.assertLess(self.data_dict["cyril"]["score"][0], self.data_dict["martin"]["score"][0])

        self.assertGreater(self.data_dict["cyril"]["score"][2], self.data_dict["martin"]["score"][2])
        self.assertLess(self.data_dict["martin"]["score"][2], self.data_dict["cyril"]["score"][2])
    

    def test_score(self):
        index= 10
        index2 = 26
        self.score = 2000
        while index > 0:
            self.ScoreJoueur()
            index -= 1
        self.assertEqual(self.score, 1800)
        self.assertIsNot(self.score, 1801)
        self.assertIsNot(self.score, 0)
        self.assertIsNot(self.score, -1000)


        self.score = 2000
        while index2 > 0:
            self.ScoreJoueur()
            index2 -= 2
        self.assertEqual(self.score, 1740)
        self.assertIsNot(self.score, 1801)
        self.assertIsNot(self.score, 0)
        self.assertIsNot(self.score, -1000)
    
    def test_pseudo(self):
        
        self.assertEqual(verif_pseudo(NONE,NONE,NONE,"toto",NONE), "toto")
        self.assertEqual(verif_pseudo(NONE,NONE,NONE,"",NONE), "")
        self.assertIsNot(verif_pseudo(NONE,NONE,NONE,"toto",NONE), "")
        self.assertIsNot(verif_pseudo(NONE,NONE,NONE,"",NONE), "toto")

    def test_delete(self):
        li_sauvegarde = self.data_dict_delete["martin"]["historique"]
        pseudo = self.dict_classement1["joueur"][0]
        data_dict = self.data_dict_delete
        index_delete = 0

        self.delete(li_sauvegarde,pseudo,data_dict,index_delete)

        self.assertEqual(self.data_dict_delete["martin"]["historique"][0], 0)
        self.assertIsNot(self.data_dict_delete["martin"]["historique"][0], 1)


if __name__ == '__main__':
    unittest.main()