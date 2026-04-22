import matplotlib.pyplot as plt
import numpy as np
import sys 



  
def sturges(x) :
	return int(np.ceil(1+3.322*np.log(x)))

class lavoro :
	sample = 0
	N_events = 0
	Sample_sum = 0
	Sample_sumsq = 0 #La somma dei quadrati
	
	def __init__(self, input_file) :
	
		with open(input_file) as f:
			self.sample = np.array([float(x) for x in f.readlines()])
		self.N_events = np.len(self.sample)
		self.Sample_sum = np.sum(self.sample)
		self.Sample_sumsq = np.sum([x*x for x in self.sample]) #come se facessi un nuovo array
		
	def media(self):
		return self.Sample_sum/self.N_events
		
	def varianza(self):
		return self.Sample_sumsq/self.N - (self.mean())**2
		
	def devst(self) :
		return np.sqrt(self.varianza())
		
	def errore_standard(self) :
		return self.devst()/np.sqrt(self.N)
		
	def isto(self) :
		N_bins = sturges(len(self.sample))
		bin_edges = np.linspace(np.floor(np.min(self.sample)),np.ceil(np.max(self.sample)),N_bins)
		print('lenghth of bid edges container:', len(bin_edges))
		fig, ax = plt.subplots( nrows= 1, ncols=1)
		ax.hist(self.sample, bins = bin_edges, label = 'Gaussian distribution', color = 'orange', density = False)
		ax.set_xlabel('variable')
		ax.set_ylabel('event coounts')
		ax.legend()
		plt.show()
		
		
	
		
	
