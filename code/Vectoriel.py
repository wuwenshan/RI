#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 18:27:03 2019

@author: 3871772
"""
from IRModel import IRModel
from TextRepresenter import PorterStemmer
import math
import Utils

class Vectoriel(IRModel):
    def __init__(self,index,weighter,normalized):
        super().__init__(index)
        self._normalized = normalized
        self._weighter = weighter
    
    

    def getScores(self,query):
        """
            query : la requête
                renvoie le score des documents en utilisant le modèle vectoriel
        """
        dictScoresDocs = dict()
        dictWeightDocs = dict() # dict contenant les poids des termes des docs qui les contiennent
        ps = PorterStemmer()
        query_stemmed = ps.getTextRepresentation(query)
        for terme in query_stemmed.keys():
            weightDocs = self._weighter.getWeightsForStem(terme)
            #print(" voici weight docs : ",weightDocs)
            dictWeightDocs[terme] = weightDocs
        q = self._weighter.getWeightsForQuery(query_stemmed)
        #print (" i am q : ",q)
        for term,value in dictWeightDocs.items():
            for doc,occ in value.items():
                if doc in dictScoresDocs.keys():
                    #print("term : ",term)
                    #print("value : ",value)
                    #print("doc : ",doc)
                    #print("occ : ",occ)
                    dictScoresDocs[doc] += q[term]*occ
                    #print(" q terme ",q[term])
                    #print(" dict scores docs : ",dictScoresDocs)
                    
                else:
                    if Utils.isPresent(q,term):
                        dictScoresDocs[doc] = q[term]*occ
                    
        #print(" dict score doc :",dictScoresDocs)
        if self._normalized == False: # score produit scalaire
            return dictScoresDocs
        else: # similarité cosinus
            norme_q =  0
            for terme,value in q.items():
                if terme in query_stemmed:
                    norme_q += math.pow(value,2)
            norme_q = math.sqrt(norme_q)
            norme_d = dict()
            
            score_d = 0
            for cle in dictScoresDocs.keys():
                dictTerms = self._weighter.getWeightsForDoc(cle)
                for key,value in dictTerms.items():
                    if value != 0:
                        score_d += math.pow(value,2)
                norme_d[cle] = math.sqrt(score_d)
                score_d = 0                
            dictScoreCos = {doc:score/((norme_q)*(norme_d[doc])) for doc,score in dictScoresDocs.items()}
            return dictScoreCos
            

        
        
    