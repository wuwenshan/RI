#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 14:39:45 2019

@author: 3874034
"""

"""
    Cette classe va permettre l'accès aux valeurs des métadonnées

"""

class Document():
    
    def __init__(self):
        """
            Constructeur initialisant toutes les balises à vide
        """
        self._I = ""
        self._T = ""
        self._B = ""
        self._A = ""
        self._K = ""
        self._W = ""
        self._X = []
        self._N = ""
    
    """
        Liste des getters & setters
    """
    
    def getI(self):
        return self._I
    
    def getT(self):
        return self._T
    
    def getB(self):
        return self._B
    
    def getA(self):
        return self._A
    
    def getK(self):
        return self._K
    
    def getW(self):
        return self._W
    
    def getX(self):
        return self._X
    
    def getN(self):
        return self._N
    
    def setI(self,_I):
        self._I = _I
        
    def setT(self,_T):
        self._T = _T
        
    def setB(self,_B):
        self._B = _B
        
    def setA(self,_A):
        self._A = _A
    
    def setK(self,_K):
        self._K = _K
    
    def setW(self,_W):
        self._W = _W
        
    def setX(self,_X):
        self._X = _X
        
    def setN(self,_N):
        self._N = _N
        
    """
        Liste des properties
    """
    
    I = property(getI, setI)
    
    T = property(getT, setT)
    
    B = property(getB, setB)
    
    A = property(getA, setA)
    
    K = property(getK, setK)
    
    W = property(getW, setW)
    
    X = property(getX, setX)
    
    N = property(getN, setN)
    
    
    
    """
        Met à jour le contenu de la balise donnée
    """
    
    def setContenu(self,balise,contenu):
        if balise == ".T":
            new_contenu = self._T+contenu+" "
            self.setT(new_contenu)
        elif balise == ".B":
            self.setB(self.getB()+contenu+" ")
        elif balise == ".A":
            self.setA(self.getA()+contenu+" ")
        elif balise == ".K":
            self.setK(self.getK()+contenu+" ")
        elif balise == ".W":
            self.setW(self.getW()+contenu+" ")
        elif balise == ".X":
            doc_pointe = contenu.split("\t")[0].strip()
            #print("Type de .X dans docu : ",type(doc_pointe))
            self._X.append(int(doc_pointe))
        elif balise == ".N":
            self.setN(self.getN()+contenu+" ")
        