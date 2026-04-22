import matplotlib.pyplot as plt
import numpy as np
import sys 
def sturges(x) :
	return int(np.ceil(1+3.322*np.log(x)))
	

def main() :
	sample = np.random.normal(10,0.5,size=10000)
	print(np.sort(sample))
	N_bins = sturges(len(sample))
	bin_edges = np.linspace(8,14,N_bins)
	print(bin_edges)
	print('lenghth of bid edges container:', len(bin_edges))
	fig, ax = plt.subplots( nrows= 1, ncols=1)
	ax.hist(sample, bins = bin_edges, color = 'orange', density = True)
	#vertical_limits = ax.get_ylim()
	print(np.sum(sample)/len(sample))
	#plt.plot([np.sum(sample)/len(sample),np.sum(sample)/len(sample)], vertical_limits, color = 'blue', label = 'media')
	plt.axvline(np.sum(sample)/len(sample), ls = '--', label = 'media')
	plt.plot(bin_edges, (1/(0.5*np.sqrt(2*np.pi)))*np.exp(-(bin_edges-10)**2/(2*0.5**2)),linewidth = 2, color = 'r',label = 'gaussiana')
	#ax.set_yscale('log')
	plt.xlim(8,13)
	plt.savefig('1d_histogram.png')
	plt.show()
			
if __name__ == "__main__":
	main ()
		
