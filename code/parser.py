#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Tue Feb 12 15:09:45 2019

@author: 3874034
"""

from document import Document

"""
    ATTENTION : parser.py est à run avant de faire des tests dessus
"""

class Parser(object):
        
    """
        Param collectionFileName : fichier texte contenant une collection 
    """
    def __init__(self,collectionFileName):
        self._collection = collectionFileName    
        
        
    """ Crée les documents et met à jour le contenu des balises   """
          
    def creationDicoDocs(self):
        dicoDocs = dict()
        fichier = open(self._collection,"r")
        for line in fichier:
            if line.startswith(".I"):
                docu = Document()
                num_doc = int(line.split(" ")[1].strip())
                docu.setI(num_doc)
                dicoDocs[num_doc] = docu
            elif line.startswith(".T") or line.startswith(".K") or line.startswith(".B") or line.startswith(".W") or line.startswith(".N") or line.startswith(".X") or line.startswith(".A"):
                balise = line.split(" ")[0].strip()
            elif not line.startswith("\n"):
                docu.setContenu(balise,line)
        fichier.close()
        return dicoDocs

       
       
