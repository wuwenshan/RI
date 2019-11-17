# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 20:41:53 2019

@author: Emmanuel
"""
from EvalMesure import EvalMesure


class Precision(EvalMesure):
    def __init__(self,k):
        """ k : le rang de la mesure de précision """
        super().__init__(k)
        
        
    def getK(self):
        return self._k
    
    def setK(self,k):
        self._k = k
    
    def evalQuery(self,liste,query):
        """
            liste : liste de couple(document,score)
            query : Object Query
            renvoie la mesure d'évaluation précision associée à la requête
        """
        #identifiants des documents pertinents pour query       
        relevants = query.Idocs
        #nombre de documents pertinents retournés dans liste
        nb_rel = 0
        for num_doc,score in liste[:self._k]:
             if num_doc in relevants:
                 nb_rel += 1
        precision_k = nb_rel/self._k
        #print("nombre de docs pertinents renvoyés pour la requête "+ str(query.I)+ " : ",nb_rel)
        #print("précision au rang : "+ str(self._k))
        #print("resultat :",precision_k)
        return precision_k
 
        
        


        