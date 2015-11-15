import numpy as np
from scipy import io
from sknn.mlp import Classifier, Layer

class NeuralNetwork(object):
    def __init__(self, _units=10):
        self.nn = Classifier(
            layers=[
                Layer("Rectifier", units=_units),
                Layer("Sigmoid")
            ],
            learning_rate = 0.001,
            learning_rule='adagrad',
            loss_type='mae',
            regularize='L2',
            n_iter=25
        )

    def train(self, X_train, y_train):
        self.nn.fit(X_train, y_train)
        print self.nn.get_params()

    def test(self, X_test):
        y_output = self.nn.predict(X_test)
        return y_output

def create_input():
    X = np.random.random((150,100))
    y = np.zeros((150,6))
    # get labels # may work may not
    for i in xrange(150):
        val = np.random.randint(1,6)
        y[i,val] = 1

    # data
    X_train = X[:100,:]
    X_test = X[100:,:]
    # labels
    y_train = y[:100, :]
    y_test = y[100:, :]
    return X_train, X_test, y_train, y_test

if __name__ == "__main__":
    X_train, X_test, y_train, y_test = create_input()
    nnObj = NeuralNetwork(100)
    nnObj.train(X_train, y_train)
    # print nnObj.test(X_test)
