

#import libraries
import matplotlib.pyplot as plt
import pandas as pd

#load the dataset using pandas
dataset = pd.read_csv("50-Startups.csv")

#assign values from the dataset to independent varible (X) and dependent variable (Y)
X = dataset.iloc[:,:-1].values
Y = dataset.iloc[:,4].values

from sklearn.preprocessing import LabelEncoder, OneHotEncoder

LabelEncoder = LabelEncoder()
X[:,3] = LabelEncoder.fit_transform(X[:,3])

onehotencoder = OneHotEncoder(categorical_features=[3])
X = onehotencoder.fit_transform(X).toarray()
#import the train_test_split from sklearn.cross_validation
from sklearn.cross_validation import train_test_split

X_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.2,random_state=0)

#import LinearRegression from sklearn.linear_model
from sklearn.linear_model import LinearRegression

regressor = LinearRegression()

#pass in the training values into the regression model
regressor.fit(X_train,y_train)

#predict the value of y using the trained model
y_pred = regressor.predict(x_test)

print(y_test)
print(y_pred)

color = ("red","blue")
plt.scatter(y_pred,y_test,c=color)
plt.xlabel("y_pred")
plt.ylabel("y_test")

#plot the scatter plot graph
plt.show()

