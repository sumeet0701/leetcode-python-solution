from linear_regression import LinearRegression
import numpy as np

# create example data 
X = np.array([[1,2,3,4],[4,5,6]]).T
y= np.array([5,17,18]) # target features

# instantiate LinearRegression Class

lr = LinearRegression(learning_rate=0.01, num_iterations=1000)

# fiting the model to data 
lr.fit(X,y)

# predict using the trained model

X_test = np.array([[7,8,9],[10,11,12]]).T
y_pred = lr.predict(X_test)


print("predictions:" , y_pred)
