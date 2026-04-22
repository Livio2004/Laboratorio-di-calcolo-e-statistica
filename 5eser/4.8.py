import matplotlib.pyplot as plt
import numpy as np
import sys 
from scipy.stats import uniform 



  
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
		
		
def main() :
	n_tot = int(input('Inserisci dimensione del campione'))
	uniform1 = uniform.rvs(size = 1000)
	variance = uniform.stats(moments = 'v')
	campione = []
	for x in range(n_tot) :
		campione.append(uniform1[x])
		
	distribuzione = lavoro(campione)
	print('La varianza del campione vale:', distribuzione.varianza2())
	print('La varianza della distribuzione uniforme vale:', variance)
	print('La varianza con il metodo TCL sul campione vale:', variance*np.sqrt(n_tot))
	
	
if __name__ == '__main__' :
	main()
	
