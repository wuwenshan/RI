# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 00:56:32 2019

@author: Emmanuel
"""
from EvalMesure import EvalMesure
import math



class NDCG(EvalMesure):
    def __init__(self,rang,requetes):
        """ 
            rang : rang pris en compte pour calculer le NDCG
            requetes : liste d'objet Query
        """
        super().__init__(rang)
        self._requetes = requetes
    
    
    
    def calcul_DCG(self,liste,query,rang):
        """
            liste : liste ordonnée de couples (num_doc,score)
            query : Object Query réprésentant la requête
            rang : rang à considérer pour appliquer la mesure
            renvoie un mesure pour la Query
        """
        
        total = 0
        #rel: liste des id de docs pertinents pour la requête
        rel = query._Idocs
        #pertinence du premier doc renvoyé par la requête
        num_doc1,score1 = liste[0] 
        if num_doc1 in rel:
            total += 1
        #pertinence de chaque document du rang 2 à p
        #print("On est dans dcg voici la liste des docs pour la requête :",liste)
        for p in range(1,rang):
            if p >= len(liste):
                return total
            #print("Element à la position "+str(p)+":",liste[p])
            num_doc,score = liste[p]
            if num_doc in rel:
                total += 1/math.log(p+1,2)
        return total




    def evalQuery(self,liste,query):
        """ moyenner le DCG d'une requete
            par rapport à toutes les DCG
            
            liste : liste de documents ordonnés par un modèle
            query : objet Query la requête à évaluer
            rang : rang à considérer pour appliquer la mesure
            renvoie le ndcg 
        """
        DCG = self.calcul_DCG(liste,query,self._k)
        IDCG = 0
        #calcul du DCG pour toutes les requêtes
        for q in self._requetes:
            IDCG += self.calcul_DCG(liste,q,self._k)
        try:
            ndcg = round(DCG/IDCG,2)
        except ZeroDivisionError:
            return 0
        return ndcg
    
    
    
    
        
        
        
        
        
        
        
        
        