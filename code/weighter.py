#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 16:31:16 2019

@author: 3874034
"""

from abc import ABC, abstractmethod

class Weighter(ABC):
    
    def __init__(self,index):
        self._index = index
        
    """
        retourne les poids des termes pour un document dont l’identifiant est idDoc
    """    
    @abstractmethod
    def getWeightsForDoc(self,idDoc):
        pass
    
    """
        retourne les poids du terme stem pour tous les documents qui le contiennent    
    """
    @abstractmethod
    def getWeightsForStem(self,stem):
        pass
    
    """
        retourne les poids des termes de la requête
    """
    @abstractmethod
    def getWeightsForQuery(self,query):
        pass