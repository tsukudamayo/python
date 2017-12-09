# _*_ coding: utf-8 _*_

from PIL import Image
import numpy as np

def pca(X):
    """
    PCA
    input: X, metrics which normalized training data
    output: mapped metrics, variance, average
    """

    # get dimmention
    num_data,dim = X.shape

    # centering data
    mean_X = X.mean(axis=0)
    X = X - mean_X

    if(dim > num_data):
        # if high dimensions
        M = np.dot(X, X.T)              # Covariance Matrix
        e,EV = np.linalg.eign(M)        # eigenk
        tmp = dot(X.T, EV).T
        V = tmp[::-1]
        S = np.sqrt(e)[::-1]
        for i in range(V.shape[1]):
            V[:, i] /= S
    else:
        U,S,V = np.linalg.svd(X)
        V = V[:num_data]
   
    # return mapped_metrics, variance, averege
    return V,S,mean_X
