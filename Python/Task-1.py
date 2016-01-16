from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
from sklearn.multiclass import OneVsOneClassifier
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC

train=pd.read_csv("train.csv")
test=pd.read_csv("test.csv")
vectorizer = CountVectorizer(analyzer = "word",max_features=5000)
train_data_features = vectorizer.fit_transform(train["Summary"])
test_data_features=vectorizer.fit_transform(test["Summary"])

resultWithOneVsRest = OneVsRestClassifier(LinearSVC(random_state=0)).fit(train_data_features, train["Topic"]).predict(test_data_features)
resultWithOneVsOne= OneVsOneClassifier(LinearSVC(random_state=0)).fit(train_data_features, train["Topic"]).predict(test_data_features)

outputWithOneVsRest = pd.DataFrame( data={"record id":test["RecordID"], "topic":resultWithOneVsRest} )
outputWithOneVsRest.to_csv( "Task1_outputWithOneVsRest.tsv", index=False, quoting=3 , sep="\t")

resultWithOneVsOne = pd.DataFrame( data={"record id":test["RecordID"], "topic":resultWithOneVsOne} )
resultWithOneVsOne.to_csv( "Task1_resultWithOneVsOne.tsv", index=False, quoting=3, sep="\t")