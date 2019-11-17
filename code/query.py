#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 18:20:13 2019

@author: 3874034
"""

class Query():
    
    """
        Init les balises à vide
        I = Identifiant de la requête
        W = Texte de la requête
        Idoc = Liste des identifiants des documents pertinents
        
    """
    
    def __init__(self):
        self._I = ""
        self._W = ""
        self._Idocs = []
        
    """
        Liste des getters er setters
    """
    
    def getI(self):
        return self._I
    
    def getW(self):
        return self._W
    
    def getIdoc(self):
        return self._Idocs
    
    def setI(self,I):
        self._I = I
        
    def setW(self,W):
        self._W = W
        
    """
        Param idR = identifiant de la requête
        Param Idocs = liste des identifiants des documents pertinents pour la requête
    """
    def setIdoc(self,Idocs):
        self._Idocs = Idocs
    
    """
        Liste des properties
    """
    
    I = property(getI,setI)

    W = property(getW,setW)
    
    Idocs = property(getIdoc,setIdoc)
    
    
    
    
    
    