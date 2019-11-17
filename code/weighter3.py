#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 17:22:31 2019

@author: 3874034
"""

from weighter import Weighter
from math import log

class Weighter3(Weighter):
    
    def __init__(self,index):
        super().__init__(index)

    def getWeightsForDoc(self,idDoc):
        """
            idDoc : id du document
            renvoie le poids des termes pour le document
        """
        return self._index.getTfsForDoc(idDoc)
    
    def getWeightsForStem(self,stem):
        if stem in self._index.getIndexInv().keys():
            return self._index.getTfsForStem(stem)
        else:
            return dict()
    
    def getWeightsForQuery(self,query):
        #idf(stem) = log((1 + N)/1+df(stem))
        dictTerms = dict()
        nb_documents = len(self._index.getIndex())
        requete = query
        for term in self._index.getIndexInv().keys():
            if term in requete:
                dictTerms[term] = log((1+nb_documents)/(1+len(self._index.getIndexInv()[term]))) 
            else:
                dictTerms[term] = 0
        return dictTerms
