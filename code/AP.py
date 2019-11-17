# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 00:29:13 2019

@author: Emmanuel
"""
from EvalMesure import EvalMesure
import Precision

class AP(EvalMesure):
    def __init__(self,k):
        super().__init__(k)
        
    def evalQuery(self,liste,query):
        #instanciation des classes Precision et Rappel afin d'utiliser leur méthode evalQuery
        somme = 1
        #documents perinents pour la requête
        rel = query.getIdoc()
        for num_doc in rel:
            #k = indice de num_doc dans la liste des docs renvoyés
            #on l'incrémente car les indices commencent à 0
            k = list.index(num_doc)
            k += 1
            #calcul de P@k
            pre = Precision(k)
            precision = pre.evalQuery(liste,query)
            somme += precision
            
        return somme/len(rel)