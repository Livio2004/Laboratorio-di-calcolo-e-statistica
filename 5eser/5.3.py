import matplotlib.pyplot as plt
import numpy as np
import sys 
from scipy.stats import norm
import random
import time 


def sturges(x):
    return int(np.ceil(1 + 3.322 * np.log(x)))


def main():
	lista1 = np.sort(norm.rvs(1, 0.5, size= 10000))
	time1 = time.time()
	square = list(map(lambda x : x**2, lista1))
	time2 = time.time()
	print(time2-time1)
	time3 = time.time()
	square2 = np.square(lista1)
	time4 = time.time()
	print(time4-time3)
	cube = np.power(lista1,3)
	fig, ax = plt.subplots(nrows=1, ncols=1)
	xmin = np.min(lista1)
	xmax = np.max(lista1)
	xmin1 = np.min(square)
	xmax1 = np.max(square)
	xmin2 = np.min(cube)
	xmax2 = np.max(cube)
	N_bins1 = sturges(len(square))
	bin_edges = np.linspace(xmin, xmax, N_bins1)
	bin_edges1 = np.linspace(xmin1, xmax1, N_bins1)
	bin_edges2 = np.linspace(xmin2, xmax2, N_bins1)
	ax.hist(lista1, bin_edges , color = 'red' , lw = 2, histtype ='step')
	ax.hist(square, bin_edges1, color = 'brown' , lw = 2, alpha = 0.2)
	ax.hist(cube, bin_edges2, color = 'blue' , lw = 2, alpha = 0.5, histtype= 'step')
	plt.show()
	

if __name__ == "__main__":
    main()
