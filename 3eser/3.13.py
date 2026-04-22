import matplotlib.pyplot as plt
import numpy as np
import sys 
from scipy.stats import norm 
def areaG(x) :
	integer = norm.cdf(x, loc = 0, scale= 1)
	result = 1 - (1-integer)*2
	return result 



def sturges(x) :
	return int(np.ceil(1+3.322*np.log(x)))
	

def main() :
	sample = np.linspace(-5,5,10000)
	mean, sigma1 = 0, 1
	sigma = np.abs(float(input('inserisci il sigma da cui vuoi calcolare l integrale:')))
	print(sigma)
	print("L'integrale dato il tuo sigma vale:", areaG(sigma))
	fig, axes = plt.subplots( nrows= 2, ncols=1)
	axes[0].plot(sample, norm.pdf(sample, loc = mean, scale=sigma1),linewidth = 2, color = 'r',label = 'gaussiana')
	axes[0].fill_between(sample,norm.pdf(sample, scale = sigma1), 0, where = (sample > -1*np.abs(sigma)) & (sample<np.abs(sigma)) ,  color = 'blue', label = 'integrale dato sigma')
	axes[1].plot(sample,norm.cdf(sample, loc = mean, scale =sigma1),lw=2, color = 'g', label = 'cdf')
	plt.legend()
	for ax in axes :
		ax.set_xlabel('Variable')
		ax.set_ylabel('Number of events')
		ax.legend()
	#ax.set_yscale('log')
	
	
	plt.show()
			
if __name__ == "__main__":
	main ()
