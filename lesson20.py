#Emily Savela; Created 13 September 2016
#Lesson 20 Computing

import numpy as np

#load in data
xa_high = np.loadtxt('data/xa_high_food.csv', comments='#')
xa_low = np.loadtxt('data/xa_low_food.csv', comments='#')

def xa_to_diameter(xa):
    """
    Convert an array of cross-sectional areas
    to diameters with commensurate units
    """

    #compute diameter from area
    #Area = pi * d^2 / 4
    diameter = np.sqrt(xa * 4 / np.pi)

    return diameter
    
