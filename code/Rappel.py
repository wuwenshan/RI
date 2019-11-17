# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 00:07:37 2019

@author: Emmanuel
"""

from EvalMesure import EvalMesure


class Rappel(EvalMesure):
    def __init__(self,k):
        super().__init__(k)
        
        
    def getK(self):
        return self._k
    
    def setK(self,k):
        self._k = k
    
    def evalQuery(self,liste,query):
        """
            liste : liste de couple(document,score)
            query : Object Query
            renvoie la mesure d'évaluation rappel associée à la requête
        """
        #identifiants des documents pertinents pour query       
        relevants = query.Idocs
        #nombre de documents pertinents retournés dans liste jusqu'au rang k
        nb_rel = 0
        for num_doc,score in liste[:self._k]:
             if num_doc in relevants:
                 nb_rel += 1
        try :         
            rappel_k = nb_rel/len(relevants)
        except ZeroDivisionError:
            return 0
        return rappel_k