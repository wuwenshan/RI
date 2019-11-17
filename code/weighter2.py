#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 17:17:58 2019

@author: 3874034
"""

from weighter import Weighter
from collections import Counter

class Weighter2(Weighter):
    
    def __init__(self,index):
        super().__init__(index)
        
        
    def getWeightsForDoc(self,idDoc):
        """
            idDoc : id du document
            renvoie le poids des termes pour le document
        """
        return self._index.getTfsForDoc(idDoc)
    
    def getWeightsForStem(self,stem):
        """
            stem : terme après preprocessing
            renvoie le poids de stem pour tous les documents qui le contiennent
        """
        if stem in self._index.getIndexInv().keys():
            return self._index.getTfsForStem(stem)
        else:
            return dict()
    
    def getWeightsForQuery(self,query):
        q = query.split(" ")
        #print(" dict : ",dict(Counter(q)))
        return dict(Counter(q))
        
    
    


