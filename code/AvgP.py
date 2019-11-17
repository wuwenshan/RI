# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 11:02:25 2019

@author: Emmanuel
"""
from Precision import Precision
from EvalMesure import EvalMesure


class AvgP(EvalMesure):
        def __init__(self,k):
            super().__init__(k)
        
        
        
        def evalQuery(self,liste,query):
            """
            liste : liste de couple(document,score)
            query : Object Query
            renvoie la mesure d'évaluation précision moyenne par rapport à la requête
            """ 
            somme = 0
            for i in range(len(liste)):
                num_doc,score = liste[i]
                if num_doc in query.Idocs:
                    precision = Precision(i+1)
                    p = precision.evalQuery(liste,query)
                    #print("précision du doc : "+str(num_doc)+" = ",p)
                    #print("rang : ",i+1)
                    somme += p
            try :
                return somme/len(query.Idocs)
            except :
                return 0
            