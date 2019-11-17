#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 11:07:33 2019

@author: 3871772
"""

import Utils

import random

import secrets

""" classe qui contient l'algorithme PageRank """

class PR():
    
    def __init__(self,indHyp,query):
        self._indHyp = indHyp
        self._query = query
        
     
    # param model : modèle utilisé
    # param n : n premiers docs retournés par un modèle
    # param k : k docs random pointant vers les n premiers
    def subGraph(self,model,n,k):
        """
            Première étape : listing des docs du sous grpahe
        """
        docsOfSubGraph = [] # liste contenant les docs du sous graphe
        seeds = model.getRanking(self._query)[:n]
        for doc,score in seeds:
            docsOfSubGraph.append(doc) # doc issu de la seed
            docsOfSubGraph += list(self._indHyp.getHyperLinksFrom(doc).keys()) # doc(s) suivant(s) de la seed
            precedents = list(self._indHyp.getHyperLinksTo(doc).keys()) # doc(s) précédent(s) de la seed
            for i in range(k):
                if len(precedents)!=0:
                    precAlea = secrets.choice(precedents) # précédent aléatoire
                    #print("prec alea : ",precAlea)
                    docsOfSubGraph.append(precAlea)
                    precedents.remove(precAlea)
                else:
                    break
        docsOfSubGraph = list(dict.fromkeys(docsOfSubGraph)) # suppression des docs en double        
        
        """
            Deuxième étape : lier les docs du sous graphe afin de reconstituer les dict précédents et suivants
        """
        dictPrec = dict()
        dictSuiv = dict()
        for doc in docsOfSubGraph:
            tabSuiv = dict()
            tabPrec = dict()
            for docSuiv, occ in self._indHyp.getHyperLinksFrom(doc).items(): # parcours des docs suivants du doc courant
                if docSuiv in docsOfSubGraph:
                    tabSuiv[docSuiv] = occ
            dictSuiv[doc] = tabSuiv
            for docPrec, nb in self._indHyp.getHyperLinksTo(doc).items(): # parcours des docs précédents du doc courant
                if docPrec in docsOfSubGraph:
                    tabPrec[docPrec] = nb
            dictPrec[doc] = tabPrec
        
        return dictPrec,dictSuiv
    

    
    
          
    

    
    """
        Formule : Sj = d*somme(Pij*Si) + (1-d)
        Param doc : le score du doc à calculer
        Param liens_suiv : dict contenant les docs pertinents cités
        Param liens_pre : dict contenant les docs pertinents cités par d'autres docs
        Param scores : liste des scores actuels des docs
        Return : le score du doc passé en paramètre
    """
    def scoreDoc(self,doc,liens_suiv,liens_pre,scores):
        d = 0.85
        score_doc = 0
        
        for pred,val in liens_pre[doc].items():
            score_doc += ((val/sum(liens_suiv[pred].values()))*scores[pred])
        return score_doc*d + (1-d)
        

    
    def getPageRank(self,eps,model,n,k):
        """
            eps: la différence prise en compte pour la convergence
            model : modèle de recherche
            n : nombre de document seeds
            k : nombre de voisins pour chaque seed
                renvoie le page rank 
        """
        precedent,suivant = self.subGraph(model,n,k) # mêmes clés pour precedent et suivant
        scores = dict()
        for key in suivant.keys():
            scores[key] = 1 / len(precedent) # init des scores avec 1 / N où N = nombre de docs dans le sous graphe
        res = dict()
        converge = False
        while converge == False:
            for doc in precedent.keys():
                res[doc] = self.scoreDoc(doc,suivant,precedent,scores)
            res = {key:val/sum(res.values()) for key,val in res.items()} # normalisation
            count = 0
            for doc in scores.keys():
                if abs(res[doc] - scores[doc]) < eps:
                    count += 1
            if count == len(scores):
                converge = True
            scores = res.copy() # affectation des scores actuels


        sorted_scores_docs = sorted(res.items(), key = lambda tup:tup[1], reverse = True)
        return sorted_scores_docs
    
    
    
    
    