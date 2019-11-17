#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 17:35:14 2019

@author: 3874034
"""

from document import Document
from parser import *
from indexerSimple import IndexerSimple
from weighter5 import Weighter5
from Vectoriel import Vectoriel
from weighter1 import Weighter1
from weighter4 import Weighter4
from weighter3 import Weighter3
from weighter2 import Weighter2
from modeleLangue import ModeleLangue
from okapi import Okapi
from queryParser import QueryParser
from Precision import Precision
from Rappel import Rappel
from F_Mesure import F_Mesure
from NDCG import NDCG
from ReciprocalRank import ReciprocalRank
from EvalIRModel import EvalIRModel
from PR import PR
from IndexationHyperlien import IndexationHyperlien
from AP import AP
from AvgP import AvgP




# Création des objects Documents 
#parser = Parser("../data/cacm/cacmShort-good.txt")
#parser = Parser("../data/cisi/cisi.txt")

parser = Parser("../data/cacm/cacm.txt")
col = parser.creationDicoDocs()

# Création des index et index inversé 
i = IndexerSimple()
i.indexation(col)
index = i.getIndex()
index_inv = i.getIndexInv()

#" A tester à la main pour vérifier que la formule est correcte" 
#tfs_for_doc = i.getTfsForDoc(5)
#tfs_idf_for_doc = i.getTfIDFsForDoc(5)

# Test des objets Weighter

w = Weighter1(i)

# Test des objets Query 
file_texts = ("../data/cacm/cacm.qry")
file_relevants =("../data/cacm/cacm.rel")

#fichierspour cisi
#file_texts = ("../data/cisi/cisi.qry")
#file_relevants =("../data/cisi/cisi.rel")

#" Objet QueryParser qui lit les documents permettant de créer les objet Query "
qp = QueryParser(file_texts,file_relevants)

#" Création d'une collection d'objet Query "
queries = qp.getQueryCollection()
first_query = queries[1]
pertinents_first_query = first_query.Idocs
queries = qp.getQueryCollection()  
first_query = queries[1]



# Modèles d'appariement 
model_langue = ModeleLangue(i)
vecto = Vectoriel(i,w,False)


scores_ml = model_langue.getRanking(first_query.W)




scores = vecto.getRanking(first_query.W)



# Mesures 
#tranformation du dictionnaire en liste de Query
list_queries = list(queries.values())
k = 50
precision = Precision(k)
rappel = Rappel(k)
f_mesure = F_Mesure(k,50)
ndcg = NDCG(k,list_queries)
rr = ReciprocalRank(k)
ap = AP(k)
avgP = AvgP(k)


mesure_p = precision.evalQuery(scores,first_query)
mesure_r =  rappel.evalQuery(scores,first_query)
mesure_f = f_mesure.evalQuery(scores,first_query)
mesure_ndcg = ndcg.evalQuery(scores,first_query)
mesure_rr = rr.evalQuery(scores,first_query)

print("precision première requete : ",mesure_p)
print("rappel première requete : ",mesure_r)
print("f_rappel première requete : ",mesure_f)
#print("ap première requete : ",ap.evalQuery(scores,first_query))
print("avgP première requete : ",avgP.evalQuery(scores,first_query))


    
""" Page Rank """    
index_graphe = IndexationHyperlien(col)
#initialisation des index
index_graphe.hyperlien()
indexPre = index_graphe._indexPre
indexSuiv = index_graphe._indexSuiv
page_rank = PR(index_graphe,first_query.W)
dico_page_rank = page_rank.getPageRank(0.001,vecto,10,3)



mesures = dict()
for q in list_queries:
    scores = vecto.getRanking(q.W)
    dico_interne = dict()
    dico_interne["Precision"] = precision.evalQuery(scores,q)
    dico_interne["Rappel"] = rappel.evalQuery(scores,q)
    dico_interne["F-Mesure"] = f_mesure.evalQuery(scores,q)
    dico_interne["NDCG"] = ndcg.evalQuery(scores,q)
    dico_interne["ReciprocalRank"] = rr.evalQuery(scores,q)
    dico_interne["AveragePrecision"] = avgP.evalQuery(scores,q)
    mesures[q._I] = dico_interne





