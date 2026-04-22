import matplotlib.pyplot as plt
import numpy as np
import sys 
def sturges(x) :
	return int(np.ceil(1+3.322*np.log(x)))
	

def main() :
	if (len(sys.argv)>3) :
		print('usa la forma:', sys.argv[0], 'input_file.txt Nmax')
		sys.exit()
		
	Nmax = int(sys.argv [2])
	
	with open(sys.argv[1]) as f:
		sample = [float(x) for x in f.readlines()]
		
	with open('eventi_unif.txt', 'r') as input_file :
		sample2 = [float(x) for x in input_file.readlines()]
	
	
	print(np.sort(sample))
	print(np.sort(sample2))
	
	N_bins1 = sturges(len(sample[:Nmax]))
	N_bins2 = sturges(len(sample[:Nmax]))
	bin_edges = np.linspace(np.floor(np.min(sample[:Nmax])),np.ceil(np.max(sample[:Nmax])),N_bins1)
	bin_edges2 = np.linspace(np.floor(np.min(sample2[:Nmax])),np.ceil(np.max(sample2[:Nmax])),N_bins2)
	print('lenghth of bid edges container:', len(bin_edges))
	print('lenghth of  second bid edges container:', len(bin_edges2))
	
	fig, ax = plt.subplots( nrows= 2, ncols=1)
	ax[0].hist(sample[:Nmax], bins = bin_edges, label = 'Gaussian distribution', color = 'orange', density = False)
	ax[1].hist(sample2[:Nmax], bins = bin_edges2, label = 'Normal distribution', color = 'green', density = False)

	for a in ax :
		a.set_xlabel('variable')
		a.set_ylabel('event coounts')
		a.legend()
		
	plt.show()
			
if __name__ == "__main__":
	main ()
		
