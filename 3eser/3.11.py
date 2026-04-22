import matplotlib.pyplot as plt
import numpy as np
import sys 
from scipy.stats import poisson, norm
def sturges(x) :
	return int(np.ceil(1+3.322*np.log(x)))
	

def main() :
	mu = int(input('Inserisci la mu della poissoniana per i momenti:'))
	sample = np.sort(poisson.rvs(mu,0, size=10000))
	print(np.sort(sample))
	poisson_fix = poisson(mu,0)
	print('Il terzo e quarto momento della distribuzione sono:', poisson_fix.stats(moments = 'sk'))
	N_bins = sturges(len(sample))
	bin_edges = np.linspace(0,2*mu+5,N_bins)
	fig, axes = plt.subplots( nrows= 2, ncols=1)
	axes[0].hist(sample, bins = bin_edges, color = 'orange', density = True, label = 'Isotgramma poisson')
	axes[1].plot(sample,poisson.cdf(sample, mu, 0.4),lw=2, color = 'g', label = 'cdf')
	plt.legend()
	for ax in axes :
		ax.set_xlabel('Variable')
		ax.set_ylabel('Number of events')
		ax.legend()
	#ax.set_yscale('log')
	plt.show()
	
			
if __name__ == "__main__":
	main ()
