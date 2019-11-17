#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 17:43:27 2019

@author: 3874034
"""


from weighter import Weighter
from math import log

class Weighter4(Weighter):
    
    def __init__(self,index):
        super().__init__(index)
        
    def getWeightsForDoc(self,idDoc):
        dictTermes = dict()
        #itération sur tous les termes du corpus
        for term in self._index.getIndexInv().keys():
            if term in self._index.getIndex()[idDoc].keys():
                dictTermes[term] = 1 + log(self._index.getIndex()[idDoc][term])
            else:
                dictTermes[term] = 0
        return dictTermes
        
    def getWeightsForStem(self,stem):
        dictTf = dict()
        dictWeightTermDoc = dict()
        if stem in self._index.getIndexInv().keys():
            for doc,occ in self._index.getIndexInv()[stem].items():
                #dictTf[doc] = occ / len(self._index.getIndex()[doc])
                dictTf[doc] = occ  
            for doc,tf in dictTf.items():
                dictWeightTermDoc[doc] = 1+log(tf)
            return dictWeightTermDoc
        else :
            return dict()
    
    def getWeightsForQuery(self,query):
        #idf(stem) = log((1 + N)/1+df(stem))
        dictTerms = dict()
        nb_documents = len(self._index.getIndex())
        requete = query
        for term in self._index.getIndexInv().keys():
            if term in requete:
                dictTerms[term] = log((1+nb_documents)/1+len(self._index.getIndexInv()[term]))
            else:
                dictTerms[term] = 0
        return dictTerms

