#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 17:19:20 2019

@author: 3871772
"""

import Utils
from collections import Counter
#from parser import Parser

    
class IndexationHyperlien():
    
    def __init__(self,documents):
        self._documents= documents
        self._indexSuiv = dict()
        self._indexPre = dict()
        
    def hyperlien(self):  
        """ indexation des liens hypertexte entre les documents """
        
        #dictionnaire d'objets Documents
        #documents = self._parser.creationDicoDocs()
        index_suivants = dict()
        index_precedents = dict()
        #pour chaque document récupération de la liste des documents qu'il cite
        for id_doc,doc in self._documents.items():
            cites = doc.getX()
            dictCites = dict(Counter(cites))
            #ajout dans l'index
            index_suivants[doc.I] = dictCites
            #pour chaque documents cités on met à jour l'index des précédents
            for doc_suiv,nb_occurence in dictCites.items():
                if doc_suiv not in index_precedents.keys():
                    index_precedents.update({doc_suiv:{id_doc:nb_occurence}})
                
                else:
                    #index_precedents[doc_suiv] = dict()
                    index_precedents[doc_suiv][id_doc] = nb_occurence
            
        self._indexSuiv = index_suivants
        self._indexPre = index_precedents
            
    
    def getHyperLinksTo(self,num_doc):
        """ num_doc : numero de document 
                    renvoie les documents qui citent num_doc 
        """
        if Utils.isPresent(self._indexPre,num_doc):
            return self._indexPre[num_doc]
            
        else :
            return dict()
    
    
    
    def getHyperLinksFrom(self,num_doc):
        """ num_doc : numero de document
                    renvoie les documents cités dans num_doc 
        """
        if Utils.isPresent(self._indexSuiv,num_doc):
            return self._indexSuiv[num_doc]
            
        else :
            return dict()