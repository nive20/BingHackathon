# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 02:59:49 2016

@author: Nivedita_Parihar Koushik Saha 
"""
from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer

train=pd.read_csv("train.csv")
test=pd.read_csv("test.csv")

km1=KMeans(n_clusters=12)
km1.fit_transform(train["RecordID"].reshape(-1,1))
km1.predict(test["RecordID"].reshape(-1,1))