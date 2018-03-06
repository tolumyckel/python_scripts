

#from sklearn import svm
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import VotingClassifier
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

#Loading the dataset using pandas library
dataset = pd.read_csv("column_2C_weka.csv")

#assign values from the dataset to X variable
X = dataset.iloc[:,:-1].values

#assign values from the dataset to y variable
y = dataset.iloc[:,-1].values

#change the values of y from categorical to numeric variable
y = pd.Categorical.from_array(y).codes

# Base Models
clf1 = LogisticRegression(random_state=1)
clf2 = GaussianNB()
clf3 = RandomForestClassifier(random_state=1)

#the voting classifier
eclf = VotingClassifier(estimators=[('lr',clf1),('gnb',clf2),('rf',clf3)],voting='hard')

#display the accuracy of each base model and the voting classifier
for clf,label in zip([clf1,clf2,clf3,eclf],['Logistic Regression','Naive Bayes','Random Forest','Ensemble']):
    scores = cross_val_score(clf,X,y,cv=5,scoring='accuracy')
    print("Accuracy: %0.2f [%s]" % (scores.mean(),label))
