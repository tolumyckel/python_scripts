#Group 3. Pearl Ita Ekanem, Hussien Khalife, Tolulope Olowonyo

#Assignment 1: Logistic Regression
#import required libraries
import pandas as pd
import numpy as np
#import the csv file containing the dataset using the read_csv method in pandas library
dataset = pd.read_csv("UCI_Credit_Card.csv")

#assign values from the dataset to independent varible (X) and dependent variable (Y)
X = dataset.iloc[:,np.r_[1:24]].values
Y = dataset.iloc[:,24].values

from sklearn.cross_validation import train_test_split

#split the variables (X and Y) into train and test data,setting the test_size to 0.2
#which means 20% of the dataset will be used to test the model
X_train,x_test,y_train,y_test = train_test_split(X,Y,test_size = 0.2, random_state=0)

#Scale the values for better performance
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()

#Scale the independent variable of train and test dataset
X_train = sc.fit_transform(X_train)
x_test = sc.fit_transform(x_test)

#import and create a logistic model
from sklearn.linear_model import LogisticRegression

classifier = LogisticRegression(random_state = 0)
classifier.fit(X_train,y_train)
y_pred = classifier.predict(x_test)

#import confusion matrix
from sklearn.metrics import confusion_matrix

#get the confusion matrix in order to calculate the accuracy of the created model
cm = confusion_matrix(y_test,y_pred)

#prints the confusion matrix result
print(cm)

#from the result of the result matrix is [[4595  108]
#                                        [ 972  325]]

#the accuracy of the model is therefore calculated as : (4595+325)/(4595+972+108+325) = 0.82
# the accuracy of the model is therefore 0.82 or 82%

#Assignment 2: SVM

#import the svm library
from sklearn import svm

#import the csv file containing the dataset using the read_csv method in pandas library


#assign values from the dataset to independent varible (X) and dependent variable (Y).
#Also, the rows are reduced to the first 300 rows out of 30,000 because it will longer time
#for the svm algorithm to process the 30,000 rows. In addition, SVM works well with small dataset.
X = dataset.iloc[:300,1:24].values
Y = dataset.iloc[:300,24].values

from sklearn.cross_validation import train_test_split

#split the variables (X and Y) into train and test data,setting the test_size to 0.2
#which means 20% of the dataset will be used to test the model
X_train,X_test,y_train,y_test = train_test_split(X,Y,test_size=0.2,random_state =4)

#Use SVM to build a classifier.
#Use the kernel feature to test the input space and transform it to higher spcace in order to
#convert not segregation problem to segregation problem
model = svm.SVC(kernel='linear')

model.fit(X_train,y_train)

#use score method to get the accuracy of the model by passing in 
#two arguments(the independent (X) test dataset and the dependent (Y) test dataset)
accuracy = model.score(X_test,y_test)

#prints the accuracy of the model
print(accuracy)

#the accuracy of the model was gotten as 0.78333333 or 78.33%
