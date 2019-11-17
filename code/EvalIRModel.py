#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 18:42:37 2019

@author: 3871772
"""

import numpy as np

class EvalIRModel():
    
    def __init__(self):
        """
        """
    
    def evaluation(self,model,requetes,mesure):
        """
            model : Oject IRModel modele de recherche de documents
            requetes : collection d'objet Query 
            mesure : Object EvalMesure modèle de mesure pour la requête et les documents
            renvoie la moyenne et l'écart-type de l'évaluation du modèle par rapport à la mesure et les requêtes
        """
        mesures = []
        for q in requetes.values():
            #documents retournés par la requete en utilisant le modèle model
            #getRanking prend en paramètre le texte de la requête
            doc_renvoyes = model.getRanking(q.W)
            #ajout dans mesures la valeur de la mesure d'évaluation retournée pour la requete q et le modèle model 
            mesures.append(mesure.evalQuery(doc_renvoyes,q))
        #print("mesures !!!!!!!!!!!!!!!!!!!!!",mesures)
        return np.mean(mesures),np.std(mesures)      