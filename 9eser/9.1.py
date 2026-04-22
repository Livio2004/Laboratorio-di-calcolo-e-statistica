import sys
import random
import matplotlib.pyplot as plt
import numpy as np
from math import floor


def exp_pdf (x, tau) :
	if tau == 0. :
		return 1 
	return np.exp(-1*x/tau)/tau
	
def likelihood(theta, pdf, lista) :
	r = 1
	for x in lista :
		r = r*pdf(x,theta)
	return r
def loglikelihood (theta, pdf, lista) :
	r = 0 
	for x in lista :
		if pdf(x, theta) >0 :
			r = r + np.log(pdf(x, theta))
	return r
	

def sturges(x) :
	return int(np.ceil(1+3.322*np.log(x)))


def inv_exp (y, lamb = 1.5) :
   
    return -1 * np.log (1-y) / lamb



def main () :
	randlist = []
	N = int(sys.argv[1])
	for i in range (N):
		randlist.append (inv_exp (random.random ()))


	Nbins = sturges(len(randlist))     
	bin_edges = np.linspace (0., 4., Nbins)  
	x = np.linspace(0,20, 1000)

	fig, ax = plt.subplots (1,1)
	ax.plot(x , exp_pdf(x, 1/1.5), color = 'green', lw = 3, label = 'exponential pdf')
	ax.set_title ('Histogram of random numbers', size=14)
	ax.set_xlabel ('random value')
	ax.set_ylabel ('events in bin')
	ax.hist (randlist, bins = bin_edges , color = 'orange', density = 'True')
	ax.set_xlim(0,6)
	ax.legend()

	plt.show()




if __name__ == "__main__":
	main ()
