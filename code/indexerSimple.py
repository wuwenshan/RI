#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 18:42:09 2019

@author: 3874034
"""
from TextRepresenter import PorterStemmer

from math import log

class IndexerSimple():
    
    """
        Initialise l'index normal et l'index inversé normal
    """
    
    def __init__(self):
        self._index = dict()
        self._indexInv= dict()
        self._indexNormalise = dict()
        self._indexInvNormalise = dict()
    
    """
        Liste des getters et setters des index
    """
    
    def setIndex(self,index):
        self._index = index
        
    def setIndexInv(self,indexInv):
        self._indexInv = indexInv
        
    def setIndexNormalise(self,indexNormalise):
        self._indexNormalise = indexNormalise
        
    def setIndexInvNormalise(self,indexInvNormalise):
        self._indexInvNormalise = indexInvNormalise
        
    def getIndex(self):
        return self._index
    
    def getIndexInv(self):
        return self._indexInv

    def getIndexNormalise(self):
        return self._indexNormalise
    
    def getIndexInvNormalise(self):
        return self._indexInvNormalise
    
    
    # collection = dictionnaire de Document
    def indexation(self,collection):
        
        """
            Partie indexation normale
        """
        index = dict()
        ind_rev = dict()
        for i in range(1,len(collection)+1):
            doc = collection[i]
            pS = PorterStemmer()
            index[i] = pS.getTextRepresentation(doc.T)
            for key,item in index[i].items():
                if key not in ind_rev.keys():
                    ind_rev.update({key:{i:item}})
                else:
                    ind_rev[key][i] = item
        self.setIndex(index)
        self.setIndexInv(ind_rev)
        
        """
            Partie indexation normalisée
        """
    
        indexNormalise = dict()
        indexInvNormalise = dict()
        somme = 0
        
        for key,dico in self._index.items():
            for keyDico, itemDico in dico.items():
                somme += itemDico
            dictInDict= dict()
            dictInDictInv = dict()
            for keyDicoBis, itemDicoBis in dico.items():
                if (somme != 0):
                    dictInDict[keyDicoBis] = itemDicoBis / somme
                    indexNormalise[key] = dictInDict
                    dictInDictInv[key] = itemDicoBis / somme
                    indexInvNormalise[keyDicoBis] = dictInDictInv
                else:
                    dictInDict[keyDicoBis] = itemDicoBis
                    indexNormalise[key] = dictInDict
                    dictInDictInv[key] = itemDicoBis
                    indexInvNormalise[keyDicoBis] = dictInDictInv
            somme = 0
        self.setIndexNormalise(indexNormalise)
        self.setIndexInvNormalise(indexInvNormalise)
        
        
    def getTfsForStem(self,stem):
        """
            stem : mot après preprocessing
            retourne la représentation (doc-tf) d’un stem à partir de l’index inverse
        """
        if stem in self._indexInv.keys() :
            return self._indexInv[stem]
        else :
            return 0
      
    
    def getTfIDFsForStem(self,stem):
       """
            stem : mot après preprocessing
            retourne la représentation (doc-TFIDF) d’un stem a partir de l’index inverse 
            formule  tf_idf(stem) = tf(stem,doc) * idf(stem)
       """
       # dictionnnaire contenant pour chaque doc la valeur tf-idf associé à stem
       dict_tf_idfs = dict()
       #nb_documents = 0
       nb_documents = len(self.getIndex())
       """
       for mot in self._indexInv.keys():
           #pour avoir le nombre de docs dans la collection
           
           for numero_doc in self._indexInv[stem].keys():
               nb_documents = max(numero_doc,nb_documents)
       """
       #récupérer dictionnaire de la forme {numdoc:nb_apparition de stem dans doc}        
       tf_stem = self.getTfsForStem(stem)
       #incrémentation de nb_documents car les indices vont de 0 à n-1
       #nb_documents += 1
       if tf_stem == 0:
           return 0
       for numero_doc in self._indexInv[stem].keys():
           idf = log((1+nb_documents)/(1+len(self.getTfsForStem(stem))))
           tfIdfStem =  tf_stem[numero_doc]* idf
           dict_tf_idfs[numero_doc] = tfIdfStem
       #print(nb_documents)
       return dict_tf_idfs
                   
      
        
    def getTfsForDoc(self,id_doc):
        """
            id_doc : numéro d'un document
            retourne la fréquence de chaque terme du document
        """
        return self.getIndex()[id_doc]
    
    
    def getTfIDFsForDoc(self,id_doc):
        """
            id_doc : numéro d'un document
            retourne la représentation tf-idf de chaque terme du document
            formule tf_idf(stem) = tf(stem,doc) * idf(stem)
        """
        dict_tf_idfs = dict()
        nb_documents = len(self.getIndex())
        #récupère un dictionnnaire de la forme {mot:nb_occurence du mot dans doc}
        dicoMotsDansDoc = self.getTfsForDoc(id_doc)
        for mot in dicoMotsDansDoc.keys():
            #la fréquence du mot dans le document doc
            tf_mot = dicoMotsDansDoc[mot]
            dfMot = len(self.getIndexInv()[mot])
            idf = log((1+nb_documents)/(1+dfMot))
            dict_tf_idfs[mot] = tf_mot * idf
        return dict_tf_idfs
            
                 
    def getStrDoc(self,doc):
        """
            doc : objet Document
            renvoie le texte du Document
        """
        return doc.T
   

       
   
    