# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 21:23:42 2019

@author: Emmanuel
"""

def isPresent(dico,mot):
    """
        dico : dict
        mot : String or Integer
        renvoie si mot est une clé de dico
    """
    #clés de dico
    str_keys = []
    #si le mot n'est pas de type string on fait un transtipage
    if type(mot) != str: 
        mot = str(mot)
    #ajout dans str_keys des clés du dico en format string    
    {str_keys.append(str(key)) for key,value in dico.items()}
    return mot in str_keys






      