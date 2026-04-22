import matplotlib.pyplot as plt
import numpy as np
import sys 
from scipy.stats import expon
import random

def sturges(x) :
	return int(np.ceil(1+3.322*np.log(x)))




class GRN :
	num = 0
	def __init__ (self, value = 0) :
		self.num = value
		
	def seed(self, seed) :
		self.num = random.seed(seed)
		
	def random(self) :
		self.num = random.random()
		return self.num

		
		
	
	
		
def rand_range(xmin, xmax, x) :
	randlist = []
	for i in x:
		result = xmin + i*(xmax-xmin)
		randlist.append(result)	
	return randlist 

	

def main() :
	if len(sys.argv) != 3 :
		print('inserire xmin e xmax')
		sys.exit()
	
	
	items = int(input('Inserisci quanti numeri casuali vuoi:'))
	seed = float(input('Quale seed vuoi?'))
	
	
	my_GRN = GRN(seed)
	sample =  []
	
	for i in range(items-1) :
		sample.append(my_GRN.random())
		
		
		
	sample = rand_range(int(sys.argv[1]), int(sys.argv[2]), sample )
	

	N_bins = sturges(len(sample))
	bin_edges = np.linspace(np.floor(np.min(sample)), np.ceil(np.max(sample)), N_bins)
	
	fig,ax = plt.subplots(nrows = 1, ncols = 1)
	ax.hist(sample, bin_edges, color = 'red', label = 'distribuzione', density = False)
	ax.set_xlabel('Dati')
	ax.set_ylabel('NUmero di eventi')
	ax.legend()
	plt.show()
	
			
if __name__ == "__main__":
	main ()
