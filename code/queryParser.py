#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 18:27:50 2019

@author: 3874034
"""

from query import Query
import re

class QueryParser():
    
    """
        Param qry : fichier tests de requêtes
        Param rel : les jugements de pertinence pour les requêtes de test
    """
    
    def __init__(self, qry, rel):
        self._qry = qry
        self._rel = rel
        
    """
        Lecture du fichier qry et renvoie les identifiants et textes
        Return : collection de Query pour le fichier .qry
    """
        
    def getQryContains(self):
        
        file = open(self._qry, "r")
        collectionOfQuery = dict()
        lastLine = 0
        for line in file:
            if (line.startswith(".I")):
                query = Query()
                if lastLine!=0:
                    query.I = lastLine
                    lastLine = 0
                else:
                    query.I = int(line[2:].strip())
                    
            elif (line.startswith(".W")):
                isReading = True
                w = ""
                while isReading:
                    ligne = file.readline().strip()
                    if (ligne.startswith(".N") or ligne.startswith(".A") or ligne.startswith(".B")):
                        isReading = False
                    elif (ligne.startswith(".I")):
                        isReading = False
                        lastLine = int(ligne[2:].strip())
                    else:
                        w += ligne
                        w += " "
                query.W = w
                collectionOfQuery[query.I] = query
        file.close()
                
        return collectionOfQuery
    
    
    """
        Lecture du fichier rel et renvoie l'id de la requête avec les id des documents pertinents
        Return : collection de Rel pour le fichier .rel
    """
    
    def getRelContains(self):
        
        file = open(self._rel, "r")
        collectionOfRel = dict()
        isFirstLine = True
        listeIdoc = []
            
        for line in file:

                
            line = line.strip()
            elLine = re.split(r'[ \t]+', line) # regex qui split les espaces et tabulations
            
            if isFirstLine:
                query = Query()
                query.I = int(elLine[0]) # premier élément de la liste = id requete
                listeIdoc.append(int(elLine[1])) # deuxième élément de la liste = id doc pertinent pour la requete
                isFirstLine = False
                
            elif query.I == int(elLine[0]):
                listeIdoc.append(int(elLine[1]))
                
            else:
                query.setIdoc(listeIdoc)
                collectionOfRel[query.I] = query
                listeIdoc = []
                query = Query()
                query.I = int(elLine[0])
                listeIdoc.append(int(elLine[1]))
        query.setIdoc(listeIdoc)
        collectionOfRel[query.I] = query
        
        file.close()
        return collectionOfRel
    
  
    
    def getQueryCollection(self):
        """ retourne un dictionnaire d'objet Query """
        #dict d'object Query avec leur texte uniquement
        queriesTexts = self.getQryContains()
        #dict d'object Query avec leur liste de docs pertinents uniquement
        queriesDocs = self.getRelContains()
        #pour tous les Query dans queriesTexts ajouter leur liste de docs pertinents qui se trouvent dans queriesDocs
        for num_query,q in queriesTexts.items():
            #print(type(num_query))
            if num_query in queriesDocs:
                q.Idocs = queriesDocs[num_query].Idocs
        
        return queriesTexts
    
    
    