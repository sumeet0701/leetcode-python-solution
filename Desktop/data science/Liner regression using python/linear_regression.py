import numpy as np

class LinearRegression:

    def __init__(self, learning_rate = 0.01,
                 num_iterations =1000):
        self.learning_rate = learning_rate
        self.num_iterations = num_iterations
        self.weights = None
        self.bais = None

    
    def fit(self,X,y):
        # initialize weights and bais to zeros
        self.weights =np.zeros(X.shape[1])
        self.bais = 0


        # perform gradient descent
        for i in range(self.num_iterations):
            # compute predictions
            y_pred = self.predict(X)

        # compute gradients
            dw = (1/X.shape[0])*np.dot(X.T,(y_pred-y))
            dw = (1/X.shape[0])*np.sum((y_pred-y))            

            # update weights and bais

            self.weights -= self.learning_rate*dw
            self.bais -= self.learning_rate * dw
    
    def predict(self,X):
        # Compute the predictions
        y_predict = self.predict(X)
        return y_predict
    
    def _predict(self,X):
        # Compute the linear combination of features and bais

        return np.dot(X, self.weights) + self.bais
    