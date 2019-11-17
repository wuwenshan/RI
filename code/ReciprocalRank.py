#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 12:11:19 2019

@author: 3871772
"""
from EvalMesure import EvalMesure


class ReciprocalRank(EvalMesure):
    def __init__(self,k):
        super().__init__(k)
        
        
    """ mesure de précision moyenne """    
    def evalQuery(self,liste,query):
        """
            liste : liste de couples (document,score) retournés par le modéle
            query : objet Query sur dont la liste est liée
            
            renvoie la mesure reciprocal rank de la requête
        """
        for i in range(self._k):
            if i < len(liste):
                num_doc,score = liste[i]
                if num_doc in query.Idocs:
                    #print("Premier doc pertinent = ",num_doc)
                    #print("Position : ",i)
                    return round(1/(i+1),3)
        
        return 0
    
           