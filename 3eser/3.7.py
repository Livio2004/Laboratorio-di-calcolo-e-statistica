import matplotlib.pyplot as plt
import numpy as np
import sys 
from scipy.stats import norm 
def sturges(x) :
	return int(np.ceil(1+3.322*np.log(x)))
	

def main() :
	sample = np.linspace(-5,5,10000)
	print(np.sort(sample))
	N_bins = sturges(len(sample))
	bin_edges = np.linspace(8,14,N_bins)
	print(bin_edges)
	print('lenghth of bid edges container:', len(bin_edges))
	fig, axes = plt.subplots( nrows= 2, ncols=1)
	axes[0].plot(sample, norm.pdf(sample, loc = 0, scale=1),linewidth = 2, color = 'r',label = 'gaussiana')
	axes[1].plot(sample,norm.cdf(sample, loc = 0, scale = 1),lw=2, color = 'g', label = 'cdf')
	plt.legend()
	for ax in axes :
		ax.set_xlabel('Variable')
		ax.set_ylabel('Number of events')
		ax.legend()
	#ax.set_yscale('log')
	plt.show()
			
if __name__ == "__main__":
	main ()
		
