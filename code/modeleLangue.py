#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 19:54:06 2019

@author: 3871772
"""

from TextRepresenter import PorterStemmer
from IRModel import IRModel




class ModeleLangue(IRModel):
    def __init__(self,index):
        super().__init__(index)
    
    
    
    def getScores(self,query):
        """
            query : texte de la requête
            renvoie un dictionnnaire contenant le score de chaque document pour la requête
        """
        ps = PorterStemmer()
        #stemmer les mots de la requête
        
        requete = dict(ps.getTextRepresentation(query))
        obj_index = self._index
        idsDoc = []
        dicoScores = dict()
        dicoTfsTermesInQueryColl = dict()
        totalTfsCol = 0
        #calculer le tf de chaque terme par rapport à l'ensemble de la collection
        for t in obj_index.getIndexInv().keys():
            #tf(t,collection) = nb d'occurence de t dans la collection
            tfTermeCollection = 0
            #dico de la forme {numero_doc:nb_occurence de t dans le doc}
            tfInDocs = obj_index.getTfsForStem(t)            
            #calcul du tfTotal dans la collection
            for num_doc in tfInDocs.keys():
                tfTermeCollection += tfInDocs[num_doc]
            totalTfsCol += tfTermeCollection
            #si t est dans la requete, l'ajouter dans un dictionnaire
            #on en aura besoin pour calculer le score des documents
            if t in requete.keys():
                dicoTfsTermesInQueryColl[t] = tfTermeCollection
        
        
        #récupérer la liste des documents qui contiennent au moins un des termes de la requête
        for term in requete.keys():
            tfs_term = obj_index.getTfsForStem(term)
            #vérifier que le terme est dans l'index inversé
            if tfs_term != 0:
                for num_doc in tfs_term.keys():
                    if num_doc not in idsDoc:
                        idsDoc.append(num_doc)
        #calculer le score des documents pour chaque terme de la requete
        # d'abord pour chaque document, récupérer l'ensemble des termes qui le compose ainsi que leur tf
        for num_doc in idsDoc:
            TotalTfTerms = 0
            dictTfTermesDoc = dict()
            tfsForDoc = obj_index.getTfsForDoc(num_doc)
            score_doc = 1
            #ensuite pour chaque terme de l'index inversé calculer son tf s'il est présent dans le document dont l'id est num_doc
            #ajouter son tf au tf total des termes du document
            for terme in obj_index.getIndexInv().keys():
                    #tfsForDoc de la forme {terme: tf(t,d)}
                    if terme in tfsForDoc.keys():
                        tfTermeDoc = tfsForDoc[terme]
                        dictTfTermesDoc[terme] = tfTermeDoc
                        TotalTfTerms += tfTermeDoc
            #calculer le ratio tf(terme,doc)/TotalTfTerms score du doc
            for stem,tf in dictTfTermesDoc.items():
                if stem in requete.keys():
                    score_doc *= tf/TotalTfTerms + dicoTfsTermesInQueryColl[stem]/totalTfsCol
                    dicoScores[num_doc] = score_doc
        return dicoScores
                
                    
                    
                
                
                
            
        
        
            
        
        

        
        
    
        