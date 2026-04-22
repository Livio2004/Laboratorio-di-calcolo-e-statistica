from iminuit import Minuit 
from iminuit.cost import LeastSquares
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import chi2

def f(x,a,b,c) :
	return a*x**2 + b*x + c
	
def sturges(x) :
	return int(np.ceil(1+3.322*np.log(x)))

	
	

def main():
	
	a = 1
	b = 2
	c = 1.5
	err_epsilon = 0.5
	N_toys = 10000
	Q_results = []
	sigma_results = []
	p_value_results = []
	for _ in range(N_toys) :
		epsilon = np.random.uniform(0, err_epsilon, size = 10)
		x_coord = np.arange(0,10,1)
		y_coord = np.zeros(10)
		for i in range(10) :
			y_coord[i] = f(x_coord[i], a, b,c) + epsilon[i]
		sigma_y = err_epsilon*np.ones(len(epsilon))
		least_squares = LeastSquares(x_coord, y_coord, sigma_y, f)
		fit = Minuit(least_squares, a=0, b=0, c = 0)
		fit.migrad()
		fit.hesse()
		Q_squared = fit.fval
		Q_results.append(Q_squared)
		ndof = fit.ndof
		
		
		sigma_variance = np.power(np.sum(y_coord-f(x_coord, a,b,c)),2)/Q_squared
		sigma = np.sqrt(sigma_variance)
		sigma_results.append(sigma)
	
	Q_results = np.sort(Q_results)	
	plt.figure(figsize=(10, 6))
	N_bins = sturges(len(Q_results))
	bin_edges = np.linspace(np.min(Q_results), np.max(Q_results), N_bins)
	plt.hist(Q_results, bin_edges, label = f'Distribuzione del Q square con {ndof} gradi di libertà', alpha=0.5, density = True)
	plt.plot(Q_results, chi2.pdf(Q_results, df = ndof), label = 'distribuzione chi quadro expected')
	plt.legend()
	plt.xlabel("x")
	plt.ylabel("y")
	plt.show()
	

	
	plt.figure(figsize=(10, 6))
	N_bins = sturges(len(sigma_results))
	bin_edges = np.linspace(np.min(sigma_results), np.max(sigma_results), N_bins)
	plt.hist(sigma_results, bin_edges, label = f'errori stimati a posteriori', alpha=0.5, density = True)
	randlist = np.absolute(np.random.normal(0,0.5,10000))
	bin_edges = np.linspace(np.min(randlist), np.max(randlist), N_bins)
	plt.hist(randlist, bin_edges, label = f'gaussiana', alpha=0.5, histtype = 'step', density = True)
	plt.axvline(err_epsilon, label = 'errore vero di yi')
	plt.legend()
	plt.xlabel("x")
	plt.ylabel("y")
	plt.show()
	
	
	
	
	
		
		
	
	
	
	
	
if __name__ == '__main__' :
	main()
