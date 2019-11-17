#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 16:52:07 2019

@author: 3874034
"""
from weighter import Weighter
from TextRepresenter import PorterStemmer

class Weighter1(Weighter):
    
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
        """
            query : requête tapée par l'utilisateur
            renvoie le poids des termes de la requête
        """
        dictTerms = dict()
        #stemmer les termes de la requête
        requete = query
        #pour tous les termes s'il est dans la requête on ajoute 1 au vecteur
        #0 sinon
        for term in self._index.getIndexInv().keys():
            if term in requete.keys():
                dictTerms[term] = 1
            else:
                dictTerms[term] = 0
        return dictTerms
        
          