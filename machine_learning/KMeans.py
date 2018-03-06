import matplotlib.pyplot as plot
from sklearn.cluster import KMeans
from sklearn import datasets
import pandas as pd
import numpy as np

iris = datasets.load_iris()

X = pd.DataFrame(iris.data)

X.columns = ['sepal_length','sepal_width','petal_length','petal_width']

y = pd.DataFrame(iris.target)
y.columns = ['Targets']
#KMeans Cluster
model = KMeans(n_clusters=3)
model.fit(X)
print(model.labels_)

colormap = np.array(['red','blue','green'])

plot.scatter(X.petal_length,X.petal_width, c= colormap[model.labels_], s= 40)
plot.title('KMeans Cluster')
plot.show()

plot.scatter(X.petal_length,X.petal_width, c= colormap[y.Targets], s= 40)
plot.title("Actual Cluster")
plot.show()
