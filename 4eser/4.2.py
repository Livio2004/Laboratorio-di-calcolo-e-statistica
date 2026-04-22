import matplotlib.pyplot as plt
import numpy as np
import sys 
from scipy.stats import expon

def sturges(x) :
	return int(np.ceil(1+3.322*np.log(x)))




class GRN :
	A = 214013
	C = 2531011
	M = 2147483647
	num = 0
	def __init__ (self, value = 0) :
		self.num = value
		
	def seed(self, seed) :
		self.num = seed
		
	def random(self) :
		self.num = (self.A*self.num + self.C) % self.M
		return self.num
		
	
	
		
	

def main() :
	items = int(input('Inserisci quanti numeri casuali vuoi:'))
	seed = float(input('Quale seed vuoi?'))
	
	my_GRN = GRN(seed)
	sample =  []
	
	for i in range(items-1) :
		sample.append(my_GRN.random())
		print(my_GRN.random())
		
	N_bins = sturges(len(sample))
	bin_edges = np.linspace(np.floor(np.min(sample)), np.ceil(np.max(sample)), N_bins)
	
	fig,ax = plt.subplots(nrows = 1, ncols = 1)
	ax.hist(sample, bin_edges, color = 'red', label = 'distribuzione', density = True)
	ax.set_xlabel('Dati')
	ax.set_ylabel('NUmero di eventi')
	ax.legend()
	plt.show()
	
			
if __name__ == "__main__":
	main ()
