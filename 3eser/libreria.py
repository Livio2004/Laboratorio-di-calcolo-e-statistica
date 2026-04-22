import matplotlib.pyplot as plt
import numpy as np
import sys 



  
def sturges(x) :
	return int(np.ceil(1+3.322*np.log(x)))

class lavoro :
	sample = []
	N_events = 0
	Sample_sum = 0
	Sample_sumsq = 0 #La somma dei quadrati
	
	def __init__(self, input_file) :
	
		with open(input_file) as f:
			self.sample = np.array([float(x) for x in f.readlines()])
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
		
	def isto(self, output_file) :
		N_bins = sturges(len(self.sample))
		bin_edges = np.linspace(np.floor(np.min(self.sample)),np.ceil(np.max(self.sample)),N_bins)
		print('lenghth of bid edges container:', len(bin_edges))
		fig, ax = plt.subplots( nrows= 1, ncols=1)
		ax.hist(self.sample, bins = bin_edges, label = 'Gaussian distribution', color = 'orange', density = False)
		ax.set_xlabel('variable')
		ax.set_ylabel('event coounts')
		ax.legend()
		plt.savefig(output_file)
		
	def dato(self) :
		print("Dati distribuzione: \nMedia:", self.media(), "\nVarianza:", self.varianza(),"\nDeviazione standard:",self.devst(),"\nErrore standard della media:",self.errore_standard())
		return "L'istogramma è stato aggiunto correttamente nella directory sottoforma di png"
		
	
		
		
	
		
	
