# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 20:15:29 2019

@author: wuwen
"""

from document import Document
from parser import *
from indexerSimple import IndexerSimple
from weighter5 import Weighter5
from weighter4 import Weighter4
from weighter3 import Weighter3
from weighter2 import Weighter2
from weighter1 import Weighter1
from Vectoriel import Vectoriel
from modeleLangue import ModeleLangue
from okapi import Okapi
from Precision import Precision
from queryParser import QueryParser

parser = Parser("../data/cacm/cacm.txt")
col = parser.creationDicoDocs()



i = IndexerSimple()
i.indexation(col)

w = Weighter5(i)
vec = Vectoriel(i,w,False)
rank = vec.getRanking("programming and engineering")

#precision = Precision(11)
#precision.evalQuery(rank,"programming and engineering")
cisi_qry = "../data/cisi/cisi.qry"
cisi_rel = "../data/cisi/cisi.rel"
cacm_qry = "../data/cacm/cacm.qry"
cacm_rel = "../data/cacm/cacm.rel"
qp = QueryParser(cacm_qry,cacm_rel)
#colqr = qp.getQueryCollection()
a = qp.getQryContains()
b = qp.getRelContains()
#c = qp.getQueryCollection()
