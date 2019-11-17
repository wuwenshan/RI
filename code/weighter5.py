#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 15:05:50 2019

@author: 3871772
"""

from weighter import Weighter
from math import log
from TextRepresenter import PorterStemmer


class Weighter5(Weighter):
    
    def __init__(self,index):
        super().__init__(index)
        
    def getWeightsForDoc(self,idDoc):
        dictTermes = dict()
        #idf(stem) = log((1 + N)/1+df(stem))
        for term in self._index.getIndexInv().keys():
            if term in self._index.getIndex()[idDoc].keys():
                nb_doc = len(self._index.getIndex())
                idf_stem = log((1+nb_doc)/(1+len(self._index.getIndexInv()[term])))
                dictTermes[term] = (1 + log(self._index.getIndex()[idDoc][term])) * idf_stem 
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
            idf = log( ( 1 + len(self._index.getIndex()) ) / (1 + len(self._index.getIndexInv()[stem] ) ) )
            for doc,tf in dictTf.items():
                dictWeightTermDoc[doc] = (1+log(tf))*idf
            return dictWeightTermDoc
        else :
            return dict()
    
    def getWeightsForQuery(self,query):
        dictTerms = dict()
        nb_documents = len(self._index.getIndex())
        #requete = PorterStemmer().getTextRepresentation(query)
        requete = query
        #print(requete.keys())
        for term in self._index.getIndexInv().keys():
            if term in requete.keys():
                #nombre d'occurence du terme dans la requete (tf(term,query))
                #idf(stem) = log((1 + N)/1+df(stem))
                tf_term = requete[term]
                idf_term = log((1+nb_documents)/(1+len(self._index.getIndexInv()[term])))
                dictTerms[term] = tf_term * idf_term
                
            else:
                dictTerms[term] = 0
        return dictTerms

