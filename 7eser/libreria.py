import matplotlib.pyplot as plt
import numpy as np
import sys 
from scipy.stats import describe


class GRN :
	num = 0
	def __init__ (self, value = 0) :
		self.num = value
		
	def seed(self, seed) :
		self.num = random.seed(seed)
		
	def random(self) :
		self.num = random.random()
		return self.num
		
		
def sturges(x) :
	return int(np.ceil(1+3.322*np.log(x)))

class lavoro :
	sample = []
	N_events = 0
	Sample_sum = 0
	Sample_sumsq = 0 #La somma dei quadrati
	
	def __init__(self, array) :
	
		self.sample = array
		self.N_events = len(self.sample)
		self.Sample_sum = np.sum(self.sample)
		self.Sample_sumsq = np.sum([x*x for x in self.sample]) #come se facessi un nuovo array
	
	def media(self):
		return self.Sample_sum /self.N_events
		
	def varianza2(self) :
		return np.var(self.sample)

	def varianza(self):
		var = self.Sample_sumsq/self.N_events - (self.media())**2
		return var
	
	def devst(self) :
		return np.sqrt(self.varianza())
			
	def errore_standard(self) :
		return self.devst()/np.sqrt(self.N_events)
	
	def skewness(self) :
		moments = list(describe(self.sample))
		return moments[4]
		
	def kurtosis(self) :
		moments = list(describe(self.sample))
		return moments[5]
		
	def isto(self) :
		N_bins = sturges(len(self.sample))
		bin_edges = np.linspace(np.floor(np.min(self.sample)),np.ceil(np.max(self.sample)),N_bins)
		print('lenghth of bid edges container:', len(bin_edges))
		fig, ax = plt.subplots( nrows= 1, ncols=1)
		ax.hist(self.sample, bins = bin_edges, label = 'Istogramma della distribuzione', color = 'orange', density = True)
		ax.set_xlabel('variable')
		ax.set_ylabel('event coounts')
		ax.legend()
		plt.show()
		
	def dato(self) :
		print("Dati distribuzione: \nMedia:", self.media(), "\nVarianza:", self.varianza(),"\nDeviazione standard:",self.devst(),"\nErrore standard della media:",self.errore_standard(),"\nI momenti della distribuzione sono(skewness e kurtosis):",self.skewness(), self.kurtosis())
		return "L'istogramma è stato aggiunto correttamente nella directory sottoforma di png"
		
def rand_range(xmin, xmax, x) :
	randlist = []
	for i in x:
		result = xmin + i*(xmax-xmin)
		randlist.append(result)	
	return randlist 
