from sklearn.linear_model import LinearRegression
import numpy as np

#dummy Data
X = np.array([[1],[2],[3],[4]])
y = np.array([2,3,6,7])

#create and train the modal
model = LinearRegression()
model.fit(X,y)

#prediction
y_predict = model.predict([[5]])
print(y_predict)