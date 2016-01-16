# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 02:59:49 2016

@author: Nivedita_Parihar Koushik Saha 
"""

from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
from sklearn.multiclass import OneVsOneClassifier
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import cross_validation
from sklearn.ensemble import RandomForestClassifier
import numpy as np

##With Bag of words and One-vs-all and One-vs-One

train=pd.read_csv("train.csv")
test=pd.read_csv("test.csv")
vectorizer = CountVectorizer(analyzer = "word",max_features=5000)
train_data_features = vectorizer.fit_transform(train["Summary"])
test_data_features=vectorizer.transform(test["Summary"])

resultWithOneVsRest = OneVsRestClassifier(LinearSVC(random_state=0)).fit(train_data_features, train["Topic"]).predict(test_data_features)
resultWithOneVsOne= OneVsOneClassifier(LinearSVC(random_state=0)).fit(train_data_features, train["Topic"]).predict(test_data_features)

outputWithOneVsRest = pd.DataFrame( data={"record_id":test["RecordID"], "topic_id":resultWithOneVsRest} )
outputWithOneVsRest.to_csv( "Task1_outputWithOneVsRest.tsv", index=False, quoting=3 , sep="\t")

resultWithOneVsOne = pd.DataFrame( data={"record_id":test["RecordID"], "topic_id":resultWithOneVsOne} )
resultWithOneVsOne.to_csv( "Task1_resultWithOneVsOne.tsv", index=False, quoting=3, sep="\t")

##with TF-idf with One-vs-all and One-vs-One
tf_idf=TfidfVectorizer(max_features=5000)
train_data_features = tf_idf.fit_transform(train["Summary"])
test_data_features=tf_idf.transform(test["Summary"])
resultWithOneVsRestModel = OneVsRestClassifier(LinearSVC(random_state=0)).fit(train_data_features, train["Topic"])
print np.mean(cross_validation.cross_val_score(resultWithOneVsRestModel,train_data_features,train["Topic"],cv=20))
resultWithOneVsRest_tfidf = resultWithOneVsRestModel.predict(test_data_features)

op=pd.DataFrame(data={"record_id":test["RecordID"],"topic_id":resultWithOneVsRest_tfidf})
op.to_csv("Task-1_With_TfIdf.tsv",index=False,quoting=3,sep="\t");