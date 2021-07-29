# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 13:45:19 2021

@author: Simplon
"""

import requests
import pandas as pd
import json


def fetch_starships(n_starships):
    uri = 'https://swapi.dev/api/starships/'
    url = f'{uri}{str(n_starships)}/'
    r= requests.get(url)
    data = r.json()
    return data



#def fetch_starships(n_starships):
    #uri = 'https://swapi.dev/api/starships/'
    #url = f'{uri}{str(n_starships)}/'
    #r= requests.get(url)
#Starter itérateur pour la première boucle
    #n = 0
#Nombre de vaisseaux souhaité 
    #z = 37
#for i in range(2,z):
    #if n == 0 : 
       # df = pd.json_normalize(fetch_starships(i))
        #n= n+1
   # else:
       # df = df.append(pd.json_normalize(fetch_starships(i)))
  #  return df