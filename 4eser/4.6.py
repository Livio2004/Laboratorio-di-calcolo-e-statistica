
import sys
import random
import matplotlib.pyplot as plt
import numpy as np
from math import floor

def sturges(x) :
	return int(np.ceil(1+3.322*np.log(x)))


def inv_exp (y, lamb = 1.5) :
   
    return -1 * np.log (1-y) / lamb



def main () :
	randlist = []
	N = int(input('Inserisci quanti numeri vuoiu nel sample'))
	for i in range (N):
		randlist.append (inv_exp (random.random ()))


	Nbins = sturges(len(randlist))     
	bin_edges = np.linspace (0., 4., Nbins)  


	fig, ax = plt.subplots (1,1)
	ax.set_title ('Histogram of random numbers', size=14)
	ax.set_xlabel ('random value')
	ax.set_ylabel ('events in bin')
	ax.hist (randlist, bins = bin_edges , color = 'orange')

	plt.show()




if __name__ == "__main__":
	main ()
