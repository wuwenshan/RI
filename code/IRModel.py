#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 17:11:36 2019

@author: 3871772
"""


from abc import abstractmethod
from indexerSimple import IndexerSimple

class IRModel(IndexerSimple):
    
    def __init__(self,index):
        self._index = index
        
    @abstractmethod    
    def getScores(self,query):
        pass    
       #renvoie un dictionnaire avec les docs comme clés et le score en value
    
    def getRanking(self,query):
        """ 
            query : le texte de la requête
                renvoie une liste de couple (doc,score) triée par ordre décroissant
        """
        scores_docs = self.getScores(query)
        sorted_scores_docs = sorted(scores_docs.items(), key = lambda tup:tup[1], reverse = True)
        return sorted_scores_docs
    
    
    
    

