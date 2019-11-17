# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 20:28:06 2019

@author: Emmanuel
"""

from abc import ABC
import abc

class EvalMesure(ABC):
    @abc.abstractmethod
    def __init__(self,k):
        self._k = k
        
        
    @abc.abstractmethod
    def evalQuery(self,liste,query):
        """ 
            liste : documents retournés par un modèle
            query :Objet Query
            retourne la valeur de la mesure
            des documents pour la requête
        """
        
        pass
    
    
    