import sys
import random
import matplotlib.pyplot as plt
import numpy as np
from math import floor

def main ():
    lista1 = []
    with open('eventi_unif.txt') as file1 :
    	for x in file1.readlines() :
    		lista1.append(float(x))
    
    mean = np.mean(lista1)
    print(mean)
    
    subset_1 = list(filter(lambda x : x>mean, lista1))
    subset_2 = list(filter(lambda x : x<=mean, lista1))
    print(np.std(lista1))
    print(np.std(subset_1))
    print(np.std(subset_2))

if __name__ == "__main__":
    main()
