# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 11:24:24 2019

@author: 3874034
"""
#from indexerSimple import IndexerSimple
from IRModel import IRModel
from TextRepresenter import PorterStemmer
from math import log

class Okapi(IRModel):
    
    """
        index : objet IndexerSimple    
    """        
    def __init__(self,index):
        super().__init__(index)
      
    
    def getScores(self,query):
        ps = PorterStemmer()
        requete = ps.getTextRepresentation(query) # {mot1 : nb1 , mot2 : nb2}
        nb_documents = len(self._index.getIndex()) # nombre de documents dans la collection
        listScores = []
        k1 = 1.2
        b = 0.75
        
        indexInv = self._index.getIndexInv()        
        index = self._index.getIndex()        
        
        count = 0 # nb total d'occurences
        score = 0
        
        for key,dico in index.items():
            for keyDico,itemDico in dico.items():
                count += itemDico
                
        avg = count / len(index)
        """
        for keyIndex, itemIndex in index.items():
        
            for key,item in dict(requete).items():
                
                idf = log((1+nb_documents)/(1+len(self._index.getTfsForStem(key))))
                f_qi_d = indexInv[key][keyIndex] 
                D = sum(self._index.getTfsForDoc(keyIndex)[term] for term in self._index.getTfsForDoc(keyIndex).keys())
                score += idf * ( ( f_qi_d * (k1+1)) / f_qi_d + k1 * ( 1 - b + b * ( D / avg ) ) )
            
            listScores[i-1] = score 
            i = i + 1
            
        """
        """
        for keyIndexInv, itemIndexInv in indexInv.items():
            
            if keyIndexInv in requete:
                
                for keyDico, itemDico in itemIndexInv.items():
                    
                    idf = log( ( 1 + nb_documents ) / ( 1 + len(itemIndexInv)) )
                    
                    print("idf",idf)
                    
                    f_qi_d = itemDico
                    
                    print("f",f_qi_d)
                    
                    D = sum(self._index.getTfsForDoc(keyDico)[term] for term in self._index.getTfsForDoc(keyDico).keys())
                    
                    print("D",D)
                    
                    score += idf * ( ( f_qi_d * (k1+1)) / f_qi_d + k1 * ( 1 - b + b * ( D / avg ) ) )    
                    
                    print("score",score)
                    
                    listScores.append((keyDico,score))
                    
                    score = 0        
        """
        dictScores = dict()
        c = 1
        liste_id = []
        #print("aaa : ",dict(requete).items())
        for mot, occu in dict(requete).items():
            if mot in indexInv.keys():
                #print("MOT : ",mot)
                #print("indexinv : ",indexInv[mot].items())
                for key,item in indexInv[mot].items():
                    #print("key : ",key)
                    #print("item : ",item)
                    idf = log( ( 1 + nb_documents ) / ( 1 + len(indexInv[mot] ) ) )
                    
                    f_qi_d = item
                    
                    D = sum(self._index.getTfsForDoc(key)[term] for term in self._index.getTfsForDoc(key).keys())
                    #print("c : ",c)
                    c += 1
                    #print("idf : ",idf)
                    #print("f_qi_d : ",f_qi_d)
                    #print("D : ",D)
        
                    score = idf * ( ( f_qi_d * 1 ) / ( f_qi_d + k1 * ( 1 - b + b * ( D / avg ) ) ) )
                    
                    #print("avg : ",avg)
                    #print("score : ",score)
                    
                    #print("key : ",key)
                    #print("list id : ",liste_id)
                    
                    if key in liste_id:
                        
                        dictScores[key] += score
                    else:
                        dictScores[key] = score
                        liste_id.append(key)
                
                    score = 0
        
        return dictScores
        
        
        