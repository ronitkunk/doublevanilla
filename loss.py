import numpy as np

train_data = np.loadtxt("data/train.csv", delimiter=',')
X = train_data[:, 0]
Y = train_data[:, 1]

def L(w, b): # L(w, b; X, Y)
    Y_hat = w * X + b
    
    loss = np.dot(Y_hat - Y, Y_hat - Y)/(2*X.shape[0]) # MSE

    # loss = - np.dot(np.split(Y_hat - Y, 2)[0], np.split(Y_hat - Y, 2)[0])/(4*X.shape[0]) + np.dot(np.split(Y_hat - Y, 2)[1], np.split(Y_hat - Y, 2)[1])/(4*X.shape[0]) # Saddle

    return loss

def grad_L(w, b):
    Y_hat = w * X + b

    L_w = np.dot(Y_hat - Y, X)/(X.shape[0]) # MSE
    L_b = np.sum(Y_hat - Y)/(X.shape[0]) # MSE

    # L_w = - (np.dot(np.split(Y_hat - Y, 2)[0], np.split(X, 2)[0]))/(2*X.shape[0]) + (np.dot(np.split(Y_hat - Y, 2)[1], np.split(X, 2)[1]))/(2*X.shape[0]) # Saddle
    # L_b = (- np.sum(np.split(Y_hat - Y, 2)[0]) + np.sum(np.split(Y_hat - Y, 2)[1]))/(X.shape[0]) # Saddle

    return (L_w, L_b)