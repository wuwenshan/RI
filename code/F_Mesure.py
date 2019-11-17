# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 00:15:19 2019

@author: Emmanuel
"""

from EvalMesure import EvalMesure
from Rappel import Rappel
from Precision import Precision

class F_Mesure(EvalMesure):
    def __init__(self,k,beta):
        super().__init__(k)
        self._beta = beta
        
        
    def getK(self):
        return self._k
    
    def setK(self,k):
        self._k = k
        
    def evalQuery(self,liste,query):
        #instanciation des classes Precision et Rappel afin d'utiliser leur méthode evalQuery
        pre = Precision(self._k)
        ra = Rappel(self._k)
        precision = pre.evalQuery(liste,query)
        rappel = ra.evalQuery(liste,query)
        try:
            #formule de la F-Mesure
            f_mesure_k =  (1+self._beta*self._beta) * (precision * rappel)/(self._beta*self._beta*precision + rappel)
        except:
            return 0
        return round(f_mesure_k,2)
        
        
        