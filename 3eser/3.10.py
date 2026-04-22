import matplotlib.pyplot as plt
import numpy as np
import sys 
from scipy.stats import binom
def sturges(x) :
	return int(np.ceil(1+3.322*np.log(x)))
	

def main() :
	sample = np.sort(binom.rvs(5,0.4, size=10000))
	print(np.sort(sample))
	N_bins = sturges(len(sample))
	bin_edges = np.linspace(-5,5,N_bins)
	fig, axes = plt.subplots( nrows= 2, ncols=1)
	axes[0].hist(sample, bins = bin_edges, color = 'orange', density = True, label = 'Isotgramma binomiale')
	axes[1].plot(sample,binom.cdf(sample, 5, 0.4),lw=2, color = 'g', label = 'cdf')
	plt.legend()
	for ax in axes :
		ax.set_xlabel('Variable')
		ax.set_ylabel('Number of events')
		ax.legend()
	#ax.set_yscale('log')
	plt.show()
			
if __name__ == "__main__":
	main ()
