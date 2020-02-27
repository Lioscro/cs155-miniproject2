import sys

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# handy function that performs the SVD for V and then gives the 2D projection of V back
def plot_2d_projection_V(V_mat, movies_df indices = list(range(10))):
    # first, perform the SVD to get the 2 columns
    A, s, vh = np.linalg.svd(V_mat)
    # get the first two columns
    u_12 = A[:,:2]
    V_bar = np.transpose(np.matmul(u_12.T, V_mat)) # returns an (n by 2) matrix
    
    # TODO: scale the data to be between -1 and 1?

    
    # now perform the actual plotting
    to_plot = V_bar[indices, :]
    plt.scatter(to_plot[:, 0], to_plot[:, 1])
    for num in range(len(indices)):

        label = f"{indices[num]}"

        plt.annotate(label, # this is the text
                     (to_plot[num, 0],to_plot[num, 1]), # this is the point to label
                     textcoords="offset points", # how to position the text
                     xytext=(5,5), # distance from text to points (x,y)
                     ha='center') # horizontal alignment can be left, right or center
    plt.show()
    return