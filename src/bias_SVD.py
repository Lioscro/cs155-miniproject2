import sys

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def grad_U(Ui, Yij, Vj, ai, bj, mu, reg, eta):
    """
    Takes as input Ui (the ith row of U), a training point Yij, the column
    vector Vj (jth column of V^T), reg (the regularization parameter lambda),
    and eta (the learning rate).

    Returns the gradient of the regularized loss function with
    respect to Ui multiplied by eta.
    """
    # just use the equation from 2a to compute the gradient of u_i
    first_term = reg * Ui
    second_term = Vj * (Yij - mu - np.dot(Ui, Vj) - ai - bj)
    return eta * (first_term - second_term)

def grad_V(Vj, Yij, Ui, ai, bj, mu, reg, eta):
    """
    Takes as input the column vector Vj (jth column of V^T), a training point Yij,
    Ui (the ith row of U), reg (the regularization parameter lambda),
    and eta (the learning rate).

    Returns the gradient of the regularized loss function with
    respect to Vj multiplied by eta.
    """
    # just use the equation from 2a to compute the gradient of u_i
    first_term = reg * Vj
    second_term = np.multiply(Ui, (Yij - mu - np.dot(Ui, Vj)) - ai - bj)
    return eta * (first_term - second_term)

def grad_a(Vj, Yij, Ui, ai, bj, mu, reg, eta):
    """
    Takes as input the column vector Vj (jth column of V^T), a training point Yij,
    Ui (the ith row of U), reg (the regularization parameter lambda),
    and eta (the learning rate).

    Returns the gradient of the regularized loss function with
    respect to Vj multiplied by eta.
    """
    # just use the equation from 2a to compute the gradient of u_i
    first_term = reg * ai
    second_term = Yij - mu - np.dot(Ui, Vj) - ai - bj
    return eta * (first_term - second_term)

def grad_b(Vj, Yij, Ui, ai, bj, mu, reg, eta):
    """
    Takes as input the column vector Vj (jth column of V^T), a training point Yij,
    Ui (the ith row of U), reg (the regularization parameter lambda),
    and eta (the learning rate).

    Returns the gradient of the regularized loss function with
    respect to Vj multiplied by eta.
    """
    # just use the equation from 2a to compute the gradient of u_i
    first_term = reg * bj
    second_term = Yij - mu - np.dot(Ui, Vj) - ai - bj
    return eta * (first_term - second_term)

def get_err(U, V, Y, a, b, mu, reg=0.0):
    """
    Takes as input a matrix Y of triples (i, j, Y_ij) where i is the index of a user,
    j is the index of a movie, and Y_ij is user i's rating of movie j and
    user/movie matrices U and V.

    Returns the mean regularized squared-error of predictions made by
    estimating Y_{ij} as the dot product of the ith row of U and the jth column of V^T.
    """
    # find the actual error of the predictions
    total_incorrect = 0.0
    for k in range(np.size(Y, 0)):
        i = int(Y[k, 0])
        j = int(Y[k, 1])
        Y_ij = Y[k, 2]
        # now try to modify both u_i and v_j
        total_incorrect += ((Y_ij - np.dot(U[i, :], V[j, :]) - mu - a[i] - b[j]) ** 2)
    # multiply by the factor of 0.5
    total_incorrect *= 0.5
    # now find the frobenius norm of U and V
    total_regularized_error = (reg / 2.0) * \
            ((np.linalg.norm(U, ord = 'fro') ** 2) + (np.linalg.norm(V, ord = 'fro') ** 2) \
            + (np.linalg.norm(a) ** 2) + (np.linalg.norm(b) ** 2))
    # now return the entire error
    return total_regularized_error + total_incorrect


def train_model(M, N, K, eta, reg, Y, eps=0.0001, max_epochs=300):
    """
    Given a training data matrix Y containing rows (i, j, Y_ij)
    where Y_ij is user i's rating on movie j, learns an
    M x K matrix U and N x K matrix V such that rating Y_ij is approximated
    by (UV^T)_ij.

    Uses a learning rate of <eta> and regularization of <reg>. Stops after
    <max_epochs> epochs, or once the magnitude of the decrease in regularized
    MSE between epochs is smaller than a fraction <eps> of the decrease in
    MSE after the first epoch.

    Returns a tuple (U, V, err) consisting of U, V, and the unregularized MSE
    of the model.
    """
    # initial the matrices of U and V to be [-0.5, 0.5]
    U = np.random.rand(M, K) - 0.5
    V = np.random.rand(N, K) - 0.5
    a = np.zeros(M)
    b = np.zeros(N)
    # get the mean of all recorded ratings
    mu = np.mean(Y[:, 2])
    # now begin the epochs
    for l in range(max_epochs):
        # quick print statements just to keep track of where we are
        if ((l + 1) % 5 == 0):
            print(f"Currently on epoch #{l + 1}..")
        # store the initial loss
        prev_err = get_err(U, V, Y, a, b, mu, reg = reg)
        # shuffle the data initially
        shuffled_Y = np.copy(Y)
        # now perform the actual shuffling
        np.random.shuffle(shuffled_Y)
        # now that the data is shuffled, we can try to adjust the values of U and V
        for k in range(np.size(shuffled_Y, 0)):
            i = int(shuffled_Y[k, 0])
            j = int(shuffled_Y[k, 1])
            Y_ij = shuffled_Y[k, 2]
            # now try to modify both u_i and v_j
            U[i, :] = U[i, :] - grad_U(U[i, :], Y_ij, V[j, :], a[i], b[j], mu, reg, eta)
            V[j, :] = V[j, :] - grad_V(V[j, :], Y_ij, U[i, :], a[i], b[j], mu, reg, eta)
            a[i] = a[i] - grad_a(V[j, :], Y_ij, U[i, :], a[i], b[j], mu, reg, eta)
            b[j] = b[j] - grad_b(V[j, :], Y_ij, U[i, :], a[i], b[j], mu, reg, eta)
        
        # get the new error
        new_err = get_err(U, V, Y, a, b, mu, reg = reg)
        loss_drop = prev_err - new_err
        # test the earl stopping condition!
        if (l == 0):
            init_drop = loss_drop
        if (l != 0 and loss_drop / init_drop <= eps):
            print(f"Stopping at epoch #{l + 1}")
            break
                
    print(f"Model training is complete!")
    return U, V, a, b, get_err(U, V, Y, a, b, mu)